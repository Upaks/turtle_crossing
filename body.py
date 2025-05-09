from turtle import Turtle

class Body(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0,-280)
        self.setheading(90)

    def up(self):
        y = self.ycor() + 10
        self.goto(self.xcor(), y)

    def refresh(self):
        self.goto(0,-280)