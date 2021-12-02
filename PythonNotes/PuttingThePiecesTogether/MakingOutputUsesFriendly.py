def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()

    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        # results.append(user_input)  # This gets the same results as the next line
        results.append(sentence_maker(user_input))  # Say something: weather is gool
                                                                    # Say something: how are you
                                                                    # Say something: \end

# print(results)


'''
>>> "how are you".startswith(("how", "what", "why")) 
True
>>>
'''


# Concatenating all strings into one string by using join
'''>>> "_".join(["how are you", "good good", "clear clear"])
'how are you_good good_clear clear'
>>>
'''

print(" ".join(results))  # Use the space between the double quotes to create a space between the double quotes.    \ee# "" Say something: weather is good
                                                                                                                    # Say something: how is the weather there
                                                                                                                    # Say something: bye
                                                                                                                    # Say something: \end
