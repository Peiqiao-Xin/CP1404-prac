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