#!/usr/bin/env python
# encoding: utf-8
# 
# Stylus, Copyright 2006-2008 Biologic Institute
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
'''
inscribe.py

This script/module creates archetypes and genes from Han definition files.

Stylus, Copyright 2006-2008 Biologic Institute.
'''

import datetime
import fnmatch
import getopt
import os
import random
import re
import shutil
import string
import stylus.codons as Codons
import stylus.common as Common
import stylus.genome as Genome
import sys
import time
import urllib2
import urlparse
import uuid

#==============================================================================
# Global Constants
#==============================================================================
_VERSION = '1.0'
_NAME = 'inscribe.py %s' % _VERSION

_HAN_DEFINITION = '''<?xml version='1.0' standalone='no'?>
<hanDefinition uuid='%s' unicode='%s' creationDate='%s' creationTool='%s' xmlns='http://biologicinstitute.org/schemas/stylus/1.0'>
<bounds %s />
<length>%r</length>
<minimumStrokeLength>%r</minimumStrokeLength>
<groups>%s</groups>
<strokes>%s</strokes>
%s
</hanDefinition>
'''

_HAN_GROUP = '''
<group>
<bounds %s />
<length>%r</length>
<weightedCenter x='%r' y='%r' />
<containedStrokes>%s</containedStrokes>
</group>
'''

_HAN_STROKE = '''
<stroke>
<bounds %s />
<length>%r</length>
<points>
<forward>%s</forward>
<reverse>%s</reverse>
</points>
</stroke>
'''

_HAN_POINT = '''<pointDistance x='%r' y='%r' fractionalDistance='%r' />'''

_HAN_OVERLAP = '''<overlap firstStroke='%d' secondStroke='%d' required='%s' />'''

_GENE_DEFINITION = '''<?xml version='1.0' encoding='UTF-8' ?>
<genome uuid='%s' %s creationDate='%s' creationTool='%s' creationParameters='%s' xmlns='http://biologicinstitute.org/schemas/stylus/1.0'>
<bases>%s</bases>
<genes>
<gene baseFirst='1' baseLast='%d'>
<origin x='%r' y='%r' />
<hanReferences>
<hanReference unicode='%s'>
<strokes>
%s
</strokes>
</hanReference>
</hanReferences>
</gene>
</genes>
</genome>
'''

_GENE_STROKE = '''<stroke baseFirst='%d' baseLast='%d' correspondsTo='%d' />'''

#==============================================================================
# Globals
#==============================================================================
class Globals:
    fInteractive = False
    uchHan = ''
    fBuildArchetype = False
    strArchetypePath = ''
    aryGenes = []
    strGenePath = ''
    urlHan = ''
    strAuthor = ''
Common.Globals.fQuiet = True

#==============================================================================
# Helper Classes
#==============================================================================
#------------------------------------------------------------------------------
# Class: Usage
#
#------------------------------------------------------------------------------
class Usage(Common.BiologicError):
    __strHelpMessage = '''
\t(-c|--code) <Unicode> - The Unicode number of the Han character to use

\t[(-d|--definition)=<archetype output path>] - Build archetype file
\t[(-g|--gene) <gene parameters>|default] - Parameters used to form the gene

\t[(-o|--output)=<output path>] - The path for gene files
\t[(-u|--urls) [<Han URL>]] - Set the URLs

\t[-a|--author] - Gene author name
\t[-q|--quiet] - Silence all output
\t[-h|--help] - Print this help

\tGene Parameters

\t<stroke order>:<head>:<tail>:<gene shaping>:<group shaping>:<stroke shaping>

\tStroke Order\to[#[r](,#[r])+ | han | min]\tOrder in which to build strokes (may be a partial list)
\tHead\th(+|-)#,(+|-)#\tAdd an incoherent section to the head of the gene specified by the offset
\tTail\tt(+|-)#,(+|-)#\tAdd an incoherent section to the tail of the gene specified by the offset
\tGene Shaping\tsx(+|-)#(%),sy(+|-)#(%),dx(+|-)#,dy(+|-)#\tAmount to scale and/or translate the entire gene
\tGroup Shaping\tg#(sx(+|-)#(%),sy(+|-)#(%),dx(+|-)#,dy(+|-)#)\tAmount to scale and/or translate the group
\tStroke Shaping\ts#(sx(+|-)#(%),sy(+|-)#(%),dx(+|-)#,dy(+|-)#)\tAmount to scale and/or translate the stroke

Related environment variables:
STYLUS_INSCRIBEARGS - The default argument string to parse (command-line overrides duplicate arguments)

STYLUS_INSCRIBEOUT  - The default output path for genome files

STYLUS_HANURL       - The URL from which to obtain Han definition files

STYLUS_AUTHOR       - Gene author

See Stylus documentation for more details.
'''
    def __init__(self, msg):
        self.msg = ''
        if msg and len(msg) > 0:
            self.msg = 'Error: ' + msg + '\n'
        if Globals.fInteractive:
            self.msg += 'Usage: ' + sys.argv[0].split("/")[-1] + '\n' + self.__strHelpMessage
    
    def __str__(self):
        return self.msg
        
