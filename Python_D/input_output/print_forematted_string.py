
'''
 %i -> Signed decimal value 
 %d -> Signed Decimal Value 
 %f -> Float Value 
 %s -> String , any other object 

'''


a= 10
b= 20

print("a vlaue:%i"%a)
print("b vlaue:%i"%b)

x= 100
y = 200
z=300

print("x=%d, y=%d, z=%d" %(x,y,z))

name = "Kali"
marks = [10,20,30,40]

print("hello %s, yOur List of marks is : %s" %(name, marks))


price = 70.56789

print("Price value is {}".format(price))
print("Price value is= %f"%price)
print("Price value is= %.2f"%price) # We have a control to print the How many decimal value we can print 