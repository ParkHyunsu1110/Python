import wx

app = wx.App()
frame = wx.Frame(None)

def onClick( event ):
    print( "Clicked" )

btn = wx.Button( frame, label = "클릭" )
btn.Bind( wx.EVT_BUTTON, onClick )

lbl = wx.StaticText( frame, label = "라벨에 입력될 텍스트" )

lbl.SetPosition(wx.Point( 160, 60 ))
btn.SetPosition(wx.Point( 150, 100))

frame.Show(True)
app.MainLoop()
