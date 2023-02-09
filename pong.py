import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("Black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # maximum possible speed
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("blue")
paddle_a.penup()  # no drawing when moving
paddle_a.goto(-350, 0)  # start position

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # maximum possible speed
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("red")
paddle_b.penup()  # no drawing when moving
paddle_b.goto(350, 0)  # start position

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2


def paddle_move(paddle, side):
    y = paddle.ycor()
    y += side
    paddle.sety(y)


window.listen()
window.onkeypress(lambda: paddle_move(paddle_a, 25), "w")
window.onkeypress(lambda: paddle_move(paddle_a, -25), "s")
window.onkeypress(lambda: paddle_move(paddle_b, 25), "Up")
window.onkeypress(lambda: paddle_move(paddle_b, -25), "Down")

# Main game loop
while True:
    window.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -340 and (ball.ycor() > paddle_a.ycor() - 50 and (ball.ycor() < paddle_a.ycor() + 50)):
        ball.dx *= -1
    if ball.xcor() > 340 and (ball.ycor() > paddle_b.ycor() - 50 and (ball.ycor() < paddle_b.ycor() + 50)):
        ball.dx *= -1
