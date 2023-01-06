from turtle import Turtle


class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.moving = 20
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in self.starting_positions:
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(i)
            self.segments.append(turtle)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.head.forward(self.moving)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def increase_by_one(self):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        last_x = self.segments[-1].xcor()
        last_y = self.segments[-1].ycor()
        turtle.goto(last_x, last_y)
        self.segments.append(turtle)
