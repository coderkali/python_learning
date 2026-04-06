# randint(begin,int) # random int value between begin adn end (begin<x<end)

from random import *
for i in range(10):
    print(randint(1,10))

# randrange(begin,end, step) # random int value between begin adn end with given step value  (begin<x<end)

# begin is opional & default value is 0
# step is optional & default value is 1 


print("*"*100)
print(randrange(5))  # begin =0 , end 5 and step 0 = [0,1,2,3,4]
print(randrange(1,5)) # begin =1 , end 5 and step 1 = [0,1,2,3,4]
print(randrange(1,11,2)) # begin =1 , end 11 and step 2

print(randrange(0,101,10)) 