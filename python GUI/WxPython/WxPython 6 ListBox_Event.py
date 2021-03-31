##ListBox

##ListBox에 사용되는 스타일 속성

##LB_SINGLE   : 한 개만 선택할 수 있다
##LB_MULTIPLE   : 여러 개를 선택할 수 있다.
##LB_HSCROLL   : 글씨가 너무 길면 가로 스크롤바가 나타난다.
##LB_ALWAYS_SB   : 항상 세로 스크롤바를 나타낸다.
##LB_SORT   : 항목을 오름차순으로 정렬한다.

##import wx
##app = wx.App()
##frame = wx.Frame( None )
##
##nameList = ["kim", "Lee", "Park", "Choi", "Jeong", "Lim", "Won", "Joo", "Yoon" ]
##
##listBox = wx.ListBox( frame, choices = nameList, style = wx.LB_ALWAYS_SB )
##
##frame.Show()
##app.MainLoop()

##ListBox

##ListBox에 사용 되는 이벤트 상수

##EVT_LISTBOX   : 선택된 것이 변경될 때마다 발생
##EVT_LISTBOX_DCLICK   : 어떤 항목을 더블클릭 할 때마다 발생

import wx

app = wx.App()
frame = wx.Frame( None )

fruitsList = [ "딸기", "사과", "수박", "복숭아", "포도", "오렌지", "귤", "레몬" ]
basket = []

fruitsBox = wx.ListBox( frame, choices = fruitsList )

def buyFruits( event ):
    fruit = fruitsList[ fruitsBox.GetSelection() ]
    basket.append( fruit )
    print( "현재 장바구니 목록 : ", end = "" )
    for i in basket :
        print( i , end = "," )
    print()

fruitsBox.Bind( wx.EVT_LISTBOX_DCLICK, buyFruits )

frame.Show()
app.MainLoop()
