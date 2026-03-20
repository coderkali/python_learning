# int() -> to convert from other types to int
# float -> int(10.989) -> 10

#Float to Int
print(int(10.990))

# COmplexy to Int 
#print(int(10+20j)) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'


# Bool to Int 
print(int(True))
print(int(False))

#Stre to Int # String internally contains only integral value & base of 10
print(int("15"))

#print(int("0B1111")) #ValueError: invalid literal for int() with base 10: '0B1111'

