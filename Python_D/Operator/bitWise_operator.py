# We can apply for int and bool
# & - Biwise and 
# | -> Bitwise OR
# ^ -> Bitwise XOR 
# ~ -> Bitwise Complment Operator
# << -> Bitwise left-shift Operator 
# >> -> Bitwise right-shift Operator 

#print(10.5 & 20.6) #TypeError: unsupported operand type(s) for &: 'float' and 'float'

print(10 & 20)
print(True & False)

# & -> If both bits are 1 then result is 1 
   # example : 1 & 1 -> 1
   # example : 1 & 0 -> 1
   # example : 0 & 1 -> 0
   # example : 0 & 0 -> 0
print(4 & 5) # 4 -> 100 & 5 -> 101 = 100 = 4
# | -> If the one bit is 1 then result is 1or result is 0
   # example : 1 & 1 -> 1
   # example : 1 & 0 -> 1
   # example : 0 & 1 -> 1
   # example : 0 & 0 -> 0
print(4 | 5) # 4 -> 100 | 5 -> 101 = 101 = 5
# ^ -> If both bits are different then the result is 1 else result is 0
   # example : 1 & 0 -> 1
   # example : 0 & 1 -> 1
   # example : 0 & 0 -> 0
   # example : 1 & 1 -> 0
print(4 ^ 5) # 4 -> 100 | 5 -> 101 = 001 = 1


# ~ 
# The most signficiant bit acts as sign bit 
# o -> +ve number
# 1 -> -ve number

# +ve number will be resposented directly in the memory 
# -ve number will be respsented in 2's complmenet form
# 1st complemnet => 0 -> 1    1-> 0
# 2's complmenet form  -> 1's complmenet for + 1
print(~4)
# Solve 
'''
  4 = 32 bit = 00000.....0100
  ~4= 32 bit = 11111.....1011 -> Negation then tahts converts from 0_. 1 and 1-> 0
  The first bit respesnets -ve number , 1 is nothing but -ve number
  Then to convertes all the bits into 2's complmenet form 
  11111.....1011 -> 1's complmenet form -> 0000....0100 -> 2's complmenet form -> 0000....0100 + 1 = 0000...0101 = 5 = Due to the first bit is negative so answer is = -5
'''
print(~5)
print(~-4)
'''
  4 = 32 bit  = First bit is 1 Then the reminaing bits are in 2's complmenet form -> 00000.....0100 
     -> 1's complement for -> 1111....1011 -> 2's complmnete form 1111....1011 + 1 =  1111....11100
  ~4 = Flip the 1-> 0 and 0 -> 1 -> 0000...00011 -> Append the 1st bit 1 [0000...000011] -> 3(answer)
'''

print(~True) # -2
