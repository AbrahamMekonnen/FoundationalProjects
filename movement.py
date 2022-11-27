from turtle import*

mv = Screen()
eye1 = Turtle()
eye2 = Turtle()
face = Turtle()
mouth = Turtle()
nose = Turtle()
n = 8
for i in range(0,n+2, 4):
    eye1.penup()
    eye1.goto(-90,120)
    eye1.pendown()
    eye1.circle(i*n)
    eye2.penup()
    eye2.goto(90,120)
    eye2.pendown()
    eye2.circle(i*n)
for i in range(3):
    nose.penup()
    nose.goto(-30,-20)
    nose.pendown()
    nose.circle(i*200,25)
    
