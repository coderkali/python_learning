n = int(input("Enter any number"))

if n ==0:
    print("ZERO")
elif n ==1:
    print("ONE")
elif n ==2:
    print("TWO")
elif n ==3:
    print("THREE")
elif n ==4:
    print("FOUR")
elif n ==5:
    print("FIVE")
elif n ==6:
    print("SIX")
elif n ==7:
    print("SEVEN")
elif n ==8:
    print("EIGHT")
elif n ==9:
    print("TEN")


words= ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

j = int(input("Enter any number"))
print(words[j])

wordsList = [ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN","ELEVEN", "TWELEVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN" ]
        
word_for_ten = ["","", "TWENTY", "THRITEE", "FOURTEE", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY","NINTEE"]

k = int(input("Enter a number from 0 to 99"))

if k<=19:
    print(wordsList[k])
elif k<=99:
    # wordOfTen = word_for_ten[k//10]
    # wordOfReminder = wordsList[k%10]
    # print(wordOfTen+" "wordOfReminder)
    print(word_for_ten[k//10]+" "+wordsList[k%10])

