import mathcalc as m
print(m.x)

m.add(10,20)
#mathcalc.substract(20,30) # NameError: name 'mathcalc' is not defined

m.substract(30,40)

from mathcalc import x,y,add,substract

print(x)
print(y)
add(10,20)
substract(30,40)
