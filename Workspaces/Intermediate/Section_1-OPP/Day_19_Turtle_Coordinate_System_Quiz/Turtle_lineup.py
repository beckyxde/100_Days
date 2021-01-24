from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 50, 80]

for turtle_index in range(0, 6):
    tim = Turtle("turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(-230, y_positions[turtle_index])

screen.exitonclick()