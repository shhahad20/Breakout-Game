from turtle import Turtle, Screen
import time
from ball import Ball
from move import Paddle
from object import Walls
from scoreborad import Scoreboard


HEIGHT = 300
WIDTH = 300
screen = Screen()
screen.setup(width=700, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)


paddle = Paddle()
ball = Ball()
bricks = Walls()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.Left, "Left")
screen.onkey(paddle.Right, "Right")
game_is_on = True


def ball_frame():
    global ball, game_is_on, scoreboard

    if ball.xcor() > WIDTH or ball.xcor() < - WIDTH:
        ball.bounce(x_bounce=True, y_bounce=False)
        return

    if ball.ycor() > HEIGHT:
        ball.bounce(x_bounce=False, y_bounce=True)
        return

    if ball.ycor() < - HEIGHT:
        scoreboard.game_over()
        ball.reset()
        game_is_on = False
        return


def ballxrectangle():
    global ball, paddle
    # record x-axis coordinates of ball and rectangle
    paddle_x = paddle.xcor()
    ball_x = ball.xcor()

    if ball.distance(paddle) < 110 and ball.ycor() < -250:
        if paddle_x > 0:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return

        elif paddle_x < 0:
            if ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return
        else:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            elif ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return


def ballxxwalls():
    global ball, bricks , scoreboard

    for brick in bricks.walls:
        if ball.distance(brick) < 40:
            brick.quantity -= 1
            scoreboard.increase_score()
            if brick.quantity == 0:
                brick.clear()
                brick.goto(2000, 2000)
                bricks.walls.remove(brick)

            if ball.xcor() > brick.left_wall:
                ball.bounce(x_bounce=True, y_bounce=False)
            elif ball.xcor() > brick.right_wall:
                ball.bounce(x_bounce=True, y_bounce=False)
            elif ball.xcor() < brick.bottom_wall:
                ball.bounce(x_bounce=False, y_bounce=True)
            elif ball.xcor() > brick.upper_wall:
                ball.bounce(x_bounce=False, y_bounce=True)


while game_is_on:

    screen.update()
    time.sleep(0.03)
    ball.move()
    ball_frame()
    ballxrectangle()
    ballxxwalls()
    if len(bricks.walls) == 0:
        scoreboard.game_win()
        game_is_on = False
        break


screen.exitonclick()
