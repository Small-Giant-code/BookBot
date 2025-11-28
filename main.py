import sys
from stats import count_book_words, count_book_characters, sort_list


if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

filepath = sys.argv[1]
book_text = get_book_text(filepath)
#print(book_text)
#print(book_text)

total_words = count_book_words(filepath)
print(f"Found {total_words} total words")

no_of_characters = count_book_characters(filepath)
#print(no_of_characters)

list_of_dictionaries = sort_list(no_of_characters)
for i in range(0, len(list_of_dictionaries)):
    dict = list_of_dictionaries[i]
    key = dict["char"]
    value = dict["num"]
    print(f"{key}: {value}")






