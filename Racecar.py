class RaceCar():
    laps = 0
    def __init__(self, color, fuel_remaining, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        for key, value in kwargs.items():
            setattr(self, key, value)
    def run_lap(self, length):
        self.fuel_remaining = self.fuel_remaining - (length * 0.125)
        self.laps += 1
            
infiniti = RaceCar("Black", 100)

infiniti.run_lap(4)
