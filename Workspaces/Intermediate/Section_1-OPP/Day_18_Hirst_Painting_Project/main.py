import colorgram
import turtle as turtle_module
import random

'''extract color palette from image using colorgram'''
# colors = colorgram.extract('hirst.jpg', 10)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
colors = [(131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48),(140, 184, 162)]
#the closer the colors are to '255' the more likely they're a shade of white, aka the background color
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

# tim.dot(random.choice(colors))

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# print(rgb_colors)

screen = turtle_module.Screen()
screen.exitonclick()