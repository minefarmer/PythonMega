'''>>> len('hello
  File "<stdin>", line 1
    len('hello
        ^
SyntaxError: unterminated string literal (detected at line 1)
>>>
>>> len('hello')
5
>>> len('hello', 'hi'
... )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: len() takes exactly one argument (2 given)
'''


def mean(*args):  # A good practice is to use (args) all of the time
    return sum(args) / len(args)

# print(mean(1, 3, 'a', 4))   # TypeError: unsupported operand type(s) for +: 'int' and 'str'
                              # PS C:\Users\pgold\CarlsHub\PythonMega
# print(mean(1, 3, 4))  # 2.6666666666666665

# print(mean(1, x=3, 4))  # print(mean(1, x=3, 4))
                        # ^
                        # SyntaxError: positional argument follows keyword argument

# print(mean(1, 'a', 4))  # print(mean(1, x=3, 4))  # print(mean(1, x=3, 4))
                        # ^
                        # SyntaxError: positional argument follows keyword argument

print(mean(1, 3, 4))  # 2.6666666666666665
