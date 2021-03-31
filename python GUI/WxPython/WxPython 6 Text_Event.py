##텍스트 상자
    ##스타일 상수 이름
    ##TE_MULTILINE  : 여러 줄을 입력받는다
    ##TE_PASSWORD   : 비밀번호 입력처럼 입력받은 것을 가려서 보여준다
    ##TE_READONLY   : 사용자가 수정할 수 없게 만든다.
##import wx
##app = wx.App()
##frame = wx.Frame(None)
##
##idtxt = wx.TextCtrl( frame, value = "아이디" )
##pwtxt = wx.TextCtrl( frame, value = "비밀번호", style = wx.TE_PASSWORD )
##
##sizer = wx.BoxSizer( wx.VERTICAL )
##frame.SetSizer( sizer )
##sizer.Add( idtxt )
##sizer.Add( pwtxt )
##
##frame.Show( True )
##app.MainLoop()

##버튼 이벤트

#GetValue, SetValue

import wx

app = wx.App()
frame = wx.Frame( None )

inputtxt = wx.TextCtrl( frame )
outputtxt = wx.TextCtrl(frame, style = wx.TE_READONLY, value = "주목해주세요" )

def changeValue( event ):
    line = inputtxt.GetValue()
    outputtxt.SetValue( line )

btn = wx.Button( frame, label = "변경" )
btn.Bind( wx.EVT_BUTTON, changeValue )

sizer = wx.BoxSizer( wx.VERTICAL )
frame.SetSizer( sizer )

sizer.Add( inputtxt )
sizer.Add( outputtxt )
sizer.Add( btn )

frame.Show()
app.MainLoop()

##텍스트 이벤트

#EVT_TEXT

import wx
##
##app = wx.App()
##frame = wx.Frame( None )
##
##inputtxt = wx.TextCtrl( frame )
##
##def changeValue( event ):
##    line = inputtxt.GetValue()
##    frame.SetTitle( line )
##
##inputtxt.Bind( wx.EVT_TEXT, changeValue )
##
##sizer = wx.BoxSizer( wx.VERTICAL )
##frame.SetSizer( sizer )
##sizer.Add( inputtxt )
##
##frame.Show( True )
##app.MainLoop()
