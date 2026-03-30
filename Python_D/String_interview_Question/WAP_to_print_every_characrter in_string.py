s = "a9b3c2"
#s1 = "aaaabbbcc"
output = ""
for ch in s:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        output = output + x*d

print(output)
