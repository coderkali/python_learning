class Test:

    @staticmethod
    def average(list1):
        result = sum(list1)/len(list1)
        print(result)

list1= [10,20,30,40]
Test.average(list1)