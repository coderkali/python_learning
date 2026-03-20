a = int(input("Enter First Number"))
b = int(input("Enter Second Number"))
c = int(input("Enter Third Number"))

min = a if a<b and a<c else b if b<c else c

print(min)

min = a if a<b<c else b if b<c else c # this is wrong 

print(min) 

max = a if a>b and b>c else b if b>c else c

print(max)


'''
  a&b 
  both numbers are equal
  first number is smaller than second number 
  first number is greate than second number 

  result = "equal" if a==b else "smaller" if a<b else "bigger"

'''

result = "Equal" if a==b else "Smaller" if a<b else "bigger"

print(result)

