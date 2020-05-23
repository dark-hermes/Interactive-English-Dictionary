import json
from difflib import get_close_matches

word_json = json.load(open("json/data.json"))


def translator(word):
    isLower = word.lower()
    isUpper = word.upper()
    isTitle = word.title()
    typo_correction = get_close_matches(isLower, word_json.keys())

    if isLower in word_json:
        return word_json[isLower]

    elif isUpper in word_json:
        return word_json[isUpper]

    elif isTitle in word_json:
        return word_json[isTitle]

    elif len(typo_correction) > 0:
        while True :
            userPrompt = input(f"Did you mean {typo_correction[0]} instead? (Y/n)\t: ")
            userPrompt = userPrompt.lower()

            if userPrompt == 'y':
                return word_json[typo_correction[0]]
            elif userPrompt == 'n':
                return "The word doesn't exists"
            else:
                return "We didn't understand your input"

    else:
        return "The word doesn't exists"

while True:
    word_input = input("\nEnter word\t: ")
    result = translator(word_input)

    if type(result) == type([]):
        for res in result:
            print("-",res)

    else:
        print(result)


        






