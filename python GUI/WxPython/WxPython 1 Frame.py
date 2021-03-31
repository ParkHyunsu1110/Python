import wx

app = wx.App()
frame = wx.Frame( None, title="wxPython Study", pos = ( 100, 0 ), size = ( 400, 300 ),
                  name="frameName", style = wx.CAPTION|wx.CLOSE_BOX )

frame.Show( True )
app.MainLoop()
