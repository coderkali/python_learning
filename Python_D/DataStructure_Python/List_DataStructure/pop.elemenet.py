# pop() method will remove last elemenet
# pop(index) method will remove at specified index

l =[10,20,30]

print(l.pop()) #30 

print(l) #[10,20]

print(l.pop()) #20

print(l) #[10]

print(l.pop()) #10

print(l) #[]

#print(l.pop())  # IndexError: pop from empty list


l1= [10,20,30,40]

print(l1.pop(1)) # Remove at index which remloves the 20 

print(l1) # [10, 30, 40]

print(l1.pop(7))  # this index is not present so gets error # IndexError: pop index out of range

