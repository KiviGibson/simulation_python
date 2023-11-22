from entity import Object
from area import Area


class Animal(Object):
    def __init__(self, x: float, y: float, distance: float, area: Area) -> None:
        super().__init__(self, x, y, area)
        self.food = []
        self.distance = distance
        self.target = None

    def move(self, x: int, y: int, speed: float) -> None:
        self.pos.x += x * speed
        self.pos.y += y * speed

    def find_target(self):
        """
        Find next target to hunt / eat
        """
        objects = self.area.find_in_distance(self)
        # find best food using numbers
        ...