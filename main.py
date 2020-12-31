from turtle import Turtle, Screen
from random import randint, choice

tm = Turtle()
screen = Screen()

screen.bgcolor((0, 0, 0))
# To use black as the background color of the canvas. (0, 0, 0) is the RGB color value
# To get RGB color value of different colors visit: https://www.rapidtables.com/web/color/RGB_Color.html

directions = [0, 90, 180, 270]
# This creates a list of different angles in which our turtle can turn.

screen.colormode(255)
# We have two color-modes, one is a float from 0 to 1 (by default) and the other is an integer from 0 to 255.
# Here we set the color mode which requires an int value from 0 to 255.

screen.setworldcoordinates(0, 0, 200, 200)
# This line sets the coordinates of the canvas. The lower left becomes 0,0 and the upper right becomes 200, 200.

tm.penup()
# This line instructs the turtle not to draw while moving.

tm.goto(100, 100)
# Moves the turtle to 100,100, which means the center of the screen.

tm.pendown()
# Instruct the turtle to again start drawing.

p = 0
# p acts as a flag variable to change the thickness of the pen after drawing 4 lines. This is done to achieve more
# randomness.

tm.speed("fast")
# This line changes turtle speed to fast from normal.

tm.hideturtle()


# This line hides the turtle, that is turtle will remain hidden while drawing.

def random_color():
    """This function return a tuple of a random RGB color"""
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


# An infinite loop is used so that turtle continues to draw the maze until the user closes the GUI.
while True:
    tm.pencolor(random_color())
    # random_color() returns a tuple of random RGB color, which is used to set the pen color of the turtle to a
    # random color.

    tm.fd(randint(5, 25))
    # This line moves the turtle in forward direction to a random number of steps from 5 to 25.

    tm.setheading(choice(directions))
    # This line turns the head of the turtle to a random direction provided in the list of directions.

    if not (0 < list(tm.position())[0] < 200 and 0 < list(tm.position())[1] < 200):
        # The above condition becomes True when the turtle moves out of the canvas. The codes in the if block is used
        # to move the turtle again back into the canvas.
        tm.penup()

        tm.goto(randint(0, 200), randint(0, 200))
        # To move the turtle to a random position within the canvas.

        tm.pendown()

    # In the below lines of code, the thickness of the pen changes after drawing 4 lines using a flag variable, p.
    p += 1
    if p < 5:
        continue
    tm.width(randint(1, 5))
    p = 0
