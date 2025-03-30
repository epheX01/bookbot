file_path = "./books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def count_book_words():
    text = get_book_text(file_path)
    wordcount = text.split()
    return len(wordcount)

def character_count(text):
    text = text.lower()
    # set_compare = set(text)
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else: 
            char_count[char] = 1

    return char_count