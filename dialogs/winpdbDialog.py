#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# generated by wxGlade 0.4 on Thu Oct 27 00:45:00 2005

"""VERY IMPORTANT: PAY ATTENTION TO TODO'S AFTER UPDATING WITH WXGLADE."""

import wx

import os,webbrowser

def _(x):
    return x

class Options(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Options.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.gui = wx.CheckBox(self, -1, _("Graphical User Interface"))
        self.chdir = wx.CheckBox(self, -1, _("Change working directory to that of script"))
        self.encryption = wx.CheckBox(self, -1, _("Use encryption (requires Python Cryptography Toolkit)"))
        self.verbose = wx.CheckBox(self, -1, _("Verbose"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Options.__set_properties
        self.gui.SetValue(1)
        self.chdir.SetValue(1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Options.__do_layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.gui, 0, wx.ALL|wx.ADJUST_MINSIZE, 4)
        sizer.Add(self.chdir, 0, wx.LEFT|wx.ADJUST_MINSIZE, 4)
        sizer.Add(self.encryption, 0, wx.ALL|wx.ADJUST_MINSIZE, 4)
        sizer.Add(self.verbose, 0, wx.ALL|wx.ADJUST_MINSIZE, 4)
        self.SetAutoLayout(True)
        self.SetSizer(sizer)
        sizer.Fit(self)
        sizer.SetSizeHints(self)
        # end wxGlade

# end of class Options


class Create(wx.Dialog):
    def __init__(self, name = '', *args, **kwds):
        # todo: VERY IMPORTANT: AFTER UPDATE WITH GLADE MAKE "choices=info['history']"!!
        self.name                   = name
        app = self.app              = kwds["parent"].app
        if not hasattr(app,'debugInfo'):
            info = self.info        = app.debugInfo = {}
            info['arguments']       = ''
            info['history']         = []
            info['gui']             = True
            info['chdir']           = True
            info['encryption']      = app.fCrypto
            info['verbose']         = app.DEBUG
        else:
            info = self.info        = app.debugInfo
        # begin wxGlade: Create.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.logo = wx.StaticBitmap(self, -1, wx.Bitmap("blenpy.png", wx.BITMAP_TYPE_ANY))
        self.title = wx.StaticText(self, -1, _("label_1"))
        self.argumentsLabel = wx.StaticText(self, -1, _("Arguments"))
        self.arguments = wx.ComboBox(self, -1, choices=info['history'], style=wx.CB_DROPDOWN)
        self.options = Options(self, -1)
        self.status = wx.StaticText(self, -1, _("WinPdb Debugger"))
        self.debug = wx.Button(self, wx.ID_OK, _("&Debug"))
        self.cancel = wx.Button(self, wx.ID_CANCEL, _("&Cancel"))
        self.help = wx.Button(self, -1, _("&Help"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.onDebug, id=wx.ID_OK)
        self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
        self.Bind(wx.EVT_BUTTON, self.onHelp, self.help)
        # end wxGlade

    def __set_properties(self):
        # todo: VERY IMPORTANT: AFTER UPDATE WITH GLADE COMMENT OUT self.arguments.SetSelection(-1)
        # begin wxGlade: Create.__set_properties
        self.SetTitle(_("SPE - Stani's Python Editor"))
        self.logo.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.title.SetBackgroundColour(wx.Colour(255, 255, 255))
        #self.arguments.SetSelection(-1)
        self.status.Enable(False)
        # end wxGlade
        self.title.SetLabel("  Debug %s"%self.name)
        info                        = self.info
        options                     = self.options
        options.gui.SetValue(info['gui'])
        if os.path.exists(self.name):
            self.arguments.SetValue(info['arguments'])
            options.chdir.SetValue(info['chdir'])
        else:
            self.arguments.SetValue('')
            self.arguments.Disable()
            options.chdir.SetValue(False)
            options.chdir.Disable()
        options.encryption.SetValue(info['encryption'])
        options.verbose.SetValue(bool(info['verbose']))
        options.encryption.Enable(self.app.fCrypto)

    def __do_layout(self):
        # begin wxGlade: Create.__do_layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        buttons = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer = wx.FlexGridSizer(1, 2, 4, 4)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.logo, 0, wx.BOTTOM|wx.EXPAND|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 4)
        sizer_1.Add(self.title, 1, wx.BOTTOM|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 4)
        sizer.Add(sizer_1, 1, wx.EXPAND, 0)
        grid_sizer.Add(self.argumentsLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 4)
        grid_sizer.Add(self.arguments, 0, wx.ALL|wx.EXPAND|wx.ADJUST_MINSIZE, 4)
        grid_sizer.AddGrowableCol(1)
        sizer.Add(grid_sizer, 0, wx.EXPAND, 0)
        sizer.Add(self.options, 1, wx.EXPAND, 0)
        buttons.Add(self.status, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 4)
        buttons.Add(self.debug, 0, wx.ALL|wx.ADJUST_MINSIZE, 4)
        buttons.Add(self.cancel, 0, wx.ALL|wx.ADJUST_MINSIZE, 4)
        buttons.Add(self.help, 0, wx.ALL|wx.ADJUST_MINSIZE, 4)
        sizer.Add(buttons, 0, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer)
        sizer.Fit(self)
        sizer.SetSizeHints(self)
        self.Layout()
        # end wxGlade

    def onDebug(self, event): # wxGlade: Create.<event_handler>
        from plugins.winpdb import __file__ as fileName
        path        = os.path.dirname(fileName)
        info        = self.info
        arguments   = info['arguments']     = self.arguments.GetValue()
        if arguments: info['history'].insert(0,arguments)
        parameters  = info['parameters']    = []
        options     = self.options
        gui         = info['gui']           = options.gui.GetValue()
        if gui:
            debugger= '%s'%os.path.join(path,'winpdb.py')
        else:
            debugger= '%s'%os.path.join(path,'rpdb2.py')
        if not os.path.exists(debugger):
            debugger= '"%s"'%debugger
        parameters.append(debugger)
        chdir       = info['chdir']         = options.chdir.GetValue()
        if chdir:
            parameters.append('-c')
        encryption  = info['encryption']    = options.encryption.GetValue()
        if not encryption:
            parameters.append('-t')
        verbose     = info['verbose']       = options.verbose.GetValue()
        if verbose:
            parameters.append('--debug')
        self.EndModal(wx.ID_OK)

    def onCancel(self, event): # wxGlade: Create.<event_handler>
        self.EndModal(wx.ID_CANCEL)

    def onHelp(self, event): # wxGlade: Create.<event_handler>
        webbrowser.open('http://www.digitalpeers.com/pythondebugger/')
        event.Skip()

# end of class Create

def options(parent, name=''):
    return Create(parent=parent,id=-1,name=name)


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    create = Create(None, -1, "")
    app.SetTopWindow(create)
    create.Show()
    app.MainLoop()
