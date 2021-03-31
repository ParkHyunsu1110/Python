##wxPython 실습 2 - 1
import wx

app = wx.App()
frame = wx.Frame( None )

panel_gender = wx.Panel( frame )
manRB = wx.RadioButton( panel_gender, label = "남자", style = wx.RB_GROUP ) 
womanRB = wx.RadioButton( panel_gender, label = "여자")
sizer1 = wx.StaticBoxSizer( wx.HORIZONTAL, panel_gender, "성별" )

sizer1.Add( manRB )
sizer1.Add( womanRB )
panel_gender.SetSizer( sizer1 )

panel_grade = wx.Panel( frame )
firstRB = wx.RadioButton( panel_grade, label = "1학년", style = wx.RB_GROUP )
secondRB = wx.RadioButton( panel_grade, label = "2학년" )
thirdRB = wx.RadioButton( panel_grade, label = "3학년" )
sizer2 = wx.StaticBoxSizer( wx.HORIZONTAL, panel_grade, "학년" )

sizer2.Add( firstRB )
sizer2.Add( secondRB )
sizer2.Add( thirdRB )
panel_grade.SetSizer( sizer2 )

sizer3 = wx.BoxSizer( wx.VERTICAL )
frame.SetSizer( sizer3 )
sizer3.Add( panel_gender )
sizer3.Add( panel_grade )

frame.Show( True )
app.MainLoop()
