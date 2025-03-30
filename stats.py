file_path = "./books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def count_book_words():
    text = get_book_text(file_path)
    wordcount = text.split()
    return len(wordcount)

def character_count():
    text = get_book_text(file_path)
    