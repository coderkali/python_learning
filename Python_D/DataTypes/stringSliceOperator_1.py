str = "kali"

print(str)
output = str[0].upper() + str[1:]

print(output)

output1 = str[:len(str)-1]+ str[-1].upper()

print(output1)
output2 = str[0].upper() + str[1:len(str)-1] + str[-1].upper()
print(output2)