def count_book_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    words = file_contents.split()
    total_words = len(words)
    return total_words

def count_book_characters(filepath):
     with open(filepath) as f:
        file_contents = f.read().lower()
        characters = list(file_contents)
        no_of_characters = {}
        for x in characters:
            if x in no_of_characters:
                no_of_characters[x] = no_of_characters[x] + 1
            else:
                no_of_characters[x] = 1
        return no_of_characters
     
def sort_on(chars):
    return chars["num"]
     
def sort_list(no_of_characters):
    list_of_dictionaries = []
    for character in no_of_characters:
        if str(character).isalpha():
            new_dictionary = {"char":character, "num": no_of_characters[character]}
            list_of_dictionaries.append(new_dictionary)
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    return list_of_dictionaries



