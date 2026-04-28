import turtle
import random
import pygame
import time

# create screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("1d1d1d")

# create Border

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# score
score = 0 
delay = 0.1

#snake
snake = turtle.Turtle()
