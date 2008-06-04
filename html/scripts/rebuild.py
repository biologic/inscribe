#!/usr/bin/python
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
rebuild.py

Re-build all Han and gene definition files from the local HCF files.

Note:
Run this script from its current directory (e.g., ./rebuild.py) within the Han directory

Copyright (c) 2008 Biologic Institute, LLC. All rights reserved.
'''

import fnmatch
import geneMaker
import getopt
import os
import os.path
import re
import stylus.common as Common
import stylus.genome as Genome
import sys

reHCF = re.compile(r'([A-Fa-f\d]+)\.hcf')
reGENE = re.compile(r'([A-Fa-f\d]+).*\.gene')

geneMaker.setGlobals([ '-o', './../', '-u', './../' ])

class Globals:
    fErase = False
    strDirPattern = '[123456789]000'
    fBuildHan = False
    fBuildGenes = False

def getArguments():
    try:
        opts, remaining = getopt.getopt(sys.argv[1:], 'ep:hg', [ 'erase', 'pattern=', 'han', 'genes' ])
    except getopt.error, err:
        raise BiologicError(str(err))

    for option, value in opts:
        if option in ('-e', '--erase'):
            Globals.fErase = True

        if option in ('-p', '--pattern'):
            Globals.strDirPattern = value
            
        if option in ('-h', '--han'):
            Globals.fBuildHan = True
            
        if option in ('-g', '--genes'):
            Globals.fBuildGenes = True
            
    if not Globals.fBuildHan and not Globals.fBuildGenes:
        Globals.fBuildGenes = not Globals.fErase

#----------------------------------------------------------------------------------------------------------------------------------------
getArguments()
for folder in fnmatch.filter(os.listdir('..'), Globals.strDirPattern):
    print 'Examining directory %s' % folder

    if Globals.fErase:
        for han in fnmatch.filter(os.listdir(os.path.join('..', folder)), '*.han'):
            os.remove(os.path.join('..', folder, han))
        for gene in fnmatch.filter(os.listdir(os.path.join('..', folder)), '*.gene'):
            os.remove(os.path.join('..', folder, gene))

    if Globals.fBuildHan:
        print 'Creating Han definitions'
        nCount = 0
        for hcf in fnmatch.filter(os.listdir(os.path.join('..', folder)), '*.hcf'):
            uchHan = reHCF.match(hcf).groups()[0]
            geneMaker.buildHan(uchHan)
            nCount += 1
            print '\t%s definition created' % uchHan
        print '\t%d definitions created' % nCount

    if Globals.fBuildGenes:
        print 'Creating default genes'
        nCount = 0
        for hcf in fnmatch.filter(os.listdir(os.path.join('..', folder)), '*.hcf'):
            uchHan = reHCF.match(hcf).groups()[0]
            aryGeneNames = geneMaker.buildGenes(uchHan, [ 'default' ])
            nCount += 1
            print '\t%s gene created' % uchHan
        
        print 'Rebuilding existing genes'
        for gene in fnmatch.filter(os.listdir(os.path.join('..', folder)), '*.gene'):
            path = os.path.realpath('../' + folder + '/' + gene)
            genome = Genome.Genome('file://' + path)
            if genome.creationParameters != 'default':
                uchGene = reGENE.match(gene).groups()[0]
                aryGeneNames = geneMaker.buildGenes(uchGene, [ genome.creationParameters ])
                nCount += 1
                print '\t%s Rebuilt gene with parameters %s' % (uchGene, genome.creationParameters)
        print '\t%d genes created' % nCount
