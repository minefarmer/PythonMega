def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean

monday_temperatures = [8.8, 9.1, 9.9]
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
print(mean(monday_temperatures))  # 9.266666666666666