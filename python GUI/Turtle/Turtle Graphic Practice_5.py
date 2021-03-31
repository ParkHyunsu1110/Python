##터틀 그래픽 5번째 실습
import turtle as t
t.shape( "turtle" )
    
##사각형 2개
t.fillcolor("skyblue")
t.begin_fill()
for i in range(3):
    t.forward(100)
    t.right(90)
t.forward(100)
t.end_fill()

t.penup()
t.forward(10)
t.right(90)
t.pendown()

t.forward(110)
t.right(90)
for i in range(4):
    t.forward(120)
    t.right(90)

t.forward(120)
t.left(90)

t.penup()
t.forward(300)
t.pendown()

##별
t.pencolor("yellow")
t.fillcolor("yellow")
t.begin_fill()
for i in range(5):
    t.forward(100)
    t.right(144)
    t.forward(100)
    t.left(72)
t.end_fill()

t.left(90)
t.penup()
t.forward(400)
t.pendown()
t.left(90)
t.pensize(10)

##무지개
t.pencolor("red")
t.forward(100)
t.penup()
t.right(90)
t.forward(10)
t.right(90)
t.pendown()

t.pencolor("orange")
t.forward(100)
t.penup()
t.left(90)
t.forward(10)
t.left(90)
t.pendown()

t.pencolor("yellow")
t.forward(100)
t.penup()
t.right(90)
t.forward(10)
t.right(90)
t.pendown()

t.pencolor("green")
t.forward(100)
t.penup()
t.left(90)
t.forward(10)
t.left(90)
t.pendown()

t.pencolor("skyblue")
t.forward(100)
t.penup()
t.right(90)
t.forward(10)
t.right(90)
t.pendown()

t.pencolor("blue")
t.forward(100)
t.penup()
t.left(90)
t.forward(10)
t.left(90)
t.pendown()

t.pencolor("purple")
t.forward(100)
t.penup()
t.right(90)
t.forward(10)
t.right(90)
t.pendown()

t.done()
