from silver_service_taxi import SilverServiceTaxi

def main():
    # fanciness=2 ⇒ base 1.23*2=2.46/km
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    taxi.drive(18)
    fare = taxi.get_fare()  # 18*2.46 + 4.50 = 48.78
    print(f"Fare for 18km: ${fare:.2f}")
    assert abs(fare - 48.78) < 1e-6

if __name__ == "__main__":
    main()