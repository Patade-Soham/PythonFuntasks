import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
color_list= [ (234, 225, 83), (195, 8, 69), (231, 54, 132), (194, 164, 15), (112, 178, 214), (199, 77, 15),
              (216, 162, 101), (34, 187, 112), (29, 104, 167), (14, 23, 64), (20, 29, 168), (212, 136, 175),
              (231, 224, 7), (197, 34, 130), (15, 181, 210), (231, 167, 197), (126, 189, 163), (10, 48, 29),
              (40, 131, 75), (141, 217, 203), (61, 22, 10), (60, 13, 27), (108, 91, 210), (235, 64, 34),
              (131, 217, 230), (183, 17, 9)]



timmy=Turtle()
timmy.shape("arrow")
timmy.speed('fastest')
timmy.penup()
timmy.setheading(230)
timmy.forward(300)
timmy.setheading(0)
number_of_dots=100

for dot_count in range(1,number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)




screen = Screen()
screen.exitonclick()
