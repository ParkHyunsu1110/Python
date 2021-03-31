##wxPython 실습 2 - 5
import wx
app = wx.App()
frame = wx.Frame( None )
##메뉴바
menubar = wx.MenuBar()
frame.SetMenuBar( menubar )

settingMenu = wx.Menu()
menubar.Append( settingMenu, "설정" )

##결과창
panel1 = wx.Panel( frame )

resultText = wx.TextCtrl( panel1,  style = wx.TE_READONLY )
sizer1 = wx.BoxSizer( wx.HORIZONTAL )
sizer1.Add( resultText )
panel1.SetSizer( sizer1 )

##버튼마다 함수 적용
calculator = []

for n in input('숫자와 기호 입력 : ').split():
    calculator.append(n)

if calculator[1] == '+':
    result = int(calculator[0]) + int(calculator[2])
elif calculator[1] == '-':
    result = int(calculator[0]) - int(calculator[2])

elif calculator[1] == '*':
    result = int(calculator[0]) * int(calculator[2])

elif calculator[1] == '/':
    result = int(calculator[0]) / int(calculator[2])

panel2 = wx.Panel( frame )

def One( event ):
    resultText.SetValue("1")
btn1 = wx.Button( panel2, label = "1" )
btn1.Bind( wx.EVT_BUTTON, One )

def Two( event ):
    resultText.SetValue("2")
btn2 = wx.Button( panel2, label = "2" )
btn2.Bind( wx.EVT_BUTTON, Two )

def Three( event ):
    resultText.SetValue("3")
btn3 = wx.Button( panel2, label = "3" )
btn3.Bind( wx.EVT_BUTTON, Three )

def Four( event ):
    resultText.SetValue( "4" )
btn4 = wx.Button( panel2, label = "4" )
btn4.Bind( wx.EVT_BUTTON, Four )

def Five( event ):
    resultText.SetValue( "5" )
btn5 = wx.Button( panel2, label = "5" )
btn5.Bind( wx.EVT_BUTTON, Five )

def Six( event ):
    resultText.SetValue( "6" )
btn6 = wx.Button( panel2, label = "6" )
btn6.Bind( wx.EVT_BUTTON, Six )

def Seven( event ):
    resultText.SetValue( "7" )
btn7 = wx.Button( panel2, label = "7" )
btn7.Bind( wx.EVT_BUTTON, Seven )

def Eight( event ):
    resultText.SetValue( "8" )
btn8 = wx.Button( panel2, label = "8" )
btn8.Bind( wx.EVT_BUTTON, Eight )

def Nine( event ):
    resultText.SetValue( "9" )
btn9 = wx.Button( panel2, label = "9" )
btn9.Bind( wx.EVT_BUTTON, Nine )

def Zero( event ):
    resultText.SetValue( "0" )
btn0 = wx.Button( panel2, label = "0" )
btn0.Bind( wx.EVT_BUTTON, Zero )

def Zerozero( event ):
    resultText.SetValue( "00" )
btn00 = wx.Button( panel2, label = "00" )
btn00.Bind( wx.EVT_BUTTON, Zerozero )

def Plus( event ):
    resultText.SetValue( " + " )
btn_plus = wx.Button( panel2, label = "+" )
btn_plus.Bind( wx.EVT_BUTTON, Plus )

def Sub( event ):
    resultText.SetValue( " - " )
btn_sub = wx.Button( panel2, label = "-" )
btn_sub.Bind( wx.EVT_BUTTON, Sub )

def Prod( event ):
    resultText.SetValue( " * " )
btn_prod = wx.Button( panel2, label = "*" )
btn_prod.Bind( wx.EVT_BUTTON, Prod )

def Div( event ):
    resultText.SetValue( " / " )
btn_div = wx.Button( panel2, label = "/" )
btn_div.Bind( wx.EVT_BUTTON, Div )

def Equals( event ):
    resultText.SetValue( str(result) )
btn_equals = wx.Button( panel2, label = "=" )
btn_equals.Bind( wx.EVT_BUTTON, Equals )


##계산기 틀
grid = wx.GridSizer(4, 4, 20, 20 )
panel2.SetSizer( grid )

grid.Add( btn1, 0, wx.EXPAND )
grid.Add( btn2, 0, wx.EXPAND )
grid.Add( btn3, 0, wx.EXPAND )
grid.Add( btn_plus, 0, wx.EXPAND )

grid.Add( btn4, 0, wx.EXPAND )
grid.Add( btn5, 0, wx.EXPAND )
grid.Add( btn6, 0, wx.EXPAND )
grid.Add( btn_sub, 0, wx.EXPAND )

grid.Add( btn7, 0, wx.EXPAND )
grid.Add( btn8, 0, wx.EXPAND )
grid.Add( btn9, 0, wx.EXPAND )
grid.Add( btn_prod, 0, wx.EXPAND )

grid.Add( btn0, 0, wx.EXPAND )
grid.Add( btn00, 0, wx.EXPAND )
grid.Add( btn_equals, 0, wx.EXPAND )
grid.Add( btn_div, 0, wx.EXPAND )

sizer = wx.BoxSizer( wx.VERTICAL )
frame.SetSizer( sizer )
sizer.Add( panel1 )
sizer.Add( panel2 )

frame.Show( True )
app.MainLoop()
