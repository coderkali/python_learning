for i in range(10):
    if i%2 != 0:
        continue
    print(i)


cart = [10,20,30,600,70,80]

for item in cart:
    if item > 500:
        print("Continue now")
        continue;
    print("Processing item:", item)
print()


l = [10,20,0,50,60,80,0,90]

for x in l:
    # print("100/{}={}".format(x,100/x))
    if(x == 0):
       print("How you can proceed with zero")
       continue
    print("100/{}={}".format(x,100/x)) 
print("Outside loop")