"""
CP1404/CP5632 Practical
Taxi class - derived from Car
"""

from car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    price_per_km = 1.23  # Class variable shared by all Taxi instances

    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance and rate."""
        return (f"{super().__str__()}, "
                f"{self.current_fare_distance}km on current fare, "
                f"${self.price_per_km:.2f}/km")

    def get_fare(self):
        """Return the price for the taxi trip, rounded to nearest 10 cents."""
        fare = self.price_per_km * self.current_fare_distance
        return round(fare * 10) / 10  # Round to nearest $0.10

    def start_fare(self):
        """Begin a new fare by resetting fare distance."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """
        Drive like parent Car but also calculate fare distance.
        Return the actual distance driven.
        """
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven