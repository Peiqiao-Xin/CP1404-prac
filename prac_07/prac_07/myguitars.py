from guitar import Guitar

def load_guitars(filename='guitars.csv'):
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def save_guitars(guitars, filename='guitars.csv'):
    with open(filename, 'w') as out_file:
        for g in guitars:
            out_file.write(f"{g.name},{g.year},{g.cost}\n")

def main():
    guitars = load_guitars()
    print("These are my guitars:")
    for g in guitars:
        print(f"  {g}")

    # Sort by year using __lt__
    guitars.sort()
    print("\nAfter sorting by year (oldest to newest):")
    for g in guitars:
        print(f"  {g}")

    # Let user add new guitars
    print("\nEnter new guitars (leave name blank to finish):")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))

    # Save updated list
    save_guitars(guitars)
    print("\nGuitars saved back to guitars.csv.")

if __name__ == "__main__":
    main()