student_grades = [9.1, 8.8, 7.5]  # This is a list  ## mutable i.e.  can be changed
student_grades = {"Marry":  9.1, "Sam": 8.8, "John": 7.5}  # This is a dictionary  ## {key: value}

mysum = sum(student_grades)
length = len(student_grades)
mean = mysum / length
print(mean)  # 8.466666666666667


monday_temperatures = (1, 4, 5)  # This is a Tuple  ## immutable i.e.  cannot be changed
monday_temperatures.append(6)  # Traceback (most recent call last):
                                # File "c:\Users\pgold\CarlsHub\PythonMega\PythonNotes\PythonBasics\Attributes.py", line 4, in <module>
                              #  mysum = sum(student_grades)
                              #  TypeError: unsupported operand type(s) for +: 'int' and 'str'
