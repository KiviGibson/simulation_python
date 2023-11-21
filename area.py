class Area:
    def __init__(self, x: int, y: int) -> None:
        x, y = abs(x), abs(y)
        self.max_x = x
        self.min_x = -x
        self.max_y = y
        self.min_y = -y
        self.animals = []
        self.vegetation = []
