##wxPython 실습 2 - 4
import wx
app = wx.App()
frame = wx.Frame( None )

menubar = wx.MenuBar()
frame.SetMenuBar( menubar )

settingMenu = wx.Menu()
menubar.Append( settingMenu, "설정" )
settingItem = wx.MenuItem( id = wx.ID_ANY, text = "환경설정" )
endItem = wx.MenuItem( id = wx.ID_ANY, text = "종료" )
settingMenu.Append( settingItem )
settingMenu.Append( endItem )

frame.Show( True )
app.MainLoop()
