import random

from animal import Animal
from food import Food


class Rabbit(Animal, Food):

    def __init__(self, x, y, area, distance=4.0, collision=0.3, speed=2.5, name=""):
        super().__init__(x, y, area, distance, collision, speed, name)
        v = random.randint(50, 100)
        super().__init__(v)

    def behaviour(self):
        ...