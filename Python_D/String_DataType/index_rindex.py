s = "ABCBA"

print(s.index("B"))
#print(s.index("Z")) # ValueError: substring not found

print(s.rindex("B"))
#print(s.rindex("z")) # ValueError: substring not found

mail = input("Enter your mailId ")
try:
    i = mail.index("@")
    print("mail id contains @ symbol")
except ValueError:
    print("mailid d;esnot exit @")


# Index with boundary

s1 = 'ABCDEFGHIJKLMN'

#print(s.index("B", 4, 8)) # From 4 to 7 # Value Error  #ValueError: substring not found
print(s.index("B", 4, 10000)) #-> This is valid 