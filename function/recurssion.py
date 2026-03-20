def fibaanchoi(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibaanchoi(n - 1) + fibaanchoi(n - 2)
    

print(fibaanchoi(10))