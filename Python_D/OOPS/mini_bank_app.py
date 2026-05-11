class Customer:
    '''
      This class by Kali and describes bank operations
    '''
    bank_name = "KALIBANK"
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance
    
    def getName(self):
        return self.name
    
    def getBalance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("After deposit , balance ::", self.balance)
    
    def withdraw(self, amount):
        if(amount > self.balance):
            print("Insuffcient Funds... Cannot perfrom this operation")
        else:
            self.balance = self.balance - amount
            print("After withdraw balance ", self.balance)
    
print("Welcome to ", Customer.bank_name)
name = input("Enter your name ::")
c = Customer(name)
while True:
    print("d -deposit \n w-withdraw \n e- exit")
    option = input("Choose your option :")
    if option.lower() == 'd':
        amount = float(input("Amount to Deposit ::"))
        c.deposit(amount)
    elif option.lower() == 'w':
        amount = float(input("Amount to withdraw ::"))
        c.withdraw(amount)
    elif option.lower() == 'e':
        print("Thanks for banking ")
        break
    else:
        print("Your options is valid , please choose valid options ")