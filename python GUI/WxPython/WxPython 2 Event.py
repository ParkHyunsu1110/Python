import wx

app = wx.App()
frame = wx.Frame( None )

def onButtonClick( event ) :
    print( "x좌표 : ", event.x )
    print( "y좌표 : ", event.y )
frame.Bind( wx.EVT_LEFT_DOWN, onButtonClick )

def onKeyClick( event ) :
    print( "누른 자판 : ", chr(event.KeyCode) )
frame.Bind( wx.EVT_CHAR, onKeyClick )

wx.MessageBox( "안녕하세요", "제목입니다", wx.OK|wx.CANCEL )
frame.Show( True )
app.MainLoop()
