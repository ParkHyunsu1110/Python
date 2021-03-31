##체크박스

#체크박스이름 = wx.CheckBox( 프레임, label = "글씨", style = 스타일상수 )

import wx

app = wx.App()
frame = wx.Frame( None )

manCheck = wx.CheckBox( frame, label = "남자" )
womanCheck = wx.CheckBox( frame, label = "여자" )

sizer = wx.BoxSizer( wx.VERTICAL )
frame.SetSizer( sizer )
sizer.Add( manCheck )
sizer.Add( womanCheck )

frame.Show()
app.MainLoop()

##체크박스 + 메시지박스

##import wx
##app = wx.App()
##frame = wx.Frame( None )
##
##manCheck = wx.CheckBox( frame, label = "남자" )
##womanCheck = wx.CheckBox( frame, label = "여자" )
##
##def checkMan( event ):
##    wx.MessageBox( "남자를 선택했습니다.", "당신의 성별은?", wx.OK )
##
##def checkWoman( event ):
##    wx.MessageBox( "여자를 선택했습니다.", "당신의 성별은?", wx.OK )
##
##manCheck.Bind( wx.EVT_CHECKBOX, checkMan )
##womanCheck.Bind( wx.EVT_CHECKBOX, checkWoman )
##
##sizer = wx.BoxSizer( wx.VERTICAL )
##frame.SetSizer( sizer )
##sizer.Add( manCheck )
##sizer.Add( womanCheck )
##
##frame.Show( True )
##app.MainLoop()

##라디오박스

#라디오박스이름 = wx.RadioButton( 프레임, label = "글씨", style =스타일상수 )

import wx

app = wx.App()
frame = wx.Frame( None )

redRB = wx.RadioButton( frame, label = "빨강", style = wx.RB_GROUP )
blueRB = wx.RadioButton( frame, label = "파랑")
greenRB = wx.RadioButton( frame, label = "초록")

circleRB = wx.RadioButton( frame, label = "원형", style = wx.RB_GROUP )
rectangleRB = wx.RadioButton( frame, label = "사각형")
triangleRB = wx.RadioButton( frame, label = "삼각형" )

sizer = wx.BoxSizer( wx.VERTICAL )
frame.SetSizer( sizer )
sizer.Add( redRB )
sizer.Add( blueRB )
sizer.Add( greenRB )

sizer.Add( circleRB )
sizer.Add( rectangleRB )
sizer.Add( triangleRB )

frame.Show( True )
app.MainLoop()

##라디오 박스

##import wx
## 
##app = wx.App()
##frame = wx.Frame( None )
## 
##redRB = wx.RadioButton( frame, label = "빨강", style = wx.RB_GROUP )
##blueRB = wx.RadioButton( frame, label = "파랑" )
##greenRB = wx.RadioButton( frame, label = "초록" )
## 
##def changeRed( event ) :
##    frame.SetBackgroundColour( wx.Colour( 255, 0, 0, 0 ) )
##    frame.Refresh()
## 
##def changeBlue( event ) :
##    frame.SetBackgroundColour( wx.Colour( 0, 0, 255, 0 ) )
##    frame.Refresh()
## 
##def changeGreen( event ) :
##    frame.SetBackgroundColour( wx.Colour( 0, 255, 0, 0 ) )
##    frame.Refresh()
## 
##redRB.Bind( wx.EVT_RADIOBUTTON, changeRed )
##blueRB.Bind( wx.EVT_RADIOBUTTON, changeBlue )
##greenRB.Bind( wx.EVT_RADIOBUTTON, changeGreen )
## 
##sizer = wx.StaticBoxSizer( wx.VERTICAL, frame, label = "배경" )
##frame.SetSizer( sizer )
##sizer.Add( redRB )
##sizer.Add( blueRB )
##sizer.Add( greenRB )
## 
##frame.Show()
##app.MainLoop()
