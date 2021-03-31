##터틀 그래픽 네번째 실습
import turtle as t


def location() :
    t.stamp()
    t.ontimer( location, 5000)

def removeAll():
    t.clear()

def moveForward():
    t.forward( 10 )
    
def turnLeft():
    t.left( 90 )
    
def turnRight():
    t.right( 90 )
    
def turnBack():
    t.right( 180 )

def colorRed():
    t.pencolor( "Red" )
    
def colorGreen():
    t.pencolor( "Green" )
    
def colorBlue():
    t.pencolor( "Blue" )

def drawCircle():
    t.circle(10)

t.shape( "turtle" )

t.ontimer( location, 5000 )

t.onscreenclick( removeAll )

t.onkeypress( moveForward, "Up" )
t.onkeypress( turnLeft, "Left")
t.onkeypress( turnRight, "Right")
t.onkeypress( turnBack, "Down")

t.onkeypress( colorRed, "r" )
t.onkeypress( colorBlue, "b" )
t.onkeypress( colorGreen, "g" )

t.onkeypress( drawCircle, "c")
t.listen()
t.done()
