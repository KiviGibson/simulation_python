from entity import Object


class Animal(Object):
    def __init__(self, x: float, y: float, area: object, distance=10.0, collision=2.0, speed=5.0) -> None:
        super().__init__(x, y, area)
        self.food = []
        self.distance = distance
        self.collision = collision
        self.speed = speed
        self.target = None
        print(x, y, speed)

    def move(self, x: int, y: int) -> None:
        self.pos.x += x * self.speed
        self.pos.y += y * self.speed

    def find_target(self):
        """
        Find next target to hunt / eat
        """
        objects = self.area.find_in_range(self)
