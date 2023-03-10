import turtle
import os

b_count = 0
a_count = 0

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

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 256)
pen.color("white")
pen.write("Blue: 0 Red: 0", align="center", font=["Helvetica", 25])


def paddle_move(paddle, side):
    y = paddle.ycor()
    if y + side < 250 and (y + side > -250):
        y += side
        paddle.sety(y)


window.listen()
window.onkeypress(lambda: paddle_move(paddle_a, 30), "w")
window.onkeypress(lambda: paddle_move(paddle_a, -30), "s")
window.onkeypress(lambda: paddle_move(paddle_b, 30), "Up")
window.onkeypress(lambda: paddle_move(paddle_b, -30), "Down")

# Main game loop
while True:
    window.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1
        os.system("afplay bounce.mp3&")
    if ball.xcor() > 390:
        b_count += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write("Blue: {} Red: {}".format(b_count, a_count), align="center", font=["Helvetica", 25])
        os.system("afplay score.mp3&")
    if ball.xcor() < -390:
        a_count += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write("Blue: {} Red: {}".format(b_count, a_count), align="center", font=["Helvetica", 25])
        os.system("afplay score.mp3&")

    if (ball.xcor() < -340) and ball.xcor() > -350 and (
            ball.ycor() > paddle_a.ycor() - 50 and (ball.ycor() < paddle_a.ycor() + 50)):
        ball.dx *= -1
        os.system("afplay bounce.mp3&")

    if (ball.xcor() > 340) and ball.xcor() < 350 and (
            ball.ycor() > paddle_b.ycor() - 50 and (ball.ycor() < paddle_b.ycor() + 50)):
        ball.dx *= -1
        os.system("afplay bounce.mp3&")
