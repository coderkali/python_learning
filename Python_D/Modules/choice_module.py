# choice() # To generate random ibject from list , tuple, string etc 

#choice(sequnce)
from random import *
fruits = ["Apple","Orange","Lemon","Bananan","Watermelon"]
print(choice(fruits)) # #Works for List , Tuple As its working for index based 

alphabets = 'ABCDEFGHIJKLMONOPQRSTUVWXYZ'

for i in range(5):
    print(choice(alphabets))

