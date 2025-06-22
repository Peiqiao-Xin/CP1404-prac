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
        else:
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