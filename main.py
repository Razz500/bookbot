def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words(file_contents))
        print(count_characters(file_contents))

def count_words(text):
    word_count = 0
    word_list = text.split()
    for word in word_list:
        word_count += 1
    return word_count

def count_characters(text):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", 
               "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letter_count = {}
    for letter in letters:
        letter_count[letter] = 0
    for i in letters:
        count = 0
        for letter in text:
            letter = letter.lower()
            if letter == i:
                count += 1
        letter_count[i] = count
    return letter_count


main()