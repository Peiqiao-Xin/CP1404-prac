from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A high-end Taxi with a flagfall and fanciness multiplier."""
    flagfall = 4.50  # class variable

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # scale the per-km price for this instance
        self.price_per_km *= fanciness

    def get_fare(self):
        # base fare + flagfall, rounded
        fare = super().get_fare() + self.flagfall
        return round(fare, 2)

    def __str__(self):
        # e.g. "Hummer, fuel=200, odo=0, 0km on current fare, $4.92/km plus flagfall of $4.50"
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"