from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.pencolor('red')

def square():
    for i in range(4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(90)
def triangle():
    for i in range(3):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(120)
def pentagon():
    for i in range(5):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(72)
def hexagon():
    for i in range(6):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(60)
def heptagon():
    for i in range(7):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(51.43)
def octagon():
    for i in range(8):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(45)
def nonagon():
    for i in range(9):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(40)
def decagon():
    for i in range(10):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(36)

triangle()
timmy_the_turtle.pencolor('green')
square()
timmy_the_turtle.pencolor('blue')
pentagon()
timmy_the_turtle.pencolor('yellow')
hexagon()
timmy_the_turtle.pencolor('orange')
heptagon()
timmy_the_turtle.pencolor('purple')
nonagon()
timmy_the_turtle.pencolor('indigo')
decagon()




screen = Screen()
screen.exitonclick()
