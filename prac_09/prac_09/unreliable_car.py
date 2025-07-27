import random

class UnreliableCar:
    """A Car that only drives when a random roll < reliability%."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability  # 0–100%

    def drive(self, distance):
        roll = random.random() * 100
        if roll < self.reliability:
            return super().drive(distance)
        return 0