#------------------------------------------------------------------------------
# Class: Constants
# 
#------------------------------------------------------------------------------
class Constants:
    strTranslate = string.maketrans('.', '_')
    
    rstrUnicode = r'[A-F\d]{4,5}'
    reUnicode = re.compile(rstrUnicode)

    rstrDigits = r'[\+|\-]?\d+'
    reDigits = re.compile(r'(%s).*' % rstrDigits)

    rstrFloats = r'[\+|\-]?\d+(?:\.\d+)?'
    reFloats = re.compile(r'.*?(%s).*' % rstrFloats)

    reOrder = re.compile(r'o((?:\d+r?(?:,\d+r?)*|han|min))')
    
    reHead = re.compile(r'h(%s),(%s)' % (rstrFloats, rstrFloats))
    reTail = re.compile(r't(%s),(%s)' % (rstrFloats, rstrFloats))

    rstrScale = r's[x|y]%s%%?' % rstrFloats
    rstrTranslate = r'd[x|y]%s' % rstrFloats
    rstrTransform = r'(?:%s|%s)(?:,(?:%s|%s)){0,3}' % (rstrScale, rstrTranslate, rstrScale, rstrTranslate)

    reScale = re.compile(rstrScale)
    reTranslate = re.compile(rstrTranslate)
    reTransform = re.compile(rstrTransform)

    reGroup = re.compile(r'g(\d+)\((%s)\)' % rstrTransform)
    reStroke = re.compile(r's(\d+)\((%s)\)' % rstrTransform)
    
    strDefault = 'default'
    
    # Note:
    # - Assume a default scale of about 50 medium vectors along the x/y axis
    # - This assumes a 500x500 incoming grid
    # - As these genes are only starting points for developing real genes (those
    #   used by Stylus experiements), it's a sufficient guess-timate. They'll
    #   work well for some genes, but likely not all such as the very small and
    #   the very large. User supplied scaling will handle those cases.
    sxDefault = ((50 * Codons.Constants.vectorMedium) / 500)
    syDefault = ((50 * Codons.Constants.vectorMedium) / 500)

#------------------------------------------------------------------------------
# Class: Transform
# 
#------------------------------------------------------------------------------
class Transform(object):
    def __init__(self, params=None, xf=None, sx=1, sy=1, dx=0, dy=0):
        self.sxIsPercentage = False
        self.syIsPercentage = False

        self.sx = sx
        self.sy = sy
        self.dx = dx
        self.dy = dy
        
        if xf:
            self.sx = xf.sx
            self.sy = xf.sy
            self.dx = xf.dx
            self.dy = xf.dy

        if params:
            if Constants.reTransform.match(params):
                for s in params.split(','):
                    if s[0] == 's':
                        nPercent = s[-1] == '%' and 100 or 1
                        if s[1] == 'x':
                            self.sxIsPercentage = True
                            self.sx = float(Constants.reFloats.match(s).groups()[0]) / nPercent
                        else:
                            self.syIsPercentage = True
                            self.sy = float(Constants.reFloats.match(s).groups()[0]) / nPercent
                    elif s[0] == 'd':
                        if s[1] == 'x':
                            self.dx = float(Constants.reFloats.match(s).groups()[0])
                        else:
                            self.dy = float(Constants.reFloats.match(s).groups()[0])
            else:
                raise Common.BiologicError('%s is not a recognized set of shaping options' % params)

    #--------------------------------------------------------------------------
    # Function: apply
    # 
    # Notes:
    # - Points are modified in-place
    # - Since scaling moves the points (by virtue of growing or reducing their
    #   values), a compensating offset (derived from the transformation's
    #   object (e.g., group, stroke) bounding rectangle) is added. This ensures
    #   that scaling shrinks or grows the points around their existing location,
    #   rather than shifting them as well.
    #--------------------------------------------------------------------------
    def apply(self, aryPoints, rectBounding=None):
        if self.sx != 1 or self.sy != 1 or self.dx or self.dy:
            ptScalingCompensation = rectBounding and Genome.Point(x=(rectBounding.ptCenter.x - (rectBounding.ptCenter.x * self.sx)), y=(rectBounding.ptCenter.y - (rectBounding.ptCenter.y * self.sy))) or Genome.Point(x=0, y=0)
            for pt in aryPoints:
                pt.x = ((pt.x + self.dx) * self.sx) + ptScalingCompensation.x
                pt.y = ((pt.y + self.dy) * self.sy) + ptScalingCompensation.y
        return aryPoints
        
    def __toName(self):
        aryParams = []
        if self.sx != 1:
            aryParams.append('sx%s%s' % (('%2.2f' % (self.sxIsPercentage and (self.sx*100) or self.sx)).translate(Constants.strTranslate), self.sxIsPercentage and 'pct' or ''))
        if self.sy != 1:
            aryParams.append('sy%s%s' % (('%2.2f' % (self.syIsPercentage and (self.sy*100) or self.sy)).translate(Constants.strTranslate), self.syIsPercentage and 'pct' or ''))
        if self.dx:
            aryParams.append('dx%s' % ('%2.2f' % self.dx).translate(Constants.strTranslate))
        if self.dy:
            aryParams.append('dx%s' % ('%2.2f' % self.dx).translate(Constants.strTranslate))
        return '_'.join(aryParams)
    name = property(__toName)

    def __str__(self):
        return 'sx%r,sy%r,dx%r,dy%r' % (self.sx, self.sy, self.dx, self.dy)

