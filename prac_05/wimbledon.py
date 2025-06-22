import csv

def load_data(filename):
    """
    Read the CSV and return a list of rows.
    Each row is a dict with keys: Year, Champion, Country.
    """
    data = []
    with open(filename, encoding="utf-8-sig", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # We only care about Champion and Country (champion's country)
            data.append({
                "year": int(row["Year"]),
                "champion": row["Champion"],
                "country": row["Country"]
            })
    return data

def count_champions(data):
    """Return a dict champion_name → number_of_titles."""
    counts = {}
    for entry in data:
        name = entry["champion"]
        counts[name] = counts.get(name, 0) + 1
    return counts

def get_countries(data):
    """Return a sorted list of unique country codes from the data."""
    countries = {entry["country"] for entry in data}
    return sorted(countries)

def print_results(champ_counts, countries):
    """Display the champions count and list of countries."""
    print("Wimbledon Champions:")
    for name, count in sorted(champ_counts.items()):
        print(f"{name} {count}")
    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))

def main():
    """Main program flow."""
    filename = "wimbledon.csv"
    data = load_data(filename)
    champ_counts = count_champions(data)
    countries = get_countries(data)
    print_results(champ_counts, countries)

if __name__ == "__main__":
    main()