s = "ABABABABABA"
s1 = s.replace("A","B")
print(s1)

s2 ="Kali Prasad Padhi"
s3 = s2.replace(" ","")
print(s3)

print("The Number of space ", s2.count(' '))
print("The Number of space ", len(s2)-len(s3))

str = "learning Python is Very Difficult"
str1 = str.replace("difficult","Easy")
str1 = str.replace("Difficult","Easy")
print(str1)