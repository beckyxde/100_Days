#Exercise using event listeners
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(100)

def move_bacwards():
    tim.backward(100)

def move_cclockwise():
    tim.left(100)

def move_clockwise():
    tim.right(100)

def clear_screen():
    tim.clear()
    tim.home()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_bacwards, "s")
screen.onkey(move_cclockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()