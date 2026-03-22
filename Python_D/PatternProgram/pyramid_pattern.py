'''
i=0     *
i=1    * *
i=2   * * *

No of space 3 for 1st row 
No of space 2 for 2nd row 

if n = 4 

no of spaces in every row : n-i-1

How many times * to print: i+1

'''

n = int(input("Enter no of rows"))

for i in range(n):
    print(" "*(n-i-1) + "* " * (i+1))