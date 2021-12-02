temps = [221, 234, 340, -9999, 230]  # -9999 = no value   # I must be careful to not devide it by 10.

new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(new_temps)  # [22.1, 23.4, 34.0, 23.0]  # [22.1, 23.4, 34.0, 0, 23.0]