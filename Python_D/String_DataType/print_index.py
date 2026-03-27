s = "ABCABCABCA"

print(s.count("ABC"))
print(s.find("ABC")) # Index of first occurenece = 0

print(s.find("ABC",3,10)) # Index of first occurenece = 3

print(s.find("ABC",6,10)) # Index of first occurenece = 6

print(s.find("ABC",9,10)) # Index of first occurenece = -1

s1 = "ABCABCABCA"
substr = "ABC"

i = s1.find(substr)
if i ==-1:
    print("Substring not found")

while i!=-1:
   print("{} present at index: {} ".format(substr,i))
   i = s.find(substr,i+len(substr), len(s1)) 
 
print("The number of occurenece :",s1.count(substr))