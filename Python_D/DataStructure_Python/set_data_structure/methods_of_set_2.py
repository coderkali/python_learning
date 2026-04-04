s = {10,20,30}

s.remove(30)
print(s)

#s.remove(50) # KeyError: 50
s.discard(30) 
s.discard(20) 

print(s)

s2 = {10,20,30,40,50}

print(s2.pop()) # Element is removed and returned  # 50 (Its a random)
print(s2.pop()) # Element is removed and returned  # 20 (Its a random)
print(s2.pop())
print(s2.pop())
print(s2.pop())
# print(s2.pop()) # KeyError: 'pop from an empty set'
print("*"*100)

s3 = {10,20,30,40,50}
print(s3)
s3.clear()
print(s3)