
#int -> float

print(float(15))
print(float(0B1111))



#complex to Float

#print(float(10+20J)) #TypeError: float() argument must be a string or a real number, not 'complex'

# Bool to float

print(float(True))
print(float(False))

# str to float 
# should contain -> int value 
# should contain -> float value 

print(float('10.0'))
print(float('20.0'))

#print(float('0XFACE')) #ValueError: could not convert string to float: '0XFACE'

#print(float('Kali')) #ValueError: could not convert string to float: 'Kali'


# complex(x)

print(complex(10)) # 10+0J
print(complex(0B1111)) # 15+0J
print(complex(10.5)) #(10.5+0j)
print(complex(True)) #(1+0j)
print(complex("10")) #(10+0j)
print(complex("10.5")) #(10.5+0j)
#print(complex("0B11111")) #ValueError: complex() arg is a malformed string


# complex(x+y)

print(complex(10,20)) # 10+20J
print(complex(10.5,20.6))  #(10.5+20.6j)
#print(complex("10","20"))  #TypeError: complex() argument 'real' must be a real number, not str
#print(complex(10,"20")) #TypeError: complex() argument 'imag' must be a real number, not str




