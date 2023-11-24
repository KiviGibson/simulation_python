from __future__ import annotations
from enviroment import Enviroment
from vector2 import Vector2


def start():
    first = Enviroment(0,10, 0, Vector2(10, 10))
    first.start()


if __name__ == '__main__':
    start()
