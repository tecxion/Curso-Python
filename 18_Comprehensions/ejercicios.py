"""
Ejercicios de Comprensiones, Iteradores y Generadores
"""

# 1. Lista con los números del 1 al 20.
numeros = [n for n in range(1, 21)]
print(numeros)


# 2. El doble de cada número.
dobles = [n * 2 for n in [1, 2, 3, 4, 5]]
print(dobles)   # [2, 4, 6, 8, 10]


# 3. Longitud de cada palabra.
palabras = ["Hola", "Mundo", "Python"]
longitudes = [len(palabra) for palabra in palabras]
print(longitudes)   # [4, 5, 6]


# 4. Múltiplos de 3 del 1 al 30 (comprensión con filtro).
multiplos_3 = [n for n in range(1, 31) if n % 3 == 0]
print(multiplos_3)   # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]


# 5. "alto" si > 15, "bajo" en caso contrario (if/else en comprensión).
valores = [12, 7, 25, 4, 18, 9, 30]
etiquetas = ["alto" if n > 15 else "bajo" for n in valores]
print(etiquetas)   # ['bajo', 'bajo', 'alto', 'bajo', 'alto', 'bajo', 'alto']


# 6. Diccionario número -> cubo (comprensión de diccionario).
cubos = {n: n ** 3 for n in range(1, 6)}
print(cubos)   # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}


# 7. Generador pares_hasta(n) con yield.
def pares_hasta(n):
    numero = 0
    while numero <= n:
        yield numero
        numero += 2

print("Pares hasta 10:")
for par in pares_hasta(10):
    print(par, end=" ")   # 0 2 4 6 8 10
print()


# 8. Generador fibonacci(cantidad).
def fibonacci(cantidad):
    a, b = 0, 1
    for _ in range(cantidad):
        yield a
        a, b = b, a + b

print("Primeros 10 de Fibonacci:")
print(list(fibonacci(10)))   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
