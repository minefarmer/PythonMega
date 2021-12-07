import time
import os  
'''If (import os) is not there, it will show:
Traceback (most recent call last):
  File "c:\Users\pgold\CarlsHub\PythonMega\class.py", line 5, in <module>
    if os.path.exists("vegetables.txt"):
NameError: name 'os' is not defined
'''

while True:
    if os.path.exists("vegetables.txt"):
        with open("vegetables.txt") as file:
            print(file.read())  # Tomato
                                # Cucumber
                                # Onion
                                # Garlic
                                # Okra
    else:
        print("File does not exixt.")
    time.sleep(10)  # Tomato
                    # Cucumber
                    # Onion
                    # Garlic
                    # Okra
                    # Tomato
                    # Cucumber
                    # Onion
                    # Garlic
                    # Okra
                    # Tomato
                    # Cucumber
                    # Onion
                    # Garlic
                    # Okra




'''import sys
>>> sys.builtin_module_names
('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections', '_contextvars', '_csv', '_datetime', '_functools', '_heapq', '_imp', '_io', '_json', '_locale', '_lsprof', '_md5', '_multibytecodec', '_opcode', '_operator', '_pickle', '_random', '_sha1', '_sha256', '_sha3', '_sha512', '_signal', '_sre', '_stat', '_statistics', '_string', '_struct', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', '_winapi', '_xxsubinterpreters', 'array', 'atexit', 'audioop', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', 'msvcrt', 'nt', 'sys', 'time', 'winreg', 'xxsubtype', 'zlib')       
>>>
>>> 
>>> 
>>> import os
>>> sys.prefix
'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.240.0_x64__qbz5n2kfra8p0'
'''