from taxi import Taxi

def main():
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)                      # Prius 1, fuel=60, odo=40, 40km on current fare, $1.23/km
    print("Current fare:", my_taxi.get_fare())  # 40 * 1.23 = 49.20

    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)                      # Prius 1, fuel=0, odo=100, 100km on current fare, $1.23/km
    print("Current fare:", my_taxi.get_fare())  # 100 * 1.23 = 123.00

if __name__ == "__main__":
    main()