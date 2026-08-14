import turtle
import random

# Create a screen and turtle
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")

# Create our funny turtle
funny_turtle = turtle.Turtle()
funny_turtle.shape("turtle")
funny_turtle.color("green")
funny_turtle.speed(5)

# Draw a silly dance
def silly_dance():
    for _ in range(4):
        funny_turtle.forward(50)
        funny_turtle.right(90)
        funny_turtle.stamp()  # Leave a footprint
    
    # Spin around like crazy
    for _ in range(8):
        funny_turtle.right(45)
        funny_turtle.forward(20)

# Make the turtle walk in a funny zigzag
def funny_walk():
    for _ in range(10):
        funny_turtle.forward(30)
        funny_turtle.setheading(random.randint(0, 360))
        funny_turtle.stamp()

# Make it wiggle
def wiggle():
    for _ in range(20):
        funny_turtle.right(10)
        funny_turtle.forward(5)
        funny_turtle.left(20)
        funny_turtle.forward(5)

# Run the funny sequence
print("🐢 Watch the funny turtle dance! 🐢")
silly_dance()
funny_walk()
wiggle()

# Add some text
funny_turtle.penup()
funny_turtle.goto(0, -250)
funny_turtle.write("MISSION ACCOMPLISHED! 🎉", align="center", font=("Arial", 20, "bold"))

screen.mainloop()