# def mean(value):
#     the_mean = sum(mylist) / len(mylist)
#     return the_mean

#     student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
#     print(mean(student_grades))

'''
>>> monday_temperatures = [8.8, 9.1, 9.9] 
>>> student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
>>> sum(monday_temperatures) / len(monday_temperatures)
9.266666666666666
>>> sum(student_grades.values()) / len(student_grades)
8.466666666666667
>>> 
'''


def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean

monday_temperatures = [8.8, 9.1, 9.9]
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
print(mean(monday_temperatures))  # 9.266666666666666
