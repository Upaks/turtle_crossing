from turtle import Turtle
import random

COLOURS = ["red", "blue", "green", "orange", "purple", "pink"]

class Cars:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.loop_counter = 0
        self.car_speed = 0.1

    def add_cars(self):
        cars = Turtle("square")
        cars.penup()
        cars.shapesize(stretch_wid=1, stretch_len=2)
        cars.color(random.choice(COLOURS))
        random_y = random.randint(-250, 250)
        cars.goto(310, random_y)
        self.all_cars.append(cars)

    def new_cars(self):
        self.loop_counter += 1
        if self.loop_counter % 6 == 0:
            self.add_cars()

    def move(self):
        for each_car in self.all_cars:
            new_x = each_car.xcor() - 10
            each_car.goto(new_x, each_car.ycor())

    def increase_speed(self):
        self.car_speed *= 0.9