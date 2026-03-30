s = "a3z2b4"

target = ""

for ch in s:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        target = target + x*d

print(target)
output=  "".join(sorted(target))
print(output)