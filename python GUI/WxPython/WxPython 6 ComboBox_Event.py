##콤보 박스

##import wx
##
##app = wx.App()
##frame = wx.Frame( None )
##
##lbl = wx.StaticText( frame, label = "과일을 선택하세요. : " )
##fruitList = [ "사과", "수박", "딸기", "오렌지", "바나나", "키위", "오렌지", "귤" ]
##combo = wx.ComboBox( frame, choices = fruitList )
##
##sizer = wx.BoxSizer( wx.VERTICAL )
##frame.SetSizer( sizer )
##sizer.Add( lbl )
##sizer.Add( combo )
##
##frame.Show( True )
##app.MainLoop()

##콤보 박스에서 가장 유용하게 사용되는 상수

##CB_READONLY   : 콤보 박스에 직접 입력이 금지된다

##import wx
##
##app = wx.App()
##frame = wx.Frame( None )
##
##lbl = wx.StaticText( frame, label = "과일을 선택하세요. : " )
##fruitList = [ "사과", "수박", "딸기", "오렌지", "바나나", "키위", "오렌지", "귤" ]
##combo = wx.ComboBox( frame, choices = fruitList, style = wx.CB_READONLY )
##
##sizer = wx.BoxSizer( wx.VERTICAL )
##frame.SetSizer( sizer )
##sizer.Add( lbl )
##sizer.Add( combo )
##
##frame.Show( True )
##app.MainLoop()

##콤보박스에서 값이 변하는 이벤트

##EVT_COMBOBOX
##SetLabelText() : 라벨의 텍스트를 변경해 주기 위함.
import wx

app = wx.App()
frame = wx.Frame( None )

lbl = wx.StaticText( frame, label = "과일을 선택하세요. : " )
fruitList = [ "사과", "수박", "딸기", "오렌지", "바나나", "키위", "오렌지", "귤" ]
combo = wx.ComboBox( frame, choices = fruitList, style = wx.CB_READONLY )

sizer = wx.BoxSizer( wx.VERTICAL )
frame.SetSizer( sizer )
sizer.Add( lbl )
sizer.Add( combo )

def changeLabel( event ):
    lbl.SetLabelText( combo.GetValue() + "을(를) 선택하셨습니다!" )

combo.Bind( wx.EVT_COMBOBOX, changeLabel )


frame.Show( True )
app.MainLoop()
