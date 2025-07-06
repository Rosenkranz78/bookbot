from stats import get_num_words, count_characters, sort_character_counts
import sys

def get_book_text(filepath):
    """Reads the contents of the file at the given path and returns it as a string."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    # Check for exactly one argument (excluding script name)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    book_contents = get_book_text(filepath)
    num_words = get_num_words(book_contents)
    char_counts = count_characters(book_contents)
    sorted_characters = sort_character_counts(char_counts)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()