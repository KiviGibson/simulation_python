from entity import Object
from food import Food


class Grass(Object, Food):
    def __init__(self, x: float, y: float, area: any) -> None:
        super().__init__(x, y, area)
        super().__init__(15.0)

    def eat(self) -> float:
        return self.value
