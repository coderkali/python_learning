'''
upper()
lower()
swapcase() -> to convert lower to upper or upper to lower
title() -> to convert all the first charaxcter to lower case
capitalize() -> first chararcter of the string will be converted to upper case and all rmainiang character can be conevrted to lower case
'''

s = "Learning Python is Very easy"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())


s1 = input("Enter First String :").upper()
s2 = input("Enter second String :").upper()

if s1==s2:
    print("Both Strings are queal")
else:
    print("Both are not equsl")



str = input("Enter any String ::")

output = str[0].upper() + str[1:len(str)-1].lower() + str[-1].upper()

print(output)