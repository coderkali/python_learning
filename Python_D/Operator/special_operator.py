'''
  Identity Operator 
    -> is  # Reference comparsion 
    -> is not 

    r1 is r2 => True if both refernces pointing to the same object 

    r1 is not r2 => true if both r1 and r2 is not pointing to same iobject 


'''


a = 10
b =10

print(a is b)
print(a is not b)

a = "Kali"
b = "Kali"

print ("*"*100)
print(a is b)
print(a is not b)


print ("*"*100)
l1 = [10,20,30,40,50]
l2 = [10,20,30,40,50]

print(id(l1))
print(id(l2))

print(l1 is l2) # False Reference Comparison 
print(l1 == l2) # True Conent COmparision


print ("--"*100)

'''
  Membership Operator 
    -> in 
    -> not in

     a in sequnce -> true
     a not in sequence  -> true

'''

s = "Learning python is easy"

print('h' in s)
print('d' in s)
print('d' not in s)
print('Python' in s)


print ("--"*100)

l =["Kali", "Meeta", "Rishi"]

print("Kali" in l)
print(" Kali " not in l)
print("Meeta" in l)
print("Rishi" in l)