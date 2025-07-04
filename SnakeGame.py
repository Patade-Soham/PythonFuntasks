from turtle import Turtle,Screen
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')

starting_position = [(0,0),(-20,0),(-40,0)]
turtles=[]
for position in starting_position:
    new_tim=Turtle()
    new_tim.shape('square')
    new_tim.color('white')
    new_tim.penup()
    new_tim.goto(position)
    turtles.append(new_tim)


game_is_on = True

while game_is_on:

    screen.update()

    time.sleep(0.1)

    for i in range(len(turtles)- 1, 0, -1):

        new_x = turtles[i].xcor()

        new_y = turtles[i].ycor()

        turtles[i].goto(new_x, new_y)

        turtles[0].forward(28)












screen.exitonclick()
