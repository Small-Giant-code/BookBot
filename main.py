from stats import count_book_words, count_book_characters, sort_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

filepath = "/home/aronm/workspace/github.com/Small-Giant-Code/BookBot/books/frankenstein.txt"
book_text = get_book_text(filepath)
#print(book_text)

total_words = count_book_words(filepath)
print(f"Found {total_words} total words")

no_of_characters = count_book_characters(filepath)
print(no_of_characters)

list_of_dictionaries = sort_list(no_of_characters)
print(list_of_dictionaries)




