import json
from difflib import get_close_matches  # library to compare text
# 1. load the json data
dictionary = json.load(open('data.json', 'r'))

# 2. Find the word in the dictionary

def translate(word):
    if word in dictionary:
        return dictionary[word]
    elif get_close_matches(word, dictionary.key())
    return "the word doesn't exist."


# 3. take user input:
word = input("Enter a word: ")
print(translate(word.lower()))