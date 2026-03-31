'''
By using inde

by using slice operator 

     -4 -3 -2 -1
l = [10,20,30,40]
     0. 1. 2  3

'''

l = [10,20,30,40]

print(l[-1]) # 40
print(l[0]) # 10
#print(l[100]) # IndexError: list index out of range


'''
slice operator 

list = l[begin:end:step]

if step is +ve => forward direction => begin to end-1
if step is -ve => Backward direction => begin to end+1

   -10,-9,-8,-7,-6,-5,-4,-3 -2 -1
l =[10,20,30,40,50,60,70,80,90,100]
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9

'''


l =[10,20,30,40,50,60,70,80,90,100]
print(l[2:7]) # [30, 40, 50, 60, 70]
print(l[2:7:2]) # [30, 50, 70]
print(l[4::2])  # From 4 th index to end of the list with step 2 [50,70,90]
print(l[8:2:-2]) # begin to end-1 -> 8th index to 2+1=3 With backward direction index with step of -2 =>  [90,70,50]

print(l[4:100]) # begin to end-1 -> 4 to 99 -> [50,60,70,80,90,100]
print(l[4:10:2]) # If in forward direction is if end value is 0 then the answer is empty [] 

print(l[::1]) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(l[::-1])  # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]