import wx
import weather
import location
import witai
import api_parsing


class GUIPanel(wx.Panel):
    def __init__(self, parent):
        self.weather = weather.Weather()
        self.location = location.Location()
        self.wit = witai.Witai()
        self.parse = api_parsing.ApiParsing()

        wx.Panel.__init__(self, parent)

        # create some sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridBagSizer(hgap=5, vgap=5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        # A multiline TextCtrl
        self.logger = wx.TextCtrl(self, size=(350, 300), style=wx.TE_MULTILINE | wx.TE_READONLY)

        self.weather_text = wx.StaticText(self, size=(100, 50), label=self.loadWeatherData())
        hSizer.Add(self.weather_text)

        # A button
        bmp = wx.Bitmap("icons/microphone_icon.png", wx.BITMAP_TYPE_ANY)
        self.button = wx.BitmapButton(self, id=wx.ID_ANY, bitmap=bmp, size=(bmp.GetWidth(), bmp.GetHeight()))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)

        # add a spacer to the sizer
        grid.Add((10, 40), pos=(2, 0))

        hSizer.Add(grid, 0, wx.ALL, 5)
        hSizer.Add(self.logger)
        mainSizer.Add(hSizer, 0, wx.ALL, 5)
        mainSizer.Add(self.button, 0, wx.CENTER)
        self.SetSizerAndFit(mainSizer)

    def OnClick(self, event):
        self.logger.AppendText(" Click on object with Id %d\n" % event.GetId())

    def loadWeatherData(self):
        json_req = self.location.create_ip_location_request()
        print(json_req)
        lat_lng = self.parse.parseLatLngFromIP(json_req)
        print(lat_lng)
        self.weather.get_current_weather(lat_lng)
        return self.weather.get_current_summary()


if __name__ == '__main__':
    app = wx.App(False)
    frame = wx.Frame(None, size=(500, 400))
    panel = GUIPanel(frame)
    frame.Show()
    app.MainLoop()
