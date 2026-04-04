word = input("Any String ")

d = {}

for ch in word:
    d[ch] = d.get(ch,0) + 1

#print(d)

for k,v in sorted(d.items()):
    print(k,"Occurs ",v," times")
