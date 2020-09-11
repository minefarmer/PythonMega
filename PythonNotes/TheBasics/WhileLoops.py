username = ''

# while username != "pypy":
#     username = input("Enter username: ")  # Enter username: py
#                                         # Enter username: ppy
#                                         # Enter username: pypy   # exits the loop here.
#                                         # sh-5.0$


# break and continue  ** use the bottom way
# while username != "pypy":
#     username = input("Enter username: ")  # Enter username: rich
#                                         Enter username: carl
#                                         Enter username: mike
#                                         Enter username: pypy
#                                         sh-5.0$


# break and continue
while True:
    username = input("Enter username: ")
    if username == 'pypy':
        break
    else:
        continue
                    # Enter username: asfd
                    # Enter username: adsf
                    # Enter username: pypy
                    # sh-5.0$ 
