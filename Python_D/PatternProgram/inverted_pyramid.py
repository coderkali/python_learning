'''
i=0  * * * *
i=1   * * *
i=2    * *
i+3     *

no of spaces in every row = i
no of star printed  (n-i)


'''

n = int(input("Enter a number"))

for i in range(n):
    print(" "*i + "* "*(n-i))