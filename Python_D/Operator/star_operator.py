print("Kali"*3)
print(3*"Kali")
#print("Kali"*"Padhi") #TypeError: can't multiply sequence by non-int of type 'str'
#print("Kali"*"3") #TypeError: can't multiply sequence by non-int of type 'str'
print("Kali"*int('3'))

print("Kali"* True)
print("This is empty String" + "Prasad"* False)