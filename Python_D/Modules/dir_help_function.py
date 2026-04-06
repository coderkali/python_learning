'''
dir() -> To list out all memembers of current module 
dir(modulename) -> To lits out all members of specfied module 

'''

import mathcalc
import math

print(dir(mathcalc))

def test():
    print("testing")

print(dir())
print(dir(math))

print(help(math))
