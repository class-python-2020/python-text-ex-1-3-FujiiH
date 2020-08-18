import os

path = os.getcwd()
 

def func_in_module_under_dir():
    print("This is '{}'.".format(__name__))