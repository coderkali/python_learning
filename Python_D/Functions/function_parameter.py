def wishMessage(name):
    print("Hello ",name,"Good Evening")

wishMessage("Kali")
#wishMessage() # TypeError: wishMessage() missing 1 required positional argument: 'name'


def squareit(num):
    sq = num * num
    print("The square of {} is {} ".format(num,sq))

squareit(5)

