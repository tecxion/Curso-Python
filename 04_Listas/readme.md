<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/03_Cadenas/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/05_Tuplas/readme.md">Siguiente Capítulo</a>
</h4>


<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/listas.png">
</h1>

# Listas

## Indice del capítulo.

- [1. Definición](#1-definición)
- [2. Creación de una lista](#2-creacion)
- [3. Acceso a una lista](#3-acceso)
    - [3.1 Indexación positiva]()
    - [3.2 Indexación negativa]()
- [4. Desempaquetado de una lista](#4-desempaquetado)
- [5. Cortar elementos de una lista](#5-slice)

 
<a name="1-definición"></a>

## 1. Definición

En python hay cuatro tipos de datos de colección: tuplas, listas, diccionarios y conjuntos.
- La Lista es una colección ordenada y que puede ser modificable, a su vez permite miembros duplicados.
- La Tupla es una colección ordenada y que no puede ser modificable, a su vez permite miembros duplicados.
- El Diccionario es una colección desordenada, no indexada y modificable, no permite miembros duplicados.
- El Conjunto es una colección desordenada, no indexada, no modificable, pero se pueden añadir nuevos elementos duplicados.

Por lo tanto en el presente capítulo hablaremos de las listas, colección de diferentes tipos de datos, ordenada y modificable. Puede contener elementos de diferentes tipos y además puede estar vacia.


<a name="2-creacion"></a>

## 2. Creación de una lista

En Python podemos crear listas de dos formas: 
- Usando la función `list()`
- Usando corchetes `[]`
```python
lst = list()
lista = [] # En este caso son dos listas vacias
```

>[!NOTE]
>Si queremos saber la longitud de una lista podemos usar la función `len()`.
```python
alumnos = ["Juan", "Pedro", "Maria", "Ana"]
asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Geografia", "Ingles"]
print("Alumnos: ", alumnos)
print(len(alumnos)) # 4
print("Asignaturas: ", asignaturas)
print(len(asignaturas)) # 6

```

- Las listas pueden contener elementos de diferentes tipos de datos.
```python
lista = [1, "Pepe", 3.14, True, {"Pais":"España", "Ciudad":"Madrid"}]
print(lista)
```
<a name="3-acceso"></a>

## 3. Acceso a elementos de una lista

- Al igual que en los String podiamos acceder a los elementos que formaban el string, en una lista también podemos acceder a sus elementos mediante indexación positiva o negativa.

### 3.1 Indexación positiva
- Accedemos a los elementos mediante su índice positivo comenzando por 0. Usando el ejemplo anterior.

| Índice | Elemento |
| --- | --- |
| 0 | 1 |
| 1 | "Pepe" |
| 2 | 3.14 |
| 3 | True |
| 4 | {"Pais":"España", "Ciudad":"Madrid"} |

```python
lista = [1, "Pepe", 3.14, True, {"Pais":"España", "Ciudad":"Madrid"}]
print(lista[0]) # 1
print(lista[1]) # "Pepe"
print(lista[2]) # 3.14
print(lista[3]) # True
print(lista[4]) # {"Pais":"España", "Ciudad":"Madrid"} También podriamos acceder al diccionario.
print(lista[4]["Pais"])
print(lista[4]["Ciudad"]) # Madrid
```

### 3.2 Indexación negativa
- Accedemos a los elementos mediante su índice negativo comenzando por -1. Usando el ejemplo anterior.
| Índice | Elemento |
| --- | --- |
| -1 | {"Pais":"España", "Ciudad":"Madrid"} |
| -2 | True |
| -3 | 3.14 |
| -4 | "Pepe" |
| -5 | 1 |

```python
lista = [1, "Pepe", 3.14, True, {"Pais":"España", "Ciudad":"Madrid"}]
print(lista[-1]) # {"Pais":"España", "Ciudad":"Madrid"}
print(lista[-2]) # True
print(lista[-3]) # 3.14
print(lista[-4]) # "Pepe"
print(lista[-5]) # 1
```

<a name="4-desempaquetado"></a>

## 4. Desempaquetado de una lista (list unpacking)
- Es posible desempaquetar una lista en varias variables, es decir, asignar los valores de una lista a varias variables, esta herramienta es muy útil cuando queremos almacenar en una variable los valores de una lista.
```python
lista = [1, "Pepe", 3.14, True, {"Pais":"España", "Ciudad":"Madrid"}, 8,75]
a, b, c, d, *rest = lista
print(a) # 1
print(b) # "Pepe"
print(c) # 3.14
print(d) # True
print(rest) # [{"Pais":"España", "Ciudad":"Madrid"}, 8,75]
```
- Otro ejemplo:
```python
paises = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','España']
gr, fr, bg, sw, *scandic, es = paises
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic) # ['Denmark', 'Finland', 'Norway', 'Iceland']
print(es)
```

<a name="5-slice"></a>

## 5. Cortar elementos de una lista