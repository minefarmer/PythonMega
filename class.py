import time
# import os

while True:
    if os.path.exists("vegetables.txt"):
        with open("vegetables.txt") as file:
            print(file.read())  # Tomato
                                # Cucumber
                                # Onion
                                # Garlic
                                # Okra
    else:
        print("File does not exixt.")
    time.sleep(10) 


