"""
EJERCICIOS
"""
companias = {"Mercadona", "Lidl", "Alcampo", "Carrefour", "Mediamarkt", "PcComponentes"}
num_A = {19, 20, 21, 22, 26, 27, 28, 29, 30}
num_B = {19, 20, 23, 24, 25, 29, 30, 31, 32}
edad = [21, 23, 30, 31, 25, 22, 21, 26, 30, 22, 19, 27, 23]

# Imprime por pantalla la longitud de `companias`
print(len(companias))

# Añade `Aldi`a companias
companias.add("Aldi")

# Añade a la vez estas compañias a companias `Decathlon, Microsoft, Apple`
companias.update("Decathlon", "Microsoft", "Apple")

# Elimina una empresa de companias
companias.remove("Alcampo")

# Une `num_A y num_B`
numeros = num_A.union(num_B)

# Encuentra la diferencia entre `num_A y num_B`
num_A.difference(num_B)

# ¿num_A es un subconjunto de num_B?
num_A.issubset(num_B)

# ¿Son num_A y num_B conjuntos distintos?
num_A.isdisjoint(num_B)

# Haz la diferencia entre `num_B y num_A`
num_B.difference(num_A)

# Haz la diferencia simétrica de `num_A y num_B`
num_A.symmetric_difference(num_B)

# Elimina el conjunto companias por completo.
del companias

# convierte edad a un conjunto y compara la longitud, ¿Cúal es más grande?
ls_edad = set(edad)
print(len(ls_edad))
print(len(edad))