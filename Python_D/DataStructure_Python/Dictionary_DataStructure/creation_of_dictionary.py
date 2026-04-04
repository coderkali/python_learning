# EMpty Dict

d = {} 
d1 = dict()

print(type(d))
print(type(d1))


# With Data 

d = {100:"Meeta",200:"Kali"}

print(d)

#List of Tuples
l = [(100,"A"),(200,"B"),(300,"C")]
d2 = dict(l)
print(d2)

# Tuple of Tuple
t = ((100,"A"),(200,"B"),(300,"C"))
d3 = dict(t)
print(d3)

# Set of List 
#s = {[100,"A"],[200,"B"],[300,"C"]} # TypeError: cannot use 'list' as a set element (unhashable type: 'list')
#d4 = dict(s)
#print(d4)



#t1 = ((100,"A",12),(200,"B",13),(300,"C",14)) #ValueError: dictionary update sequence element #0 has length 3; 2 is required
#d5 = dict(t1)
#print(d5)


# By Using Dynamic Input

d = eval(input("Enter Dict ::"))

print(d)