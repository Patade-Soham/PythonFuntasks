from turtle import Turtle, Screen
import random
red_turtle=Turtle()
green_turtle=Turtle()
blue_turtle=Turtle()
yellow_turtle=Turtle()
screen=Screen()

red_turtle.color('red')
green_turtle.color('green')
blue_turtle.color('blue')
yellow_turtle.color('yellow')

red_turtle.shape('turtle')
green_turtle.shape('turtle')
blue_turtle.shape('turtle')
yellow_turtle.shape('turtle')

red_turtle.penup()
green_turtle.penup()
blue_turtle.penup()
yellow_turtle.penup()

screen.setup(640,600)

red_turtle.goto(-300,-40)
green_turtle.goto(-300,0)
blue_turtle.goto(-300,40)
yellow_turtle.goto(-300,80)

lis=[red_turtle,green_turtle,blue_turtle,yellow_turtle]


bet=screen.textinput(prompt='which turtle will win ? ', title='turtle_race')
is_race_on=False
if bet:
    is_race_on=True

def run(turt):

    num=random.randint(10,40)
    turt.forward(num)



while is_race_on:
    for turtle in lis:
        run(turtle)
        if turtle.xcor() > 280:
            print(f'{turtle.pencolor()} wins!')
            is_race_on=False
            if bet==turtle.pencolor():
                print('you won the bet')
            elif bet!=turtle.pencolor():
                print('you lose the bet')
            break













screen.exitonclick()
