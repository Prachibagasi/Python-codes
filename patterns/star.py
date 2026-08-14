import turtle
import math

t = turtle.Turtle()
t.speed(1)
t.color("blue")

size = 200                     # length of each triangle side
R = size / math.sqrt(3)        # distance from center to each triangle's corner

def draw_triangle(t, start_angle):
    # start_angle = direction (in degrees) from center to the triangle's first corner
    t.penup()
    x = R * math.cos(math.radians(start_angle))
    y = R * math.sin(math.radians(start_angle))
    t.goto(x, y)
    t.setheading(start_angle + 150)   # points turtle along the first side
    t.pendown()

    for i in range(3):
        t.forward(size)
        t.left(120)

# Triangle 1 (pointing up)
draw_triangle(t, 90)

# Triangle 2 (pointing down) - rotated 180 degrees around the same center
draw_triangle(t, 270)

turtle.done()