#------------------------------------------------------------------------------
# Class: GeneSpecification
# 
#------------------------------------------------------------------------------
class GeneSpecification(object):
    def __init__(self, strParameters, han):
        self.__han = han

        self.__fOrderHan = True
        self.__fOrderMin = False
        self.__aryOrder = None
        self.__ptHead = None
        self.__ptTail = None
        self.__xf = None
        
        self.__fHasGroup = False
        self.__xfGroups = [ None for i in xrange(len(self.__han.aryGroups)) ]
        
        self.__fHasStroke = False
        self.__xfStrokes = [ None for i in xrange(len(self.__han.aryStrokes)) ]

        if strParameters:
            for param in strParameters.split(':'):
                mo = Constants.reOrder.match(param)
                if mo:
                    self.__fOrderHan = False
                    if mo.groups()[0] == 'han':
                        self.__fOrderHan = True
                    elif mo.groups()[0] == 'min':
                        self.__fOrderMin = True
                    else:
                        self.__aryOrder = [ (int(Constants.reDigits.match(i).groups()[0])-1, (i[-1] == 'r' and True or False)) for i in mo.groups()[0].split(',') ]
                        self.__aryOrder += [ (i, False) for i in xrange(len(self.__han.aryStrokes)) if not (i, False) in self.__aryOrder and not (i, True) in self.__aryOrder ]
                    continue
            
                mo = Constants.reHead.match(param)
                if mo:
                    self.__ptHead = Genome.Point(x=float(mo.groups()[0]), y=float(mo.groups()[1]))
                    continue
            
                mo = Constants.reTail.match(param)
                if mo:
                    self.__ptTail = Genome.Point(x=float(mo.groups()[0]), y=float(mo.groups()[1]))
                    continue
            
                mo = Constants.reTransform.match(param)
                if mo:
                    self.__xf = Transform(params=param)
                    continue
            
                mo = Constants.reGroup.match(param)
                if mo:
                    self.__fHasGroup = True
                    self.__xfGroups[int(mo.groups()[0])-1] = Transform(params=mo.groups()[1])
                    continue
            
                mo = Constants.reStroke.match(param)
                if mo:
                    self.__fHasStroke = True
                    self.__xfStrokes[int(mo.groups()[0])-1] = Transform(params=mo.groups()[1])
                    continue
            
                raise Common.BiologicError('%s is not a recognized gene option' % param)
                
        if not self.__aryOrder:
            self.__aryOrder = self.__getDefaultOrder()
            
    #--------------------------------------------------------------------------
    # Function: __getDefaultOrder
    # 
    # Build a reasonable stroke traversal order that loosely attempts to
    # minimize the incoherent regions.
    #--------------------------------------------------------------------------
    def __getDefaultOrder(self):
        # If requested, use Han ordering
        if self.__fOrderHan:
            return [ (i, False) for i in xrange(len(self.__han.aryStrokes)) ]
        
        # Build an array of all stroke start/end points as co-located pairs
        # - The start point for a stroke is at (stroke# * 2) and the endpoint at (stroke# * 2 + 1)
        aryPoints = [ st.aryPointsForward[i] for st in self.__han.aryStrokes for i in [0,-1] ]
        
        # Build a "cost" array containing the measured distance between all possible point pairs
        # - Rows are indexed the same as the point array and contain the "cost" to each other possible point
        # - The loop below ignores invalid comparisons (which change with each iteration),
        #   so generate all values rather than filtering at this point
        aryCost = [ ([ 0 ] * len(aryPoints)) for i in xrange(len(aryPoints)) ]
        for i in xrange(len(aryPoints)):
            for j in xrange(i,len(aryPoints)):
                aryCost[i][j] = aryCost[j][i] = Genome.Line(aryPoints[i], aryPoints[j]).length
        
        # Build an initial set of possible orderings that include just one stroke each
        # - Points are referenced indirectly via an index into the point array
        aryOrder = [ [ i*2, i*2+1 ] for i in xrange(len(self.__han.aryStrokes)) ]
        
        # Collapse possible orderings until one remains
        # - For each ordering, calculate its preferred joining and the cost of not doing so
        #   Select the least expensive, combine, and repeat
        while len(aryOrder) > 1:
            
            # First, build an array of preferred combinations
            # - Each entry contains the a four item tuple containing the index (into aryOrder) of
            #   the join-er, a T/F flag indicating if the join uses the join-er's start/end point,
            #   the index (into aryOrder) of the join-ee, a T/F flag indicating if the join uses the
            #   join-ee's start/end point, and the cost of not making the join (which is the distance
            #   to the next closest point less the length of the proposed join)
            aryPreferred = []
            for i in xrange(len(aryOrder)-1):
                iMinFirstOrder = 0
                nMinCostFirst = sys.maxint
                nNextToMinCostFirst = sys.maxint

                iMinLastOrder = 0
                nMinCostLast = sys.maxint
                nNextToMinCostLast = sys.maxint
                
                iSourcePointFirst = aryOrder[i][0]
                iSourcePointLast = aryOrder[i][-1]

                for j in xrange(i+1, len(aryOrder)):
                    iTargetPointFirst = aryOrder[j][0]
                    iTargetPointLast = aryOrder[j][-1]
                    
                    if aryCost[iSourcePointFirst][iTargetPointFirst] < nMinCostFirst:
                        nNextToMinCostFirst = nMinCostFirst - aryCost[iSourcePointFirst][iTargetPointFirst]
                        nMinCostFirst = aryCost[iSourcePointFirst][iTargetPointFirst]
                        iMinFirstOrder = (True, j, True)
                        
                    if aryCost[iSourcePointFirst][iTargetPointLast] < nMinCostFirst:
                        nNextToMinCostFirst = nMinCostFirst - aryCost[iSourcePointFirst][iTargetPointLast]
                        nMinCostFirst = aryCost[iSourcePointFirst][iTargetPointLast]
                        iMinFirstOrder = (True, j, False)
                    
                    if aryCost[iSourcePointLast][iTargetPointFirst] < nMinCostLast:
                        nNextToMinCostLast = nMinCostLast - aryCost[iSourcePointLast][iTargetPointFirst]
                        nMinCostLast = aryCost[iSourcePointLast][iTargetPointFirst]
                        iMinLastOrder = (False, j, True)
                        
                    if aryCost[iSourcePointLast][iTargetPointLast] < nMinCostLast:
                        nNextToMinCostLast = nMinCostLast - aryCost[iSourcePointLast][iTargetPointLast]
                        nMinCostLast = aryCost[iSourcePointLast][iTargetPointLast]
                        iMinLastOrder = (False, j, False)
                
                aryPreferred.append((i, iMinFirstOrder[0], iMinFirstOrder[1], iMinFirstOrder[2], nNextToMinCostFirst))
                aryPreferred.append((i, iMinLastOrder[0], iMinLastOrder[1], iMinLastOrder[2], nNextToMinCostLast))
            
            # Next, sort descending by cost and select a join
            # - Specifying min selects the highest priority join
            # - Otherwise, randomly select a join favoring those with a higher priority
            aryPreferred.sort(lambda t1, t2: int(t2[4]-t1[4]))
            if self.__fOrderMin:
                iSelected = 0
            else:
                nSkipCost = 0
                for join in aryPreferred:
                    nSkipCost += join[4]
                nSkippedSelected = random.random() * nSkipCost
                nSkipCost = 0
                iSelected = -1
                while nSkippedSelected > nSkipCost:
                    iSelected += 1
                    nSkipCost += aryPreferred[iSelected][4]

            # Join the two order entries, reversing their contents if needed
            iSourceOrder = aryPreferred[iSelected][0]
            if aryPreferred[iSelected][1]:
                aryOrder[iSourceOrder].reverse()

            iTargetOrder = aryPreferred[iSelected][2]
            aryTargetOrder = aryOrder[iTargetOrder]
            if not aryPreferred[iSelected][3]:
                aryTargetOrder.reverse()

            aryOrder[iSourceOrder] += aryOrder[iTargetOrder]
            aryOrder[iTargetOrder:iTargetOrder+1] = []
            
        # Convert the final ordering into a stroke order array
        # - Only examine the first point index of each stored pair
        # - Convert it to a stroke index and a False/True reversed (or not) flag
        return [ ( aryOrder[0][i] >> 1, (aryOrder[0][i] & 0x1) ) for i in xrange(0,len(aryOrder[0]),2) ]

    #--------------------------------------------------------------------------
    # Function: mapStrokeToHan
    # 
    # Return the Han stroke index corresponding to the passed stroke index.
    # Note:
    # - Both indexes are 0-based.
    #--------------------------------------------------------------------------
    def mapStrokeToHan(self, iStroke):
        return self.__aryOrder[iStroke][0]

    #--------------------------------------------------------------------------
    # Function: getPoints
    # 
    # Return an array of Point arrays shaped and ordered as per the specification.
    #--------------------------------------------------------------------------
    def getPoints(self):
        # Begin with a copy of the points for each stroke in Han order
        xfPoints = [ [ Genome.Point(pt=pt) for pt in st.aryPointsForward ] for st in self.__han.aryStrokes ]
        
        # Apply stroke shaping
        for iS in xrange(len(self.__xfStrokes)):
            if self.__xfStrokes[iS]:
                self.__xfStrokes[iS].apply(xfPoints[iS], self.__han.aryStrokes[iS].bounds)
        
        # Apply group shaping
        for iG in xrange(len(self.__xfGroups)):
            if self.__xfGroups[iG]:
                hanGroup = self.__han.aryGroups[iG]
                for iS in hanGroup.containedStrokes:
                    self.__xfGroups[iG].apply(xfPoints[iS], hanGroup.bounds)
        
        # Apply gene shaping
        # - If the caller provided gene shaping, then merge it with the default
        # - Otherwise, use the default shaping
        xf = self.__xf and Transform(sx=(self.__xf.sx*Constants.sxDefault), sy=(self.__xf.sy*Constants.syDefault), dx=self.__xf.dx, dy=self.__xf.dy) or Transform(sx=Constants.sxDefault, sy=Constants.syDefault)
        iP = 0
        for pts in xfPoints:
            xf.apply(pts)
                
        # Order the points (reversing any as requested)
        xfPoints = [ fR and xfPoints[iS].reverse() or xfPoints[iS] for iS, fR in self.__aryOrder ]
                
        # Add points for incoherent ranges and convert all into tuples that include a coherency flag
        xfPoints = [ [ not i%2 and True or False, (i%2 and i/2 < len(xfPoints) and [ Genome.Point(pt=xfPoints[(i/2)][-1]), Genome.Point(pt=xfPoints[(i+1)/2][0]) ] or xfPoints[i/2]) ] for i in xrange(len(xfPoints)*2-1) ]
        
        # Add any requested incoherent head and tail
        # (This is performed here so they the preceding code does not treat them as coherent segments)
        if self.__ptHead:
            xfPoints.insert(0, [ False, [ self.__ptHead, ptStart ] ])
        if self.__ptTail:
            ptEnd = xfPoints[-1][-1]
            xfPoints.append([ False, [ ptEnd, Genome.Point(x=(ptEnd.x + self.__ptTail.x), y=(ptEnd.y + self.__ptTail.y)) ] ])
        
        # Offset the points such that they always begin at the origin (less any user-specified displacment)
        ptStart = xfPoints[0][1][0]
        if ptStart.x != 0 or ptStart.y != 0:
            dx = self.__xf and self.__xf.dx or 0
            dy = self.__xf and self.__xf.dy or 0
            xf = Transform(dx=(dx-ptStart.x), dy=(dy-ptStart.y))
            iP = 0
            for fCoherent, pts in xfPoints:
                xf.apply(pts)

        return xfPoints
        
    def __isDefault(self):
        return (not self.__aryOrder or self.__fOrderHan) and not self.__ptHead and not self.__ptTail and not self.__xf and not self.__fHasGroup and not self.__fHasStroke
    isDefault = property(__isDefault)
        
    def toName(self, strUnicode):
        if self.isDefault:
            return strUnicode
        else:
            return '%s-%s%s%s%s%s%s' % (strUnicode,
                                        (self.__aryOrder and not self.__fOrderHan) and '-o%s' % '_'.join([ '%d%s' % (i+1, f and 'r' or '') for i,f in self.__aryOrder ]) or '',
                                        self.__ptHead and '-h%d_%d' % (self.__ptHead.x, self.__ptHead.y) or '',
                                        self.__ptTail and '-t%d_%d' % (self.__ptTail.x, self.__ptTail.y) or '',
                                        self.__xf and '-%s' % self.__xf.name or '',
                                        self.__fHasGroup and '-' + '-'.join(['g%d_%s' % (i+1, self.__xfGroups[i].name) for i in xrange(len(self.__xfGroups)) if self.__xfGroups[i]]) or '',
                                        self.__fHasStroke and '-' + '-'.join(['s%d_%s' % (i+1, self.__xfStrokes[i].name) for i in xrange(len(self.__xfStrokes)) if self.__xfStrokes[i]]) or '')

    def __str__(self):
        if self.isDefault:
            return 'default'
        else:
            aryGene = []
            if self.__aryOrder:
                aryGene.append('o%s' %','.join([ '%d%s' % (i+1, f and 'r' or '') for i,f in self.__aryOrder]))
            if self.__ptHead:
                aryGene.append('h%s' % str(self.__ptHead))
            if self.__ptTail:
                aryGene.append('t%s' % str(self.__ptHead))
            if self.__xf:
                aryGene.append(str(self.__xf))
            aryGene += [ 'g%d(%s)' % (i+1, str(self.__xfGroups[i])) for i in xrange(len(self.__xfGroups)) if self.__xfGroups[i] ]
            aryGene += [ 'g%d(%s)' % (i+1, str(self.__xfStrokes[i])) for i in xrange(len(self.__xfStrokes)) if self.__xfStrokes[i] ]
            return ':'.join(aryGene)

