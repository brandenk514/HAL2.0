import wx


class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title=title)

        # Setting up the menu.
        filemenu = wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "&Exit", " Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        self.Show(True)


class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, size=(300, 300))

        self.grid_sizer = wx.GridBagSizer(hgap=3, vgap=3)

        self.weather_text = wx.StaticText(self, label="Here is some weather")
        self.grid_sizer.Add(self.weather_text, pos=(0, 0))

        self.time_text = wx.StaticText(self, label="12:00")
        self.grid_sizer.Add(self.time_text, pos=(0, 3))

        # A button
        self.button = wx.Button(self, label="Ask")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.grid_sizer.Add(self.button, pos=(2, 2))

        self.SetSizerAndFit(self.grid_sizer)

    def OnClick(self):
        s = 0


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame(None, "HAL")
    panel = MainPanel(frame)
    frame.Show()
    app.MainLoop()
