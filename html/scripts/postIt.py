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
postIt.py

A POST-handler script for the Inscribe web pages.

Copyright (c) 2008 Biologic Institute, LLC. All rights reserved.
'''

import cgi
import cgitb; cgitb.enable()
import inscribe
import os
import stylus.common as Common
import sys

def returnMsg(strMsg, fError=False):
    print '%d:%s' % (fError and 1 or 0, strMsg)

def main():
    form = cgi.FieldStorage()
    
    if not 'code' in form or not form['code']:
        raise Common.BiologicError('Han unicode value is missing')
    uchHan = form.getfirst('code').upper()

    if 'hcf' in form:
        pathHCF = Common.resolvePath('./../../Archetypes/' + Common.makeHanPath(uchHan + Common.Constants.extHCF))
        try:
            fileHCF = os.open(pathHCF, os.O_CREAT | os.O_TRUNC | os.O_WRONLY, 0664)
            os.write(fileHCF, form['hcf'].value)
            os.close(fileHCF)
        except IOError, err:
            raise Common.BiologicError('Unable to write %s - %s' % (pathHCF, str(err)))
            
        inscribe.setGlobals([ '-d', './../../Archetypes/', '-u', './../../Archetypes/' ])
        inscribe.buildHan(uchHan)

        inscribe.setGlobals([ '-o', './../../Genes/', '-u', './../../Archetypes/' ])
        aryGeneNames = inscribe.buildGenes(uchHan, [ 'default' ])
        returnMsg('Successfully created Han definition and default gene (%s) for %s' % (aryGeneNames[0], uchHan))
    
    if 'gene' in form:
        inscribe.setGlobals([ '-o', './../../Genes/', '-u', './../../Archetypes/' ])
        aryGeneNames = inscribe.buildGenes(uchHan, [ form.getfirst('gene') ])
        returnMsg('Successfully created gene - saved as %s' % aryGeneNames[0])

try:
    print 'Content-type: text/plain\n'
    main()
except Common.BiologicError, err:
    returnMsg('ERROR: %s' % str(err), True)
