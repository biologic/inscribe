//----------------------------------------------------------------------------------------
//
// Inscribe.js
//
// Stylus, Copyright 2006-2008 Biologic Institute
// 
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
// 
//     http://www.apache.org/licenses/LICENSE-2.0
// 
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//----------------------------------------------------------------------------------------

var xhr = new XMLHttpRequest();
var hanCode;

function parseArgs()
{
	var strArgs = window.location.search;

	if (strArgs.charAt(0) == '?')
	{
		strArgs = strArgs.substr(1);
	}

	var aryArgs = strArgs.split('&');

	for (var i=0; i < aryArgs.length; i++)
	{
		if (aryArgs[i].indexOf('code=') == 0)
		{
			hanCode = aryArgs[i].substr(aryArgs[i].indexOf('=')+1).toUpperCase();
		}
	}
}
	
function postHandler()
{
	if (xhr.readyState != 4) return;

	var strMsg;
	var fError;

	if (xhr.status == 200)
	{
		var aryResponse = xhr.responseText.split(':');
		
		if (aryResponse.length > 1)
		{
			fError = aryResponse[0];

			aryResponse.shift();
			strMsg = aryResponse.join(':');
		}
		else
		{
			fError = 1;
			strMsg = 'Server Error - ' + aryResponse.join(':');
		}
	}
	else
	{
		fError = 1;
		strMsg = xhr.status + ':' + xhr.statusText;
	}
	
	if (fError > 0)
	{
		strMsg = hanCode + ' failed to save -- ' + strMsg;
	}

	setMsg(strMsg, fError);
}

function doPost(strArgs)
{
	xhr.onreadystatechange = postHandler;
	xhr.open('POST', 'scripts/postIt.py', true);
	xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded')
	xhr.send('code=' + hanCode + (strArgs.length ? '&' + strArgs : ''));
}

function getHandler()
{
	if (xhr.readyState != 4) return;

	var mcInscribe = document.getElementById('Inscribe');
	var strHan = (xhr.status != 200
					? 'han: ' + hanCode
					: xhr.responseText);
	mcInscribe.loadHan(strHan);
	clearMsg();
}

function doGet(strPath)
{
	xhr.onreadystatechange = getHandler;
	xhr.open('GET', strPath, true);
	xhr.send();
}

function loadHan()
{
	setMsg('Loading Han ' + hanCode, 0);

	doGet('../Archetypes/' + hanCode.substr(0,hanCode.length-3) + '000/' + hanCode + '.hcf');
	return true;
}

function saveHan(strHan)
{
	setMsg('Saving Archetype and creating default gene for ' + hanCode, 0);
	doPost('hcf=' + encodeURIComponent(strHan));
	return true;
}

function saveGene()
{
	var paramsGene = document.getElementById('paramsGene').value;
	if (paramsGene == '')
		paramsGene = 'default';
	setMsg('Creating gene for ' + hanCode + ' with ' + paramsGene, 0);
	doPost('gene=' + encodeURIComponent(paramsGene));
	return true;
}

function clearMsg()
{
	setMsg('', 0);
}

function setMsg(strMsg, fError)
{
	document.getElementById('msgStatus').innerHTML = (fError > 0 ? "<span class='ERROR'>ERROR: " : "<span class='SUCCESS'>") + strMsg + '</span>';
}

parseArgs();
