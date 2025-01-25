def count_words(string):
    word_list = string.split()
    return len(word_list)

def count_letters(string):
    letters_counted = {}
    lower_string = string.lower()
    for s in lower_string:
        if s in letters_counted:
            letters_counted[s] = letters_counted[s] + 1
        else:
            letters_counted[s] = 1
    return letters_counted

def print_report(book_path):
    with open(book_path) as book:
        book_contents = book.read()
        print(f"--- Begin report of {book_path} ---")
        
        print(f"{count_words(book_contents)} words found in the document")
        print("")
        
        counted_letters = count_letters(book_contents)
        for l in counted_letters:
            if l.isalpha():
                print(f"The '{l}' character was found {counted_letters[l]} times")
                
        print("--- End report ---")


def main():
    print_report("books/frankenstein.txt")

main()