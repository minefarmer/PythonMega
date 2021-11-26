def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean()

print(mean([1, 4, 6]))



def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

mymean = mean([0, 3, 4])
print(mymean + 10)  # 12.333333333333334
