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
codons.py

This script contains codon related data used by Stylus scripts.

Stylus, Copyright 2006-2008 Biologic Institute.
'''

import random
import re

#==============================================================================
# Global Constants
#==============================================================================
# Note:
# These values are identical to those used by Stylus when compiled with double precision
_E = 2.71828182845905
_ONE_OVER_SQRT2 = 0.707106781186548

class Constants:
    reSPLITCODONS = re.compile(r'(.{3})')

    # Indexes into vector arrays by vector length
    iVectorShort = 0
    iVectorMedium = 1
    iVectorLong = 2

    vectorShort = 1
    vectorMedium = 1.648721270700128;
    vectorLong = _E;
    stepDiagonalShort = _ONE_OVER_SQRT2;
    stepDiagonalMedium = 1.165821990798562;

# Directions
class Directions:
    Stop = 0
    North = 1
    Northeast = 2
    East = 3
    Southeast = 4
    South = 5
    Southwest = 6
    West = 7
    Northwest = 8

    __mapDirectionToName = [
        'STP',
        'No',
        'Ne',
        'Ea',
        'Se',
        'So',
        'Sw',
        'We',
        'Nw'
        ]
    def __toName(iDirection):
        return Directions.__mapDirectionToName[iDirection]
    toName = staticmethod(__toName)

    __mapDirectionToOpposite = [
        Stop,
        South,
        Southwest,
        West,
        Northwest,
        North,
        Northeast,
        East,
        Southeast
        ]
    def __toOpposite(iDirection):
        return Directions.__mapDirectionToOpposite[iDirection]
    toOpposite = staticmethod(__toOpposite)
    
    def __add(iDirection, nDirection):
        return ((iDirection - 1 + nDirection) % 8) + 1
    add = staticmethod(__add)
    
    def __sub(iDirection, nDirection):
        return ((iDirection - 1 + 8 - nDirection) % 8) + 1
    sub = staticmethod(__sub)
    
# Vector identifiers
class Vectors:
    Stop = 0

    NorthShort = 1
    NorthMedium = 2
    NorthLong = 3

    NortheastShort = 4
    NortheastMedium = 5

    EastShort = 6
    EastMedium = 7
    EastLong = 8

    SoutheastShort = 9
    SoutheastMedium = 10

    SouthShort = 11
    SouthMedium = 12
    SouthLong = 13

    SouthwestShort = 14
    SouthwestMedium = 15

    WestShort = 16
    WestMedium = 17
    WestLong = 18

    NorthwestShort = 19
    NorthwestMedium = 20
    
    __mapFromDirectionLengthToVector = [
            [ Stop ],
            [ NorthShort, NorthMedium, NorthLong ],
            [ NortheastShort, NortheastMedium ],
            [ EastShort, EastMedium, EastLong ],
            [ SoutheastShort, SoutheastMedium ],
            [ SouthShort, SouthMedium, SouthLong ],
            [ SouthwestShort, SouthwestMedium ],
            [ WestShort, WestMedium, WestLong ],
            [ NorthwestShort, NorthwestMedium ]
        ]
    
    def __create(iDirection, iLength=Constants.iVectorMedium):
        return Vectors.__mapFromDirectionLengthToVector[iDirection][iLength]
    create = staticmethod(__create)
    
    __mapVectorToDirection = [
        Directions.Stop,

        Directions.North,
        Directions.North,
        Directions.North,
        
        Directions.Northeast,
        Directions.Northeast,

        Directions.East,
        Directions.East,
        Directions.East,

        Directions.Southeast,
        Directions.Southeast,

        Directions.South,
        Directions.South,
        Directions.South,
        
        Directions.Southwest,
        Directions.Southwest,

        Directions.West,
        Directions.West,
        Directions.West,

        Directions.Northwest,
        Directions.Northwest
        ]

    def __toDirection(id):
        return Vectors.__mapVectorToDirection[id]
    toDirection = staticmethod(__toDirection)
    
    __mapVectorToLength = [
        Constants.iVectorShort,

        Constants.iVectorShort,
        Constants.iVectorMedium,
        Constants.iVectorLong,
        
        Constants.iVectorShort,
        Constants.iVectorMedium,

        Constants.iVectorShort,
        Constants.iVectorMedium,
        Constants.iVectorLong,

        Constants.iVectorShort,
        Constants.iVectorMedium,

        Constants.iVectorShort,
        Constants.iVectorMedium,
        Constants.iVectorLong,
        
        Constants.iVectorShort,
        Constants.iVectorMedium,

        Constants.iVectorShort,
        Constants.iVectorMedium,
        Constants.iVectorLong,

        Constants.iVectorShort,
        Constants.iVectorMedium
        ]

    def __toLength(id):
        return Vectors.__mapVectorToLength[id]
    toLength = staticmethod(__toLength)
    
    # Indexed by vector identifier
    __mapVectorToName = [
        'STP',

        'Nos',
        'Nom',
        'Nol', 

        'Nes',
        'Nem',

        'Eas',
        'Eam',
        'Eal',

        'Ses',
        'Sem',

        'Sos',
        'Som',
        'Sol',

        'Sws',
        'Swm',

        'Wes',
        'Wem',
        'Wel',

        'Nws',
        'Nwm'
        ]

    def __toName(id):
        return Vectors.__mapVectorToName[id]
    toName = staticmethod(__toName)
    
    __mapVectorToOpposite = [
        Stop,

        SouthShort,
        SouthMedium,
        SouthLong,

        SouthwestShort,
        SouthwestMedium,

        WestShort,
        WestMedium,
        WestLong,

        NorthwestShort,
        NorthwestMedium,

        NorthShort,
        NorthMedium,
        NorthLong,

        NortheastShort,
        NortheastMedium,

        EastShort,
        EastMedium,
        EastLong,

        SoutheastShort,
        SoutheastMedium
        ]

    def __toOpposite(id):
        return Vectors.__mapVectorToOpposite[id]
    toOpposite = staticmethod(__toOpposite)
    
    def __toVector(id):
        return _vectors[id]
    toVector = staticmethod(__toVector)

# Indexed by codon numeric value
_mapCodonToVector = [
    Vectors.NorthLong, #  00 - TTT
    Vectors.NorthLong, #  01 - TTC
    Vectors.NorthMedium, #  02 - TTA
    Vectors.NorthMedium, #  03 - TTG
    
    Vectors.SoutheastMedium, #  04 - TCT
    Vectors.SoutheastMedium, #  05 - TCC
    Vectors.SoutheastMedium, #  06 - TCA
    Vectors.SoutheastMedium, #  07 - TCG
    
    Vectors.SouthLong, #  08 - TAT
    Vectors.SouthLong, #  09 - TAC
    Vectors.Stop, #  10 - TAA
    Vectors.Stop, #  11 - TAG
    
    Vectors.NorthwestMedium, #  12 - TGT
    Vectors.NorthwestMedium, #  13 - TGC
    Vectors.Stop, #  14 - TGA
    Vectors.NorthwestMedium, #  15 - TGG
    
    Vectors.NorthShort, #  16 - CTT
    Vectors.NorthShort, #  17 - CTC
    Vectors.NorthShort, #  18 - CTA
    Vectors.NorthShort, #  19 - CTG
    
    Vectors.SoutheastShort, #  20 - CCT
    Vectors.SoutheastShort, #  21 - CCC
    Vectors.SoutheastShort, #  22 - CCA
    Vectors.SoutheastShort, #  23 - CCG
    
    Vectors.SouthMedium, #  24 - CAT
    Vectors.SouthMedium, #  25 - CAC
    Vectors.SouthShort, #  26 - CAA
    Vectors.SouthShort, #  27 - CAG
    
    Vectors.NorthwestShort, #  28 - CGT
    Vectors.NorthwestShort, #  29 - CGC
    Vectors.NorthwestShort, #  30 - CGA
    Vectors.NorthwestShort, #  31 - CGG
    
    Vectors.NortheastMedium, #  32 - ATT
    Vectors.NortheastMedium, #  33 - ATC
    Vectors.NortheastMedium, #  34 - ATA
    Vectors.NortheastMedium, #  35 - ATG
    
    Vectors.EastLong, #  36 - ACT
    Vectors.EastLong, #  37 - ACC
    Vectors.EastMedium, #  38 - ACA
    Vectors.EastMedium, #  39 - ACG
    
    Vectors.SouthwestMedium, #  40 - AAT
    Vectors.SouthwestMedium, #  41 - AAC
    Vectors.SouthwestMedium, #  42 - AAA
    Vectors.SouthwestMedium, #  43 - AAG
    
    Vectors.WestLong, #  44 - AGT
    Vectors.WestLong, #  45 - AGC
    Vectors.WestMedium, #  46 - AGA
    Vectors.WestMedium, #  47 - AGG
    
    Vectors.NortheastShort, #  48 - GTT
    Vectors.NortheastShort, #  49 - GTC
    Vectors.NortheastShort, #  50 - GTA
    Vectors.NortheastShort, #  51 - GTG
    
    Vectors.EastShort, #  52 - GCT
    Vectors.EastShort, #  53 - GCC
    Vectors.EastShort, #  54 - GCA
    Vectors.EastShort, #  55 - GCG
    
    Vectors.SouthwestShort, #  56 - GAT
    Vectors.SouthwestShort, #  57 - GAC
    Vectors.SouthwestShort, #  58 - GAA
    Vectors.SouthwestShort, #  59 - GAG
    
    Vectors.WestShort, #  60 - GGT
    Vectors.WestShort, #  61 - GGC
    Vectors.WestShort, #  62 - GGA
    Vectors.WestShort  #  63 - GGG
    ]

#==============================================================================
# Classes
#==============================================================================
class Vector(object):
    def __toName(self):
        return Vectors.toName(self.id)
    name = property(__toName)
    
    def __toCodon(self):
        return random.choice(self.codons)
    codon = property(__toCodon)
    
    def __str__(self):
        return self.name
    
class STP(Vector):
    def __init__(self):
        self.dx = 0
        self.dy = 0
        self.length = 0
        self.direction = 0
        self.id = Vectors.Stop
        self.codons = [ 'TAA', 'TAG', 'TGA' ]
        
class Nol(Vector):
    def __init__(self):
        self.dx = 0
        self.dy = Constants.vectorLong
        self.length = Constants.vectorLong
        self.direction = Directions.North
        self.id = Vectors.NorthLong
        self.codons = [ 'TTT', 'TTC' ]
    
class Nom(Vector):
    def __init__(self):
        self.dx = 0
        self.dy = Constants.vectorMedium
        self.length = Constants.vectorMedium
        self.direction = Directions.North
        self.id = Vectors.NorthMedium
        self.codons = [ 'TTA', 'TTG' ]
    
class Nos(Vector):
    def __init__(self):
        self.dx = 0
        self.dy = Constants.vectorShort
        self.length = Constants.vectorShort
        self.direction = Directions.North
        self.id = Vectors.NorthShort
        self.codons = [ 'CTT', 'CTC', 'CTA', 'CTG' ]


class Nem(Vector):
    def __init__(self):
        self.dx = Constants.stepDiagonalMedium
        self.dy = Constants.stepDiagonalMedium
        self.length = Constants.vectorMedium
        self.direction = Directions.Northeast
        self.id = Vectors.NortheastMedium
        self.codons = [ 'ATT', 'ATC', 'ATA', 'ATG' ]

class Nes(Vector):
    def __init__(self):
        self.dx = Constants.stepDiagonalShort
        self.dy = Constants.stepDiagonalShort
        self.length = Constants.vectorShort
        self.direction = Directions.Northeast
        self.id = Vectors.NortheastShort
        self.codons = [ 'GTT', 'GTC', 'GTA', 'GTG' ]

class Eal(Vector):
    def __init__(self):
        self.dx = Constants.vectorLong
        self.dy = 0
        self.length = Constants.vectorLong
        self.direction = Directions.East
        self.id = Vectors.EastLong
        self.codons = [ 'ACT', 'ACC' ]
    
class Eam(Vector):
    def __init__(self):
        self.dx = Constants.vectorMedium
        self.dy = 0
        self.length = Constants.vectorMedium
        self.direction = Directions.East
        self.id = Vectors.EastMedium
        self.codons = [ 'ACA', 'ACG' ]
    
class Eas(Vector):
    def __init__(self):
        self.dx = Constants.vectorShort
        self.dy = 0
        self.length = Constants.vectorShort
        self.direction = Directions.East
        self.id = Vectors.EastShort
        self.codons = [ 'GCT', 'GCC', 'GCA', 'GCG' ]
    
class Sem(Vector):
    def __init__(self):
        self.dx = Constants.stepDiagonalMedium
        self.dy = -Constants.stepDiagonalMedium
        self.length = Constants.vectorMedium
        self.direction = Directions.Southeast
        self.id = Vectors.SoutheastMedium
        self.codons = [ 'TCT', 'TCC', 'TCA', 'TCG' ]

class Ses(Vector):
    def __init__(self):
        self.dx = Constants.stepDiagonalShort
        self.dy = -Constants.stepDiagonalShort
        self.length = Constants.vectorShort
        self.direction = Directions.Southeast
        self.id = Vectors.SoutheastShort
        self.codons = [ 'CCT', 'CCC', 'CCA', 'CCG' ]

class Sol(Vector):
    def __init__(self):
        self.dx = 0
        self.dy = -Constants.vectorLong
        self.length = Constants.vectorLong
        self.direction = Directions.South
        self.id = Vectors.SouthLong
        self.codons = [ 'TAT', 'TAC' ]
    
class Som(Vector):
    def __init__(self):
        self.dx = 0
        self.dy = -Constants.vectorMedium
        self.length = Constants.vectorMedium
        self.direction = Directions.South
        self.id = Vectors.SouthMedium
        self.codons = [ 'CAT', 'CAC' ]
    
class Sos(Vector):
    def __init__(self):
        self.dx = 0
        self.dy = -Constants.vectorShort
        self.length = Constants.vectorShort
        self.direction = Directions.South
        self.id = Vectors.SouthShort
        self.codons = [ 'CAA', 'CAG' ]
    
class Swm(Vector):
    def __init__(self):
        self.dx = -Constants.stepDiagonalMedium
        self.dy = -Constants.stepDiagonalMedium
        self.length = Constants.vectorMedium
        self.direction = Directions.Southwest
        self.id = Vectors.SouthwestMedium
        self.codons = [ 'AAT', 'AAC', 'AAA', 'AAG' ]

class Sws(Vector):
    def __init__(self):
        self.dx = -Constants.stepDiagonalShort
        self.dy = -Constants.stepDiagonalShort
        self.length = Constants.vectorShort
        self.direction = Directions.Southwest
        self.id = Vectors.SouthwestShort
        self.codons = [ 'GAT', 'GAC', 'GAA', 'GAG' ]

class Wel(Vector):
    def __init__(self):
        self.dx = -Constants.vectorLong
        self.dy = 0
        self.length = Constants.vectorLong
        self.direction = Directions.West
        self.id = Vectors.WestLong
        self.codons = [ 'AGT', 'AGC' ]
    
class Wem(Vector):
    def __init__(self):
        self.dx = -Constants.vectorMedium
        self.dy = 0
        self.length = Constants.vectorMedium
        self.direction = Directions.West
        self.id = Vectors.WestMedium
        self.codons = [ 'AGA', 'AGG' ]
    
class Wes(Vector):
    def __init__(self):
        self.dx = -Constants.vectorShort
        self.dy = 0
        self.length = Constants.vectorShort
        self.direction = Directions.West
        self.id = Vectors.WestShort
        self.codons = [ 'GGT', 'GGC', 'GGA', 'GGG' ]
    
class Nwm(Vector):
    def __init__(self):
        self.dx = -Constants.stepDiagonalMedium
        self.dy = Constants.stepDiagonalMedium
        self.length = Constants.vectorMedium
        self.direction = Directions.Northwest
        self.id = Vectors.NorthwestMedium
        self.codons = [ 'TGT', 'TGC', 'TGG' ]

class Nws(Vector):
    def __init__(self):
        self.dx = -Constants.stepDiagonalShort
        self.dy = Constants.stepDiagonalShort
        self.length = Constants.vectorShort
        self.direction = Directions.Northwest
        self.id = Vectors.NorthwestShort
        self.codons = [ 'CGT', 'CGC', 'CGA', 'CGG' ]

#------------------------------------------------------------------------------
# Function: codonToVector
# 
# Retrieve the vector object for the passed codon
#------------------------------------------------------------------------------
def codonToVector(strCodon):
    return _vectors[_mapCodonToVector[(strCodon[0] == 'G' and 48 or (strCodon[0] == 'A' and 32 or (strCodon[0] == 'C' and 16 or 0))) +
                                    (strCodon[1] == 'G' and 12 or (strCodon[1] == 'A' and  8 or (strCodon[1] == 'C' and  4 or 0))) + 
                                    (strCodon[2] == 'G' and  3 or (strCodon[2] == 'A' and  2 or (strCodon[2] == 'C' and  1 or 0)))]]
                    
#------------------------------------------------------------------------------
# Function: codonToName
# 
# Retrieve the vector name for the passed codon
#------------------------------------------------------------------------------
def codonToName(strCodon):
    return codonToVector(strCodon).name

#------------------------------------------------------------------------------
# Function: toCodonCount
# 
#------------------------------------------------------------------------------
def toCodonCount(countBases):
    return (countBases + 2) / 3

#------------------------------------------------------------------------------
# Function: toCodonBoundary
# 
#------------------------------------------------------------------------------
def toCodonBoundary(baseIndex):
    return (baseIndex - (baseIndex % 3))

#------------------------------------------------------------------------------
# Function: toCodonIndex
# 
#------------------------------------------------------------------------------
def toCodonIndex(baseIndex):
    return toCodonBoundary(baseIndex) / 3
    
#------------------------------------------------------------------------------
# Function: isCoherent
# 
#------------------------------------------------------------------------------
def isCoherent(aryTrivector):
    return _COHERENCE[aryTrivector[0]][aryTrivector[1]][aryTrivector[2]]

if __name__ == "__main__":
    pass

# Indexed by vector identifier
_vectors = [
    STP(),

    Nos(),
    Nom(),
    Nol(),

    Nes(),
    Nem(),

    Eas(),
    Eam(),
    Eal(),

    Ses(),
    Sem(),

    Sos(),
    Som(),
    Sol(),

    Sws(),
    Swm(),

    Wes(),
    Wem(),
    Wel(),

    Nws(),
    Nwm()
    ]

# Triple indexed by vector identifier
_COHERENCE = [
    [
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ]
    ],

    [
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True  ],

    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True  ],

    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ]
    ],

    [
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True  ],

    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True  ],

    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ]
    ],

    [
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True  ],

    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True  ],

    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ]
    ],

    [
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True  ],

    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True  ],

    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True  ],

    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, True , True  ],

    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, True , True  ],

    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False ],

    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False ],

    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False ],

    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False ],

    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False ],

    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, False, True , True  ],

    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, False, True , True  ]
    ],

    [
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True  ],

    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True  ],

    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True  ],

    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, True , True  ],

    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, True , True  ],

    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False ],

    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False ],

    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False ],

    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False ],

    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False ],

    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, False, True , True  ],

    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, False, True , True  ]
    ],

    [
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False ],

    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False ],

    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ]
    ],

    [
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False ],

    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False ],

    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ]
    ],

    [
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False ],

    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False ],

    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ]
    ],

    [
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False ],

    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False ],

    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ]
    ],

    [
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False ],

    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , False, False, False, False, False, False, False, False, False, False ],

    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, True , True , True , True , True , True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ]
    ],

    [
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False ],

    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False ],

    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False ],

    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ]
    ],

    [
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False ],

    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False ],

    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False ],

    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ]
    ],

    [
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False, False, False, False, False, False ],

    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False ],

    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False ],

    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False ],

    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ]
    ],

    [
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , True , True  ],

    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , True , True  ],

    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ],

    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ]
    ],

    [
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , False, False, False, False, False ],

    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , False, False ],

    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , True , True  ],

    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True , True , True  ],

    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ],

    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ]
    ],

    [
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False ],

    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False ],

    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False ],

    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ],

    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ]
    ],

    [
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False ],

    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False ],

    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False ],

    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ],

    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ]
    ],

    [
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False ],

    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False ],

    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , False, False ],

    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, True , True , True , True , True , True , True , True , True , True  ],

    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ],

    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ]
    ],

    [
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, False, True , True  ],

    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, False, True , True  ],

    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ],

    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ],

    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ],

    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ],

    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ],

    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ],

    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ]
    ],

    [
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP    STP
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos    Nos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom    Nom
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol    Nol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True  ],

    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes    Nes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, False, True , True  ],

    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem    Nem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, False, False, False, False, False, True , True  ],

    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas    Eas
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam    Eam
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal    Eal
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses    Ses
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem    Sem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos    Sos
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som    Som
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol    Sol
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False ],

    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws    Sws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ],

    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm    Swm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, False, False, False, False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ],

    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes    Wes
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ],

    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem    Wem
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ],

    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel    Wel
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , False, False, False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ],

    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws    Nws
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ],

    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm    Nwm
    	#  STP    Nos    Nom    Nol    Nes    Nem    Eas    Eam    Eal    Ses    Sem    Sos    Som    Sol    Sws    Swm    Wes    Wem    Wel    Nws    Nwm
    	[  False, True , True , True , True , True , False, False, False, False, False, False, False, False, True , True , True , True , True , True , True  ]
    ]
]

if __name__ == "__main__":
    # Ensure that each codon in a vector maps to that vector
    for v in _vectors:
        for c in v.codons:
            assert(v == codonToVector(c))
            
    # Ensure each possible codon maps to a vector containing that codon
    for b1 in 'TCAG':
        for b2 in 'TCAG':
            for b3 in 'TCAG':
                c = b1+b2+b3
                v = codonToVector(c)
                assert(c in v.codons)
                
    # Generate codon mapping table for use in Stylus C/C++ file
    iCodon = -1
    for b1 in 'TCAG':
        for b2 in 'TCAG':
            for b3 in 'TCAG':
                c = b1+b2+b3
                v = codonToVector(c)
                iCodon += 1
                print 'ACID_%s, // %02d - %s' % (v.name, iCodon, c)
            print
