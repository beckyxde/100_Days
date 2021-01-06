from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("SandyBrown")

#TODO 1: Have the turtle move in a square

for _ in range(4):
    tim.forward(100)
    tim.right(90)

#TODO 2: Have the turtle move in a dashed line

for _ in range(15):
    tim.forward(10)
    tim.pu()
    tim.forward(10)
    tim.pd()

#TODO 3: Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon
# to make a shape, divide 360 by the number of sides to get the angles
# make each of the lines a random different color

colors = ["medium aquamarine", "teal", "aquamarine", "sea green", "olive drab", "green yellow", "medium sea green"]

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range (3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

draw_shape()

#TODO 4: Draw a random walk

directions = [90, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))

'''Practicing with tuples - Generate a random color'''
# import turtle as t
# import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [90, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color)
    tim.forward(30)
    tim.setheading(random.choice(directions))

#TODO 5: Draw a Spirograph

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random.color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)




screen = Screen()
screen.exitonclick()