s = "One Two Three Four Five Six"
l = s.split()

print(l)

i =0
l1=[]
for x in l:
   if(i%2==0):
      l1.append(x)
   else:
      l1.append(l[i][::-1])
   i= i+1

print(l1)

output = " ".join(l1)
print(output)