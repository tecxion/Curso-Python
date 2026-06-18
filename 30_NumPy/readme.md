<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/29_Tests/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/31_Pandas/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/numpy.png">
</h1>


<h1 align="center">NumPy: cálculo numérico</h1><br>

<h3>Índice</h3>

- [1. ¿Qué es NumPy y por qué se usa?](#1-qué-es-numpy-y-por-qué-se-usa)
- [2. Instalación e importación](#2-instalación-e-importación)
- [3. Crear arrays](#3-crear-arrays)
- [4. Atributos de un array](#4-atributos-de-un-array)
- [5. Operaciones vectorizadas](#5-operaciones-vectorizadas)
- [6. Indexado y slicing](#6-indexado-y-slicing)
- [7. Máscaras booleanas](#7-máscaras-booleanas)
- [8. Funciones estadísticas y de agregación](#8-funciones-estadísticas-y-de-agregación)
- [9. Arrays de dos dimensiones](#9-arrays-de-dos-dimensiones)
- [10. Ejercicios](#10-ejercicios)

<a name = "1-qué-es-numpy-y-por-qué-se-usa"></a>

## 1. ¿Qué es NumPy y por qué se usa?

**NumPy** (*Numerical Python*) es la librería base del cálculo numérico y científico en Python. Es el cimiento sobre el que se construyen Pandas, Matplotlib, scikit-learn y casi todo el ecosistema de datos e inteligencia artificial. A partir de aquí entramos en el bloque **avanzado** del curso: la ciencia de datos.

Su pieza central es el **array** (`ndarray`): una estructura parecida a una lista, pero **mucho más rápida** y pensada para operar con miles o millones de números a la vez.

¿Por qué no usar listas normales? Por dos razones:
- **Velocidad**: NumPy está escrito en C por debajo y opera sobre bloques de memoria contigua.
- **Comodidad**: puedes sumar, multiplicar o aplicar funciones a **todo** el array de una vez, sin bucles.

```python
# Con una lista normal necesitarías un bucle
numeros = [1, 2, 3, 4]
dobles = [n * 2 for n in numeros]

# Con NumPy, directamente sobre todo el array
import numpy as np
numeros = np.array([1, 2, 3, 4])
dobles = numeros * 2     # array([2, 4, 6, 8])
```

<a name = "2-instalación-e-importación"></a>

## 2. Instalación e importación

NumPy es una librería externa (recuerda el día 19): se instala con `pip` dentro de tu entorno virtual:

```bash
pip install numpy
```

Por convención **universal**, se importa con el alias `np`:

```python
import numpy as np
```

<a name = "3-crear-arrays"></a>

## 3. Crear arrays

Hay muchas formas de crear arrays según lo que necesites:

```python
import numpy as np

# A partir de una lista
a = np.array([1, 2, 3, 4])

# Rango de números (como range, pero array)
b = np.arange(0, 10, 2)      # [0 2 4 6 8]

# N números repartidos entre dos valores
c = np.linspace(0, 1, 5)     # [0.   0.25 0.5  0.75 1.  ]

# Arrays llenos de ceros o unos
ceros = np.zeros(3)          # [0. 0. 0.]
unos = np.ones(3)            # [1. 1. 1.]

# Números aleatorios entre 0 y 1
aleatorios = np.random.rand(3)
```

<a name = "4-atributos-de-un-array"></a>

## 4. Atributos de un array

Cada array tiene atributos que describen su forma y contenido:

```python
import numpy as np

a = np.array([10, 20, 30, 40])
print(a.shape)   # (4,)     -> la forma (4 elementos)
print(a.size)    # 4        -> número total de elementos
print(a.ndim)    # 1        -> número de dimensiones
print(a.dtype)   # int64    -> tipo de los datos
```

<a name = "5-operaciones-vectorizadas"></a>

## 5. Operaciones vectorizadas

Esta es la magia de NumPy: las operaciones se aplican a **cada elemento** automáticamente (lo llamamos *vectorización*). Nada de bucles.

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)      # [11 22 33 44]
print(a * 2)      # [2 4 6 8]
print(a ** 2)     # [ 1  4  9 16]
print(b / a)      # [10. 10. 10. 10.]

# También funciones matemáticas sobre todo el array
print(np.sqrt(a))  # raíz cuadrada de cada elemento
```

<a name = "6-indexado-y-slicing"></a>

## 6. Indexado y slicing

Se accede igual que en las listas (día 4), con índices y rebanadas:

```python
import numpy as np

a = np.array([10, 20, 30, 40, 50])

print(a[0])      # 10  (primer elemento)
print(a[-1])     # 50  (último)
print(a[1:4])    # [20 30 40]  (del índice 1 al 3)
print(a[::2])    # [10 30 50]  (de dos en dos)
```

<a name = "7-máscaras-booleanas"></a>

## 7. Máscaras booleanas

Una de las herramientas más potentes: filtrar elementos con una **condición**. El array de `True/False` que genera la condición se usa para seleccionar:

```python
import numpy as np

a = np.array([15, 3, 22, 8, 30, 1])

print(a > 10)        # [ True False  True False  True False]

# Usamos la condición para FILTRAR
print(a[a > 10])     # [15 22 30]

# Modificar los que cumplen la condición
a[a < 10] = 0
print(a)             # [15  0 22  0 30  0]
```

<a name = "8-funciones-estadísticas-y-de-agregación"></a>

## 8. Funciones estadísticas y de agregación

NumPy resuelve estadística básica en una línea:

```python
import numpy as np

datos = np.array([4, 8, 15, 16, 23, 42])

print(datos.sum())     # 108  -> suma
print(datos.mean())    # 18.0 -> media
print(datos.max())     # 42   -> máximo
print(datos.min())     # 4    -> mínimo
print(datos.std())     # desviación estándar
print(np.median(datos))# 15.5 -> mediana
```

<a name = "9-arrays-de-dos-dimensiones"></a>

## 9. Arrays de dos dimensiones

Los arrays pueden tener varias dimensiones, como una **tabla** (matriz). Es la base de cómo se guardan imágenes, hojas de datos, etc:

```python
import numpy as np

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matriz.shape)     # (2, 3)  -> 2 filas, 3 columnas
print(matriz[0, 1])     # 2       -> fila 0, columna 1
print(matriz[1])        # [4 5 6] -> fila 1 entera
print(matriz.sum(axis=0))  # [5 7 9]   -> suma por columnas
print(matriz.sum(axis=1))  # [ 6 15]   -> suma por filas
```

<a name = "10-ejercicios"></a>

## 10. Ejercicios

Los ejercicios están en **tres niveles**. Empieza por el Nivel 1 y ve subiendo.

### Nivel 1 — Básico
1. Crea un array con los números del 1 al 10 y muéstralo.
2. Crea un array con los números pares del 0 al 20 usando `np.arange`.
3. Dado `np.array([5, 10, 15, 20])`, multiplica todos sus elementos por 3.
4. Crea un array de 5 ceros y otro de 5 unos.

### Nivel 2 — Aplicado
5. Dado `np.array([12, 7, 25, 4, 18, 9])`, calcula su suma, media, máximo y mínimo.
6. Del mismo array, usa una máscara booleana para obtener solo los valores mayores que 10.
7. Crea un array con 10 números aleatorios y cuenta cuántos son mayores que 0.5.
8. Tienes las temperaturas de una semana en grados Celsius: `[20, 22, 19, 24, 25, 23, 21]`. Conviértelas todas a Fahrenheit (F = C * 9/5 + 32) de una sola operación.

### Nivel 3 — Reto
9. Crea una matriz 3x3 con los números del 1 al 9 y calcula la suma de cada fila y de cada columna.
10. Tienes las notas de 4 alumnos en 3 exámenes (una matriz 4x3). Calcula la nota media de cada alumno (media por filas) y la media de cada examen (media por columnas).
11. Genera 1000 números aleatorios y calcula qué porcentaje cae por debajo de 0.5 (debería acercarse al 50%).

> [!NOTE]
> Pistas:
> - `import numpy as np` siempre al principio.
> - Para filtrar: `array[array > valor]`.
> - Para medias por fila/columna usa `.mean(axis=1)` y `.mean(axis=0)`.
> - Una matriz se crea pasando una lista de listas a `np.array(...)`.
> - Para contar cuántos cumplen una condición: `(array > 0.5).sum()`.

<h3 align = "center">
¡Has entrado en la ciencia de datos! NumPy es el motor; mañana montamos encima la herramienta estrella para analizar datos: Pandas.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/29_Tests/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/31_Pandas/readme.md">Día siguiente</a>
</h4>
