<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/10_Funciones/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/11_Listas_2/readme.md">Siguiente Capítulo</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/modulos.png">
</h1>


<h1 align="center">Comprensión de Listas</h1><br>

<h3>Índice</h3>

- [1. Comprensión de Listas (List Comprehensions)](#1-comprensión-de-listas-list-comprehensions)
- [2. Función Lambda](#2-función-lambda)
  - [2.1 Creación de una función Lambda](#21-creación-de-una-función-lambda)
  - [2.2 Función Lambda dentro de otra función](#22-función-lambda-dentro-de-otra-función)
- [3. Ejercicios.](#3-ejercicios)



<a name = "1-comprensión-de-listas-list-comprehensions"></a>

## 1. Comprensión de Listas (List Comprehensions)

La comprensión de listas es una forma concisa y eficiente de crear listas en Python, combinando bucles y condicionales en una sola línea. Es una de las características más elegantes y poderosas del lenguaje.
```python
# Sintaxis
[expresion for elemento in iterable]
# expresion: Operación a realizar con cada elemento.
# elemento: Variable temporal que toma cada valor del iterable.
# iterable: Secuencia (lista, tupla, rango, etc) que se recorre.
# Ejempl, crear una lista de cuadrados.
# Forma tradicional
cuadrados = []
for x in range(5):
    cuadrados.append(x ** 2)
# Con comprensión de listas
cuadrados = [x ** 2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Otro ejemplo.
lenguaje = "Python"
# Tradicional.
lista = list(lenguaje)
print(lista) # ["P","y","t","h","o","n"]
# Con list Comprehension
lista = [i for i in lenguaje]
print(lista) # ["P","y","t","h","o","n"]
```

- La comprensión de listas se puede combinar con la expresión if, veamos un ejemplo.
```python
# Sintaxis
[expresion for elemento in iterable if condicion]
# Ejemplo.
pares = [n for n in range (30) if n % 2 == 0]
print(pares) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
impares = [n for n in range(23) if n % 2 != 0]
print(impares)
numeros = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
positivos = [n for n in numeros if n > 0]
print(positivos)
negativos = [n for n in numeros if n < 0]
print(negativos)

```

- Comprensión de listas anidadas.

Esto es útil para trabajar con matrices o listas de listas, ejemplo.
```python
# Aplanar una matriz
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplanada = [num for fila in matriz for num in fila] # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Producto Cartesiono
A = [1, 2]
B = ['a', 'b']
producto = [(a, b) for a in A for b in B] # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```

<a name = "2-función-lambda"></a>

## 2. Función Lambda

Las funciones lambda (también llamadas funciones anónimas) pueden combinarse con comprensión de listas para crear operaciones más dinámicas y flexibles.
```python
# Sintaxis
lambda argumentos: expresion
```
- No tiene nombre (por eso es "anónima").
- Solo puede contener una expresión (no múltiples líneas de código).
- Útil para operaciones rápidas donde no necesitas definir una función con def.

<a name = "21-creación-de-una-función-lambda"></a>

### 2.1 Creación de una función Lambda

Para crear una función lambda, usamos la palabra clave lambda seguida de uno o más parámetros y, a continuación, de una expresión.
La función lambda no utiliza el método de retorno, sino que devuelve explícitamente la expresión.

<a name = "22-función-lambda-dentro-de-otra-función"></a>

### 2.2 Función Lambda dentro de otra función


<a name = "3-ejercicios" ></a>

## 3. Ejercicios.



































<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/10_Funciones/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/11_Listas_2/readme.md">Siguiente Capítulo</a>
</h4>