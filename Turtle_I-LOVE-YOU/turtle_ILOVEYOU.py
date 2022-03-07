# Turtle library to draw figures
from turtle import *
import math as m

"""
speed(1)
bgcolor('black')
color('cyan')
pensize(5)
"""

# 1. Octagon
""" 
for i in range(8):
    forward (100)
    right(45)
"""

# 2. Square
""" 
for i in range(4):
    forward(100)
    left(90)
"""

# 3. Rectangle
"""
for i in range(4):
    if i%2 == 0:
        forward(300)
    else:
        forward(100)
    left(90)
"""

# 4. Circle
"""
bgcolor('black')
c = Turtle()
c.speed(1)
c.color('cyan')
c.pensize(2)
c.circle(50)
"""

# 5. I LOVE YOU
speed(1)
bgcolor('black')

# I
penup()
color('yellow')
goto(-400, 0)
pendown()
left(90)
forward(50)
right(90)
forward(50)
backward(100)
forward(50)
right(90)
forward(100)
left(90)
forward(50)
backward(100)

# L
penup()
color('red')
goto(-250,50)
pendown()
right (90)
forward(100)
left(90)
forward (70)

# O
penup()
color('green')
goto(-120,-50)
pendown()
circle(50)
print (pos())

# V
penup()
color('blue')
goto(-60,50)
pendown()
right (60)
forward (115.470053838)
left (120)
forward (115.470053838)
right (60)

# E
penup()
color('white')
goto(80,50)
pendown()
forward(70)
backward(70)
right(90)
forward(50)
left (90)
forward(70)
backward(70)
right (90)
forward(50)
left (90)
forward(70)

# Y
penup()
color('cyan')
goto(150+100+28.8675,0)
pendown()
right (90)
forward(50)
backward(50)
left (135)
forward (100/m.sqrt(2))
backward(100/m.sqrt(2))
left(90)
forward (100/m.sqrt(2))
backward(100/m.sqrt(2))
right (90)
print (pos())

# O
penup()
color('grey')
goto(430,-45)
pendown()
circle(55)
print (pos())


# U
penup()
color('orange')
goto(480,50)
pendown()
right (135)
forward (100)
left (90)
forward (70)
left (90)
forward (100)

hideturtle()
mainloop()

