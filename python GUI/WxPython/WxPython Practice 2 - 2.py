##wxPython 실습 2 - 2
import wx
app = wx.App()
frame = wx.Frame(None)

panel1 = wx.Panel( frame )
nametxt = wx.TextCtrl( panel1 )
sizer0 = wx.StaticBoxSizer( wx.VERTICAL, panel1, "이름" )
sizer0.Add( nametxt )
panel1.SetSizer( sizer0 )

panel2 = wx.Panel( frame )
manRB = wx.RadioButton( panel2, label = "남자", style = wx.RB_GROUP ) 
womanRB = wx.RadioButton( panel2, label = "여자")
sizer1 = wx.StaticBoxSizer( wx.VERTICAL, panel2, "성별" )

sizer1.Add( manRB )
sizer1.Add( womanRB )
panel2.SetSizer( sizer1 )

panel3 = wx.Panel( frame )
movieCB = wx.CheckBox( panel3, label = "영화")
bookCB = wx.CheckBox( panel3, label = "독서")
tripCB = wx.CheckBox( panel3, label = "여행")
workCB = wx.CheckBox( panel3, label = "운동")
sizer2 = wx.StaticBoxSizer( wx.VERTICAL, panel3, "취미" )

sizer2.Add( movieCB )
sizer2.Add( bookCB )
sizer2.Add( tripCB )
sizer2.Add( workCB )
panel3.SetSizer( sizer2 )

panel4 = wx.Panel( frame )
btn = wx.Button( panel4, label = "입력" )
sizer3 = wx.BoxSizer( wx.VERTICAL )

sizer3.Add( btn )
panel4.SetSizer( sizer3 )

grid = wx.GridSizer( 2, 2, 10, 10 )
frame.SetSizer( grid )

grid.Add( panel1, 0, wx.EXPAND )
grid.Add( panel2, 0, wx.EXPAND )
grid.Add( panel3, 0, wx.EXPAND )
grid.Add( panel4, 0, wx.EXPAND )

frame.Show( True )
app.MainLoop()
