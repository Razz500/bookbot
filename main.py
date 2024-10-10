def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words(file_contents))

def count_words(text):
    word_count = 0
    word_list = text.split()
    for word in word_list:
        word_count += 1
    return word_count


main()