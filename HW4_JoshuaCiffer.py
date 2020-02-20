"""
Joshua Ciffer
CS 100 Section 029
September 17th, 2019
"""
import turtle
a = 3
b = 4
c = 5
if a < b:
	print("OK")
else:
	print("NOT OK")
if c < b:
	print("OK")
else:
	print("NOT OK")
if (a + b) == c:
	print("OK")
else:
	print("NOT OK")
if a**2 + b**2 == c**2:
	print("OK")
else:
	print("NOT OK")

color = input("What color: ")
width = int(input("What line width: "))
length = int(input("What line length: "))
shape = input("What shape: ")

screen = turtle.Screen()
tortile = turtle.Turtle()
tortile.color(color)
tortile.width(width)
if shape == 'line':
	tortile.forward(length)
elif shape == 'triangle':
	tortile.forward(length)
	tortile.right(120)
	tortile.forward(length)
	tortile.right(120)
	tortile.forward(length)
	tortile.right(120)
elif shape == 'square':
	tortile.forward(length)
	tortile.right(90)
	tortile.forward(length)
	tortile.right(90)
	tortile.forward(length)
	tortile.right(90)
	tortile.forward(length)
	tortile.right(90)
