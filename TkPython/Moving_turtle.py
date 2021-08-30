import turtle as t
import random as rd
import time as tm


def inside_window():
    left_limit = (-t.window_width() / 2) + 100
    right_limit = (t.window_width() / 2) - 100
    top_limit = (t.window_height() / 2) - 100
    bottom_limit = (-t.window_height() / 2) + 100
    (x, y) = t.pos()
    if x > left_limit and x < right_limit and y > bottom_limit and y < top_limit:
        return True
    else:
        return False


def move_turtle():
    if inside_window():
        t.right(rd.randint(0, 180))
        t.forward(rd.randint(100, 200))
    else:
        t.backward(rd.randint(100, 200))


t.shape("turtle")
t.fillcolor("red")
t.bgcolor("black")
t.speed("slow")
t.pensize(2)

while True:
    move_turtle()
    tm.sleep(1)
