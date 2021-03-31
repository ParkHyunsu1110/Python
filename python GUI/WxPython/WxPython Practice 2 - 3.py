##WxPyhton 실습 2 - 3
import wx
app = wx.App()
frame = wx.Frame(None)

lbl = wx.StaticText( frame, label = "성적 입력 시스템" )

panel1 = wx.Panel( frame )
koreaText = wx.TextCtrl( panel1 )
sizer1 = wx.StaticBoxSizer( wx.VERTICAL, panel1, "국어" )
sizer1.Add( koreaText )
panel1.SetSizer( sizer1 )

panel2 = wx.Panel( frame )
mathText = wx.TextCtrl( panel2 )
sizer2 = wx.StaticBoxSizer( wx.VERTICAL, panel2, "수학" )
sizer2.Add( mathText )
panel2.SetSizer( sizer2 )

panel3 = wx.Panel( frame )
englishList = [ "A", "B", "C", "D" ]
combo = wx.ComboBox( panel3, choices = englishList, style = wx.CB_READONLY )

sizer3 = wx.StaticBoxSizer( wx.VERTICAL, panel3, "영어" )
panel3.SetSizer( sizer3 )
sizer3.Add( combo )

sizer4 = wx.BoxSizer( wx.VERTICAL )
frame.SetSizer( sizer4 )
sizer4.Add( lbl )
sizer4.Add( panel1 )
sizer4.Add( panel2 )
sizer4.Add( panel3 )

frame.Show( True )
app.MainLoop()
