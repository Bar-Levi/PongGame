import turtle
import time
import os
import random

# Setting players' preferences.
flag = False
left_name = input("\nHey!\nBefore we start, please fill the following settings:\nEnter left player's name: ")
print("\nHey " + left_name + "!")
while not flag:
    LeftUpKey = input("(For using the arrows type 'Up'/'Down')\nEnter UP button: ")
    LeftDownKey = input("Enter DOWN button: ")
    if LeftUpKey != LeftDownKey:
        flag = True
    else:
        print("We're sorry " + left_name + ", but you chose the same button as 'Up' and 'Down' - Please choose 2 different buttons.")

flag = False
right_name = input("\nEnter right player's name: ")
print("Hey " + right_name + "!")
if LeftUpKey != 'Up' and LeftDownKey != 'Down':
    print("(For using the arrows type 'Up'/'Down')")
while not flag:
    RightUpKey = input("Enter UP button: ")
    RightDownKey = input("Enter DOWN button: ")
    if RightUpKey != RightDownKey:
        if RightUpKey != LeftUpKey and RightUpKey != LeftDownKey and RightDownKey != LeftUpKey and RightDownKey != LeftDownKey:
            flag = True
        else:
            print(
                "We're sorry " + right_name + ", buy one or more of your buttons is already in use - Please choose different buttons.")
    else:
        print(
            "We're sorry " + right_name + ", but you chose the same button as 'Up' and 'Down' - Please choose different buttons.")

WinScore = int(input("Choose the winning score: "))

# Creating the game window.
window_width = 1200
window_height = 400
window = turtle.Screen()
window.title("PingPong by BarLevi")
window.bgcolor("black")
window.setup(window_width, window_height)
window.tracer(0)

# Creating the left bat.
lb_width = 1
lb_height = 5
left_bat = turtle.Turtle()
left_bat.speed(0)
left_bat.shape("square")
left_bat.shapesize(lb_height, lb_width)
left_bat.color("yellow")
left_bat.penup()
left_bat.goto(-(window_width / 2 - 50), 0)

# Creating the right bat.
rb_width = 1
rb_height = 5
right_bat = turtle.Turtle()
right_bat.speed(0)
right_bat.shape("square")
right_bat.shapesize(rb_height, rb_width)
right_bat.color("yellow")
right_bat.penup()
right_bat.goto(window_width / 2 - 50, 0)

# Creating the ball.
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Creating the score.
pen1 = turtle.Turtle()
pen1.color("white")
pen1.speed(0)
pen1.hideturtle()
pen1.penup()
pen1.goto(0, 0)

pen2 = turtle.Turtle()
pen2.color("white")
pen2.speed(0)
pen2.hideturtle()
pen2.penup()

# Setting first teleporter
teleporter1 = turtle.Turtle()
teleporter1.pencolor("gray")
teleporter1.speed(1)
teleporter1.hideturtle()
teleporter1.penup()
triangle1 = turtle.Turtle()
triangle1.speed(0)
triangle1.color("gray")
triangle1.penup()
triangle1.hideturtle()


# Setting second teleporter
teleporter2 = turtle.Turtle()
teleporter2.pencolor("gray")
teleporter2.speed(1)
teleporter2.hideturtle()
teleporter2.penup()
triangle2 = turtle.Turtle()
triangle2.speed(0)
triangle2.color("gray")
triangle2.penup()
triangle2.hideturtle()

teleported = False
GameEnded = False

def SetTeleporters():
    global teleporter1
    global teleporter2
    radius = 15
    x = random.randrange(-int(window_width / 2 - window_width / 10), int(window_width / 2 - window_width / 10))
    y = random.randrange(-int(window_height / 2 - window_height / 10), int(window_height / 2 - window_height / 10))
    teleporter1.goto(x, y)
    teleporter1.pendown()
    teleporter1.circle(radius)
    triangle1.goto(x, y+radius)
    triangle1.showturtle()
    triangle1.shape("triangle")
    teleporter1.penup()
    x = random.randrange(-int(window_width / 2 - window_width / 10), int(window_width / 2 - window_width / 10))
    y = random.randrange(-int(window_height / 2 - window_height / 10), int(window_height / 2 - window_height / 10))
    teleporter2.goto(x, y)
    teleporter2.pendown()
    teleporter2.circle(radius)
    triangle2.goto(x, y+radius)
    triangle2.showturtle()
    triangle2.shape("triangle")
    teleporter2.penup()
    return True


