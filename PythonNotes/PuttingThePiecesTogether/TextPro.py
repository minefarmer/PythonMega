# Step one   11
# Step two   23
# Step three   46
# 
# 
# 
# 
# 
# 
# 
# def sentance_maker(phrase):
#     interrogatives = ("how", "What", "why")
#     capitalized = phrase.capitalize()
#     if phrase.startswith(interrogatives):
#         return "{}?".format(capitalized)
#     else:
#         return "{}.".format(capitalized)

# print(sentance_maker("how are you")) # How are you?



# Step 2
# def sentance_maker(phrase):
#     interrogatives = ("how", "What", "why")
#     capitalized = phrase.capitalize()
#     if phrase.startswith(interrogatives):
#         return "{}?".format(capitalized)
#     else:
#         return "{}.".format(capitalized)

# results = []
# while True:
#     user_input = input("Say Something: ")
#     if user_input == "\end":
#         break
#     else:
#         results.append(user_input)

# print(results)  # Say Something: how are you
#                 # Say Something: weather is good
#                 # Say Something: \end
#                 # ['how are you', 'weather is good']


# Step three
def sentance_maker(phrase):
    interrogatives = ("how", "What", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []
while True:
    user_input = input("Say Something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentance_maker(user_input))

print(" ".join(results))  # Say Something: weather is good
                        # Say Something: how is the weather there
                        # Say Something: bye
                        # Say Something: \end
                        # Weather is good. How is the weather there? Bye.


