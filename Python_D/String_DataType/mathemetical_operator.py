'''
concateniantion apply for string type only 

'''


s = "Kali" + "Prasad"
print(s)

#s = "Kali" + 2 #TypeError: can only concatenate str (not "int") to str
print(s)

s = "Kali"*3 # Valid
print(s)
s = 3*"Kali" # Valid
print(s)

#s = "Kali"*3.0  #TypeError: can't multiply sequence by non-int of type 'float'

'''
String + String -> Valid 
String * String -> Not Valid
String + Int -> Not valid
String * int -. valid 
'''