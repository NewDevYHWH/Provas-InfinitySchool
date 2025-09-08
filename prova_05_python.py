def maior_numero(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
print(maior_numero(5, 8, 3))
print(maior_numero(12, 7, 12))
print(maior_numero(-1, -5, -3))