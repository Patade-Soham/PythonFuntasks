from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WINNING_SCORE = 5


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)


line = Turtle()
line.color("white")
line.hideturtle()
line.penup()
line.goto(0, 300)
line.setheading(270)
for _ in range(30):
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(10)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if (ball.distance(l_paddle) < 50 and ball.xcor() < -320) or \
       (ball.distance(r_paddle) < 50 and ball.xcor() > 320):
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

 
    if scoreboard.l_score == WINNING_SCORE or scoreboard.r_score == WINNING_SCORE:
        winner = "Left" if scoreboard.l_score == WINNING_SCORE else "Right"
        scoreboard.game_over(winner)
        game_is_on = False

screen.exitonclick()
