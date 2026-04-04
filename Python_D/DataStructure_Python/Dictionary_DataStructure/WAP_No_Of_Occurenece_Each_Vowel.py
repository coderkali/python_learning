word = input("Any String ")

vowel = {"a","e","i","o","u"}

d ={}

for ch in word:
    if ch in vowel:
        d[ch] = d.get(ch,0) +1


for k,v in d.items():
    print(k,"Occurs ",v," times")