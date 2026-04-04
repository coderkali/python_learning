'''
Global variable
a=10 -> Global variable
def f1():
  print(a)

Local Variable

'''

a=10
def f1():
  print(a)
def f2():
  print(a)

f1()
f2()

