def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean

monday_temperatures = [8.8, 9.1, 9.9]
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
print(mean(monday_temperatures))  # 9.266666666666666



'''>>> x = 3
>>> y = 1
>>> if x > y:
...     print("x is greater than y")
... elif x == y:
...     print("x is equal to y")
... else:
...     print("x is less than y")
... 
x is greater than y
>>> 
'''
