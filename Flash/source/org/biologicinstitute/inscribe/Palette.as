﻿/**----------------------------------------------------------------------------	Component: Palette	Description: Class that implements the tool palette within Inscribe.		Stylus, Copyright 2006-2008 Biologic Institute	Licensed under the Apache License, Version 2.0 (the "License");	you may not use this file except in compliance with the License.	You may obtain a copy of the License at	    http://www.apache.org/licenses/LICENSE-2.0	Unless required by applicable law or agreed to in writing, software	distributed under the License is distributed on an "AS IS" BASIS,	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.	See the License for the specific language governing permissions and	limitations under the License.*/import mx.core.UIComponent;import mx.managers.DepthManager;import mx.transitions.Tween;import mx.utils.Delegate;import org.biologicinstitute.inscribe.Inscribe;import org.biologicinstitute.inscribe.Han;import org.biologicinstitute.inscribe.Tab;import org.biologicinstitute.inscribe.DirectionTab;import org.biologicinstitute.inscribe.FinishTab;import org.biologicinstitute.inscribe.GroupsTab;import org.biologicinstitute.inscribe.OrderTab;import org.biologicinstitute.inscribe.OverlapsTab;import org.biologicinstitute.inscribe.PositionTab;import org.biologicinstitute.inscribe.StrokesTab;class org.biologicinstitute.inscribe.Palette extends UIComponent{	static var symbolName:String = "Palette";	static var symbolOwner:Object = Palette;	var className:String = "Palette";	private var boundingBox_mc:MovieClip;	private static var BORDER_WIDTH:Number = 5;	private static var MESSAGE_OFFSET:Number = 2;		private static var TAB_ANIMATION_SECONDS:Number = 1;		private var _mcControls:MovieClip;	private var _txtMessage:TextField;		private var _han:MovieClip;	function set han(mc:MovieClip)	{//		trace("Setting han to " + mc + " " + Han(mc));		_han = mc;	}		private var _inscribe:Inscribe;	function set inscribe(objInscribe:Inscribe):Void	{//		trace("Setting inscribe to " + obj + " " + Inscribe(obj));		_inscribe = objInscribe;	}		static var SHOW_POSITIONTAB:Number      = 0x0001;	static var SHOW_STROKESTAB:Number       = 0x0002;	static var SHOW_DIRECTIONTAB:Number     = 0x0004;	static var SHOW_ORDERTAB:Number         = 0x0008;	static var SHOW_GROUPSTAB:Number        = 0x0010;	static var SHOW_INTERSECTIONSTAB:Number = 0x0020;	static var SHOW_JOINSTAB:Number         = 0x0040;	private static var SHOW_FINISHTAB:Number= 0x0100;		static var SHOW_EDITORTABS:Number = 0x0103;		// Position, Strokes, Finish	static var SHOW_REVIEWERTABS:Number = 0x017B;	// Position, Strokes, Order, Groups, Intersections, Joins, Finish	static var SHOW_GENETABS:Number = 0x010B;		// Direction, Order, Finish	static var SHOW_ALLTABS:Number = 0xFFFF;		private var _grfTabs:Number = SHOW_ALLTABS;	function set tabs(n:Number)	{		_grfTabs = n | SHOW_FINISHTAB;		ensureTabs();	}	function get tabs():Number	{		return _grfTabs;	}	private static var TAB_CLASSNAME:Number = 0;	private static var TAB_CLASSINSTANCE:Number = 1;	private static var TAB_SHOWFLAG:Number = 2;	private var _aryTabs:Array = new Array();	private var _aryAllTabs:Array = [								 	[ PositionTab, null, SHOW_POSITIONTAB ],								 	[ StrokesTab, null, SHOW_STROKESTAB ],								 	[ DirectionTab, null, SHOW_DIRECTIONTAB ],								 	[ OrderTab, null, SHOW_ORDERTAB ],								 	[ GroupsTab, null, SHOW_GROUPSTAB ],									[ OverlapsTab, null, SHOW_INTERSECTIONSTAB ],									[ OverlapsTab, null, SHOW_JOINSTAB ],								 	[ FinishTab, null, SHOW_FINISHTAB ]								 	];		private var _iTab:Number = 0;	function set tab(n:Number)	{		ensureTab(n-1);	}	function get tab():Number	{		return _iTab+1;	}		function set tabId(n:Number)	{		for (var i=0; i < _aryTabs.length; i++)		{			if (_aryAllTabs[_aryTabs[i]][TAB_SHOWFLAG] == n)			{				ensureTab(i);			}		}	}	function get tabId():Number	{		return _aryAllTabs[_aryTabs[_iTab]][TAB_SHOWFLAG];	}		private var _tabHeight:Number = 0;	function get tabHeight():Number	{		return _tabHeight;	}		private var _tabWidth:Number = 0;	function get tabWidth():Number	{		return _tabWidth;	}		function init()	{		super.init();		// useHandCursor = false;		boundingBox_mc._visible = false;		boundingBox_mc._width = 0;		boundingBox_mc._height = 0;	}		function createChildren():Void	{		super.createChildren();				var mask:MovieClip = createChildAtDepth("maskPalette", DepthManager.kTop, { _visible: false, _x: 0, _y: 0 });		setMask(mask);//		trace("Palette loading tabs - " + _aryTabs.length + " tabs");		for (var i=0; i < _aryAllTabs.length; i++)		{			_aryAllTabs[i][TAB_CLASSINSTANCE] = createClassChildAtDepth(_aryAllTabs[i][TAB_CLASSNAME], DepthManager.kTop, { han: _han, palette: this });			_aryAllTabs[i][TAB_CLASSINSTANCE].move(0, height);						if (_aryAllTabs[i][TAB_SHOWFLAG] == SHOW_INTERSECTIONSTAB)			{				_aryAllTabs[i][TAB_CLASSINSTANCE].required = true;			}//			trace("Created " + _aryAllTabs[i][TAB_CLASSNAME].symbolOwner.symbolName + " into slot " + i + " as " + _aryAllTabs[i][TAB_CLASSINSTANCE]);		}		_mcControls = createChildAtDepth("mcControls", DepthManager.kTop);		_mcControls._y = height - _mcControls._height - 1;				var fDone:Function = function()		{			_inscribe.saveState(true);		}		var fPause:Function = function()		{			_inscribe.saveState(false);		}		_mcControls.btnNext.onRelease = Delegate.create(this, nextTab);		_mcControls.btnBack.onRelease = Delegate.create(this, prevTab);		_mcControls.btnPause.onRelease = Delegate.create(this, fPause);		_mcControls.btnSave.onRelease = Delegate.create(this, fDone);				var txtFormat:TextFormat = new TextFormat();		txtFormat.font = Inscribe.MESSAGE_FONT;		txtFormat.size = Inscribe.MESSAGE_SIZE;				_txtMessage = _mcControls.createTextField("txtMessage", _mcControls.getNextHighestDepth(),												  _mcControls.btnPause._x,												  _mcControls.btnPause._y + _mcControls.btnPause._height + MESSAGE_OFFSET,												  _mcControls.btnNext._width + _mcControls.btnNext._x - _mcControls.btnPause._x + 1,												  Inscribe.MESSAGE_HEIGHT);		_txtMessage._quality = "HIGH";		_txtMessage.selectable = false;		_txtMessage.setNewTextFormat(txtFormat);				var mcBorder:MovieClip = createChildAtDepth("mcBorder", DepthManager.kTop);		_tabHeight = mcBorder._height - BORDER_WIDTH;		_tabWidth = mcBorder._width - BORDER_WIDTH;		ensureTabs();				size();	}		function Palette()	{//		trace("Palette created");		ensureTab(_iTab);	}		function size()	{		super.size();	}		function onKeyDown()	{		_aryAllTabs[_aryTabs[_iTab]][TAB_CLASSINSTANCE].onKeyDown();	}		function onKeyUp()	{		_aryAllTabs[_aryTabs[_iTab]][TAB_CLASSINSTANCE].onKeyUp();	}		function nextTab()	{		tab++;	}		function prevTab()	{		tab--;	}		function reset()	{		for (var i=0; i < _aryAllTabs.length; i++)		{			if (_aryAllTabs[i][TAB_CLASSINSTANCE])				_aryAllTabs[i][TAB_CLASSINSTANCE].reset();		}				ensureTab(0);	}		private function ensureTab(iTab:Number)	{		if (iTab < 0 || iTab >= _aryTabs.length)		{			iTab = 0;		}//		trace("Moving from tab " + _iTab + " to tab " + iTab + " of " + _aryTabs.length + " tabs");		var tabCurrent = _aryAllTabs[_aryTabs[_iTab]][TAB_CLASSINSTANCE];		var tabNext = _aryAllTabs[_aryTabs[iTab]][TAB_CLASSINSTANCE];		var fAtStart:Boolean = (iTab == 0);		var fAtEnd:Boolean = (iTab == _aryTabs.length-1);				Inscribe.enableButton(_mcControls.btnNext, !fAtEnd, !fAtEnd);		Inscribe.enableButton(_mcControls.btnBack, !fAtStart, true);		Inscribe.enableButton(_mcControls.btnPause, !fAtEnd, !fAtEnd);		Inscribe.enableButton(_mcControls.btnSave, fAtEnd, fAtEnd);		tabNext.activate(true);		_inscribe.setContextMenu(tabNext.menu);				if (iTab != _iTab)		{			var fForward:Boolean = (iTab > _iTab);			var yStart:Number;			var yEnd:Number;			var tabAnimate;						if (fForward)			{				yStart = _mcControls._y;				yEnd = 1;				tabNext._y = yStart;				tabAnimate = tabNext;								for (var i=_iTab+1; i < iTab; i++)				{					_aryAllTabs[_aryTabs[i]][TAB_CLASSINSTANCE]._y = _mcControls._y;				}			}			else			{				yStart = 1;				yEnd = _mcControls._y;				tabNext._y = yStart;				tabAnimate = tabCurrent;								for (var i=iTab+1; i < _iTab; i++)				{					_aryAllTabs[_aryTabs[i]][TAB_CLASSINSTANCE]._y = _mcControls._y;				}			}			_iTab = iTab;			var tw:Tween = new Tween(tabAnimate, "_y", mx.transitions.easing.Strong.easeOut, yStart, yEnd, TAB_ANIMATION_SECONDS, true);			tw.onMotionStopped = function ()			{				tabCurrent.activate(false);			}		}		else		{			tabNext._y = 1;		}				setMessage("Step " + (_iTab+1) + " of " + _aryTabs.length);	}		private function ensureTabs()	{		_aryTabs.length = 0;		for (var i=0; i < _aryAllTabs.length; i++)		{			if (_grfTabs & _aryAllTabs[i][TAB_SHOWFLAG])				_aryTabs[_aryTabs.length] = i;		}				if (_iTab >= _aryTabs.length)			_iTab = _aryTabs.length - 1;	}		private function setMessage(str:String, fImportant:Boolean)	{		var txtFormat:TextFormat = _txtMessage.getTextFormat();		txtFormat.color = (fImportant						   ? Inscribe.MESSAGE_IMPORTANT						   : Inscribe.MESSAGE_NORMAL);		_txtMessage.text = str;		_txtMessage.setTextFormat(txtFormat);	}}