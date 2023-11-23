import turtle
from random import random, randint
import time

CURSOR_SIZE = 20

num=0
def increase_score():
    global num
    num += 1

def my_circle(color):

    radius = randint(10, 50)

    kaplumbaga = turtle.Turtle()
    kaplumbaga.shape("turtle")
    kaplumbaga.color("pink")
    kaplumbaga.speed(0)
    kaplumbaga.penup()
    kaplumbaga.goto(-200, -100)




    while True:
        nx = randint(2 * radius - width // 2, width // 2 - radius * 2)
        ny = randint(2 * radius - height // 2, height // 2 - radius * 2)

        kaplumbaga.goto(nx, ny)

        for other_radius, other_circle in circles:
            if kaplumbaga.distance(other_circle) < 2 * max(radius, other_radius):
                break
        else:
            break

    kaplumbaga.showturtle()
    kaplumbaga.onclick(lambda x, y, t=kaplumbaga: (kaplumbaga.hideturtle(), increase_score()))
    return radius, kaplumbaga


screen = turtle.Screen()
screen.bgcolor("grey")
screen.title("Speed kaplumbaga")

width, height = screen.window_width(), screen.window_height()

circles = []

gameLength = 5
# Higher number means faster blocks
# 1-10
difficulty = 10
startTime = time.time()
while True:
    time.sleep(1/difficulty)

    rgb = (random(), random(), random())

    timeTaken = time.time() - startTime

    circles.append(my_circle(rgb))
    screen.title('SCORE: {}, TIME LEFT: {}'.format(num,int(round(gameLength - timeTaken,0))))

    if time.time() - startTime > gameLength:
        break

screen.title('FINISHED! FINAL SCORE: {}'.format(num))

screen.mainloop()