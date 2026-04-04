'''
def f1(*y,x=10):
   Defining Function -> Varibale Argument or default argument 


f1(10,20,30,x =40) -> Postional Argument , Keyword arguemnt 


1) Positional vs Keyword argument 
a) We can use both positional argument and keyword arguments in same function 
     But first should have positioonal argument then keyword argumnet   


2) Deafult vs Non-Deafult arguments 
After defaut argument we shouldn't take after non-default arguments 
Deafult arguments hsould be last argument 

3) Varibale Length vs Normal Arguments 
After varibale length arguments if we are taking any normal arguments we have to provide values by using keyword for that normal argument 
More than one variable length arguments are not allowed 

'''


def f1(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4)

f1(3,2)
f1(10,20,30,40)
f1(10,20,arg4=100)
f1(10,20,arg3=123,arg4=100)
# f1(arg4=100,arg1=20,arg3=100) # TypeError: f1() missing 1 required positional argument: 'arg2'

# f1()# Invalid  TypeError: f1() missing 1 required positional argument: 'arg2'

#f1(arg3=10,arg4=100,20,30)
#    #Invalid  SyntaxError: positional argument follows keyword argument
#.   After keyword argument we can't take positional arguments 

# f1(4,5,arg2=6) # Invalid  # TypeError: f1() got multiple values for argument 'arg2'

# f1(4,5,arg3=6,arg5=10) # TypeError: f1() got an unexpected keyword argument 'arg5'. Did you mean 'arg1'?

