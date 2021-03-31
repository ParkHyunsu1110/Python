##WxPython 두번째 실습
import wx

app = wx.App()
frame = wx.Frame(None)

def messageBox( event ):
    wx.MessageBox( "알림창입니다.", "알림창입니다.", wx.OK|wx.CANCEL )

btn_alert = wx.Button( frame, label = "알림창" )
btn_alert.Bind( wx.EVT_BUTTON, messageBox )

def exitPro( event ):
    exit(0)

btn_exit = wx.Button( frame, label = "종료하기" )
btn_exit.Bind( wx.EVT_BUTTON, exitPro )

lbl_a = wx.StaticText(frame, label = "WxPython")
lbl_b = wx.StaticText(frame, label = "두번째 실습")

btn_alert.SetPosition( wx.Point( 100, 60 ))
btn_exit.SetPosition(wx.Point( 200, 60))
lbl_a.SetPosition( wx.Point( 100, 20 ))
lbl_b.SetPosition( wx.Point( 200, 20 ))

frame.Show(True)
app.MainLoop()
