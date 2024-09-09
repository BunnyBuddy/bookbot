from collections import Counter
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_characters(text.lower())
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("")
    list_of_dicts = [{'name': key, 'num': value} for key, value in num_characters.items()]
    list_of_dicts.sort(reverse=True, key=sort_on)
    for item in list_of_dicts:
        if item["name"].isalpha():
            print(f"The '{item['name']}' character was found {item['num']} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def get_num_words(text):
    words = text.split()
    return len(words)

def get_characters(text):
    char_count = Counter(text.lower())
    charactersList = dict(char_count)
    return charactersList


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
