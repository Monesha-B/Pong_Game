from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
score = Score()

# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.up()
# paddle.home()
# paddle.shapesize(stretch_len=0.75, stretch_wid=5)
# paddle.goto(350,0)
#
#
# def paddleup():
#     paddle.goto(350,250)
#
# def paddledown():
#     paddle.goto(350, -250)

screen.listen()
screen.onkey(key="Up", fun=right_paddle.paddle_up)
screen.onkey(key="Down", fun=right_paddle.paddle_down)
screen.onkey(key="w", fun=left_paddle.paddle_up)
screen.onkey(key="s", fun=left_paddle.paddle_down)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(right_paddle) < 100 and ball.xcor() > 320 or ball.distance(left_paddle) < 100 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 350:
        ball.reset_position()
        score.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -350:
        ball.reset_position()
        score.r_point()

# game_is_on = True
# t = 0.5
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     ball.move()
#
#
#     if ball.ycor() > 285 or ball.ycor()< -285:
#         ball.bounce_y()
#
#
#
#     if ball.distance(right_paddle) < 100 and ball.xcor() > 320:
#         ball.bounce_x()
#         t -= 0.09
#         score.l_point()
#     elif ball.distance(left_paddle) < 100 and ball.xcor() < -320:
#         ball.bounce_x()
#         t -= 0.09
#         score.r_point()
#
#
#     if ball.xcor() >= 350 or ball.xcor() < -340:
#         ball.refresh()
#         # print("went off the limit")

screen.exitonclick()