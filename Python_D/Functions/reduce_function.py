from functools import reduce

l = [10,20,30,40,50]

reuslt = reduce(lambda x,y:x+y,l)

print(reuslt)

# Find the sum operation of first 100 number

result = reduce(lambda x,y:x+y,range(1,5))
print(result)