def DeleteTeleporters():
    global teleporter1, teleporter2, triangle1, triangle2
    teleporter1.clear()
    teleporter2.clear()
    triangle1.hideturtle()
    triangle2.hideturtle()
    return False


def Teleport():
    global teleporter1, teleporter2, teleported
    if (not teleported and (teleporter1.xcor() - 20) <= ball.xcor() <= (teleporter1.xcor() + 20) and
            (teleporter1.ycor() - 20) <= ball.ycor() <= (teleporter1.ycor() + 20)):
        ball.setx(teleporter2.xcor())
        ball.sety(teleporter2.ycor())
        teleported = True
        os.system("afplay TeleportingSound.wav&")
    elif (not teleported and (teleporter2.xcor() - 20) <= ball.xcor() <= (teleporter2.xcor() + 20) and
            (teleporter2.ycor() - 20) <= ball.ycor() <= (teleporter2.ycor() + 20)):
        ball.setx(teleporter1.xcor())
        ball.sety(teleporter1.ycor())
        teleported = True
        os.system("afplay TeleportingSound.wav&")


def GameStart():
    global GameEnded
    GameEnded = False
    timer = 0
    teleporters_on = False
    global left_score, right_score, teleported
    left_score = right_score = 0
    pen1.clear()
    pen2.clear()
    pen2.goto(0, 0)
    pen2.write("Game is starting in ...", align="center", font=("Courier", 30, "normal"))
    pen1.goto(0, -50)
    pen1.write("3", align="center", font=("Courier", 50, "normal"))
    os.system("afplay 3Countdown.wav&")
    time.sleep(0.9)
    pen1.clear()
    pen1.write("2", align="center", font=("Courier", 50, "normal"))
    time.sleep(0.9)
    pen1.clear()
    pen1.write("1", align="center", font=("Courier", 50, "normal"))
    time.sleep(0.9)
    pen1.clear()
    pen2.clear()
    pen1.write("Good luck!", align="center", font=("Courier", 100, "normal"))
    time.sleep(0.9)
    pen1.clear()
    pen1.goto(0, window_height / 2 - 65)
    NewRound()
    while True:
        window.listen()
        timer += 1
        if timer % 210 == 0:
            os.system("afplay GameplaySound.wav&")
        if timer % 500 == 0:
            if teleporters_on:
                teleporters_on = DeleteTeleporters()
            else:
                teleporters_on = SetTeleporters()
        if teleporters_on:
            Teleport()
        # Moves the ball.
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        # Border checking.
        if ball.ycor() >= (window_height / 2 - 10) or ball.ycor() <= -(window_height / 2 - 10):
            ball.dy *= -1
        elif ball.xcor() >= (window_width / 2 - 10):
            left_score += 1
            if left_score == WinScore:
                PlayAgain()
            NewRound()
        elif ball.xcor() <= -(window_width / 2 - 10):
            right_score += 1
            if right_score == WinScore:
                PlayAgain()
            NewRound()
        CheckRightHit()
        CheckLeftHit()
        GameTwist()
        window.update()


def GameTwist():
    ball.dx *= 1.001
    ball.dy *= 1.001
    left_bat.speed(abs(ball.dx + 5))
    right_bat.speed(abs(ball.dx + 5))
    if abs(ball.dx) >= 10:
        ball.color("red")
        left_bat.color("purple")
        right_bat.color("purple")
    elif abs(ball.dx) >= 7:
        ball.color("blue")
        left_bat.color("red")
        right_bat.color("red")
    elif abs(ball.dx) >= 5:
        ball.color("green")
        left_bat.color("blue")
        right_bat.color("blue")
    elif abs(ball.dx) >= 3:
        ball.color("yellow")
        left_bat.color("green")
        right_bat.color("green")


def LeftUp():
    if left_bat.ycor() + lb_height * 20 / 2 + 20 <= window_height / 2:
        left_bat.sety(left_bat.ycor() + 20)
    elif left_bat.ycor() + lb_height * 20 / 2 + 10 <= window_height / 2:
        left_bat.sety(left_bat.ycor() + 10)


