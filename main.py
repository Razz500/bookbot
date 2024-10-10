def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_characters(file_contents)
        char_count.sort(reverse=True, key=sort_dict)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")
        format_list(char_count)

def count_words(text):
    word_count = 0
    word_list = text.split()
    for word in word_list:
        word_count += 1
    return word_count

def count_characters(text):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", 
               "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    list_of_dicts = []
    for letter in letters:
        letter_count = {}
        letter_count["char"] = letter
        letter_count["count"] = 0
        for char in text:
            char = char.lower()
            if char == letter:
                letter_count["count"] += 1
        list_of_dicts.append(letter_count)
    return list_of_dicts

def dict_to_list(dict):
    dict_list = []
    for key in dict:
        new_dict = {}
        new_dict[key] = dict[key]
        dict_list.append(new_dict)
    return dict_list

def sort_dict(dict):
    return dict["count"]

def format_list(list):
    for dic in list:
        print(f"The '{dic["char"]}' character was found {dic["count"]} times")



main()