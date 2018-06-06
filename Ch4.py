import math
import turtle
bob = turtle.Turtle()

# Exercises

# 1. Write a function called square that
# takes a parameter named t, which is a turtle.
# It should use the turtle to draw a square.
# Write a function call that passes bob
# as an argument to square, and then run the program again.


def square(t):
    for j in range(4):
        t.fd(100)
        t.lt(90)


# -> square(bob)


# 2. Add another parameter, named length, to square.
# Modify the body so length of the sides is length,
# and then modify the function call to provide
# a second argument. Run the program again.
# Test your program with a range of values for length.

def square2(t, length):
    for k in range(4):
        t.fd(length)
        t.lt(90)


# -> square2(bob, 150)


# 3. Make a copy of square and change the name to polygon.
# Add another parameter named n and modify the body
# so it draws an n-sided regular polygon.
# Hint: The exterior angles of an n-sided
# regular polygon are 360/n degrees.

def polygon(t, n, length):
    for k in range(n):
        t.fd(length)
        t.lt(360/n)


# -> polygon(bob, 4, 200)
# -> polygon(bob, 6, 50)


# 4. Write a function called circle that takes
# a turtle, t, and radius, r, as parameters
# and that draws an approximate circle by calling
# polygon with an appropriate length and number of sides.
# Test your function with a range of values of r.
# Hint: figure out the circumference of the circle
# and make sure that length * n = circumference.


def circle(t, r):
    circumference = 2*math.pi*r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)


# -> circle(bob, 25)


# 5. Make a more general version of circle called arc
# that takes an additional parameter angle,
# which determines what fraction of a circle to draw.
# angle is in units of degrees, so when angle=360,
# arc should draw a complete circle.

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)


# -> arc(bob, 50, 180.0)
# -> arc(bob, 70, 270.0)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon2(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)


def arc2(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)


def circle2(t, r):
    arc2(t, r, 360)


# -> circle2(bob, 40)
# -> polygon(bob, 4, 200)


def arc3(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def petal(t, r, angle):
    for i in range(2):
        arc3(t, r, angle)
        t.lt(180-angle)


def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360/n)


def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()


move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

turtle.mainloop()



