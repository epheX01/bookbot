from stats import *
def main():
    count = character_count(get_book_text(file_path))
    print(f"{count_book_words()} words found in the document")
    print(f"{count}")
main()