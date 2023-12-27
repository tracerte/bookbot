def main():
    book_path = "books/frankenstein.txt"
    print_report(book_path)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    return len(text.split())


def count_letters(text):
    letter_count = {}
    text = text.lower()
    for c in text:
        if c.isalpha():
            try:
                letter_count[c] += 1
            except KeyError:
                letter_count[c] = 1
    return letter_count


def sort_dict_by_value_descending(letter_dict):
    letter_dict_sorted = sorted(
        letter_dict.items(), key=lambda x: x[1], reverse=True)
    return dict(letter_dict_sorted)


def print_report(book_path):
    print(f"--- Begin report of {book_path} ---")
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document\n")
    letter_count = count_letters(text)
    letter_count_sorted = sort_dict_by_value_descending(letter_count)
    for letter in letter_count_sorted:
        print(
            f"The '{letter}' character was found {letter_count[letter]} times")
    print("--- End report ---")


main()
