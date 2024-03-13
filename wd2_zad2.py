from turtle import *


def main():
    pencolor('green')
    speed(100)
    for j in range(6):
        for i in range(10):
            forward(45)
            left(36)
        left(60)
    pencolor('red')
    right(60)
    forward(35)
    left(60)
    forward(35)
    left(120)
    forward(35)
    for i in range(5):
        right(60)
        forward(35)
        left(120)
        forward(35)
    right(60)
    forward(35)
    left(60)
    forward(35)
    for i in range(5):
        left(60)
        forward(70)
    left(60)
    forward(35)
    exitonclick()


main()