def LeftDown():
    if left_bat.ycor() - lb_height * 20 / 2 - 20 >= -window_height / 2:
        left_bat.sety(left_bat.ycor() - 20)


def RightUp():
    if right_bat.ycor() + rb_height * 20 / 2 + 20 <= window_height / 2:
        right_bat.sety(right_bat.ycor() + 30)
    elif right_bat.ycor() + rb_height * 20 / 2 + 10 <= window_height / 2:
        right_bat.sety(right_bat.ycor() + 10)


def RightDown():
    if right_bat.ycor() - rb_height * 20 / 2 - 20 >= -window_height / 2:
        right_bat.sety(right_bat.ycor() - 20)


def CheckLeftHit():
    global teleported
    if ((left_bat.ycor() - lb_height * 20 / 2 <= ball.ycor() <= left_bat.ycor() + lb_height * 20 / 2)
            and left_bat.xcor() + lb_width * 20/2 >= ball.xcor() and ball.dx < 0):
        ball.dx *= -1
        teleported = False
        os.system("afplay HittingSound.wav&")


def CheckRightHit():
    global teleported
    if ((right_bat.ycor() - rb_height * 20 / 2 <= ball.ycor() <= right_bat.ycor() + rb_height * 20 / 2)
            and right_bat.xcor() - rb_width * 20/2 <= ball.xcor() - ball.dx and ball.dx > 0):
        ball.dx *= -1
        teleported = False
        os.system("afplay HittingSound.wav&")


def NewRound():
    global left_score
    global right_score
    ball.setx(0)
    ball.sety(0)
    positiveX = int(random.randint(0, 1))
    if positiveX:
        ball.dx = 1.75
    else:
        ball.dx = -1.75
    positiveY = int(random.randint(0, 1))
    if positiveY:
        ball.dy = 1.75
    else:
        ball.dy = -1.75
    ball.color("white")
    right_bat.speed(1)
    left_bat.speed(1)
    right_bat.color("yellow")
    left_bat.color("yellow")
    time.sleep(0.5)
    right_bat.goto(window_width / 2 - 50, 0)
    left_bat.goto(-(window_width / 2 - 50), 0)
    pen1.clear()
    pen2.goto(0, window_height / 2 - 20)
    pen2.write("Press 'P' to pause/unpause.", align="center",
               font=("Courier", 15, "normal"))
    pen1.write(left_name + " " + str(left_score) + " - " + str(right_score) + " " + right_name, align="center",
               font=("Courier", 40, "normal"))


def GameOver():
    if GameEnded:
        window.bye()


def PlayAgain():
    global left_score
    global right_score
    global GameEnded
    GameEnded = True
    os.system("afplay ClapsSound.wav&")
    pen1.clear()
    pen1.goto(0, 0)
    if left_score > right_score:
        pen1.write(left_name + " is the winner!\nThanks for playing :)", align="center", font=("Courier", 40, "normal"))
    else:
        pen1.write(right_name + " is the winner!\nThanks for playing :)", align="center",
                   font=("Courier", 40, "normal"))
    window.update()
    pen1.clear()
    DeleteTeleporters()
    time.sleep(3)
    pen1.write("Press 'Enter'/'Return' to play again.\nPress 'Q' to quit.", align="center",
               font=("Courier", 20, "normal"))
    window.onkey(GameOver, 'q')
    window.onkey(GameStart, 'Return')
    while 1:
        window.listen()
        window.update()


def Pause():
    global p
    global left_score
    global right_score
    p += 1
    while p % 2:
        pen1.clear()
        pen1.write("Game is paused.", align="center", font=("Courier", 40, "normal"))
    pen1.clear()
    pen1.write(left_name + " " + str(left_score) + " - " + str(right_score) + " " + right_name, align="center",
               font=("Courier", 40, "normal"))


p = 0
window.onkeypress(LeftUp, LeftUpKey)
window.onkeypress(LeftDown, LeftDownKey)
window.onkeypress(RightUp, RightUpKey)
window.onkeypress(RightDown, RightDownKey)
window.onkeypress(Pause, 'p')

left_score = right_score = 0
GameStart()
