import wx
import os


class GUI(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400, 600))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        file_menu = wx.Menu()
        # wx.ID_ABOUT and wx.ID_EXIT are standard ids provided by wxWidgets.

        menuAbout = file_menu.Append(wx.ID_FILE, "&About", " Information about this program")

        menuExit = file_menu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")
        menuFile = file_menu.Append(wx.ID_FILE, "&Test", "File button")
        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(file_menu, "&File")  # Adding the "file_menu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        # Set events.
        self.Bind(wx.EVT_MENU, self.OnFile, menuFile)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Show(True)

    def OnFile(self, e):
        dlg = wx.MessageDialog(self, "Test", "About Test", wx.OK)
        dlg.ShowModal()  # Show it
        dlg.Destroy()

    def OnAbout(self, e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog(self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal()  # Show it
        dlg.Destroy()  # finally destroy it when finished.

    def OnExit(self, e):
        self.Close(True)  # Close the frame.


app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = GUI(None, "Test Frame")
frame.Show(True)  # Show the frame.
app.MainLoop()
