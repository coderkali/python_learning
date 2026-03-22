'''
i=0      *
i=1    *   *
i=2   *  *  *
i=0    *   *
i=1      *

no of rows in each row = n-i-1
no of * in each row = i+1
=================
Second Part::

no of rows in each row = i+1
no of * in each row = n-i
'''


n = int(input("Enter a number"))

for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1))


for i in range(n):
    print(" "*i + "* "*(n-i))