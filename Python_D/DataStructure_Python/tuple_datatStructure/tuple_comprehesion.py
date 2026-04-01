l = [x*x for x in range(1,10)]

print(l)


# Compreshsion object is not applicable 

t = (x*x for x in range(1,10))

print(t) #This is not a tuple object but generator <generator object <genexpr> at 0x100f08ee0> 