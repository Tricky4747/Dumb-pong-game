import turtle

window = turtle.Screen()

window.title('Pong Game by Rithu')
window.bgcolor("black")
window.setup(800, 600)
window.tracer()

# paddle a
paddle_a = turtle.Turtle()
paddle_a.speed()
paddle_a.shape('square')
paddle_a.shapesize(4, 0.8)
paddle_a.color('cyan')
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle b

paddle_b = turtle.Turtle()
paddle_b.speed()
paddle_b.shape('square')
paddle_b.shapesize(4, 0.8)
paddle_b.color('purple')
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed()
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0, 0)

ball.dx = 5
ball.dy = 5
# Functions


def paddle_a_up():
    y = paddle_a.ycor()
    y += 33
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 33
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 33
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 33
    paddle_b.sety(y)


# keyword binding
window.listen()
window.onkeypress(paddle_a_up, 'w')
window.onkeypress(paddle_a_down, 's')
window.onkeypress(paddle_b_up, 'Up')
window.onkeypress(paddle_b_down, 'Down')

# game loop
while True:
    window.update()

    # ball movement
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # bouncing(ball)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # ball reset
    if ball.xcor() > 410:
        ball.hideturtle()
        ball.goto(0, 0)
        ball.showturtle()
        ball.dx = 5
        ball.dy = 5
        ball.dx *= -1
        ball.dy *= -1

    if ball.xcor() < -410:
        ball.hideturtle()
        ball.goto(0, 0)
        ball.showturtle()
        ball.dx = 5
        ball.dy = 5
        ball.dx *= -1

    # bouncing off paddles
    if ball.xcor() > 340 and ball.xcor() < 370 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1.1

    if ball.xcor() < -340 and ball.xcor() > -370 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
        ball.setx(-340)
        ball.dx *= -1.1

   # paddle reset
    if paddle_a.ycor() < -330:
        paddle_a.hideturtle
        paddle_a.goto(paddle_a.xcor(), 330)
        paddle_a.showturtle

    if paddle_b.ycor() < -330:
        paddle_b.hideturtle
        paddle_b.goto(paddle_b.xcor(), 330)
        paddle_b.showturtle

    if paddle_a.ycor() > 330:
        paddle_a.hideturtle
        paddle_a.goto(paddle_a.xcor(), -330)
        paddle_a.showturtle

    if paddle_b.ycor() > 330:
        paddle_b.hideturtle
        paddle_b.goto(paddle_b.xcor(), -330)
        paddle_b.showturtle
