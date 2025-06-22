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