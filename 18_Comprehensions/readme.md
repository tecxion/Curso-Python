<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/17_Ficheros/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/19_Entornos_Virtuales/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/comprehensions.png">
</h1>


<h1 align="center">Comprensiones, Iteradores y Generadores</h1><br>

<h3>Índice</h3>

- [1. Comprensión de listas (List Comprehension)](#1-comprensión-de-listas-list-comprehension)
- [2. Comprensión con condición](#2-comprensión-con-condición)
- [3. Comprensión de diccionarios y conjuntos](#3-comprensión-de-diccionarios-y-conjuntos)
- [4. Iterables e iteradores](#4-iterables-e-iteradores)
- [5. Generadores y yield](#5-generadores-y-yield)
- [6. Expresiones generadoras](#6-expresiones-generadoras)
- [7. ¿Cuándo usar cada cosa?](#7-cuándo-usar-cada-cosa)
- [8. Ejercicios](#8-ejercicios)

<a name = "1-comprensión-de-listas-list-comprehension"></a>

## 1. Comprensión de listas (List Comprehension)

Una **comprensión de listas** es una forma corta y elegante de crear listas en una sola línea. Es una de las características más queridas (y reconocibles) de Python.

Mira cómo simplifica un bucle clásico:

```python
# Forma tradicional con un bucle for
cuadrados = []
for numero in range(1, 6):
    cuadrados.append(numero ** 2)
print(cuadrados)   # [1, 4, 9, 16, 25]

# La MISMA operación con una comprensión de listas
cuadrados = [numero ** 2 for numero in range(1, 6)]
print(cuadrados)   # [1, 4, 9, 16, 25]
```

La estructura es: `[expresión for elemento in iterable]`. Se lee casi como en lenguaje natural: *"el cuadrado de cada número en el rango"*.

```python
nombres = ["ana", "luis", "marta"]
mayusculas = [nombre.upper() for nombre in nombres]
print(mayusculas)   # ['ANA', 'LUIS', 'MARTA']
```

<a name = "2-comprensión-con-condición"></a>

## 2. Comprensión con condición

Podemos añadir un `if` al final para **filtrar** qué elementos entran en la lista:

```python
# Solo los números pares
numeros = range(1, 11)
pares = [n for n in numeros if n % 2 == 0]
print(pares)   # [2, 4, 6, 8, 10]
```

También podemos usar un `if/else` **antes** del `for` para transformar según una condición:

```python
numeros = [1, 2, 3, 4, 5]
etiquetas = ["par" if n % 2 == 0 else "impar" for n in numeros]
print(etiquetas)   # ['impar', 'par', 'impar', 'par', 'impar']
```

>[!NOTE]
>Cuidado con la posición: el `if` **solo** (filtrar) va al final; el `if/else` (elegir un valor u otro) va al principio, justo después de la expresión.

<a name = "3-comprensión-de-diccionarios-y-conjuntos"></a>

## 3. Comprensión de diccionarios y conjuntos

La misma idea funciona para crear **diccionarios** (con `{clave: valor ...}`) y **conjuntos** (con `{...}`):

```python
# Comprensión de DICCIONARIO
numeros = [1, 2, 3, 4]
cuadrados = {n: n ** 2 for n in numeros}
print(cuadrados)   # {1: 1, 2: 4, 3: 9, 4: 16}

# Comprensión de CONJUNTO (sin duplicados)
letras = {letra for letra in "programacion"}
print(letras)   # {'p', 'r', 'o', 'g', 'a', 'm', 'c', 'i', 'n'}
```

<a name = "4-iterables-e-iteradores"></a>

## 4. Iterables e iteradores

Dos conceptos que conviene distinguir:

- **Iterable**: cualquier objeto que se puede recorrer con un `for` (listas, tuplas, strings, diccionarios, conjuntos…).
- **Iterador**: el objeto que va entregando los elementos **uno a uno**, recordando por dónde va.

Con `iter()` convertimos un iterable en un iterador, y con `next()` pedimos el siguiente elemento:

```python
numeros = [10, 20, 30]
iterador = iter(numeros)

print(next(iterador))   # 10
print(next(iterador))   # 20
print(next(iterador))   # 30
# next(iterador) -> StopIteration: ya no quedan elementos
```

De hecho, cuando haces un `for`, Python está usando `iter()` y `next()` por debajo de forma automática.

<a name = "5-generadores-y-yield"></a>

## 5. Generadores y yield

Un **generador** es una función especial que, en lugar de devolver todos los valores de golpe con `return`, los va entregando **uno a uno** con la palabra reservada **`yield`**. Esto es muy eficiente con la memoria porque **no guarda todos los valores a la vez**: los crea según se piden.

```python
def contar_hasta(n):
    numero = 1
    while numero <= n:
        yield numero       # entrega un valor y "pausa" la función aquí
        numero += 1

# El generador no calcula nada hasta que lo recorremos
for valor in contar_hasta(5):
    print(valor)   # 1, 2, 3, 4, 5
```

La diferencia con `return`: al llegar a `yield` la función **se pausa** y recuerda su estado; en la siguiente petición continúa justo donde se quedó.

```python
def numeros_pares():
    n = 0
    while True:        # ¡un generador infinito! Imposible con una lista
        yield n
        n += 2

generador = numeros_pares()
print(next(generador))   # 0
print(next(generador))   # 2
print(next(generador))   # 4
```

>[!IMPORTANT]
>Si tuvieras que procesar un millón de números, una lista los guardaría TODOS en memoria a la vez. Un generador los produce de uno en uno, gastando muchísima menos memoria. Por eso son tan útiles con grandes cantidades de datos.

<a name = "6-expresiones-generadoras"></a>

## 6. Expresiones generadoras

Son como una comprensión de listas pero con **paréntesis** en lugar de corchetes. Crean un generador (no calculan nada hasta que se recorre):

```python
# Comprensión de lista: crea la lista entera en memoria
lista = [n ** 2 for n in range(1000000)]   # ocupa mucho

# Expresión generadora: produce los valores uno a uno
generador = (n ** 2 for n in range(1000000))  # ocupa casi nada

# Muy útil combinada con funciones como sum()
suma = sum(n ** 2 for n in range(1, 6))
print(suma)   # 55
```

<a name = "7-cuándo-usar-cada-cosa"></a>

## 7. ¿Cuándo usar cada cosa?

- **Comprensión de listas** → cuando quieres crear una lista a partir de otra de forma corta y necesitas tenerla entera (para recorrerla varias veces, ordenarla, etc.).
- **Generador / expresión generadora** → cuando vas a recorrer los datos **una sola vez** o cuando son **muchísimos** y no quieres llenar la memoria.

>[!NOTE]
>No fuerces las comprensiones: si la lógica es complicada (varios `if`, varios `for` anidados), a veces un bucle `for` normal se lee mucho mejor. La legibilidad es lo primero.

<a name = "8-ejercicios"></a>

## 8. Ejercicios

1. Usa una comprensión de listas para crear una lista con los números del 1 al 20.

2. Usa una comprensión de listas para obtener una lista con el doble de cada número de `[1, 2, 3, 4, 5]`.

3. Dada la lista `["Hola", "Mundo", "Python"]`, crea con una comprensión otra lista con la longitud de cada palabra.

4. Usa una comprensión con condición para obtener solo los números **múltiplos de 3** del 1 al 30.

5. Dada la lista `[12, 7, 25, 4, 18, 9, 30]`, crea con una comprensión una lista que ponga `"alto"` si el número es mayor que 15 y `"bajo"` en caso contrario.

6. Crea con una comprensión de diccionario un diccionario que asocie cada número del 1 al 5 con su cubo (número elevado a 3).

7. Escribe un generador `pares_hasta(n)` que vaya entregando los números pares desde 0 hasta `n` usando `yield`. Recórrelo con un `for`.

8. Escribe un generador `fibonacci(cantidad)` que entregue los primeros `cantidad` números de la sucesión de Fibonacci (cada número es la suma de los dos anteriores: 0, 1, 1, 2, 3, 5, 8...).

> [!NOTE]
> Pistas para los ejercicios:
> - Estructura básica: `[expresión for elemento in iterable]`.
> - Para filtrar: `[x for x in lista if condición]`.
> - Para elegir un valor u otro: `[a if condición else b for x in lista]`.
> - Diccionario: `{clave: valor for elemento in iterable}`.
> - Un generador es una función normal que usa `yield` en vez de `return`.
> - Para Fibonacci puedes ir guardando los dos últimos: `a, b = 0, 1` y luego `a, b = b, a + b`.

<h3 align = "center">
¡Ya escribes Python idiomático! Estás muy cerca del proyecto final. Antes, un día imprescindible para cualquier proyecto real: los entornos virtuales y la gestión de paquetes.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/17_Ficheros/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/19_Entornos_Virtuales/readme.md">Día siguiente</a>
</h4>