#==============================================================================
# Helper Functions
#==============================================================================
#------------------------------------------------------------------------------
# Function: setGlobals
# 
#------------------------------------------------------------------------------
def setGlobals(aryArgs=[], strArgs=''):
    envArgs = Common.readEnvironment('$STYLUS_INSCRIBEARGS')
    argv = envArgs and envArgs.split() or []
    argv += aryArgs
    argv += strArgs.split()
    
    Globals.strGenePath = Common.readEnvironment('$STYLUS_INSCRIBEOUT')
    Globals.urlHan = Common.readEnvironment('$STYLUS_HANURL')
    Globals.strAuthor = Common.readEnvironment('$STYLUS_AUTHOR')

    try:
        opts, remaining = getopt.getopt(argv,
                    'c:d:g:o:u:a:qh',
                    [ 'code=', 'definition', 'gene=', 'output=', 'urls=', 'author=', 'quiet', 'help' ])
        if len(remaining) > 0:
            remaining[0].strip()
            if len(remaining) > 1 or remaining[0]:
                raise Usage(' '.join(remaining) + ' contains unexpected arguments')
    except getopt.error, err:
        raise Usage(' '.join(argv[1:]) + ' contains unknown arguments')

    for option, value in opts:
        if option in ('-c', '--code'):
            if not Constants.reUnicode.match(value):
                raise Usage(value + ' is not a valid Unicode number')
            Globals.uchHan = value

        if option in ('-d', '--definition'):
            Globals.fBuildArchetype = True
            Globals.strArchetypePath = value

        if option in ('-g', '--gene'):
            Globals.aryGenes.append(value)

        if option in ('-o', '--output'):
            Globals.strGenePath = value

        if option in ('-u', '--urls'):
            Globals.urlHan = value
            
        if option in ('-a', '--author'):
            Globals.strAuthor = value

        if option in ('-q', '--quiet'):
            Common.Globals.fQuiet = True

        if option in ('-h', '--help'):
            raise Usage('')

    if Globals.fInteractive and not Globals.uchHan:
        raise Usage('Required code was not specified')

    if Globals.fBuildArchetype and not Globals.strArchetypePath:
        raise Usage('Required archetype path was not specified')

    if Globals.fBuildArchetype:
        Globals.strArchetypePath = Common.resolvePath(Globals.strArchetypePath)
        if not os.path.exists(Globals.strArchetypePath):
            try: os.makedirs(Globals.strArchetypePath)
            except OSError: raise Usage('Unable to create ' + Globals.strArchetypePath)
        
    if len(Globals.aryGenes) > 0 and not Globals.strGenePath:
        raise Usage('Required gene output path was not specified')

    if len(Globals.aryGenes) > 0:
        Globals.strGenePath = Common.resolvePath(Globals.strGenePath)
        if not os.path.exists(Globals.strGenePath):
            try: os.makedirs(Globals.strGenePath)
            except OSError: raise Usage('Unable to create ' + Globals.strGenePath)
        
    if not Globals.urlHan:
        raise Usage('Required Han URL was not specified')
    Globals.urlHan = Common.pathToURL(Globals.urlHan, Common.Constants.schemeFile)
    
