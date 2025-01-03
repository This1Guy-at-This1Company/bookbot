import re


def main():
    book_path = "books/frankenstein.txt"   
    book_text = get_book_text(book_path) 
    number_of_words = count_words(book_text)
    print(f'---- Begin report of {book_path} ----\n')
    print(f"There were {number_of_words} words in the book. See below for how often each letter occured.\n")
    char_count = count_chars(book_text)
    compile_report(char_count)
    print('\n---- End of Report ----')
    
    #print(book_text)

def compile_report(dict):
    for letter in dict:
        print(f"The letter '{letter}' occured {dict[letter]} times")



def count_words(book_string):
    words = book_string.split()
    word_count = len(words)
    return word_count

def count_chars(book_string):
    just_chars = re.sub(r'[^a-zA-Z]','', book_string)

    occurance_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                       'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    
    for char in just_chars.lower():
        occurance_dict[char] += 1
    
    return occurance_dict


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


main()



