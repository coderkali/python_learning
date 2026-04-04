s1 = {10,20,30}
s2 ={30,40,50}

# s3 = s1+s2 # TypeError: unsupported operand type(s) for +: 'set' and 'set'

#s3 = s1*3 # TypeError: unsupported operand type(s) for *: 'set' and 'int'

s3 = {10,20,30}
s4 ={30,20,10}

print(s3==s4) # True
print(s3!=s4) # False


s5 = {10,20,30}
s6 ={30,20,10,3,1,2,3,4,5}
print("*"*100)
print(s5<s6)
print(s5<=s6)
print(s5>s6)
print(s5>=s6)

print("*"*100)
# Membership

s = {10,20,30,40}

print(10 in s)
print(50 not in s)