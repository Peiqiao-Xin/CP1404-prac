# Practical 05


#state_names.py

# Constant dictionary mapping Australian state codes to full names
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

def lookup_state():
    """Prompt user for state code and display full name, until blank."""
    while True:
        state_code = input("Enter short state (or blank to quit): ").strip()
        if not state_code:
            break
        # Normalize to uppercase so lookup is case-insensitive
        state_code = state_code.upper()
        try:
            # EAFP: try to get the name, catch KeyError if not found
            full_name = CODE_TO_NAME[state_code]
        except KeyError:
            print(f"Invalid short state '{state_code}'")
        elses
            print(f"{state_code} is {full_name}")

def print_all_states():
    """Print all state codes and names, aligned neatly."""
    # Determine the width to align codes
    max_code_width = max(len(code) for code in CODE_TO_NAME)
    for code, name in CODE_TO_NAME.items():
        # f-string with variable width
        print(f"{code:{max_code_width}} is {name}")

def main():
    """Main entry point."""
    print("All states:")
    print_all_states()
    print()  # blank line
    lookup_state()

if __name__ == "__main__":
    main()





#hex_colours.py

# Constant dictionary of some colour names to their hex codes
COLOUR_TO_HEX = {
    "aliceblue":    "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua":         "#00ffff",
    "beige":        "#f5f5dc",
    "black":        "#000000",
    "blue":         "#0000ff",
    "fuchsia":      "#ff00ff",
    "gray":         "#808080",
    "green":        "#008000",
    "yellow":       "#ffff00"
}

def main():
    """Allow the user to look up hex codes until they enter blank."""
    while True:
        name = input("Enter colour name (or blank to quit): ").strip()
        if not name:
            break
        key = name.lower()
        code = COLOUR_TO_HEX.get(key)
        if code:
            print(f"{name.title()} ⇒ {code}")
        else:
            print(f"Sorry, '{name}' is not in my list.")

if __name__ == "__main__":
    main()

#word_occurrences.py

def count_words(text):
    """Count occurrences of each word in the given text string."""
    counts = {}
    for word in text.split():
        word = word.lower()  # normalize to lowercase
        counts[word] = counts.get(word, 0) + 1
    return counts

def print_counts(counts):
    """Print word counts sorted alphabetically, aligned in columns."""
    # Sort keys alphabetically
    words = sorted(counts)
    # Determine length of longest word for alignment
    max_len = max(len(word) for word in words)
    for word in words:
        print(f"{word:{max_len}} : {counts[word]}")

def main():
    """Main program flow."""
    text = input("Text: ").strip()
    counts = count_words(text)
    print_counts(counts)

if __name__ == "__main__":
    main()

#emails.py


def extract_name_from_email(email):
    """
    Extract a tentative name from an email address.
    E.g. 'john.doe@example.com' → 'John Doe'
    """
    local_part = email.split("@")[0]
    parts = local_part.replace(".", " ").split()
    # Title-case each component
    return " ".join(part.title() for part in parts)

def get_user_confirmation(prompt, default=True):
    """
    Ask user a Y/n question.
    Returns True for yes, False for no.
    Default is True if user just presses Enter.
    """
    resp = input(prompt).strip().lower()
    if resp in ("", "y", "yes"):
        return True
    return False

def main():
    """
    Build a dictionary of email → name, prompting the user.
    """
    email_to_name = {}
    while True:
        email = input("Email: ").strip()
        if not email:
            break
        # Propose a name from the email
        proposed = extract_name_from_email(email)
        if get_user_confirmation(f"Is your name {proposed}? (Y/n) "):
            name = proposed
        else:
            name = input("Name: ").strip()
        email_to_name[email] = name

    # Print out the collected entries
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()

#wimbledon.py

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
#kivy_layout.kv.py

# This is a Kv file declaring the GUI layout.
BoxLayout:
    orientation: 'vertical'

    # Status label at top (20% of height)
    Label:
        text: app.status_text
        font_size: 60
        size_hint_y: 0.2

    # Buttons for increment/decrement
    BoxLayout:
        orientation: 'horizontal'
        Button:
            text: "Up"
            on_press: app.handle_press(1)
        Button:
            text: "Down"
            on_press: app.handle_press(-1)

    # Dynamically added name buttons appear here
    BoxLayout:
        id: names_box

    # New label added at bottom (10% of height)
    Label:
        text: "I did this :)"
        size_hint_y: 0.1
        font_size: 24
        halign: 'center'
        valign: 'middle'
