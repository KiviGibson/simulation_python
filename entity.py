from vector2 import Vector2


class Object:
    def __init__(self, x: float, y: float, area: object):
        self.pos = Vector2(x, y)
        self.area = area

    @property
    def pos(self) -> Vector2:
        return self._pos

    @pos.setter
    def pos(self, pos: Vector2) -> None:
        self._pos = pos
