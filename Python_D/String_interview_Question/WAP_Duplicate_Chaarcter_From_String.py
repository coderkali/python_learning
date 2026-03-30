s = "AABBCCDDEEFF"

output = ""

for ch in s:
    if ch not in output:
        output = output + ch

print(output)


s1 = "ABBBDDCCFFEE"

l = []

for ch in s:
    if ch not in l:
        l.append(ch)

print("".join(l))

s2 = "jgfjgfwwwwwjhgfjhgwwwjhgjhgw"

s3 =set(s)

output= "".join(s3)

print(s3)