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