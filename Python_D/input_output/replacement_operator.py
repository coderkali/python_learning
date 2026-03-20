l = [10,20,30,40,50]

print(l)

t = (10,20,30,40,50)

print(t)


# Replacemenet Operator 
name = "Kali"
salary = "160000"
gf = "Meeta"

print("Hello {}, Your salary {} and your wife {} is waiting".format(name,salary,gf))

print("Hello {0}, Your salary {1} and your wife {2} is waiting".format(name,salary,gf))

print("Hello {n}, Your salary {s} and your wife {f} is waiting".format(s=salary,f=gf,n=name))


a,b,c,d =10,20,30,40

print("a = {}, b ={}, c={}, d={}".format(a,b,c,d))