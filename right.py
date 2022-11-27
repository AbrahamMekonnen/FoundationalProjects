from turtle import*
mv = Screen()
spaceship = Turtle()


#color("green")
speed(90)
def up():
    spaceship.setheading(90)
    

mv.listen()

mv.onkey(up, 'Up')

    
    

while True:
    spaceship.forward(speed)
    


