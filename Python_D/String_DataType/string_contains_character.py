'''
 isalnum
 islphac
 islower
 isupper
 isdigit
 istitle
 isspace

'''

print("Kali123".isalnum()) #true
print("Kali123".isalpha()) #false
print("Kali".isalpha()) #true
print("Prasad".isdigit()) #False
print("5765765".isdigit()) #true
print("abcd".islower()) #true
print("Abc".isupper()) #False
print("Kali Prasad Padhi".istitle()) #true
print("Kali prasad padhi".istitle()) #False
print(" ".isspace()) #True