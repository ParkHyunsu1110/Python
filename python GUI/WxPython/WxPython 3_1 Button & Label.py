import wx

app = wx.App()
frame = wx.Frame( None )

lbl = wx.StaticText( frame, label = "Today is Sunny day!!!" )

btn = wx.Button(frame, label = "Today is rainy day..." )

frame.Show( True )
app.MainLoop()
