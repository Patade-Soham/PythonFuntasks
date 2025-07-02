from turtle import Turtle, Screen

tim=Turtle()
screen=Screen()

def moveForward():
    tim.forward(10)
def moveBackward():
    tim.backward(10)
def moveLeft():
    tim.left(10)
def moveRight():
    tim.right(10)
def clearscreen():
    tim.clear()
    tim.penup()
    tim.home()

screen.listen()
screen.onkey(moveForward, "w")
screen.onkey(moveBackward, "s")
screen.onkey(moveLeft, "a")
screen.onkey(moveRight, "d")
screen.onkey(clearscreen, "c")

screen.exitonclick()
