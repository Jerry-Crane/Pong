import turtle
import winsound

#Background
# The size of the converted .wav file of the music is too big, so I had to shorten it.
winsound.PlaySound("score.wav", winsound.SND_ASYNC)

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)

#A
a = turtle.Turtle()
a.speed(0)
a.shape("square")
a.color("white")
a.penup()
a.goto(-350,0)
a.shapesize(stretch_wid=5, stretch_len=1)

#B
b = turtle.Turtle()
b.speed(0)
b.shape("square")
b.color("white")
b.penup()
b.goto(+350,0)
b.shapesize(stretch_wid=5, stretch_len=1)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("pink")
ball.penup()
ball.goto(0,0)
ball.dx = 0.07
ball.dy = 0.07

# Control functions
  # a
def a_up():
    y = a.ycor()
    y += 20
    a.sety(y)

def a_down():
    y = a.ycor()
    y -= 20
    a.sety(y)

  # b
def b_up():
    y = b.ycor()
    y += 20
    b.sety(y)

def b_down():
    y = b.ycor()
    y -= 20
    b.sety(y)


# Score
scr = turtle.Turtle()
scr.speed(0)
scr.color("white")
scr.penup()
scr.hideturtle()
scr.goto(0, 260)
scr.write("Paradis Island: 0  Marley: 0", align="center", font=("Courier", 24, "normal"))

scr_a = 0
scr_b = 0

#Call function
wn.listen()
wn.onkeypress(a_up, "w")
wn.onkeypress(a_down, "s")

wn.onkeypress(b_up, "Up")
wn.onkeypress(b_down, "Down")



# main loop
while True:
    wn.update()

    #ball move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bottle_pop_1.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bottle_pop_1.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
       ball.goto(0,0)
       ball.dx *= -1
       scr_a += 1
       scr.clear()
       scr.write("Paradis Island: {}  Marley: {}".format(scr_a, scr_b), align="center", font=("Courier", 24, "normal"))
       winsound.PlaySound("bottle_pop_1.wav", winsound.SND_ASYNC)
       
    if ball.xcor() < -390:
       ball.goto(0,0)
       ball.dx *= -1
       scr_b += 1
       scr.clear()
       scr.write("Paradis Island: {}  Marley: {}".format(scr_a, scr_b), align="center", font=("Courier", 24, "normal"))
       winsound.PlaySound("bottle_pop_1.wav", winsound.SND_ASYNC)

    # paddle collide ball
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < b.ycor() + 50 and ball.ycor() > b.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1
        winsound.PlaySound("bottle_pop_1.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -330 and ball.xcor() < 350) and (ball.ycor() < a.ycor() + 50 and ball.ycor() > a.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1
        winsound.PlaySound("bottle_pop_1.wav", winsound.SND_ASYNC)
       
        












        
