s= "B4A1D3"

print(sorted(s))

alphabets = []
digits = []
for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digits.append(ch)

print(alphabets)
print(digits)

l1= " ".join(sorted(alphabets) + sorted(digits))
print(l1)

