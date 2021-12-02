# myfile = open('fruits.txt')
# print(myfile.read())    # Pear
#                         # apple
#                         # orange
#                         # mandarin
#                         # watermelon
#                         # pomegranate


myfile = open('fruits.txt')
content = myfile.read()

print(content)  # Pear
                # apple
                # orange
                # mandarin
                # watermelon
                # pomegranate
print(content)  # Pear
                # apple
                # orange
                # mandarin
                # watermelon
                # pomegranate


myfile = open('fruits.txt')
content = myfile.read()
myfile.close()

print(content)  # Pear
                # apple
                # orange
                # mandarin
                # watermelon
                # pomegranate
