def f1(func):
    func()


def f2():
    print("f2 function")


f1(f2)

list1 =[1,2,3,4,5,6,7,8,9]

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

list2 = list(filter(is_even,list1))
print(list2)