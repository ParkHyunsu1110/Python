import wx
 
app = wx.App()
frame = wx.Frame( None )
  
panel1 = wx.Panel( frame )
btn1 = wx.Button( panel1, label = "버튼1" )
btn2 = wx.Button( panel1, label = "버튼2" )
btn3 = wx.Button( panel1, label = "버튼3" )
sizer1 = wx.BoxSizer( wx.HORIZONTAL )
sizer1.Add( btn1 )
sizer1.Add( btn2 )
sizer1.Add( btn3 )
panel1.SetSizer( sizer1 )
 
panel2 = wx.Panel( frame )
btn4 = wx.Button( panel2, label = "버튼4" )
btn5 = wx.Button( panel2, label = "버튼5" )
btn6 = wx.Button( panel2, label = "버튼6" )
sizer2 = wx.BoxSizer( wx.VERTICAL )
sizer2.Add( btn4 )
sizer2.Add( btn5 )
sizer2.Add( btn6 )
panel2.SetSizer( sizer2 )
 
sizer3 = wx.GridSizer( 2, 1, 10, 10 )
frame.SetSizer( sizer3 )
sizer3.Add( panel1 )
sizer3.Add( panel2 )
 
 
frame.Show()
app.MainLoop()

