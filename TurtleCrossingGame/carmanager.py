import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()
        
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-230, 230)
            new_car.goto(300, new_y)
            self.all_cars.append(new_car)
            
    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT