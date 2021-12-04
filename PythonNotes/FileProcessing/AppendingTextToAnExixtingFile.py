# with open("vegetables.txt", "a") as myfile:
#     myfile.write("\nOkra")
#     content = myfile.read()
    
# print(content)  # Traceback (most recent call last):
#                 #   File "c:\Users\pgold\CarlsHub\PythonMega\class.py", line 3, in <module>
#                 #     content = myfile.read()
#                 # io.UnsupportedOperation: not readable



with open("vegetables.txt", "a+") as myfile:
    myfile.write("\nOkra")
    content = myfile.read()
    
print(content)  # Tomato
                # Cucumber
                # Onion
                # Garlic
                # Okra
