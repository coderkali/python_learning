s = "ABLLLXXXQQQLLBACBABBA"
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
print(l)

for ch in l:
    print("{} occurs {} times ".format(ch,s.count(ch)))


print("**********************")

for ch in sorted(l):
    print("{} occurs {} times ".format(ch,s.count(ch)))


print("**********************")

s = "ABLLLXXXQQQLLBACBABBA"
s1 = set(s)

for ch in sorted(s1):
    print("{} occurs {} times ".format(ch,s.count(ch)))