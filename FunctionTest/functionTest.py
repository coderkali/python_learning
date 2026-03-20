def test(name):
    print("Hello...", name)

print(test("kali"))
print(id(test("Kali")))

test1 = test

print(test1("Kali"))
print(id(test1("Kali")))


del test

print(test1("Prasad"))