#------------------------------------------------------------------------------
# Function: loadHan
# 
#------------------------------------------------------------------------------
def loadHan(strUnicode):
    urlHan = Common.pathToURL(Common.makeHanPath(strUnicode + Common.Constants.extHan), Globals.urlHan)
    try: han = Genome.Han(urlHan)
    except LookupError, err: raise Common.BiologicError('%s is missing one or more required elements or attributes - %s' % (urlHan, str(err)))
    except OSError, err: raise Common.BiologicError('Unable to open URL %s - %s' % (urlHan, str(err)))
    except urllib2.URLError, err: raise Common.BiologicError('Unable to open URL %s - %s' % (urlHan, str(err)))
    return han

#==============================================================================
# Main Routines
#==============================================================================
#------------------------------------------------------------------------------
# Function: buildHan
# 
#------------------------------------------------------------------------------
def buildHan(uchHan):
    Common.say('Creating Han Definition file for ' + uchHan)

    hcf = Genome.HCF(Common.pathToURL(Common.makeHanPath(uchHan + Common.Constants.extHCF), Globals.urlHan))
    
    aryGroups = [ _HAN_GROUP % (str(hcfG.bounds), hcfG.length, hcfG.ptCenter.x, hcfG.ptCenter.y,
                            ' '.join([ str(i+1) for i in hcfG.containedStrokes])) for hcfG in hcf.aryGroups ]
    aryStrokes = [ _HAN_STROKE % (str(hcfS.bounds),
                                hcfS.length,
                                '\n'.join([ _HAN_POINT % (ptd.x, ptd.y, ptd.distance) for ptd in hcfS.aryPointsForward]),
                                '\n'.join([ _HAN_POINT % (ptd.x, ptd.y, ptd.distance) for ptd in hcfS.aryPointsReverse]) ) for hcfS in hcf.aryStrokes ]
    aryOverlaps = [ _HAN_OVERLAP % (hcfO.firstStroke, hcfO.secondStroke, hcfO.fRequired and 'true' or 'false') for hcfO in hcf.aryOverlaps ]
    strHan = _HAN_DEFINITION % (str(uuid.uuid4()).upper(), hcf.unicode, datetime.datetime.utcnow().isoformat(), _NAME,
                                str(hcf.bounds), hcf.length, hcf.minimumStrokeLength,
                                '\n'.join(aryGroups),
                                '\n'.join(aryStrokes),
                                aryOverlaps and ('<overlaps>%s</overlaps>' % '\n'.join(aryOverlaps)) or '')
                                
    strPath = Common.resolvePath(os.path.join(Globals.strArchetypePath, Common.makeHanPath(hcf.unicode + Common.Constants.extHan)))
    strDir = os.path.dirname(strPath)
    if not os.path.exists(strDir):
        try: os.makedirs(os.path.dirname(strPath))
        except OSError, err: raise Common.BiologicError('Unable to create %s - %s' % (strDir, str(err)))

    try:
        fileHan = os.open(strPath, os.O_CREAT | os.O_TRUNC | os.O_WRONLY, 0664)
        os.write(fileHan, strHan)
    except IOError, err: raise Common.BiologicError('Unable to create %s - %s' % (strPath, str(err)))
    os.close(fileHan)
    
    Common.say('Han definition written to ' + strPath)
    return

