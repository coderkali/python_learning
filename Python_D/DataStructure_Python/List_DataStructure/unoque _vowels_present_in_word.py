vowels = ['a','e','i','o','u']

word = input("Enter any string :")

result = []

for ch in word:
    if ch in vowels:
        if ch not in result:
            result.append(ch)

print(result)


result1 = [ch for ch in vowels if ch in word]
print(result1)