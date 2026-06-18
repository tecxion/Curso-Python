"""
Ejercicios de Itertools y Herramientas Funcionales
"""
import itertools

# 1. chain para unir tres listas.
unidas = list(itertools.chain([1, 2], [3, 4], [5, 6]))
print(unidas)   # [1, 2, 3, 4, 5, 6]


# 2. count del 0 al 10 de 2 en 2.
for numero in itertools.count(0, 2):
    if numero > 10:
        break
    print(numero, end=" ")   # 0 2 4 6 8 10
print()


# 3. accumulate (sumas acumuladas).
print(list(itertools.accumulate([10, 20, 30, 40])))   # [10, 30, 60, 100]


# 4. product: dos dados.
dados = list(itertools.product(range(1, 7), repeat=2))
print(f"Hay {len(dados)} combinaciones de dos dados")   # 36
print(dados[:5])   # primeras 5: [(1,1),(1,2),(1,3),(1,4),(1,5)]


# 5. combinations: parejas de amigos.
amigos = ["Ana", "Luis", "Marta", "Pedro"]
for pareja in itertools.combinations(amigos, 2):
    print(pareja)


# 6. islice: primeros 7 números pares.
pares = itertools.islice(itertools.count(0, 2), 7)
print(list(pares))   # [0, 2, 4, 6, 8, 10, 12]


# 7. enumerate: lista de la compra numerada.
compra = ["pan", "leche", "huevos", "fruta"]
for numero, producto in enumerate(compra, start=1):
    print(f"{numero}. {producto}")


# 8. all y any.
numeros = [15, 22, 8, 19]
print(f"¿Todos > 5? {all(n > 5 for n in numeros)}")   # True
print(f"¿Alguno > 20? {any(n > 20 for n in numeros)}")  # True
