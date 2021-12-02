"""Type "help", "copyright", "credits" or "license" for more information.
>>> len("abc")
3
>>> isinstance("abc", str)
True
>>> help(len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

>>> >>> len("abc")
3

>>> isinstance("abc", str)
True

>>> help(isinstance)  
Help on built-in function isinstance in module builtins:

isinstance(obj, class_or_tuple, /)
    Return whether an object is an instance of a class or of a subclass thereof.        

    A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to        
    check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
    or ...`` etc.
"""


def area(a, b):
    return a + b

print(area(4, 5))  # 9  ## Non-keyword argmunents

print(area(b=4, a=5))  # Keyword arguments  ## their position can be reversed


