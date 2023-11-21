from vector2 import Vector2


class Object:
    def __init__(self, x: int, y: int):
        self.pos = Vector2(x, y)

    @property
    def position(self):
        return self.pos
