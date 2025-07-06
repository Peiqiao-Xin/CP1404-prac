"""
CP1404/CP5632 Practical - Client code to use the Car class with names.
"""

from prac_06.car import Car

def main():
    """Demo test code to show how to use Car class with name."""
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"Fuel in limo: {limo.fuel}")
    distance_driven = limo.drive(115)
    print(f"Limo drove {distance_driven} km.")
    print(limo)

main()