from turtle import *

def draw_branch(length):
    if length < 5:
        return
    forward(length)
    right(20)
    draw_branch(length - 10)
    left(40)
    draw_branch(length - 10)
    right(20)
    backward(length)

pensize(2)
pencolor("brown")
goto(0, -200)
left(90)
draw_branch(100)

done()