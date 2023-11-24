from animal import Animal


class Rabbit(Animal):

    def __init__(self, x, y, area, distance=4.0, collision=0.3, speed=2.5, name=""):
        super().__init__(x, y, area, distance, collision, speed, name)

    def behaviour(self):
        ...