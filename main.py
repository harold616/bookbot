import sys
from stats import get_num_words, get_dict_count, sort_characters_by_count, print_report

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    chars_dict = get_dict_count(book_text)
    chars_sorted_dict = sort_characters_by_count(chars_dict)
    print_report(book_path, num_words, chars_sorted_dict)


main()