import turtle
from random import *
from turtle import Turtle ,Screen
# import colorgram as cg
#
# color_list = cg.extract("image1.jpg", 15)
# color_palette = []
#
# for count in range(len(color_list)):
#     rgb = color_list[count]
#     color = rgb.rgb
#     red = color.r
#     green = color.g
#     blue = color.b
#     color_palette.append((red, green, blue))
#
# print(color_palette)
turtle.colormode(255)
colors = [(231, 223, 226), (205, 156, 112), (149, 161, 184), (83, 92, 127), (202, 94, 76), (218, 203, 132), (150, 85, 68), (192, 148, 160), (113, 83, 91), (93, 111, 101), (159, 172, 167), (221, 170, 179)]
tim = Turtle()
tim.hideturtle()
print(choice(colors))
tim.penup()
tim.speed("fastest")
tim.setheading(185)
tim.forward(400)
tim.setheading(0)

def draw_painting():

    for _ in range(10):
        tim.forward(70)

        tim.dot(40, choice(colors))



for _ in range(10):
    draw_painting()
    tim.setheading(90)
    tim.forward(70)
    tim.setheading(180)
    tim.forward(700)
    tim.setheading(0)


screen = Screen()
screen.exitonclick()