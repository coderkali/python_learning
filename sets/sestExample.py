s = {3,23,41,23,45,67,89,90,34}

print(s, type(s))


#print(s[3]) # This will raise an error because sets are unordered and do not support indexing



print(len(s)) # returns the number of items in the set
print(max(s)) # returns the maximum value in the set
print(min(s)) # returns the minimum value in the set
print(sum(s)) # returns the sum of all items in the set 


print(23 in s) # returns True if 23 is in the set, False otherwise
print(100 in s) # returns True if 100 is in the set, False otherwise 

s.add(100) # adds 100 to the set
print(s)

# s.remove(100) # removes 100 from the set
# print(s)    

s.discard(200) # removes 100 from the set if it exists, does nothing if it doesn't exist
print(s)

s.pop() # removes and returns an arbitrary element from the set
print(s)    




