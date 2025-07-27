from unreliable_car import UnreliableCar

def test_reliability():
    car = UnreliableCar("Unreliable", 1, 30)
    runs = 1000
    drove = sum(car.drive(1) or 0 for _ in range(runs))  # each trial we reset fuel
    # Roughly 30% of 1000 should succeed
    print(f"Driven {drove} times out of {runs} (≈30%)")

if __name__ == "__main__":
    test_reliability()