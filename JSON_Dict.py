import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        print("did u mean: %s" %get_close_matches(word,data.keys())[0])
        ans=input("press 'y' for yes;'n'for no-")
        if ans=='y':
            return data[get_close_matches(word,data.keys())[0]]
        elif ans=='n':
            return ("no such word available")
        else:
            return ("plese enter y or n")
    else:
        return ("word meaning not available")





word=input("enter a word you want to know about")
output=translate(word)
if type(output)==list:
    for i in output:
        print(i)
else:
    #hh
    print(output)