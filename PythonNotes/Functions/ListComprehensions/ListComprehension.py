# Using list comprehension   16
# Using list comprehension with if conditional   23
# Using list comprehension with if-else   35
# 
#


# temps = [221, 234, 348, 230]

# Not using list comprehension
# new_temps = []
# for temp in temps:
#     new_temps.append(temp / 10)

# print(new_temps)  # [22.1, 23.4, 34.8, 23.0]


# Using list comprehension
# new_temps = [temp / 10 for temp in temps]

# print(new_temps)  # [22.1, 23.4, 34.8, 23.0]



# Using list comprehension with if conditional
# temps = [221, 234, 349, -9999, 30]

# new_temps = [temp / 10 for temp in temps if temp != -9999]

# print(new_temps)  # [22.1, 23.4, 34.9, 3.0]




# Using list comprehension with if-else
temps = [221, 234, 340, -9999, 230]

new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(new_temps)
