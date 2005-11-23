#!/usr/bin/env python
# generated by wxGlade 0.3.1 on Thu Oct 02 01:22:53 2003

"""Preferences can be added in three steps:
1. Add the control with wxGlade
2. Append the name to the VALUES list
3. Add an entry in _spe/default.cfg"""

import ConfigParser,os,types
from wx.gizmos import EditableListBox
import wx
import sm.wxp.smdi as smdi

VALUES = ['AutoComplete','AutoReloadChangedFile','Backup','CallTips',
          'CheckFileOnSave','ConvertTabsToSpaces','Encoding','Mdi',
          'EdgeColumn','PythonDocs','RecentFileAmount','RedirectShell', 
          'Redraw', 'Signature', 'SaveBeforeRun', 'Shortcuts', 'ShowShell',
          'StripTrailingSpaces', 'TabWidth','Terminal', 'TerminalRun',
          'TerminalRunExit', 'UpdateSidebar','UseTabs','ViewWhiteSpace',
          'IndentationGuides', 'ViewEdge','WebBrowser','WordChars',
          'WxPythonDocs']

def _(x):
    return x
          
class Create(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Create.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.notebook_1 = wx.Notebook(self, -1, style=0)
        self.Paths = wx.Panel(self.notebook_1, -1)
        self.Editor = wx.Panel(self.notebook_1, -1)
        self.GeneralEditor_staticbox = wx.StaticBox(self.Editor, -1, _("General"))
        self.tabsWhiteSpaces_staticbox = wx.StaticBox(self.Editor, -1, _("Tabs && white spaces"))
        self.Guides_staticbox = wx.StaticBox(self.Editor, -1, _("Guides"))
        self.AutoCompletion_staticbox = wx.StaticBox(self.Editor, -1, _("Auto complete"))
        self.general_Label_staticbox = wx.StaticBox(self.Paths, -1, _("General"))
        self.terminal_Label_staticbox = wx.StaticBox(self.Paths, -1, _("Terminal Emulator"))
        self.html_Label_staticbox = wx.StaticBox(self.Paths, -1, _("Html"))
        self.General = wx.Panel(self.notebook_1, -1)
        self.Backup = wx.CheckBox(self.General, -1, _("Create backup files"))
        self.RedirectShell = wx.CheckBox(self.General, -1, _("Redirect output to spe shell"))
        self.CheckFileOnSave = wx.CheckBox(self.General, -1, _("Check file for syntax errors on save"))
        self.ShowShell = wx.CheckBox(self.General, -1, _("Show shell"))
        self.label_di = wx.StaticText(self.General, -1, _("Document Interface*"))
        self.Mdi = wx.ComboBox(self.General, -1, choices=[_("<default>")], style=wx.CB_DROPDOWN|wx.CB_READONLY)
        self.label_recent = wx.StaticText(self.General, -1, _("Amount of recent files"))
        self.RecentFileAmount = wx.TextCtrl(self.General, -1, _("100"))
        self.label_redraw = wx.StaticText(self.General, -1, _("Auto redraw Blender every [sec]"))
        self.Redraw = wx.TextCtrl(self.General, -1, _("1"))
        self.label_encoding = wx.StaticText(self.General, -1, _("Encoding"))
        self.Encoding = wx.ComboBox(self.General, -1, choices=[_("<default>"), _("ascii, 646, us-ascii (English)"), _("cp037, IBM037, IBM039 (English)"), _("cp424, EBCDIC-CP-HE, IBM424 (Hebrew)"), _("cp437, 437, IBM437 (English)"), _("cp500, EBCDIC-CP-BE, EBCDIC-CP-CH, IBM500 (Western Europe)"), _("cp737 (Greek)"), _("cp775, IBM775 (Baltic languages)"), _("cp850, 850, IBM850 (Western Europe)"), _("cp852, 852, IBM852 (Central and Eastern Europe)"), _("cp855, 855, IBM855 (Bulgarian, Byelorussian, Macedonian, Russian, Serbian)"), _("cp856 (Hebrew)"), _("cp857, 857, IBM857 (Turkish)"), _("cp860, 860, IBM860 (Portuguese)"), _("cp861, 861, CP-IS, IBM861 (Icelandic)"), _("cp862, 862, IBM862 (Hebrew)"), _("cp863, 863, IBM863 (Canadian)"), _("cp864, IBM864 (Arabic)"), _("cp865, 865, IBM865 (Danish, Norwegian)"), _("cp869, 869, CP-GR, IBM869 (Greek)"), _("cp874 (Thai)"), _("cp875 (Greek)"), _("cp1006 (Urdu)"), _("cp1026, ibm1026 (Turkish)"), _("cp1140, ibm1140 (Western Europe)"), _("cp1250, windows-1250 (Central and Eastern Europe)"), _("cp1251, windows-1251 (Bulgarian, Byelorussian, Macedonian, Russian, Serbian)"), _("cp1252, windows-1252 (Western Europe)"), _("cp1253, windows-1253 (Greek)"), _("cp1254, windows-1254 (Turkish)"), _("cp1255, windows-1255 (Hebrew)"), _("cp1256, windows1256 (Arabic)"), _("cp1257, windows-1257 (Baltic languages)"), _("cp1258, windows-1258 (Vietnamese)"), _("latin_1, iso-8859-1, iso8859-1, 8859, cp819, latin, latin1, L1 (West Europe)"), _("iso8859_2, iso-8859-2, latin2, L2 (Central and Eastern Europe)"), _("iso8859_3, iso-8859-3, latin3, L3 (Esperanto, Maltese)"), _("iso8859_4, iso-8859-4, latin4, L4 (Baltic languagues)"), _("iso8859_5, iso-8859-5, cyrillic (Bulgarian, Byelorussian, Macedonian, Russian, Serbian)"), _("iso8859_6, iso-8859-6, arabic (Arabic)"), _("iso8859_7, iso-8859-7, greek, greek8 (Greek)"), _("iso8859_8, iso-8859-8, hebrew (Hebrew)"), _("iso8859_9, iso-8859-9, latin5, L5 (Turkish)"), _("iso8859_10, iso-8859-10, latin6, L6 (Nordic languages)"), _("iso8859_13, iso-8859-13 (Baltic languages)"), _("iso8859_14, iso-8859-14, latin8, L8 (Celtic languages)"), _("iso8859_15, iso-8859-15 (Western Europe)"), _("koi8_r (Russian)"), _("koi8_u (Ukrainian)"), _("mac_cyrillic, maccyrillic (Bulgarian, Byelorussian, Macedonian, Russian, Serbian)"), _("mac_greek, macgreek (Greek)"), _("mac_iceland, maciceland (Icelandic)"), _("mac_latin2, maclatin2, maccentraleurope (Central and Eastern Europe)"), _("mac_roman, macroman (Western Europe)"), _("mac_turkish, macturkish (Turkish)"), _("utf_16, U16, utf16 (all languages)"), _("utf_16_be, UTF-16BE (all languages (BMP only))"), _("utf_16_le, UTF-16LE (all languages (BMP only))"), _("utf_7, U7 (all languages)"), _("utf_8, U8, UTF, utf8 (all languages)")], style=wx.CB_DROPDOWN|wx.CB_READONLY)
        self.label_shortcuts = wx.StaticText(self.General, -1, _("Keyboard shortcuts*"))
        self.Shortcuts = wx.ComboBox(self.General, -1, choices=[_("<default>"), _("Windows"), _("Macintosh")], style=wx.CB_DROPDOWN)
        self.label_font = wx.StaticText(self.Editor, -1, _("Font"))
        self.Font = wx.TextCtrl(self.Editor, -1, _("Courier New, 10"))
        self.chooseFont = wx.Button(self.Editor, -1, _("Choose"))
        self.label_wordchars = wx.StaticText(self.Editor, -1, _("Word characters"))
        self.WordChars = wx.TextCtrl(self.Editor, -1, "")
        self.label_calltips = wx.StaticText(self.Editor, -1, _("Calltips"))
        self.CallTips = wx.ComboBox(self.Editor, -1, choices=[_("disable"), _("first paragraph only"), _("whole documentation")], style=wx.CB_DROPDOWN|wx.CB_READONLY)
        self.label_sidebar = wx.StaticText(self.Editor, -1, _("Update sidebar"))
        self.UpdateSidebar = wx.ComboBox(self.Editor, -1, choices=[_("realtime"), _("when clicked"), _("when manually refreshed (F5)")], style=wx.CB_DROPDOWN|wx.CB_READONLY)
        self.AutoReloadChangedFile = wx.CheckBox(self.Editor, -1, _("Auto reload changed file"))
        self.SaveBeforeRun = wx.CheckBox(self.Editor, -1, _("Check if file is saved before run"))
        self.ViewWhiteSpace = wx.CheckBox(self.Editor, -1, _("Show whitespaces"))
        self.UseTabs = wx.CheckBox(self.Editor, -1, _("Use tabs"))
        self.ConvertTabsToSpaces = wx.CheckBox(self.Editor, -1, _("Convert tabs to spaces on open"))
        self.StripTrailingSpaces = wx.CheckBox(self.Editor, -1, _("Strip trailing spaces on save"))
        self.label_tabWidth = wx.StaticText(self.Editor, -1, _("Tab width"))
        self.TabWidth = wx.SpinCtrl(self.Editor, -1, "4", min=0, max=100)
        self.IndentationGuides = wx.CheckBox(self.Editor, -1, _("Show indentation guides"))
        self.ViewEdge = wx.CheckBox(self.Editor, -1, _("Show eol (end of line) guide"))
        self.label_edgeColumn = wx.StaticText(self.Editor, -1, _("Show eol guide at col"))
        self.EdgeColumn = wx.SpinCtrl(self.Editor, -1, "79", min=0, max=100)
        self.AutoComplete = wx.CheckBox(self.Editor, -1, _("Active"))
        self.AutoCompleteIgnore = EditableListBox(self.Editor, -1, "Ignore")
        self.signatureLabel = wx.StaticText(self.Paths, -1, _("Signature"))
        self.Signature = wx.ComboBox(self.Paths, -1, choices=[], style=wx.CB_DROPDOWN)
        self.browseSignature = wx.Button(self.Paths, -1, _("Browse"))
        self.label_terminal = wx.StaticText(self.Paths, -1, _("Open"))
        self.Terminal = wx.ComboBox(self.Paths, -1, choices=[_("<default>"), _("start \"Spe console - Press Ctrl+Break to stop\" /D\"%(path)s\""), _("cd \\\"%(path)s\\\"; /usr/bin/Eterm -e"), _("cd \\\"%(path)s\\\"; /usr/X11R6/bin/xterm -e"), _("cd \\\"%(path)s\\\"; /usr/bin/wterm -e"), _("cd \\\"%(path)s\\\"; /usr/bin/aterm -e"), _("cd \\\"%(path)s\\\"; /usr/bin/rxvt-xterm -e"), _("cd \\\"%(path)s\\\"; /usr/bin/gnome-terminal -e"), _("cd \\\"%(path)s\\\"; /usr/bin/open -a Terminal")], style=wx.CB_DROPDOWN)
        self.label_terminalRun = wx.StaticText(self.Paths, -1, _("Run"))
        self.TerminalRun = wx.ComboBox(self.Paths, -1, choices=[_("<default>"), _("start \"Spe - %(file)s - Press Ctrl+Break to stop\" /D\"%(path)s\" start /B python \"%(file)s\""), _("/usr/bin/Eterm -e 'cd \"%(path)s\"; python \"%(file)s\"'"), _("/usr/X11R6/bin/xterm -e 'cd \"%(path)s\"; python \"%(file)s\"'"), _("/usr/bin/wterm -e 'cd \"%(path)s\"; python \"%(file)s\"'"), _("/usr/bin/aterm -e 'cd \"%(path)s\"; python \"%(file)s\"'"), _("/usr/bin/rxvt-xterm -e 'cd \"%(path)s\"; python \"%(file)s\"'"), _("/usr/bin/gnome-terminal -e 'cd \"%(path)s\"; python \"%(file)s\"'")], style=wx.CB_DROPDOWN)
        self.label_terminalRunExit = wx.StaticText(self.Paths, -1, _("Run && Exit"))
        self.TerminalRunExit = wx.ComboBox(self.Paths, -1, choices=[_("<default>"), _("start \"Spe - %(file)s - Press Ctrl+Break to stop\" /D\"%(path)s\" python \"%(file)s\""), _("/usr/bin/Eterm -e 'cd \"%(path)s\"; python \"%(file)s\"'"), _("/usr/X11R6/bin/xterm -e 'cd \"%(path)s\"; python \"%(file)s\"'"), _("/usr/bin/wterm -e 'cd \"%(path)s\"; python \"%(file)s\"'"), _("/usr/bin/aterm -e 'cd \"%(path)s\"; python \"%(file)s\"'"), _("/usr/bin/rxvt-xterm -e 'cd \"%(path)s\"; python \"%(file)s\"'"), _("/usr/bin/gnome-terminal -e 'cd \"%(path)s\"; python \"%(file)s\"'")], style=wx.CB_DROPDOWN)
        self.label_webBrowser = wx.StaticText(self.Paths, -1, _("Webbrowser"))
        self.WebBrowser = wx.ComboBox(self.Paths, -1, choices=[_("<default>"), _("/usr/bin/mozilla -remote"), _("/usr/bin/mozilla"), _("/usr/bin/gnome-moz-remote"), _("/usr/bin/konqueror"), _("/usr/bin/mozilla-firebird"), _("/usr/bin/netscape"), _("/usr/bin/galeon"), _("/usr/bin/skipstone"), _("/usr/bin/xterm -e lynx"), _("/usr/local/bin/opera")], style=wx.CB_DROPDOWN)
        self.label_pythonDocs = wx.StaticText(self.Paths, -1, _("Python docs"))
        self.PythonDocs = wx.ComboBox(self.Paths, -1, choices=[_("<default>"), _("/usr/share/doc/python-docs-2.2.3/html"), _("/usr/share/doc/python-docs/html"), _("/usr/share/doc/python-docs2.2/html")], style=wx.CB_DROPDOWN)
        self.label_wxPythonDocs = wx.StaticText(self.Paths, -1, _("wxPython docs"))
        self.WxPythonDocs = wx.ComboBox(self.Paths, -1, choices=[_("<default>"), _("/usr/share/doc/wxPython-2.4.2.4/docs"), _("/usr/share/doc/wxPython-docs")], style=wx.CB_DROPDOWN)
        self.label_warning = wx.StaticText(self, -1, _("Settings marked with * will only be updated next time SPE starts."))
        self.defaults = wx.Button(self, -1, _("Defaults"))
        self.save = wx.Button(self, -1, _("Save"))
        self.Cancel = wx.Button(self, -1, _("Cancel"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnBrowseSignature, self.browseSignature)
        # end wxGlade
        self.parent=args[0]
        self.update()
        wx.EVT_BUTTON(self.chooseFont, self.chooseFont.GetId(), self.OnChooseFontButton)
        wx.EVT_BUTTON(self.defaults, self.defaults.GetId(), self.OnDefaultsButton)
        wx.EVT_BUTTON(self.save, self.save.GetId(), self.OnSaveButton)
        wx.EVT_BUTTON(self.Cancel, self.Cancel.GetId(), self.OnCancelButton)

    def __set_properties(self):
        #todo: always after wxGlade update: #self.Signature.SetSelection(-1)!!
        self.__fill()
        # begin wxGlade: Create.__set_properties
        self.SetTitle(_("Spe preferences"))
        self.Backup.SetValue(1)
        self.RedirectShell.SetValue(1)
        self.CheckFileOnSave.SetValue(1)
        self.ShowShell.SetValue(1)
        self.Mdi.SetSelection(0)
        self.Encoding.SetSelection(0)
        self.Shortcuts.SetSelection(0)
        self.CallTips.SetSelection(2)
        self.UpdateSidebar.SetSelection(0)
        self.AutoReloadChangedFile.SetValue(1)
        self.SaveBeforeRun.SetValue(1)
        self.ConvertTabsToSpaces.SetValue(1)
        self.IndentationGuides.SetValue(1)
        self.ViewEdge.SetValue(1)
        self.AutoComplete.SetValue(1)
        self.AutoCompleteIgnore.SetMinSize((-1, 150))
        #self.Signature.SetSelection(-1)
        self.Terminal.SetSelection(0)
        self.TerminalRun.SetSelection(0)
        self.TerminalRunExit.SetSelection(0)
        self.WebBrowser.SetSelection(0)
        self.PythonDocs.SetSelection(0)
        self.WxPythonDocs.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Create.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        bottom = wx.BoxSizer(wx.HORIZONTAL)
        paths_Sizer = wx.BoxSizer(wx.VERTICAL)
        html_Label = wx.StaticBoxSizer(self.html_Label_staticbox, wx.HORIZONTAL)
        html_Sizer = wx.FlexGridSizer(4, 2, 4, 4)
        terminal_Label = wx.StaticBoxSizer(self.terminal_Label_staticbox, wx.HORIZONTAL)
        terminal_Sizer = wx.FlexGridSizer(4, 2, 4, 4)
        general_Label = wx.StaticBoxSizer(self.general_Label_staticbox, wx.VERTICAL)
        general_Label_Sizer = wx.FlexGridSizer(1, 3, 0, 0)
        grid_sizer_1 = wx.FlexGridSizer(3, 2, 4, 4)
        AutoCompletion = wx.StaticBoxSizer(self.AutoCompletion_staticbox, wx.VERTICAL)
        Guides = wx.StaticBoxSizer(self.Guides_staticbox, wx.VERTICAL)
        eol = wx.BoxSizer(wx.HORIZONTAL)
        tabsWhiteSpaces = wx.StaticBoxSizer(self.tabsWhiteSpaces_staticbox, wx.VERTICAL)
        grid_sizer_2 = wx.FlexGridSizer(4, 1, 4, 4)
        width = wx.BoxSizer(wx.HORIZONTAL)
        GeneralEditor = wx.StaticBoxSizer(self.GeneralEditor_staticbox, wx.VERTICAL)
        grid_general = wx.FlexGridSizer(3, 3, 4, 4)
        generalSizer = wx.FlexGridSizer(6, 1, 4, 4)
        grid_sizer_4 = wx.FlexGridSizer(3, 2, 4, 4)
        sizer_1.Add((4, 4), 0, 0, 0)
        sizer_2.Add((4, 4), 0, 0, 0)
        generalSizer.Add(self.Backup, 0, wx.LEFT|wx.TOP|wx.ADJUST_MINSIZE, 4)
        generalSizer.Add(self.RedirectShell, 0, wx.LEFT, 4)
        generalSizer.Add(self.CheckFileOnSave, 0, wx.LEFT, 4)
        generalSizer.Add(self.ShowShell, 0, wx.LEFT, 4)
        grid_sizer_4.Add(self.label_di, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 4)
        grid_sizer_4.Add(self.Mdi, 0, wx.EXPAND, 0)
        grid_sizer_4.Add(self.label_recent, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 4)
        grid_sizer_4.Add(self.RecentFileAmount, 0, wx.EXPAND, 0)
        grid_sizer_4.Add(self.label_redraw, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 4)
        grid_sizer_4.Add(self.Redraw, 0, wx.EXPAND, 0)
        grid_sizer_4.Add(self.label_encoding, 0, wx.LEFT|wx.FIXED_MINSIZE, 4)
        grid_sizer_4.Add(self.Encoding, 0, wx.EXPAND|wx.FIXED_MINSIZE, 0)
        grid_sizer_4.Add(self.label_shortcuts, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 4)
        grid_sizer_4.Add(self.Shortcuts, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        grid_sizer_4.AddGrowableCol(1)
        generalSizer.Add(grid_sizer_4, 1, wx.EXPAND, 0)
        self.General.SetAutoLayout(True)
        self.General.SetSizer(generalSizer)
        generalSizer.Fit(self.General)
        generalSizer.SetSizeHints(self.General)
        generalSizer.AddGrowableCol(0)
        GeneralEditor.Add((4, 4), 0, 0, 0)
        grid_general.Add(self.label_font, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_general.Add(self.Font, 0, wx.EXPAND, 0)
        grid_general.Add(self.chooseFont, 0, 0, 0)
        grid_general.Add(self.label_wordchars, 0, wx.ADJUST_MINSIZE, 0)
        grid_general.Add(self.WordChars, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        grid_general.Add((20, 20), 0, wx.ADJUST_MINSIZE, 0)
        grid_general.Add(self.label_calltips, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_general.Add(self.CallTips, 0, wx.EXPAND, 0)
        grid_general.Add((20, 20), 0, 0, 0)
        grid_general.Add(self.label_sidebar, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_general.Add(self.UpdateSidebar, 0, wx.EXPAND, 0)
        grid_general.Add((20, 20), 0, 0, 0)
        grid_general.AddGrowableCol(1)
        GeneralEditor.Add(grid_general, 1, wx.EXPAND, 0)
        GeneralEditor.Add((4, 4), 0, 0, 0)
        GeneralEditor.Add(self.AutoReloadChangedFile, 0, 0, 0)
        GeneralEditor.Add((4, 4), 0, 0, 0)
        GeneralEditor.Add(self.SaveBeforeRun, 0, wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(GeneralEditor, 1, wx.EXPAND, 0)
        grid_sizer_2.Add((4, 4), 0, 0, 0)
        grid_sizer_2.Add(self.ViewWhiteSpace, 0, 0, 0)
        grid_sizer_2.Add(self.UseTabs, 0, 0, 0)
        grid_sizer_2.Add(self.ConvertTabsToSpaces, 3, 0, 0)
        grid_sizer_2.Add(self.StripTrailingSpaces, 0, 0, 0)
        width.Add(self.label_tabWidth, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        width.Add((4, 4), 0, 0, 0)
        width.Add(self.TabWidth, 0, 0, 0)
        width.Add((64, 4), 0, 0, 0)
        grid_sizer_2.Add(width, 1, wx.EXPAND, 0)
        tabsWhiteSpaces.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(tabsWhiteSpaces, 0, wx.EXPAND, 0)
        Guides.Add((4, 4), 0, 0, 0)
        Guides.Add(self.IndentationGuides, 0, 0, 0)
        Guides.Add((4, 4), 0, 0, 0)
        Guides.Add(self.ViewEdge, 0, 0, 0)
        Guides.Add((4, 4), 0, 0, 0)
        eol.Add(self.label_edgeColumn, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        eol.Add((4, 4), 0, 0, 0)
        eol.Add(self.EdgeColumn, 0, 0, 0)
        eol.Add((64, 4), 0, 0, 0)
        Guides.Add(eol, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(Guides, 1, wx.EXPAND, 0)
        AutoCompletion.Add(self.AutoComplete, 0, 0, 0)
        AutoCompletion.Add(self.AutoCompleteIgnore, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(AutoCompletion, 1, wx.EXPAND, 0)
        self.Editor.SetAutoLayout(True)
        self.Editor.SetSizer(grid_sizer_1)
        grid_sizer_1.Fit(self.Editor)
        grid_sizer_1.SetSizeHints(self.Editor)
        general_Label_Sizer.Add(self.signatureLabel, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        general_Label_Sizer.Add(self.Signature, 1, wx.LEFT|wx.RIGHT|wx.TOP|wx.EXPAND|wx.ADJUST_MINSIZE, 5)
        general_Label_Sizer.Add(self.browseSignature, 0, wx.RIGHT|wx.TOP|wx.ADJUST_MINSIZE, 5)
        general_Label_Sizer.AddGrowableCol(1)
        general_Label.Add(general_Label_Sizer, 1, wx.EXPAND, 0)
        paths_Sizer.Add(general_Label, 0, wx.EXPAND, 0)
        terminal_Sizer.Add(self.label_terminal, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        terminal_Sizer.Add(self.Terminal, 0, wx.RIGHT|wx.TOP|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)
        terminal_Sizer.Add(self.label_terminalRun, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        terminal_Sizer.Add(self.TerminalRun, 0, wx.RIGHT|wx.TOP|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)
        terminal_Sizer.Add(self.label_terminalRunExit, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        terminal_Sizer.Add(self.TerminalRunExit, 0, wx.RIGHT|wx.TOP|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)
        terminal_Sizer.AddGrowableCol(1)
        terminal_Label.Add(terminal_Sizer, 1, wx.EXPAND, 0)
        paths_Sizer.Add(terminal_Label, 1, wx.EXPAND|wx.ALIGN_RIGHT, 0)
        html_Sizer.Add(self.label_webBrowser, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        html_Sizer.Add(self.WebBrowser, 0, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)
        html_Sizer.Add(self.label_pythonDocs, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        html_Sizer.Add(self.PythonDocs, 0, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)
        html_Sizer.Add(self.label_wxPythonDocs, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        html_Sizer.Add(self.WxPythonDocs, 0, wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5)
        html_Sizer.AddGrowableCol(1)
        html_Label.Add(html_Sizer, 1, wx.EXPAND, 0)
        paths_Sizer.Add(html_Label, 1, wx.EXPAND|wx.ALIGN_RIGHT, 0)
        self.Paths.SetAutoLayout(True)
        self.Paths.SetSizer(paths_Sizer)
        paths_Sizer.Fit(self.Paths)
        paths_Sizer.SetSizeHints(self.Paths)
        self.notebook_1.AddPage(self.General, _("General"))
        self.notebook_1.AddPage(self.Editor, _("Editor"))
        self.notebook_1.AddPage(self.Paths, _("Paths"))
        sizer_2.Add(self.notebook_1, 1, wx.EXPAND, 0)
        sizer_2.Add((4, 4), 0, 0, 0)
        bottom.Add(self.label_warning, 1, 0, 0)
        bottom.Add(self.defaults, 0, wx.RIGHT, 4)
        bottom.Add(self.save, 0, wx.RIGHT, 4)
        bottom.Add(self.Cancel, 0, 0, 0)
        sizer_2.Add(bottom, 0, wx.EXPAND, 0)
        sizer_2.Add((4, 4), 0, 0, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_1.Add((4, 4), 0, 0, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        self.Layout()
        # end wxGlade

    def __fill(self):
        #mdi
        keys = smdi.DI.keys()
        keys.remove('<default>')
        keys.sort()
        for key in keys:
            self.Mdi.Append(key)

    def update(self):
        for name in VALUES: self._update(name)
        self.Font.SetValue(self.parent.get('Font'))
        self.AutoCompleteIgnore.SetStrings(self.parent.getValue('AutoCompleteIgnore'))

    def _update(self,name):
        """Update one automatically"""
        item=self.__dict__[name]
        if type(item.GetValue()) in [types.StringType,types.UnicodeType]:
            try:
                item.SetValue(self.parent.get(name))
            except:
                print 'SPE.dialogs.preferencesDialog.py error: can not set value',self.parent.get(name)
        else:
            item.SetValue(self.parent.getValue(name))

    def OnChooseFontButton(self, event):
        data = wx.FontData()
        face,size=self.Font.GetValue().split(',')
        size=eval(size)
        try:
            font=wx.Font(size,wx.DEFAULT,wx.NORMAL,wx.NORMAL,0,face)
        except:
            font=wx.SystemSettings_GetFont(wx.SYS_OEM_FIXED_FONT)
        data.SetInitialFont(font)
        #data
        dialog=wx.FontDialog(self,data)
        try:
            if dialog.ShowModal() == wx.ID_OK:
                data = dialog.GetFontData()
                font = data.GetChosenFont()
                colour = data.GetColour()
                self.Font.SetValue('%s,%s'%(font.GetFaceName(),font.GetPointSize()))
        finally:
            dialog.Destroy()
        
    def OnDefaultsButton(self, event):
        self.Close()

    def OnSaveButton(self, event):
        #Editor
        for name in VALUES: self.set(name)
        self.set('Font')
        self.set('AutoCompleteIgnore')
        self.parent.preferencesSave()
        self.Close()

    def set(self,name,value=None):
        """Sets"""
        if value==None:
            if name=='AutoCompleteIgnore':
                value=str(self.__dict__[name].GetStrings())
            else:
                value=str(self.__dict__[name].GetValue())
        self.parent.set(name,value,save=0)
        

    def OnCancelButton(self, event):
        self.Close()

    def OnBrowseSignature(self, event): # wxGlade: Create.<event_handler>
        path=self.Signature.GetValue()
        defaultDir, defaultFile = os.path.split(path)   
        dlg = wx.FileDialog(self,defaultDir = defaultDir, defaultFile = defaultFile, style = wx.OPEN|wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            path        = dlg.GetPath()
            self.Signature.SetValue(path)
        dlg.Destroy()

# end of class Create

if __name__=='__main__':
    prefs=Create(None,-1,'haha')
    prefs.Show()