#------------------------------------------------------------------------------
# Function: buildSegment
# 
#------------------------------------------------------------------------------
def buildSegment(ptStart, fCoherent, aryPoints):

    # For incoherent, horizontal, or vertical straight segments, select vectors by minimizing distance to the target point
    if len(aryPoints) <= 2 and (not fCoherent or (aryPoints[0].x - aryPoints[1].x) == 0 or (aryPoints[0].y - aryPoints[1].y) == 0):
        aryVectors = []
        ln = Genome.Line(ptStart, ptStart)
    
        for ptTarget in aryPoints[1:]:
            ln.ptEnd = ptTarget
        
            while ln.length >= Codons.Constants.vectorShort:
                idVector = Codons.Vectors.create(ln.direction, (ln.length >= Codons.Constants.vectorMedium and Codons.Constants.iVectorMedium or Codons.Constants.iVectorShort))
                vector = Codons.Vectors.toVector(idVector)
                aryVectors.append(idVector)
                ln.ptStart = Genome.Point(x=(ln.ptStart.x + vector.dx), y=(ln.ptStart.y + vector.dy))
    
        ptEnd = Genome.Point(x=ln.ptStart.x, y=ln.ptStart.y)

    # For all others, select vectors by attempting to minimize the deviation between them and the traced segment
    else:
        # First, create a scaled set of points with the associated fractional distance
        aryPtd = [ Genome.PointDistance(x=aryPoints[0].x, y=aryPoints[0].y, distance=0) ]
        lengthPts = 0
        for i in xrange(1,len(aryPoints)):
            lengthPts += Genome.Line(aryPoints[i-1], aryPoints[i]).length
            aryPtd.append(Genome.PointDistance(x=aryPoints[i].x, y=aryPoints[i].y, distance=lengthPts))
        for ptd in aryPtd:
            ptd.distance /= lengthPts

        # Next, select vectors that minimize the deviation to the lines of the given points
        # - Assume a length near to that of the given points to start
        # - Deviation is the same as in Stylus; the distance between the point and the point at the same fractional distance
        #   from among those in the traced segment
        # - Iterate until deviation no longer improves or the ending point begins to wander away
        # - The loop disregards the initial deviation so as to best fit the segment; the initial deviation is adjust for
        #   at completion
        aryVectorMedium = [ Codons.Vectors.NorthMedium,
                            Codons.Vectors.NortheastMedium,
                            Codons.Vectors.EastMedium,
                            Codons.Vectors.SoutheastMedium, 
                            Codons.Vectors.SouthMedium,
                            Codons.Vectors.SouthwestMedium,
                            Codons.Vectors.WestMedium,
                            Codons.Vectors.NorthwestMedium
                            ]

        maxDeviation = sys.maxint
        ptEnd = Genome.Point(pt=ptStart)
        aryVectors = []
        lengthVectors = ((lengthPts * 0.90) // Codons.Constants.vectorMedium) * Codons.Constants.vectorMedium

        ptStartOffset = Genome.Point(aryPtd[0].x - ptStart.x, aryPtd[0].y - ptStart.y)

        while True:
            ptEndCurrent = Genome.Point(pt=ptStart)
            maxDeviationCurrent = -sys.maxint-1
            aryVectorsCurrent = []
            lengthCurrent = 0
            while lengthCurrent < lengthVectors:
                idSelected = Codons.Vectors.Stop
                deviationSelected = sys.maxint
                for idVector in aryVectorMedium:
                    vector = Codons.Vectors.toVector(idVector)
                    ln = Genome.Line(Genome.Point(x=ptEndCurrent.x+vector.dx+ptStartOffset.x, y=ptEndCurrent.y+vector.dy+ptStartOffset.y),
                                    Genome.getPointBetween(aryPtd, (lengthCurrent + vector.length) / lengthVectors))
                    if deviationSelected > ln.length:
                        deviationSelected = ln.length
                        idSelected = idVector

                maxDeviationCurrent = max(maxDeviationCurrent, deviationSelected)
                aryVectorsCurrent.append(idSelected)
                vector = Codons.Vectors.toVector(idSelected)
                ptEndCurrent.x += vector.dx
                ptEndCurrent.y += vector.dy
                lengthCurrent += (vector.length // Codons.Constants.vectorMedium) * Codons.Constants.vectorMedium

            # Terminate when either
            # - Deviation begins to worsen, rather than improve
            # - Or, the vectors have not changed *and* the assumed length would grow by less than 1/2 of a short vector (basically, it's not likely to make a difference)
            lnCurrent = Genome.Line(ptEndCurrent, aryPoints[-1])
            if maxDeviationCurrent >= maxDeviation or (aryVectorsCurrent == aryVectors and lnCurrent.length < (Codons.Constants.vectorShort/2.0)):
                break

            maxDeviation = maxDeviationCurrent
            aryVectors = aryVectorsCurrent
            ptEnd = ptEndCurrent
            lengthVectors += lnCurrent.length

    return ptEnd, aryVectors
    
#------------------------------------------------------------------------------
# Function: validateCoherence
# 
#------------------------------------------------------------------------------
def validateCoherence(arySegments):
    # Collapse all segments into a single list and measure coherence
    aryVectors = [ i for f, ary in arySegments for i in ary ]
    aryCoherence = [ 0 for i in xrange(len(aryVectors)) ]
    for i in xrange(2, len(aryVectors)):
        if Codons.isCoherent([ aryVectors[i-2], aryVectors[i-1], aryVectors[i-0] ]):
            aryCoherence[i-2] += 1
            aryCoherence[i-1] += 1
            aryCoherence[i-0] += 1
            
    # Divide measured coherence into lists matching the original segments
    for i in xrange(len(arySegments)):
        aryCoherence[i:i] = [ aryCoherence[i:i+len(arySegments[i][1]) ] ]
        aryCoherence[i+1:i+1+len(arySegments[i][1])] = []

    # Check the expected coherence of each segment against that measured
    for i in xrange(len(arySegments)):
        fCoherent, aryVectors = arySegments[i]
        if (fCoherent and aryCoherence[i].count(0)) or (not fCoherent and (aryCoherence[i].count(0) != len(aryCoherence[i]))):
            if i > 0:
                fC, aryV = arySegments[i-1]
                Common.sayError('Coherent(%c) %d - %s' % (fC and 'T' or 'F', len(aryV), ' '.join([ Codons.Vectors.toName(id) for id in aryV ])))
            Common.sayError('Coherent(%c) %d - %s' % (fCoherent and 'T' or 'F', len(aryVectors), ' '.join([ Codons.Vectors.toName(id) for id in aryVectors ])))
            Common.sayError('                - %s' % ' '.join([ ' %d ' % j for j in aryCoherence[i] ]))
            if i < len(arySegments)-1:
                fC, aryV = arySegments[i+1]
                Common.sayError('Coherent(%c) %d - %s' % (fC and 'T' or 'F', len(aryV), ' '.join([ Codons.Vectors.toName(id) for id in aryV ])))
            raise Common.BiologicError('Failed to create a gene with proper coherence - segment %d should be %s but has %s vectors' % (i+1,
                                                                                                                                fCoherent and 'Coherent' or 'Incoherent',
                                                                                                                                fCoherent and 'Incoherent' or 'Coherent'))
    
#------------------------------------------------------------------------------
# Function: buildGenes
# 
#------------------------------------------------------------------------------
def buildGenes(uchHan, aryGenes):
    Common.say('Creating %d gene(s)' % len(aryGenes))
    
    han = loadHan(uchHan)
    
    strAuthor = Globals.strAuthor and (" author='%s'" % Globals.strAuthor) or ''

    aryGeneNames = []
    for specification in aryGenes:
        Common.say('Creating gene from specification ' + specification)

        gs = GeneSpecification(specification != Constants.strDefault and specification or '', han)
        gsName = gs.toName(han.unicode) + Common.Constants.extGene
        gsPoints = gs.getPoints()
        Common.say('Gene to be named ' + gsName)

        ptCurrent = Genome.Point(pt=gsPoints[0][1][0])
        arySegments = []

        # Convert each set of points into a list of vectors
        for iSegment in xrange(len(gsPoints)):
            fCoherent, aryPoints = gsPoints[iSegment]
            
            # Build the segment starting from the current location
            # - Ensure incoherent segments always begin at the current location
            #   (This causes moves to absorb the tracing error, effectively trading placement error for stroke fit error.)
            if not fCoherent:
                aryPoints[0].x = ptCurrent.x
                aryPoints[0].y = ptCurrent.y
            ptCurrent, aryVectors = buildSegment(ptCurrent, fCoherent, aryPoints)
            
            if not fCoherent:
                # If the segment contains too few vectors, pad it with an incoherent sequence
                # - If there are no vectors, use No/So/Ea/We - binding code will ensure proper coherence at the endpoints
                # - Otherwise, use the four points of the direction "compass" that are guaranteed incoherent with the last vector
                if len(aryVectors) < 3:
                    iDirection = len(aryVectors) and Codons.Directions.add(Codons.Vectors.toDirection(aryVectors[-1]), 3) or Codons.Directions.North
                    aryVectors.append(Codons.Vectors.create(iDirection))
                    aryVectors.append(Codons.Vectors.create(Codons.Directions.toOpposite(iDirection)))
                    
                    iDirection = Codons.Directions.add(iDirection, 2)
                    aryVectors.append(Codons.Vectors.create(iDirection))
                    aryVectors.append(Codons.Vectors.create(Codons.Directions.toOpposite(iDirection)))
                    
                # Inject vectors to force incoherency for incoherent segments
                # - Essentially, add a vector pair to every two that forces incoherency
                # - Walking the list must take into account injected vector pairs
                else:
                    iVector = 0
                    while iVector < len(aryVectors):
                        if Codons.isCoherent([aryVectors[iVector-2], aryVectors[iVector-1], aryVectors[iVector+0]]):
                            idVector = aryVectors[iVector]
                            aryVectors.insert(iVector+0, Codons.Vectors.toOpposite(idVector))
                            aryVectors.insert(iVector+1, idVector)
                        iVector += 1

            # Ensure the vectors "bind" without affecting the coherence of an adjoining segment
            if iSegment:
                fCoherencePrev, aryVectorsPrev = arySegments[-1]
                if Codons.isCoherent([ aryVectorsPrev[-2], aryVectorsPrev[-1], aryVectors[0] ]) or Codons.isCoherent([ aryVectorsPrev[-1], aryVectors[0], aryVectors[1] ]):
                    if not fCoherencePrev:
                        aryVectorsPrev += [ Codons.Vectors.toOpposite(aryVectorsPrev[-1]), aryVectorsPrev[-1], aryVectors[0], Codons.Vectors.toOpposite(aryVectors[0]) ]
                    else:
                        aryVectors[:0] = [ Codons.Vectors.toOpposite(aryVectorsPrev[-1]), aryVectorsPrev[-1], aryVectors[0], Codons.Vectors.toOpposite(aryVectors[0]) ]

            arySegments.append((fCoherent, aryVectors))

        validateCoherence(arySegments)

        aryCodons = [ Codons.Vectors.toVector(idVector).codon for fCoherent, aryVectors in arySegments for idVector in aryVectors ]
        aryCodons[:0] = [ 'ATG' ]
        aryCodons.append(Codons.Vectors.toVector(Codons.Vectors.create(Codons.Directions.Stop, Codons.Constants.iVectorShort)).codon)

        aryStrokes = []
        iStroke = 0
        iBase = 4
        for fCoherent, aryVectors in arySegments:
            if fCoherent:
                aryStrokes.append(_GENE_STROKE % (iBase, iBase+(len(aryVectors)*3-1), gs.mapStrokeToHan(iStroke)+1))
                iStroke += 1
            iBase += len(aryVectors) * 3

        strGene = _GENE_DEFINITION % (str(uuid.uuid4()).upper(), strAuthor, datetime.datetime.utcnow().isoformat(), _NAME, str(gs),
                                    ''.join(aryCodons), len(aryCodons)*3,
                                    gsPoints[0][1][0].x, gsPoints[0][1][0].y,
                                    han.unicode,
                                    '\n'.join(aryStrokes))

        strPath = Common.resolvePath(os.path.join(Globals.strGenePath, Common.makeHanPath(gsName)))
        strDir = os.path.dirname(strPath)
        if not os.path.exists(strDir):
            try: os.makedirs(os.path.dirname(strPath))
            except OSError, err: raise Common.BiologicError('Unable to create %s - %s' % (strDir, str(err)))
        
        try:
            fileGene = os.open(strPath, os.O_CREAT | os.O_TRUNC | os.O_WRONLY, 0664)
            os.write(fileGene, strGene)
        except IOError, err: raise Common.BiologicError('Unable to create %s - %s' % (strPath, str(err)))
        os.close(fileGene)
        
        Common.say('\tWrote %s - %d codons, %d bases' % (strPath, len(aryCodons), len(aryCodons)*3))
        aryGeneNames.append(gsName)

    return aryGeneNames

#------------------------------------------------------------------------------
# Function: main
# 
#------------------------------------------------------------------------------
def main(argv=None):
    try:
        Globals.fInteractive = True
        Common.Globals.fQuiet = False

        setGlobals(sys.argv[1:])

        if Globals.fBuildArchetype:
            Common.say('Archetypes Directory: %s' % Globals.strArchetypePath)
        if len(Globals.aryGenes) > 0:
            Common.say('Gene Directory      : %s' % Globals.strGenePath)
        Common.say('Han URL             : %s' % Globals.urlHan)
    
        if Globals.fBuildArchetype:
            buildHan(Globals.uchHan)

        if Globals.aryGenes:
            buildGenes(Globals.uchHan, Globals.aryGenes)

        return 0

    except Common.BiologicError, err:
        Common.sayError(err.msg)
        return 2

if __name__ == "__main__":
    sys.exit(main())
