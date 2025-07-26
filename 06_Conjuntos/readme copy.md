<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/04_Listas/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/06_Conjuntos/readme.md">Siguiente Capítulo</a>
</h4>


<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/tuplas.png">
</h1>

<h1 align="center">Tuplas</h1><br>

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