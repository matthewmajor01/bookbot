from stats import get_num_words
from stats import get_character_dict
from stats import get_sorted_chars

def get_book_text (filepath):

    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main ():

    book_text = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")
    chars_dict = get_character_dict(book_text)
    sorted_dict = get_sorted_chars(chars_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("------------ Word Count ------------")
    print(f"Found {num_words} total words")
    print("------------ Character Count ------------")
    for d in sorted_dict:
        if d["char"].isalpha():
            print(f"{d['char']}: {d['num']}")
    print("============ END ============")

main()
