from entity import Object
from food import Food


class Grass(Object,Food):
    def __init__(self):
        super().__init__()