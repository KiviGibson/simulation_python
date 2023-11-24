class DayLightCycle:
    def __init__(self, is_day: bool, day_duration: float, night_duration: float):
        self.is_day = is_day
        self.day_duration = day_duration
        self.night_duration = night_duration
        self.current_duration = self.decide(is_day)

    def decide(self, faze: bool) -> float:
        if faze:
            return self.day_duration
        return self.night_duration

    def update(self) -> None:
        self.current_duration -= 1

    def change_faze(self) -> None:
        self.is_day = not self.is_day
        self.current_duration = self.decide(self.is_day)
