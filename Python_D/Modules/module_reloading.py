import mathcalc
import mathcalc
import mathcalc
import mathcalc
import mathcalc
import time
import importlib


# Even we import the module multiple times , it is still loads one time 

mathcalc.add(10,20)
print("Enter into sleeping state")
time.sleep(12)
print("Just wakeup")

# import mathcalc
# mathcalc.product(10,20) # As this function add at runtime , so ity won't be avilalble

importlib.reload(mathcalc)
mathcalc.product(10,20)

