from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def display_taxis(taxis):
    for i, t in enumerate(taxis):
        print(f"{i} - {t}")

def choose_taxi(taxis):
    display_taxis(taxis)
    choice = input("Choose taxi: ")
    try:
        idx = int(choice)
        if 0 <= idx < len(taxis):
            return taxis[idx]
    except ValueError:
        pass
    print("Invalid taxi choice")
    return None

def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4),
    ]
    bill = 0.0
    current = None

    print("Let's drive!")
    while True:
        print(MENU)
        choice = input(">>> ").lower()
        if choice == 'q':
            break
        elif choice == 'c':
            current = choose_taxi(taxis) or current
        elif choice == 'd':
            if current is None:
                print("You need to choose a taxi before you can drive")
            else:
                dist = float(input("Drive how far? "))
                cost = current.drive(dist) * getattr(current, 'price_per_km', 0)
                # for SilverServiceTaxi, add flagfall via get_fare:
                if hasattr(current, 'get_fare') and not isinstance(current, Taxi):
                    # recalc via get_fare() difference
                    cost = current.get_fare() - bill
                bill += cost
                print(f"Your {current.name} trip cost you ${cost:.2f}")
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

if __name__ == "__main__":
    main()