def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

user_input = float(input('Enter temperature: '))  # 7
print(weather_condition(user_input))  # Cold