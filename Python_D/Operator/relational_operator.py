# >, >=, <, <=

a =10
b =20

print(a<b)
print(a>b)
print(a>=b)
print(a<=b)

print("*"*100)

s1 = "a" # Unicode 97
s2=  "b" # Unicode 98

print(s1<s2)

s3 = "Kali"
s4 = "Kali"

print(s3<s4)
print(s3>s4)
print(s3>=s4)
print(s3<=s4)

print(ord('a'))
print(ord('A'))
print(chr(97))

print("*"*100)

print(True > False)
print(True >= False)
print(True < False)
print(True <= False)

print("*"*100)

#print(10<"Kali") #TypeError: '<' not supported between instances of 'int' and 'str'

a = 10
b= 20

if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")


print("*"*100)


print(10<20)
print(10<20<30) 
print(10<20<30<40) 
print(10<20<30<40>50) 
