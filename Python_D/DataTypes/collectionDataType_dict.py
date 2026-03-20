# d = {k1:v1, k2:v2, k3:v3}

# Grop of key pair
# Order is not preserved
# No Duplicate keys 
# Duplicate Values allowed
# Hetrogenous Object allowed 
# mutable
# Indexing or sliciing is not applicable
d = {100: "kali", 99:"Meeta", 300:"Krithvik"}

print(d)
print(type(d))

print(d[100])
print(d[99])

d[100] = "Kpp"
print(d)
