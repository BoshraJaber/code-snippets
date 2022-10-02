import json
from difflib import get_close_matches  # library to compare text
# 1. load the json data
dictionary = json.load(open('data.json', 'r'))

# 2. Find the word in the dictionary
# 2.1 if the word in the dictionary, return it
# 2.2 else, suggest to the user a similar word


def translate(word):
    if word in dictionary:
        return dictionary[word]
    return find_similar(word)


def find_similar(word):
    similar_word = get_close_matches(word, dictionary.keys())
    if len(similar_word) > 0:
        newWord = input(
            "Did you mean %s instead? \n Enter Y if yes or N if no, Q if you want to exit: " % similar_word[0])
        if newWord == "Y":
            return dictionary[similar_word[0]]
        if newWord == 'N':
            print("We didn't find a match \n Try to enter a new word")
            enter_word()
        if newWord == 'Q':
            return "Thanks for using our dictionary"

# 3. take user input:


def enter_word():
    word = input("Enter a word: ")
    output = translate(word.lower())
    if type(output == list):
        for item in output:
            print(item)
    else:
        print(output)

print(enter_word())
