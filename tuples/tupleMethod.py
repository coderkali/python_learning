t = (3,12,5,8,2)

print(t.count(5)) # counts the number of times 5 appears in the tuple
print(t.index(8)) # returns the index of the first occurrence of 8 in the tuple
print(len(t)) # returns the number of items in the tuple
print(max(t)) # returns the maximum value in the tuple
print(min(t)) # returns the minimum value in the tuple
print(sum(t)) # returns the sum of all items in the tuple   

t[0] = 10 # this will raise an error because tuples are immutable   
