# import turtle
# import random

# # Function to draw a colorful spirograph-like pattern
# def draw_spirograph(radius):
#     turtle.speed(0)
#     turtle.bgcolor('white')
#     turtle.pensize(2)
#     num_circles = 36
#     for _ in range(num_circles):
#         turtle.color(random.random(), random.random(), random.random())
#         turtle.circle(radius)
#         turtle.left(360 / num_circles)

#     turtle.hideturtle()
#     turtle.done()

# # Main function to set up the turtle screen and draw the pattern
# def main():
#     screen = turtle.Screen()
#     screen.title("Colorful Spirograph")
#     radius = 100
#     draw_spirograph(radius)

# if __name__ == "__main__":
#     main()
import turtle
import random

# Function to draw the name "Nanjundi" with random colors
def draw_name():
    screen = turtle.Screen()
    screen.bgcolor('black')
    
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-150, 0)
    turtle.pendown()

    # Define colors
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple','white']
    
    # Draw each letter with a random color
    for letter in "Nanjundi":
        color = random.choice(colors)
        turtle.color(color)
        turtle.write(letter, font=('Tahoma', 50, 'bold'))
        turtle.penup()
        turtle.forward(40)  # Space between letters
        turtle.pendown()

    turtle.hideturtle()

    # Add some background graphics
    for _ in range(30):
        turtle.penup()
        x = random.randint(-screen.window_width() // 2, screen.window_width() // 2)
        y = random.randint(-screen.window_height() // 2, screen.window_height() // 2)
        size = random.randint(10, 100)
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color(random.choice(colors))
        turtle.begin_fill()
        turtle.circle(size)
        turtle.end_fill()

    turtle.done()

# Main function to start drawing
def main():
    draw_name()

if __name__ == "__main__":
    main()
