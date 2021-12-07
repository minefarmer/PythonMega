# import time
import os
import pandas

while True:
    if os.path.exists("temps_today.csv"):
        data = pandas.read_csv("temps_today.csv")
        print(data.mean())
    else:
        print("File does not exixt.")
    # time.sleep(10) # dtype: float64
                    # st1     22.150
                    # st2    21.275
                    # dtype: float64
                    # st1     22.150
                    # st2    21.275
                    # dtype: float64
