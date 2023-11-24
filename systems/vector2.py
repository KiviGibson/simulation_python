from __future__ import annotations


class Vector2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, x: float):
        self._x = x

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, y: float):
        self._y = y

    @classmethod
    def zero(cls) -> Vector2:
        return Vector2(0, 0)
