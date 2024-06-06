# python3 ./algorithms/fractal/koch-curve.py

import turtle

s = turtle.getscreen()
t = turtle.Turtle()

def kochCurve(depth, angle, length):
  t.left(angle)
  if(depth == 0):
    t.forward(length)
  else:
    angle = 0
    kochCurve(depth - 1, angle, length / 3)
    kochCurve(depth - 1, angle + 60, length / 3)
    kochCurve(depth - 1, angle - 120, length / 3)
    kochCurve(depth - 1, angle + 60, length / 3)

size = 360
depth = 4
turtle.setworldcoordinates(-1, -1, size, size)
t.penup()
t.goto(0, size / 2)
t.pendown()
t.speed(0)
kochCurve(depth, 0, size)