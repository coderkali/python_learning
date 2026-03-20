'''
  py test.py 10 20 30( The arguments are list type )

  sysy module -> argv 

  argv = [test.py,10,20,30]
  argv[0] is a  test.py not the 10 

    py test.py Kali Prasad -> Space is seperator between COmmand line argument 
    py test.py "Kali Prasad" -> This is one word

'''

from sys import argv
print(type(argv))
print(argv)
print(argv[0])
print("Length ", len(argv))
print(argv[1]+ argv[2])
print(int(argv[1])+ int(argv[2]))
#print(argv[100]) #IndexError: list index out of range




