import turtle
import random

colors = ["green", "blue", "pink", "yellow", "orange",]
gosho = turtle.Turtle()
gosho.speed(0)
gosho.width(5)

window = turtle.Screen()
window.bgcolor("grey")

def up():
    gosho.setheading(90)
    gosho.forward(50)

def down():
    gosho.setheading(270)
    gosho.forward(50)

def left():
    gosho.setheading(180)
    gosho.forward(50)

def right():
    gosho.setheading(0)
    gosho.forward(50)

def right_click(x, y):
    gosho.color(random.choice(colors))



turtle.listen()

turtle.onscreenclick(right_click, 3)

turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

turtle.mainloop()