s = "Kali"
print(s[0])
print(s[-1])
#print(s[100]) # IndexError: string index out of range

str = input("Enter any string ::")


i =0
for x in str:
    print("The character {} present at +ve index: {} and at -ve index {}".format(x,i,i-len(str))) 
    i= i +1


