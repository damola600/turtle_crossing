from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.keep_generating = True
        self.create_cars()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        for i in range(20):
            x_cor = random.randint(-280, 280)
            y_cor = random.randint(-250, 250)
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(x_cor, y_cor)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            y_cor = random.randint(-250, 250)
            car.setheading(180)
            car.forward(self.car_speed)
            if car.xcor() < -310:
                car.color(random.choice(COLORS))
                car.goto(310, y_cor)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
