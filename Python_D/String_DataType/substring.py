'''
find('B') -> index of this given substring from first occurence , if that is not found then -1 
rfind("B") -> Index of the position from last to first
find("B",beginIndex, endIndex) -> find(substring, begin, end-1) -> begin("B", 3, 8) ->  from 3 to 7

'''

s = "BCDA"

print(s.find("B"))
print(s.rfind("A"))
print(s.find("B", 3, 8)) # As B is not found between 3 to 7 index so its return -1

print(s.rfind("B", 1, 4)) 
