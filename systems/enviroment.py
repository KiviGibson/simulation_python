from vector2 import Vector2
from arena import Area
from entities.animal import Animal
from random import randrange


class Enviroment:
    def __init__(self, fox_amount: int, rabbit_amount: int, start_grass_amount: int, area_size: Vector2):
        self.is_day = True
        self.area = Area(int(area_size.x), int(area_size.y))
        for _ in range(start_grass_amount):
            ...
        for _ in range(rabbit_amount):
            x = randrange(int(-area_size.x), int(area_size.x))
            y = randrange(int(-area_size.y), int(area_size.y))
            speed = randrange(5, 10)
            self.spawn(x, y, speed)
        for _ in range(fox_amount):
            ...

    def update(self) -> None:
        ...

    def start(self) -> None:
        for e in self.area.objects:
            if isinstance(e, Animal):
                e.find_target()

    def spawn(self, x: float, y: float, speed: float) -> None:
        ani = Animal(x, y, self.area, speed=speed)
        self.area.add_object(ani)
