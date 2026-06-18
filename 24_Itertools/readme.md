<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/23_Decoradores_Avanzados/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/25_Context_Managers/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/itertools.png">
</h1>


<h1 align="center">Itertools y Herramientas Funcionales</h1><br>

<h3>Índice</h3>

- [1. ¿Qué es itertools?](#1-qué-es-itertools)
- [2. Iteradores infinitos: count, cycle y repeat](#2-iteradores-infinitos-count-cycle-y-repeat)
- [3. Combinar iterables: chain y zip_longest](#3-combinar-iterables-chain-y-zip_longest)
- [4. Agrupar y acumular: groupby y accumulate](#4-agrupar-y-acumular-groupby-y-accumulate)
- [5. Combinatoria: product, permutations y combinations](#5-combinatoria-product-permutations-y-combinations)
- [6. Cortar iterables: islice](#6-cortar-iterables-islice)
- [7. Funciones útiles: enumerate, zip y any/all](#7-funciones-útiles-enumerate-zip-y-anyall)
- [8. Ejercicios](#8-ejercicios)

<a name = "1-qué-es-itertools"></a>

## 1. ¿Qué es itertools?

En el día 18 viste los iteradores y generadores. **`itertools`** es un módulo de la librería estándar lleno de funciones que crean y combinan iteradores de forma **muy eficiente** (gastan poca memoria, porque producen los valores uno a uno).

```python
import itertools
```

Son herramientas que resuelven en una línea cosas que de otra forma requerirían bucles enredados. Vamos a ver las más útiles.

<a name = "2-iteradores-infinitos-count-cycle-y-repeat"></a>

## 2. Iteradores infinitos: count, cycle y repeat

Estas tres funciones generan secuencias **infinitas**, así que hay que cortarlas (con un `break`, un `if`, o `islice`):

```python
import itertools

# count: cuenta desde un número, de forma infinita
for numero in itertools.count(10, 2):   # empieza en 10, salta de 2 en 2
    if numero > 20:
        break
    print(numero)   # 10, 12, 14, 16, 18, 20

# cycle: repite una secuencia sin fin
contador = 0
for color in itertools.cycle(["rojo", "verde", "azul"]):
    print(color)
    contador += 1
    if contador == 5:
        break
# rojo, verde, azul, rojo, verde

# repeat: repite un valor (n veces o infinito)
print(list(itertools.repeat("hola", 3)))   # ['hola', 'hola', 'hola']
```

<a name = "3-combinar-iterables-chain-y-zip_longest"></a>

## 3. Combinar iterables: chain y zip_longest

```python
import itertools

# chain: une varios iterables en uno solo
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(list(itertools.chain(lista1, lista2)))   # [1, 2, 3, 4, 5, 6]

# zip_longest: como zip, pero no se detiene en el más corto
nombres = ["Ana", "Luis", "Marta"]
edades = [30, 25]
print(list(itertools.zip_longest(nombres, edades, fillvalue="?")))
# [('Ana', 30), ('Luis', 25), ('Marta', '?')]
```

>[!NOTE]
>El `zip` normal (que verás en la sección 7) se detiene en cuanto se acaba la lista más corta. `zip_longest` sigue hasta la más larga, rellenando los huecos con `fillvalue`.

<a name = "4-agrupar-y-acumular-groupby-y-accumulate"></a>

## 4. Agrupar y acumular: groupby y accumulate

```python
import itertools

# accumulate: sumas (o la operación que indiques) acumuladas
numeros = [1, 2, 3, 4, 5]
print(list(itertools.accumulate(numeros)))   # [1, 3, 6, 10, 15]

# groupby: agrupa elementos CONSECUTIVOS iguales
letras = "aaabbbccd"
for letra, grupo in itertools.groupby(letras):
    print(letra, len(list(grupo)))
# a 3
# b 3
# c 2
# d 1
```

>[!IMPORTANT]
>`groupby` solo agrupa elementos que están **seguidos**. Si quieres agrupar todos los iguales aunque estén desordenados, primero ordena con `sorted()`.

<a name = "5-combinatoria-product-permutations-y-combinations"></a>

## 5. Combinatoria: product, permutations y combinations

Estas tres son oro puro cuando necesitas generar combinaciones:

```python
import itertools

# product: producto cartesiano (todas las parejas posibles)
colores = ["rojo", "azul"]
tallas = ["S", "M", "L"]
print(list(itertools.product(colores, tallas)))
# [('rojo', 'S'), ('rojo', 'M'), ('rojo', 'L'), ('azul', 'S'), ('azul', 'M'), ('azul', 'L')]

# permutations: todas las ordenaciones posibles (importa el orden)
print(list(itertools.permutations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# combinations: grupos sin importar el orden
print(list(itertools.combinations(["A", "B", "C"], 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]
```

<a name = "6-cortar-iterables-islice"></a>

## 6. Cortar iterables: islice

Con las listas usabas el *slicing* (`lista[2:5]`). Pero un iterador o un generador **no** se puede cortar así. Para eso está **`islice`**:

```python
import itertools

# Tomar los primeros 5 números de un generador infinito
primeros_cinco = itertools.islice(itertools.count(1), 5)
print(list(primeros_cinco))   # [1, 2, 3, 4, 5]

# Tomar del 2º al 5º elemento (índices 2 a 5)
letras = "abcdefgh"
print(list(itertools.islice(letras, 2, 5)))   # ['c', 'd', 'e']
```

<a name = "7-funciones-útiles-enumerate-zip-y-anyall"></a>

## 7. Funciones útiles: enumerate, zip y any/all

Aunque no están en `itertools`, estas funciones integradas trabajan con iterables y las usarás constantemente:

```python
# enumerate: recorre dando el índice y el valor a la vez
for indice, nombre in enumerate(["Ana", "Luis"], start=1):
    print(indice, nombre)   # 1 Ana / 2 Luis

# zip: empareja varios iterables
nombres = ["Ana", "Luis"]
notas = [9, 7]
for nombre, nota in zip(nombres, notas):
    print(f"{nombre}: {nota}")

# any / all: ¿alguno / todos cumplen?
numeros = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in numeros))   # True  (todos pares)
print(any(n > 5 for n in numeros))         # True  (alguno > 5)
```

<a name = "8-ejercicios"></a>

## 8. Ejercicios

1. Usa `itertools.chain` para unir las listas `[1, 2]`, `[3, 4]` y `[5, 6]` en una sola.

2. Usa `itertools.count` para imprimir los números del 0 al 10 de 2 en 2 (córtalo con un `break`).

3. Usa `itertools.accumulate` para obtener las sumas acumuladas de `[10, 20, 30, 40]`.

4. Usa `itertools.product` para generar todas las combinaciones de lanzar dos dados (números del 1 al 6).

5. Usa `itertools.combinations` para mostrar todas las parejas posibles de los amigos `["Ana", "Luis", "Marta", "Pedro"]`.

6. Usa `itertools.islice` para obtener los primeros 7 números pares (a partir de un `count`).

7. Usa `enumerate` para imprimir una lista de la compra numerada empezando en 1.

8. Usa `all` y `any` para comprobar, en la lista `[15, 22, 8, 19]`, si todos son mayores que 5 y si alguno es mayor que 20.

> [!NOTE]
> Pistas para los ejercicios:
> - Casi todo en `itertools` devuelve un iterador: envuélvelo en `list(...)` para verlo.
> - Cuidado con los infinitos (`count`, `cycle`): siempre necesitan un `break` o un `islice`.
> - Para dos dados: `itertools.product(range(1, 7), repeat=2)`.
> - `combinations(lista, 2)` te da las parejas sin repetir.
> - `all(condición for x in lista)` y `any(...)` se combinan genial con comprensiones.

<h3 align = "center">
¡Ya manejas los iterables como un profesional! Mañana, una herramienta elegante para gestionar recursos: los context managers.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/23_Decoradores_Avanzados/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/25_Context_Managers/readme.md">Día siguiente</a>
</h4>
