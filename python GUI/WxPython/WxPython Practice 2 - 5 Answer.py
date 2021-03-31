import wx

app = wx.App()
frame = wx.Frame( None )

#메뉴바
menubar = wx.MenuBar()
frame.SetMenuBar( menubar )

setMenu = wx.Menu()
menubar.Append( setMenu, "설정" )

frame.SetTitle( "계산기 만들기" )
mainSizer = wx.BoxSizer( wx.VERTICAL )
frame.SetSizer( mainSizer )

numbers = []
expression = []

#텍스트
panel1 = wx.Panel( frame )
sizer1 = wx.GridSizer( 1, 1, 50, 50 )
panel1.SetSizer( sizer1 )

numberText = wx.TextCtrl( panel1, style = wx.TE_READONLY )
sizer1.Add( numberText, flag = wx.EXPAND )
mainSizer.Add( panel1, flag = wx.EXPAND )

#키패드
panel2 = wx.Panel( frame )
sizer2 = wx.BoxSizer( wx.HORIZONTAL )
panel2.SetSizer( sizer2 )

mainSizer.Add( panel2, flag = wx.EXPAND )

#숫자
panel3 = wx.Panel( panel2 )
sizer3 = wx.GridSizer( 4, 3, 10, 10 )
panel3.SetSizer( sizer3 )

btn1 = wx.Button( panel3, label = "1" )
btn2 = wx.Button( panel3, label = "2" )
btn3 = wx.Button( panel3, label = "3" )
btn4 = wx.Button( panel3, label = "4" )
btn5 = wx.Button( panel3, label = "5" )
btn6 = wx.Button( panel3, label = "6" )
btn7 = wx.Button( panel3, label = "7" )
btn8 = wx.Button( panel3, label = "8" )
btn9 = wx.Button( panel3, label = "9" )
btn0 = wx.Button( panel3, label = "0" )
btn00 = wx.Button( panel3, label = "00" )
equalsbtn = wx.Button( panel3, label = "=" )

#숫자 함수
def number1( event ):
    line = numberText.GetValue()
    line = line + "1"
    numberText.SetValue( line )
def number2( event ):
    line = numberText.GetValue()
    line = line + "2"
    numberText.SetValue( line )
def number3( event ):
    line = numberText.GetValue()
    line = line + "3"
    numberText.SetValue( line )
def number4( event ):
    line = numberText.GetValue()
    line = line + "4"
    numberText.SetValue( line )
def number5( event ):
    line = numberText.GetValue()
    line = line + "5"
    numberText.SetValue( line )
def number6( event ):
    line = numberText.GetValue()
    line = line + "6"
    numberText.SetValue( line )
def number7( event ):
    line = numberText.GetValue()
    line = line + "7"
    numberText.SetValue( line )
def number8( event ):
    line = numberText.GetValue()
    line = line + "8"
    numberText.SetValue( line )
def number9( event ):
    line = numberText.GetValue()
    line = line + "9"
    numberText.SetValue( line )
def number0( event ):
    line = numberText.GetValue()
    line = line + "0"
    numberText.SetValue( line )
def number00( event ):
    line = numberText.GetValue()
    line = line + "00"
    numberText.SetValue( line )
def addEquals( event ):
    line = numberText.GetValue()
    numbers.append( int(line ) )

    print( "result : ", expression[0] )

    if expression[0] == "+" :
        numberText.SetValue( str( numbers[0] + numbers[1] ) )
        
    elif expression[0] == "-" :
        numberText.SetValue( str( numbers[0] - numbers[1] ) )
        
    elif expression[0] == "*" :
        numberText.SetValue( str( numbers[0] * numbers[1] ) )
        
    elif expression[0] == "/" :
        numberText.SetValue( str( numbers[0] / numbers[1] ) )
        
    else :
        numberText.SetValue( str( numbers[0]) )

btn1.Bind( wx.EVT_BUTTON, number1 )
btn2.Bind( wx.EVT_BUTTON, number2 )
btn3.Bind( wx.EVT_BUTTON, number3 )
btn4.Bind( wx.EVT_BUTTON, number4 )
btn5.Bind( wx.EVT_BUTTON, number5 )
btn6.Bind( wx.EVT_BUTTON, number6 )
btn7.Bind( wx.EVT_BUTTON, number7 )
btn8.Bind( wx.EVT_BUTTON, number8 )
btn9.Bind( wx.EVT_BUTTON, number9 )
btn0.Bind( wx.EVT_BUTTON, number0 )
btn00.Bind( wx.EVT_BUTTON, number00 )
equalsbtn.Bind( wx.EVT_BUTTON, addEquals )

sizer3.Add( btn1 )
sizer3.Add( btn2 )
sizer3.Add( btn3 )
sizer3.Add( btn4 )
sizer3.Add( btn5 )
sizer3.Add( btn6 )
sizer3.Add( btn7 )
sizer3.Add( btn8 )
sizer3.Add( btn9 )
sizer3.Add( btn0 )
sizer3.Add( btn00 )
sizer3.Add( equalsbtn )

sizer2.Add( panel3, flag = wx.EXPAND )

#연산기호
panel4 = wx.Panel( panel2 )
sizer4 = wx.GridSizer( 4, 1, 10, 10 )
panel4.SetSizer( sizer4 )

plusBtn = wx.Button( panel4, label = "+" )
minusBtn = wx.Button( panel4, label = "-" )
multipleBtn = wx.Button( panel4, label = "*" )
divisionBtn = wx.Button( panel4, label = "/" )

def addPlus( event ) :
    line = numberText.GetValue()
    numbers.append( int( line ) )
    expression.append( "+" )
    line = ""
    numberText.SetValue( line )
 
def addMinus( event ) :
    line = numberText.GetValue()
    numbers.append( int( line ) )
    expression.append( "-" )
    line = ""
    numberText.SetValue( line )
 
def addMultiple( event ) :
    line = numberText.GetValue()
    numbers.append( int( line ) )
    expression.append( "*" )
    line = ""
    numberText.SetValue( line )
 
def addDivision( event ) :
    line = numberText.GetValue()
    numbers.append( int( line ) )
    expression.append( "/" )
    line = ""
    numberText.SetValue( line )
	
plusBtn.Bind( wx.EVT_BUTTON, addPlus )
minusBtn.Bind( wx.EVT_BUTTON, addMinus )
multipleBtn.Bind( wx.EVT_BUTTON, addMultiple )
divisionBtn.Bind( wx.EVT_BUTTON, addDivision )
 
sizer4.Add( plusBtn, flag = wx.EXPAND )
sizer4.Add( minusBtn, flag = wx.EXPAND )
sizer4.Add( multipleBtn, flag = wx.EXPAND )
sizer4.Add( divisionBtn, flag = wx.EXPAND )
 
sizer2.Add( panel4, flag = wx.EXPAND )

frame.Show(True)
app.MainLoop()
