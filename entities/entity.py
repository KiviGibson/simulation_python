from vector2 import Vector2


class Object:
    def __init__(self, x: float, y: float, area: object):
        self.pos = Vector2(x, y)
        self.area = area
        self.name = ""

    @property
    def pos(self) -> Vector2:
        return self._pos

    @pos.setter
    def pos(self, pos: Vector2) -> None:
        self._pos = pos

    def __str__(self):
        return f"{self.name}: {str(self.pos.x)}, {str(self.pos.y)}"
