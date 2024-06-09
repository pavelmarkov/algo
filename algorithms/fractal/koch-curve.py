# python3 ./algorithms/fractal/koch-curve.py

import turtle

s = turtle.getscreen()
t = turtle.Turtle()

def kochCurve(depth, angle, length):
  t.left(angle)
  if(depth == 0):
    t.forward(length)
  else:
    kochCurve(depth - 1, 0, length / 3)
    kochCurve(depth - 1, 60, length / 3)
    kochCurve(depth - 1, -120, length / 3)
    kochCurve(depth - 1, 60, length / 3)

size = 360
depth = 3
turtle.setworldcoordinates(-1, -1, size+100, size+100)
t.penup()
t.goto(0, (size +100) / 2)
t.pendown()
t.speed(5)
kochCurve(depth, 0, size)
t.left(-120)
kochCurve(depth, 0, size)
t.left(-120)
kochCurve(depth, 0, size)