from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_list = []

    def spawn_car(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.setposition(300, random.randint(-250, 250))
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            self.car_list.append(car)

    def move_car(self):
        for car in self.car_list:
            car.forward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
