#  Exceptions

# a = 1
# b = "2"
# print(int(2.5) 
# print(a + b)  # File "c:\Users\pgold\CarlsHub\PythonMega\class.py", line 3
            #     print(int(2.5) 
            #         ^
            # SyntaxError: '(' was never closed


# a = 1
# b = "2"
# print(int(2.5))
# print(a + b)  # Traceback (most recent call last):
            #   File "c:\Users\pgold\CarlsHub\PythonMega\class.py", line 4, in <module>
            #     print(a + b)  # File "c:\Users\pgold\CarlsHub\PythonMega\class.py", line 3
            # NameError: name 'a' is not defined


# a = 1
# b = "2"
# print(int(2.5))
# print(a + b)  # Traceback (most recent call last):
                # File "c:\Users\pgold\CarlsHub\PythonMega\class.py", line 22, in <module>
                #     print(a + b)
                # TypeError: unsupported operand type(s) for +: 'int' and 'str'


# a = 1
# b = "2"
# print(int(2.5))  # 2
# print(str(a) + b)  # 12


# a = 1
# b = "2"
# print(int(2.5))  # 2
# print(c)  # Traceback (most recent call last):
            # File "c:\Users\pgold\CarlsHub\PythonMega\class.py", line 37, in <module>
            #     print(c)  #
            # NameError: name 'c' is not defined


# a = 1
# b = "2"
# c = 3
# print(int(2.5))  # 2
# print(c)  # 3


a = 1
b = "2"
c = 3
print(int(2.5))  # 2
print(c/0)  # Traceback (most recent call last):
            # File "c:\Users\pgold\CarlsHub\PythonMega\class.py", line 54, in <module>
            #     print(c/0)  # 3
            # ZeroDivisionError: division by zero
