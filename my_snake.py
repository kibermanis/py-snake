import turtle
import random
import time

win = turtle.Screen()
win.title('Turtle game by Māris')
win.bgcolor('orange')
win.setup(width=600, height=600)
win.tracer(0)  # Turns off the screen updates

food = turtle.Turtle()
food.penup()
food.speed(speed=0.51)
food.color('red')
food.shape('square')
food.goto(0,100)

head = turtle.Turtle()
head.penup()
head.shape(name='turtle')
head.direction = 'stop'

segments = []
delay = 0.1
score = 0
high_score = 0

pen = turtle.Turtle()
pen.speed(10)
pen.shape('square')
pen.color('white')
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write(arg="Score: 0  High Score: 0", align="center", font=("Arial", 30, "bold"))

def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

##################################
while True:
    win.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(2)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.setpos(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 30, "bold"))

        # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 30, "bold"))

        # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            segments = []
            # for segment in segments:
            #     segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 30, "bold"))

    time.sleep(delay)


turtle.done()


