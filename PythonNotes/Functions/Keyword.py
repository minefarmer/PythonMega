# Non-keyword arguments   10
# Keyword arguments   15
# Default values   28
# doesn't work   39
# Some functions take exactly two arguments   50
# Print will take an indefinate number of arguments   68
# creating functions with an arbitrary number of arguments arugements   75
# 
# 
# def area(a, b):
#     return a * b

# print(area(4, 5))  # 20  *** the numbers four and five are non-keyword arguments  ^^^ AKA AS POSITIONAL ARUGEMENTS


# keyword agruments
# def area(a, b):
#     return a * b

# print(area(a=4, b=5))  # 20  *** the a=4 and a=5 are keyword arguments
# print(area(b=4, a=5))  # 20  *** order does not change the result
# print(area(a=5, b=4))  # 20  *** order does not change the result
# print(area(b=5, a=4))  # 20  *** order does not change the result




#  Default values
# def area(a, b=6):
#     return a * b

# print(area(a=5))  # 30
# print(area(a=5, b=7))  # 35   *** here the value of keyword b is overwritten
# print(area(5, 7))  # 35   *** here the value of keyword b is overwritten




# doesn't work
# def area(a=4, b):
#     return a * b

# print(area(5, 7))  #  def area(a=4, b):
#           # ^
#           # SyntaxError: non-default argument follows default argument




# Some functions take exactly two arguments
# >>> len('hello')
# 5
# >>> len('hello', 'hi')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: len() takes exactly one argument (2 given)

# >>> isinstance(6, int)  # ***************************************** I.E.
# True
# >>> isinstance(6, int, int)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: isinstance expected 2 arguments, got 3




# Print will take an infinate number of arguments
# >>> print(3, 4, 5, 6, 7, 10)
# (3, 4, 5, 6, 7, 10)




# creating functions with an arbitrary number of arguments arugements
# def mean(*args):
#     return args
#     # return type(args)  # <class 'tuple'>

# print(mean(1, 3, 'a', 4))  # (1, 3, 'a', 4)


# def mean(*args):
#     return sum(args) / len(args)

# print(mean(1, 3, 4))  # {'a': 1, 'b': 2, 'c': 3}


def mean(**kwargs):
    return kwargs

print(mean(a=1, b=2, c=3))  # {'a': 1, 'b': 2, 'c': 3}