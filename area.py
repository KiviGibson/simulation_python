import math
from animal import Animal


class Area:
    def __init__(self, x: int, y: int) -> None:
        x, y = abs(x), abs(y)
        self.max_x = x
        self.min_x = -x
        self.max_y = y
        self.min_y = -y
        self.objects = []

    def find_in_distance(self, who: Animal) -> list:
        targets = [i for i in self.objects if i != who]
        result = []
        pos = who.pos
        for target in targets:
            dist = math.sqrt(pow(pos.x - target.pos.x, 2) + pow(pos.y - target.pos.y, 2))
            if dist < who.distance:
                result.append(target)
        return result
