'''
in 
not in 


'''

s = "k" in "Kali"
print(s)

s = "K" in "Kali"
print(s)

s = "K" not in "Kali"
print(s)

s1 = input("Enter main string:: ")
s2 = input("Enter Sub String :: ")

if s2 in s1:
    print("s2 is present in s1")
else:
    print("s2 is not present in s1")