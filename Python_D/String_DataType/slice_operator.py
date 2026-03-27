'''
 s[begin:end]
 Substring from begin index to end-1 index
 Begin is optional & default value is 0
 end is optional & default value is len(s)
'''

s = "abcdefghijk"

print(s[2:7]) # cdefg
print(s[:7])  # abcdefg
print(s[2:]) #cdefghijk
print(s[:]) # abcdefghijk

'''
 s[begin:end:step]

 step = jump those manay character 
'''

s1 = 'abcdefghijk'
print(s1[2:7])
print(s1[2:7:2])
print(s1[2::2])
print(s1[:9:2])
print(s1[:9:2])
print(s1[::2])




