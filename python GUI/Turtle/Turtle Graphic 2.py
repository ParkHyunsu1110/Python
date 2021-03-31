##원과 관련된 함수들	
##circle( 반지름, 각도 ) 반지름을 가지고, 각도에 해당하는 반지름 또는, 부채꼴을 그리는 함수
##circle( 반지름, 각도, 다각형 )
##pensize( 굵기 )
##pencolor( 색상 )
##bgcolor( 색상 )
##fillcolor( 색상 )
##color( 펜색상, 채우기색상 )
##begin_fill()
##end_fill()

##
##import turtle as t
##
##t.shape( "turtle" )
####t.circle(100)
##t.circle(100, 360, 5)
##
##t.done()

	
##pensize( 굵기 )       # 선의 굵기를 지정한다
##pencolor( 색상 )     # 선의 색상을 지정한다
	
##import turtle as t
## 
##t.shape( "turtle" )
## 
##t.forward( 50 )
##t.pensize( 3 )
##t.forward( 50 )
##t.pensize( 1 )
##t.forward( 50 )
##t.pencolor( "blue" )
##t.forward( 50 )
##t.pencolor( "red" )
##t.forward( 50 )
##t.done()
	
##bgcolor( 색상 )    # 배경 색상을 칠하는 코드
##fillcolor( 색상 )     # 도형 내부 색상을 지정하는 코드
##begin_fill()    # 내부 색상을 칠하는 코드
##end_fill()     # 내부 색상 칠하기를 끝내는 코드

##import turtle as t
## 
##t.shape( "turtle" )
## 
##t.fillcolor( "yellow" )
##t.begin_fill()
##t.circle( 40 )
##t.forward( 100 )
##t.circle( 40 )
##t.end_fill()
##t.forward( 100 )
##t.circle( 40 )
##t.done()
	
##import turtle as t
## 
##	
##t.shape( "turtle" )
## 
##t.fillcolor( "yellow" )
##t.begin_fill()
##t.circle( 40 )
##t.forward( 100 )
##t.end_fill()
##t.fillcolor( "blue" )
##t.begin_fill()
##t.circle( 40 )
##t.end_fill()
##t.forward( 100 )
##t.circle( 40 )
##t.done()

import turtle as t
 
t.shape( "turtle" )
 
t.bgcolor( "green" )
