s = "KaliPrasad"

i =0

print("character present at even index")

while i < len(s):
    if(i%2==0):
      print("Even Index :;",s[i])
    else:
      print("Odd Index :: ",s[i])
    i = i+1

print("#"*10)

print("Character at even index ::", s[0::2])

print("Character at even index ::", s[1::2])