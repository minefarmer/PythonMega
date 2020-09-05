# def mean(mylist):
#     the_mean = sum(mylist) / len(mylist)
#     return the_mean

# student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}
# print(mean(student_grades))  # Traceback (most recent call last):
#                             # File "/home/carl/Github/PythonMega/PythonNotes/TheBasics/Conditionals.py", line 6, in <module>
#                             #     print(mean(student_grades))
#                             # File "/home/carl/Github/PythonMega/PythonNotes/TheBasics/Conditionals.py", line 2, in mean
#                             #     the_mean = sum(mylist) / len(mylist)
#                             # TypeError: unsupported operand type(s) for +: 'int' and 'str'



# IF conditionals
# def mean(value):
#     if type(value) == dict:
#         the_mean = sum(value.values()) / len(value)
#     else:
#         the_mean = sum(value) / len(value)
        
#     return the_mean

# student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}
# print(mean(student_grades))  # 8.466666666666667


# def mean(value):
#     if type(value) == dict:
#         the_mean = sum(value.values()) / len(value)
#     else:
#         the_mean = sum(value) / len(value)
        
#     return the_mean

# monday_temperatures = [8.8, 9.1, 9.9]
# # student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}
# print(mean(monday_temperatures))  # 9.266666666666666


def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
        
    return the_mean

monday_temperatures = [8.8, 9.1, 9.9]
# student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}
print(mean(monday_temperatures))  # 9.266666666666666