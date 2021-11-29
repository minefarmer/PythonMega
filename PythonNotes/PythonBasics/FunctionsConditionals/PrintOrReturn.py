# def mean(mylist):
#     the_mean = sum(mylist) / len(mylist)
#     return None

# print(mean([1, 4, 6]))  # None


# def mean(mylist):
#     the_mean = sum(mylist) / len(mylist)
#     print(the_mean)  # 3.6666666666666665

# print(mean([1, 4, 6]))  # None


# def mean(mylist):
#     the_mean = sum(mylist) / len(mylist)
#     print(the_mean)  # 3.6666666666666665

# print(mean([1, 4, 6]))  # None

# mymean = mean([0, 3, 4])  # 2.3333333333333335
# print(mymean + 10)  # Traceback (most recent call last):
# #   File "c:\Users\pgold\CarlsHub\PythonMega\PythonNotes\PythonBasics\PrintOrReturn.py", line 22, in <module>
# #     print(mymean + 10)TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'


# def mean(mylist):
#     the_mean = sum(mylist) / len(mylist)
#     return the_mean

# mymean = mean([0, 3, 4])
# print(mymean + 10)  # 12.333333333333334


def mean(mylist):
    print("Function started")  # Function started
    the_mean = sum(mylist) / len(mylist)
    return the_mean

mymean = mean([0, 3, 4])
print(mymean + 10)  # 12.333333333333334
