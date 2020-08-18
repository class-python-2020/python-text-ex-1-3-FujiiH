def func(v):
    i = v + 3
    return i


import sys
print(sys.path)

def func_in_module_under_dir():
    print("This is '{}'.".format(__name__))