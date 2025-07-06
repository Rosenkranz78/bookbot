def get_num_words(text):
    """Count and return the number of words in the given text."""
    words = text.split()
    return len(words)

def count_characters(text):
    """
    Counts how many times each character appears in the text (case-insensitive).
    Returns a dictionary with characters as keys and their counts as values.
    """
    char_counts = {}
    for char in text.lower():  # Convert to lowercase to avoid duplicates
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


def sort_character_counts(char_dict):
    """
    Takes a dictionary of character counts and returns a list of dictionaries,
    each with keys 'char' and 'num', sorted by 'num' in descending order.
    Only includes alphabetical characters using .isalpha().
    """
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})

    sorted_list.sort(key=lambda item: item["num"], reverse=True)
    return sorted_list