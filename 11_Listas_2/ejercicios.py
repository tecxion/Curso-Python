pares = [n for n in range (30) if n % 2 == 0]
print(pares) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
impares = [n for n in range(23) if n % 2 != 0]
print(impares)
numeros = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
positivos = [n for n in numeros if n > 0]
print(positivos)
negativos = [n for n in numeros if n < 0]
print(negativos)