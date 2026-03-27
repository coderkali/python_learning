'''
 "kali" < "Meeta"

 Unicode value of char
 a= 97
 b =98
 c = 99
 d = 100

 A-> 65
 B->66
 C->67
 D->68
 E->69

 K < M

'''

s = "Kali" < "Meeta"
print(s)

s = "ramba" < "ramya"
print(s)


s1 = input("Enter First String ")
s2 = input("Enter Second String ")

if s1 ==s2:
    print("Both Strings are Equal")
elif s1<s2:
    print("s1 is smaller than s2")
else:
    print("s1 is greater than s2")