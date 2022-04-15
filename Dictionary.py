import json
from difflib import get_close_matches

d = json.load(open("Dictionary.json"))

def translate(w):
    w = w.lower()

    if w in d:
        return d[w]
    elif len(get_close_matches(w, d.keys())) > 0:
        yn = input("Did you mean %s instead? Enter 'Y' if Yes or 'N' if No : " %get_close_matches(w, d.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return d[get_close_matches(w, d.keys())[0]]
        elif yn == "n":
            return "That word doesn't exist. Please check again"
        else:
            return "We didn't understand your entry"
    else:
                return "That word doesn't exist. Please check again"

word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
input("Press ENTER to exit")