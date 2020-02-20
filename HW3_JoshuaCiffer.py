"""
Joshua Ciffer
CS 100 2019F Section 029
HW 03, September 10th, 2019
"""
import turtle
import math

screen = turtle.Screen()
tortile = turtle.Turtle()
length = 100

tortile.width(10)

# Triangle
tortile.color('red')
tortile.forward(length)
tortile.right(120)
tortile.forward(length)
tortile.right(120)
tortile.forward(length)
tortile.right(120)

# Square
tortile.color('green')
tortile.forward(length)
tortile.right(90)
tortile.forward(length)
tortile.right(90)
tortile.forward(length)
tortile.right(90)
tortile.forward(length)
tortile.right(90)

# Pentagon
tortile.color('blue')
tortile.forward(length)
tortile.right(72)
tortile.forward(length)
tortile.right(72)
tortile.forward(length)
tortile.right(72)
tortile.forward(length)
tortile.right(72)
tortile.forward(length)
tortile.right(72)

# 2
tortile.circle(50)
tortile.circle(100)
tortile.circle(150)
tortile.circle(200)

# 3
print(math.factorial(100))
print(math.log(1000000), 2)
print(math.gcd(63, 49))
