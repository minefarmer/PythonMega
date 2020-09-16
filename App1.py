import json
from difflib import get_close_matches


# Mis-spelled words   # 28
# Non-existing word   $ 45
# Dealing with a mispelled word   62
# getting close matches   62
# Getting close matches - 2   81
# 
# 
# 
# 
# 

# data = json.load(open("data.json"))

# def translate(word):
#     return data[word]

# word = input("Enter words: ")  # rain

# print(translate(word))  # ['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.', 'To fall from the clouds in drops of water.']




# Mis-spelled word
# data = json.load(open("data.json"))

# def translate(w):
#     if w in data:
#         return data[w]
#     else:
#         return"The word doesn't exist. Please doble check it."Please doble check it.

# word = input("Enter word: ")  # snotee

# print(translate(word))  # The word doesn't exist. 





# Non-existing word
# data = json.load(open("data.json"))

# def translate(w):
#     w = w.lower()
#     if w in data:
#         return data[w]
#     else:
#         return"The word doesn't exist. Please doble check it."  # The word doesn't exist. Please doble check it.

# word = input("Enter word: ")  # Snot

# print(translate(word))  # ['Mucus from the nose.']




# # getting close matches  #### Did you mean rain instead?  **** is printed when I mis-spell a word.
# data = json.load(open("data.json"))

# def translate(w):
#     w = w.lower()
#     if w in data:
#         return data[w]
#     elif len(get_close_matches(w, data.keys())) > 0:
#         return "Did you mean %s instead?" % get_close_matches(w, data.keys())[0]  # Did you mean rain instead?  **** is printed when I mis-spell a word.
#     else:
#         return"The word doesn't exist. Please doble check it."  

# word = input("Enter word: ")  # rainn

# print(translate(word))




# getting close matches  
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])  # Did you mean rain instead? Enter Y if yes, or N if no. Y
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist. Please double check it."  

word = input("Enter word: ")  # rainn

print(translate(word))  # ['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.', 'To fall from the clouds in drops of water.']

output = translate(word)

for item in output:
    print(item)

if type(output) == list:
    for item in output:
        print(item)