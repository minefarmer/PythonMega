# File open   10 - 21
# File close   41
# A better way  to  open, read and close the file is to use the (with context manager)   66
# Closing the file after reading it, using the (with context manager).   78
# Opening files after moveing them   93
# Using "w", etc.   108
# Appending text to an existing file   116
# 
# 
# 
# myfile = open("Fruits.txt")
# print(myfile.read())  # pear
                        # apple
                        # orange
                        # mandarin
                        # watermelon
                        # pomegranate



# myfile = open("Fruits.txt")
# content = myfile.read()

# print(content)  # pear
#                 # apple
#                 # orange
#                 # mandarin
#                 # watermelon
#                 # pomegranate

# print(content)  # pear
#                 # apple
#                 # orange
#                 # mandarin
#                 # watermelon
#                 # pomegranate




#  File close
# myfile = open("Fruits.txt")
# content = myfile.read()
# myfile.close()

# print(content)  # pear   ***** this operation was performed before the file was closed
#                 # apple
#                 # orange
#                 # mandarin
#                 # watermelon
#                 # pomegranate



# # myfile = open("Fruits.txt")
# content = myfile.read()
# myfile.close()
# print(content)  # Traceback (most recent call last):   ***** this operation was performed after the file was closed
#                 # File "/home/rich/Mathub/PythonMega/MyFile.py", line 45, in <module>
#                 #     content = myfile.read()
#                 # NameError: name 'myfile' is not defined




#  A better way  to  open, read and close the file is to use the (with context manager)

# with open("Fruits.txt") as myfile:
#     content = myfile.read()

# print(content)  # pear
#                 # apple
#                 # orange
#                 # mandarin
#                 # watermelon
#                 # pomegranate

# Closing the file after reading it, using the (with context manager).
# with open("Fruits.txt") as myfile:
#     content = myfile.read()
#     myfile.close()

# print(content)  # pear
#                 # apple
#                 # orange
#                 # mandarin
#                 # watermelon
#                 # pomegranate




# Opening files after moveing them
# with open("PythonNotes/FileProcessing/Fruits.txt") as myfile:
#     content = myfile.read()
#     myfile.close()

# print(content)  # pear   # files are opened in read mode by default
#                 # apple
#                 # orange
#                 # mandarin
#                 # watermelon
#                 # pomegranate




# Using "w.
# with open("Vegetables.txt", "w") as myfile:
#     myfile.write("Tomato\nCucumber\nOnion\n")
#     myfile.write("Garlic")




# Appending text to an existing file
# with open("Fruits.txt", "a") as myfile:
#     myfile.write("\nOkra")
