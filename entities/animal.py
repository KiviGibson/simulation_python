import random

from entity import Object


class Animal(Object):
    names = [
        "James", "Jose", "Joel", "Jan",
        "Jaś", "Jegor", "Jelan", "Janek",
        "Juzek", "Jutek", "Janik", "John",
        "Jeremy", "Jerry", "Jasmine", "Jola",
        "Georg", "Gregory", "Gal", "Goofie"
    ]

    def __init__(self, x: float, y: float, area: any, distance=10.0, collision=2.0, speed=5.0, name="") -> None:
        super().__init__(x, y, area)
        self.food = []
        self.distance = distance
        self.collision = collision
        self.speed = speed
        self.target = None
        self.name = Animal.pick_a_name(name)
        self.hungermeter = 100
        self.hunger_duration = 0.6

    def behaviour(self) -> None:
        ...

    def move(self, x: int, y: int) -> None:
        self.pos.x += x * self.speed
        self.pos.y += y * self.speed

    def find_target(self):
        """
        Find next target to hunt / eat
        """
        objects = self.area.find_in_range(self)
        print(f"{str(self)}: {[str(i) for i in objects]}")

    @staticmethod
    def pick_a_name(name="") -> str:
        if name != "":
            return name
        return Animal.names[random.randint(0, len(Animal.names)-1)]

    def __str__(self):
        return super().__str__()
