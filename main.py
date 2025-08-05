import sys
from stats import count_words, character_count, sort_on, sort_chars

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text (path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main(file):
    text_out = get_book_text(file)
    #count = char(text_out)
    words = count_words(text_out)
    chars = character_count(text_out)
    list_of_dicts = sort_chars(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for entry in list_of_dicts:
        print(entry["char"] + ": " + str(entry["num"]))
    print("============= END ===============")


main(sys.argv[1])