def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "cold"

# print(weather_condition(5))  # cold
# print(weather_condition(8))  # warm



# user_input = float(input("Enter temperature:"))  # 5
# print(weather_condition(user_input))  # cold



# user_input = float(input("Enter some input:"))
# print(type(user_input), user_input)  # <class 'float'> 6.0



user_input = int(input("Enter some input:"))
print(type(user_input), user_input)  # Traceback (most recent call last):
#   File "c:\Users\pgold\CarlsHub\PythonMega\PythonNotes\PythonBasics\UserInput.py", line 22, in <module>    user_input = int(input("Enter some input:"))
# ValueError: invalid literal for int() with base 10: '6.3'
