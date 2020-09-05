# def mean(mylist):
#     the_mean = sum(mylist) / len(mylist)
#     return the_mean

# print(mean([1, 4, 5]))  # 3.3333333333333335



# oz = 5  # THIS IS NOT WORKING.!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def food(oz):
#     return oz * 29.86765



# def mean(mylist):
#     the_mean = sum(mylist) / len(mylist)
#     print(the_mean)  # None

# print(mean([1, 4, 5]))  # 3.3333333333333335



# def mean(mylist):
#     the_mean = sum(mylist) / len(mylist)
#     # print(the_mean)  # None  ## do not use

# mymean = mean([0, 3, 4])  # 2.3333333333333335
# # print(mymean + 10)  # Traceback (most recent call last):
# #   File "/home/carl/Github/PythonMega/PythonNotes/TheBasics/CreatingFunctions.py", line 28, in <module>
# #     print(mymean + 10)  # 3.3333333333333335
# # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'



def mean(mylist):
    print("Function started!")  # Function started!
    the_mean = sum(mylist) / len(mylist)
    return the_mean

mymean = mean([0, 3, 4]) 