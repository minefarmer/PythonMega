# name = input("Enter your name: ")
# surname = input("Enter your surname: ")

# message = "Hello %s %s" % (name, surname)
# message = f"Hello {user_input}"
# print(message)  #  File "/home/rich/Mathub/PythonMega/PythonNotes/TheBasics/StringFormatting.py", line 5, in <module>
#                 #     message = f"Hello {user_input}"
#                 # NameError: name 'user_input' is not defined


# after line 5 is commeted out
name = input("Enter your name: ")
surname = input("Enter your surname: ")

message = "Hello %s %s" % (name, surname)
# message = f"Hello {user_input}"
print(message)  