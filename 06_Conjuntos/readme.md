<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/05_Tuplas/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/07_Diccionarios/readme.md">Siguiente Capítulo</a>
</h4>


<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/sets.png">
</h1>

<h1 align="center">Diccionarios</h1><br>

<h4>Índice</h4>

- [1. Descripción.](#1-descripción)
- [2. Creando un conjuntos.](#2-creando-un-conjuntos)
- [3. Obtener la longitud del conjunto](#3-obtener-la-longitud-del-conjunto)
- [4. Acceder a los elementos de un conjunto](#4-acceder-a-los-elementos-de-un-conjunto)
- [5. Comprobar un elemento](#5-comprobar-un-elemento)
- [6. Agregar elementos a un conjunto.](#6-agregar-elementos-a-un-conjunto)
- [7. Eliminar elementos de un conjunto.](#7-eliminar-elementos-de-un-conjunto)
  - [7.1 Limpiar un conjunto](#71-limpiar-un-conjunto)
  - [7.2 Eliminar un conjunto](#72-eliminar-un-conjunto)
- [8. Convertir una lista en un conjunto](#8-convertir-una-lista-en-un-conjunto)
- [9. Conjuntos de unión](#9-conjuntos-de-unión)
- [10. Encontrar elementos compartidos en conjuntos.](#10-encontrar-elementos-compartidos-en-conjuntos)
- [11. Subconjuntos y Superconjuntos.](#11-subconjuntos-y-superconjuntos)
- [12. Diferencia entre dos conjuntos.](#12-diferencia-entre-dos-conjuntos)
  - [12.1 Diferencia Simétrica de conjuntos.](#121-diferencia-simétrica-de-conjuntos)
- [13. Conjuntos de unión](#13-conjuntos-de-unión)
- [A tener en cuenta en los conjuntos.](#a-tener-en-cuenta-en-los-conjuntos)
- [14. Ejercicios](#14-ejercicios)


## 1. Descripción.

Un Conjunto o Sets en python es una estructura de datos fundamental, una colección de datos desordenada, mutable y no indexada de elementos únicos _(Sin duplicados)_

<a name ="2-creando-un-conjunto"></a>

## 2. Creando un conjuntos.

Para crear un conjunto tenemos dos formas diferentes declarándolo con **set()** creando un conjunto varcio o con las llaves **{ }** para que tenga elementos iniciales, ejemplo.
```python
# Sintaxis
set_1 = set()
set_2 = {"elemnto_1", "elemento_2", "elemento_3"}
# Ejemplo
alumnos = set() # Sin elementos iniciales
alumnos = {"Pedro", "Jose", "Juan", "Alfonso"}
alumnas = {"Ana", "Tamara", "Elvira", "Marta"}
```

<a name ="3-obtener-la-longitud-del-conjunto"></a>

## 3. Obtener la longitud del conjunto

Al igual que en las listas y las tuplas, usamos el método _len()_, ejemplo.
```python
#Sintaxis
set_1 = {"elemento_1","elemento_2","elemento_3"}
print(len(set_1))
# Ejemplo
alumnos = {"Pedro", "Jose", "Juan", "Alfonso"}
alumnas = {"Ana","Elvira", "Marta"}
print(len(alumnos))
print(len(alumnas))
```

<a name ="4-Acceder-a-los-elementos-de-un-conjunto"></a>

## 4. Acceder a los elementos de un conjunto

Para acceder a los elementos de un conjunto usamos los bucles que los veremos en temas posteriores, ¡Aguanta! todo llega.

<a name = "5-comprobar-un-elemento"></a>

## 5. Comprobar un elemento

Si queremos comprobar si un elemento está contenido en un conjunto ya sabemos como hacerlo, con el operador **in** que nos devolverá un booleano, ejemplo.
```python
# Sintaxis
st = {"elemento_1","elemento_2","elemento_3"}
print("elemento_1" in st) #True
# Ejemplo
alumnos = {"Pedro", "Marta", "Alfonso"}
print("Alfonso" in alumnos) # True
print("Ana" in alumnos) # False
```

<a name = "6-agregar-elementos-a-un-conjunto"></a>

## 6. Agregar elementos a un conjunto.

Los sets no permiten cambiar elementos pero si podemos agregar nuevos elementos a el, siempre y cuando sean elementos inmutables (Las listas no podrían añadirse), vamos a ver dos formas de agregar elementos a un set.

- Primera forma, con el elemento add(), ejemplo
```python
# Sintaxis
st = {"elemento_1", "elemento_2"}
st.add("elemento_3")
# Ejemplo
alumnos = {"Noe","Amelia","Jack"}
alumnos.add("Sergio") 
print(alumnos)# {'Jack', 'Sergio', 'Amelia', 'Noe'} como podemos ver no mantiene el orden,
#Si lo ejecutas varias veces variará el orden.
```

- Segunda forma, esta forma es para agregar varios elementos al conjunto, se usa la función update(), está función toma como argumento una lista, ejemplo.
```python
# Sintaxis
st = {"elemento_1", "elemento_2", "elemento_3"}
st.update(["elemento_4", "elemento_5", "elemento_6"])
# Ejemplo
alumnos = {"Marta", "Luis"}
alumnos.update(["Pedro", "Mario", "Vero"])
print(alumnos)
```

<a name ="7-eliminar-elementos-de-un-conjunto"></a>

## 7. Eliminar elementos de un conjunto.

Para eliminar un elemento de un conjunto usamos el método _remove()_, sin embargo si no encuentra el elemento generará un error. por el contrario si usamos _discard()_ no genera error.
```python
# Sintaxis
st = {"elemento_1", "elemento_2", "elemento_3"}
st.remove("elemento_2") # eliminar el elemento_2
# st.remove("element_4") genera error y el programa no continua
st.discard("elemento_4") # no genera error el programa continua
st.discard("elemento_1") # elimina al elemento_1
print(st)
# Ejemplo 
alumnos = {"Sergi", "Marc", "Josep"}
alumnas = {"Carla", "Tania", "Esga"}
alumnos.remove("Sergi")
alumnas.discard("Susana") # No genera error continua
alumnas.discard("Carla")
print(alumnos)
print(alumnas)
```

- El método _pop()_ elimina un elemento aleatorio de un conjunto y devuelve el elemento eliminado, ejemplo.
```python
# Sintaxis
st = {"elemento_1", "elemento_2"}
st.pop() # elimina elemento aleatorio
# Ejemplo
alumnos = {"Pepe", "Marcos", "Ana", "Marta"}
alumno_eliminado = alumnos.pop()
print(alumno_eliminado) # imprime el alumno eliminado
print(alumnos) # imprime el set sin el alumno eliminado en el paso anterior
```

<a name = "71-limbiar-un-conjunto"></a>

### 7.1 Limpiar un conjunto

Podemos limpar el conjunto sin borrarlo completamente usando el método _clear()_
```python
# Sintaxis
st = {"elemento_1","elemento_2","elemento_3"}
st.clear()
# Ejemplo
alumnos = {"Pepe", "Gustavo", "Joaquin"}
alumnos.clear()
print(alumnos) # set()
```
<a name="72-eliminar-un-conjunto"></a>

### 7.2 Eliminar un conjunto

Si queremos eliminar un conjunto por completo, al igual que en listas y tuplas usamos el método _del()_, ejemplo
```python
# Sintaxis
st = {"elemento_1", "elemento_2"}
del st
# Ejemplo
alumnos = {"Juan", "Antonio", "Ana", "Carlos"}
del alumnos
print(alumnos) # Da error NameError: name 'alumnos' is not defined
```

<a name = "8-convertir-una-lista-en-un-conjunto"></a>

## 8. Convertir una lista en un conjunto

Podemos convertir listas en conjuntos y conjuntos en listas, pero hay que tener una cosa en cuenta al convertir las listas en conjuntos se eliminarán los duplicados y solo se guardarán los elementos únicos, ejemplo.
```python
# Sintaxis
lista = ["elemento_1", "elemento_2", "elemento_3", "elemento_1", "elemento_2"]
st = set(lista)
# Ejemplo
alumnos = ["Pedro", "Ana", "Jesus", "Pedro", "Jesus"]
alumnos = set(alumnos)
print(alumnos) # {'Ana', 'Jesus', 'Pedro'}
```

<a name = "9-conjuntos-de-unión">

## 9. Conjuntos de unión

Para unir dos conjuntos podemos usar los métodos _union()_ y _update()_, los cuales definimos a continuación.

- Utilizando el método **union()**
```python
# Sintaxis
st1 = {"elem_1", "elem_2", "elem_3"}
st2 = {"elem_4", "elem_5", "elem_6"}
st3 = st1.union(st2)
# Ejemplo
alumnos = {"Pedro", "Jesus", "Alvaro"}
alumnas = {"Ana", "Marta", "Silvia"}
todos_alumnos = alumnos.union(alumnas)
print(todos_alumnos) # {'Jesus', 'Ana', 'Pedro', 'Alvaro', 'Silvia', 'Marta'}
```

- El método **update()** añade un conjunto a otro.
```python
# Sintaxis
st1 = {"elem_1", "elem_2", "elem_3"}
st2 = {"elem_4", "elem_5", "elem_6"}
st1.update(st2)
# Ejemplo
alumnos = {"Santos", "Elvis"}
alumnas = {"Ana", "Carla"}
alumnos.update(alumnas)
print(alumnos) # {'Ana', 'Carla', 'Elvis', 'Santos'}
```

<a name = "10-encontrar-elementos-compartidos-en-conjuntos"></a>

## 10. Encontrar elementos compartidos en conjuntos.

el métoo _intersection()_ devuelve de entre dos conjuntos los elementos que comparten, podemos verlo mejor con un ejemplo.
```python
# Sintaxis
st_1 = {"elem_1", "elem_2", "elem_3", "elem_4"}
st_2 = {"elem_2", "elem_4"}
st_1.intersection(st_2) # si hacemos print(st_1.intersection(st_2)) devolverá {'elem_4', 'elem_2'}
# Ejemplo
python = {"p","y","t","h","o","n"}
dron = {"d","r","o","n"}
print(python.intersection(dron)) # {'n', 'o'}
```

<a name ="11-subconjuntos-y-superconjuntos"></a>

## 11. Subconjuntos y Superconjuntos.

Para que podamos entender los subconjuntos y los superconjuntos es más fácil con la definición de ambas.
- **Subconjunto**: Un conjunto A es subconjunto de B si todos los elementos de A están contenidos en B _issubset()_
- **Superconjunto**: Un conjunto B es superconjunto de A si contiene todos los elementos de A _issuperset()_

```python
# Sintaxis
st_1 = {"elem_1","elem_2","elem_3","elem_4"}
st_2 = {"elem_3","elem_4"}
st_2.issubset(st_1) # True
st_1.issuperset(st_2) # True
# Ejemplo
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
pares = {2, 4, 6, 8, 10}
numeros.issubset(pares) # False, ya que es un superconjunto de 
numeros.issuperset(pares) # True
pares.issubset(numeros) # True
```

<a name ="12-diferencia-entre-dos-conjuntos"></a>

## 12. Diferencia entre dos conjuntos.

Usando el método _difference()_ podemos comprobar los elementos diferentes que tienen dos conjuntos, ejemplo.
```python
# Sintaxis
st_1 = {"elemento_1", "element_2", "elemento_3", "elemento_4"}
st_2 = {"elemento_1", "elemento_3"}
st_2.difference(st_1) # set()
st_1.difference(st_2) # {"elemento_2", "elemento_4"}
# Ejemplo
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
pares = {2, 4, 6, 8, 10}
print(numeros.difference(pares)) # {1, 3, 5, 7, 9}
print(pares.difference(numeros)) # set()
###
python = {"p","y","t","h","o","n"}
dron = {"d","r","o","n"}
print(python.difference(dron)) # {'p', 't', 'y', 'h'}
print(dron.difference(python)) # {'d', 'r'}
```
<a name = "121-diferencia-simétrica-de-conjuntos"> </a>

### 12.1 Diferencia Simétrica de conjuntos.

La diferencia simétrica se diferencia y valga la redundancia de la diferencia que en este caso se incluyen los elementos de ambos conjuntos que no están en el otro conjunto y se usa el método _symmetric_difference()_, ejemplo.

```python
# Sintaxis
st_1 = {"elem_1", "elem_2", "eleme_3"}
st_2 = {"elem_0", "elem_2","elem_4"}
st_2.symmetric_difference(st_1) # {'elem_1', 'eleme_3', 'elem_4', 'elem_0'}
# Ejemplo
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
pares = {2, 4, 6, 8, 10, 12, 14, 16, 18}
print(pares.symmetric_difference(numeros)) # {1, 3, 5, 7, 9, 12, 14, 16, 18}
### 
python = {"p","y","t","h","o","n"}
dron = {"d","r","o","n"}
print(python.symmetric_difference(dron)) # {'y', 'd', 'r', 't', 'p', 'h'}
print(dron.symmetric_difference(python)) # {'y', 'p', 't', 'd', 'r', 'h'}
```



<a name = "13-conjuntos-de-unión"></a>

## 13. Conjuntos de unión

Podemos comprobar si dos elementos no tienen ningún elemento en común con el método _isdisjoint()_ que nos devuelve un boolean si esos conjuntos no comparten ningún elemento.
```python
# Sintaxis
st_1 = {"elem_1", "elem_2", "elem_3"}
st_2 = {"elem_4", "elem_5"}
st_3 = {"elem_1", "elem_4"}
st_2.isdisjoint(st_1) # True st_1 y st_2 no comparten elementos
st_3.isdisjoint(st_1) # False st_1 y st_3 si comparten elem_1
st_3.isdisjoint(st_2) # False st_2 y st_3 si comparten elem_4
# Ejemplo.
pares = {0, 2, 4, 6, 8}
impares = {1, 3, 5, 7, 9}
numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.isdisjoint(pares)) # False
print(numeros.isdisjoint(impares)) # False
print(pares.isdisjoint(impares)) # True
```

<a name = "a-tener-en-cuenta-en-los-conjuntos"></a>

## A tener en cuenta en los conjuntos.

- Debemos tener en cuenta en los conjuntos que podemos usar los métodos anteriormente utilizados para el uso de la unión, de las diferencias y los conjuntos de unión pero también podemos usar símbolos matemáticos que nos ayudan a acortar código y que sea algo más legible.
  - Para la **Unión** podemos usar `|`
  - Para la **Intersección** podemos usar `&`
  - Para la **diferencia** podemos usar `-`
  - Para la **diferencia simétrica** podemos usar `^`
  - Como método **issubset()** usamos el operador `<=`
  - Como método **issuperset()** usamos el operador `>=`

A continuación os dejo un ejemplo con estas opciones.
```python
# Ejemplo
pares = {0, 2, 4, 6, 8}
impares = {1, 3, 5, 7, 9}
numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros_aleatorios = {0, 1, 4, 5, 8, 9}
print(pares | impares) # Union {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print (pares & numeros_aleatorios) # Interseccion {0, 8, 4}
print (impares - numeros_aleatorios) # diferencia {3, 7}
print (pares ^ numeros_aleatorios) # diferencia simétrica {1, 2, 5, 6, 9}
print (pares <= impares) # False
print (pares <= numeros) # True
print (impares >= pares) # False
print (impares >= numeros) # True
```

😊 ¡Estupendo! Ya has llegado al final de los sets (Conjuntos), vamos a probar lo aprendido con unos ejercicios.


<a name = "14-ejercicios" ></a>

## 14. Ejercicios

```python
#sets 
companias = {"Mercadona", "Lidl", "Alcampo", "Carrefour", "Mediamarkt", "PcComponentes"}
num_A = {19, 20, 21, 22, 26, 27, 28, 29, 30}
num_B = {19, 20, 23, 24, 25, 29, 30, 31, 32}
edad = [21, 23, 30, 31, 25, 22, 21, 26, 30, 22, 19, 27, 23]
```

- Imprime por pantalla la longitud de `companias`
- Añade `Aldi`a companias
- Añade a la vez estas compañias a companias `Decathlon, Microsoft, Apple`
- Elimina una empresa de companias
- Une `num_A y num_B`
- Encuentra la diferencia entre `num_A y num_B`
- ¿num_A es un subconjunto de num_B?
- ¿Son num_A y num_B conjuntos distintos?
- Haz la diferencia entre `num_B y num_A`
- Haz la diferencia simétrica de `num_A y num_B`
- Elimina el conjunto companias por completo.
- convierte edad a un conjunto y compara la longitud, ¿Cúal es más grande?


<h3>
Ya estás preparado para el siguiente tema, vas por buen camino.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/05_Tuplas/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/07_Diccionarios/readme.md">Siguiente Capítulo</a>
</h4>