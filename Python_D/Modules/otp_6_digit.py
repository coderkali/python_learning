from random import *

otp = ""
for i in range(6):
    otp = otp + str(randint(0,9))

print(otp)


# generate otp with 1,3,5 characters are alphabet symbols and 2,4,6 are digits 
alphabets = 'ABCDEFGHIJKLMONOPQRSTUVWXYZ'
digits = '0123456789'

for i in range(10):
    print(choice(alphabets),choice(digits),choice(alphabets),choice(digits),choice(alphabets),choice(digits),sep="")

