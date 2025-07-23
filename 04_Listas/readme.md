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
    - [3.1 Indexación positiva](#indexacion-positiva)
    - [3.2 Indexación negativa](#indexacion-negativa)
- [4. Desempaquetado de una lista](#4-desempaquetado)
- [5. Cortar elementos de una lista](#5-slice)
    - [5.2 Mediante indexación positiva](#positiva)
    - [5.2 Mediante indexación negativa](#negativa)
- [6. Modificación de una lista](#6-modificacion)
- [7. Comprobar elementos de una lista](#7-comprobacion)
- [8. Agregar elementos a una lista](#8-agregar)
- [9. Eliminar elementos de una lista](#9-eliminar)
- [10. Copiar una lista](#10-copiar)
- [11. Unir listas](#11-unir-listas)
- [12. Contar elementos de una lista](#12-Contar)
- [13. Encontrar elementos de una lista](#13-encontrar-indice)
- [14. Invertir una lista](#14-invertir-lista)
- [15. Ordenar elementos de una lista](15-ordenar)
- [16. Ejercicios de repaso](#16-ejercicios)

 
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

<a name="indexacion-positiva"></a>

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
<a name = "indexacion-negativa"></a>

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

Mediante la indexación positiva o negativa,podemos realizar "cortes" en las listas es decir obtener los datos que nosotros queremos dentro de la lista según el orden de la misma.

<a name ="positiva"></a>

### 5.1 Cortar elementos mediante la indexación positiva

```python
alumnos = ['Juan', 'Pepe', 'Maria', 'Ana', 'Luis', 'Sara', 'Jose', 'Luisa', 'Carlos', 'Luis']
todos_alumnos = alumnos[0:10]
todos_alumnos2 = alumnos[0:]
print(todos_alumnos) # ['Juan', 'Pepe', 'Maria', 'Ana', 'Luis', 'Sara', 'Jose', 'Luisa', 'Carlos', 'Luis']
print(todos_alumnos2) # ['Juan', 'Pepe', 'Maria', 'Ana', 'Luis', 'Sara', 'Jose', 'Luisa', 'Carlos', 'Luis']
pepe_maria_ana = alumnos[1:4]
print(pepe_maria_ana) # ['Pepe', 'Maria', 'Ana']
sara_jose_luisa = alumnos[5:8]
print(sara_jose_luisa)
```

>[!NOTE]
>Si añadimos un tercer parámetro a la indexación, este nos permitirá indicar el número de elementos que queremos que nos devuelva la lista, por ejemplo: alumnos[1:4:2] nos devolverá la lista con los elementos de la posición 1, 3 y 5.

```python
alumnos = ['Juan', 'Pepe', 'Maria', 'Ana', 'Luis', 'Sara', 'Jose', 'Luisa', 'Carlos', 'Luis']
pepe_maria_ana = alumnos[1:4:2]
print(pepe_maria_ana) # ['Pepe', 'Ana']
saltos_de_dos = alumnos[1:10:2]
print(saltos_de_dos) # ['Pepe', 'Ana', 'Sara', 'Luisa', 'Luis']
saltos_de_tres = alumnos[0:10:3]
print(saltos_de_tres) # ['Juan', 'Ana', 'Jose', 'Luis']
```

<a name ="negativa"></a>

### 5.2 Cortar elementos mediante la indexación negativa
Al igual que en la indexación negativa, para cortar la cadena usaremos índices negativos.
```python
alumnos = ['Juan', 'Pepe', 'Maria', 'Ana', 'Luis', 'Sara', 'Jose', 'Luisa', 'Carlos', 'Luis']
todos_alumnos = alumnos[-10:]
print(todos_alumnos) # ['Juan', 'Pepe', 'Maria', 'Ana', 'Luis', 'Sara', 'Jose', 'Luisa', 'Carlos', 'Luis']
pepe_maria_ana = alumnos[-5:-2]
print(pepe_maria_ana) # ['Sara', 'Jose', 'Luisa']
sara_jose_luisa = alumnos[-6:-3]
print(sara_jose_luisa) # ['Luis', 'Sara', 'Jose']
```
<a name="6-modificacion"></a>

### 6. Modificación de una lista
Para modificar una lista es tan simple como asignarle un nuevo valor a la posición que queramos, por ejemplo:
```python
alumnos = ['Juan', 'Pepe', 'Maria', 'Ana', 'Luis', 'Sara', 'Jose', 'Luisa', 'Carlos', 'Luis']
alumnos[0] = 'Juan Carlos'
print(alumnos) # ['Juan Carlos', 'Pepe', 'Maria', 'Ana', 'Luis', 'Sara', 'Jose', 'Luisa', 'Carlos', 'Luis']
alumnos[-5] = 'Elena'
print(alumnos) # ['Juan Carlos', 'Pepe', 'Maria', 'Ana', 'Elena', 'Jose', 'Luisa', 'Carlos', 'Luis']
```

>[!NOTE]
>Como podemos ver se puede modificar los elementos de una lista por indexación positiva y negativa, solo debemos saber que elemento queremos modificar.

<a name="7-comprobacion"></a>

### 7. Comprobación de elementos en una lista
Para comprobar si un elemento se encuentra en una lista, utilizaremos el operador in, por ejemplo:
```python
alumnos = ['Juan', 'Pepe', 'Maria', 'Ana', 'Luis', 'Sara', 'Jose', 'Luisa', 'Carlos', 'Luis']
print('Juan' in alumnos) # True
print('Juan Carlos' in alumnos) # False
```

<a name="8-agregar"></a>

### 8. Agregar elementos a una lista

- Para agregar elementos al final de una lista, utilizaremos el método append, por ejemplo:

```python
# Sintaxis
lista = list()
lista.append(item)
# Ejemplo
alumnos = ['pedro', 'juan', 'pepe', 'maria', 'ana']
alumnos.append('luis')
print(alumnos) # ['pedro', 'juan', 'pepe', 'maria', 'ana', 'luis']
```

- Para agregar elementos a una lista en una posición determinada, utilizaremos el método insert, por ejemplo:
```python
# Sintaxis
lista = list()
lista.insert(index, item)
# Ejemplo
alumnos = ["pedro","Juan","pepe","maria","ana"]
alumnos.insert(2,"luis")
print(alumnos) # ['pedro', 'Juan', 'luis', 'pepe', 'maria', 'ana']
```

<a name="9-eliminar"></a>

### 9. Eliminar elementos de una lista

El método remove(), elimina el primer elemento de la lista que coincida con el elemento indicado, por ejemplo:
```python
# Sintaxis
lista = list()
lista.remove(item)
# Ejemplo
alumnos = ['juan', 'pedro', 'pepe', 'maria', 'ana']
alumnos.remove('juan')
print(alumnos) # ['pedro', 'pepe', 'maria', 'ana']
```

- El método pop() elimina el indice especificado (o el último elento si no especifica el índice), por ejemplo:
```python
# Sintaxis
lista = ["elemento_1", "elemento_2", "elemento_3"]
lista.pop() # el último elemento, ["elemento_1", "elemento_2"]
lista.pop(0) # el elemento con índice 0, ["elemento_2", "elemento_3"]
```
- El método clear() elimina todos los elementos de una lista, por ejemplo:
```python
# Sintaxis
lista = ["elemento_1", "elemento_2", "elemento_3"]
lista.clear() # []
```
- El método del() elimina una lista, por ejemplo:
```python
lista = ["elemento_1", "elemento_2", "elemento_3"]
del lista[index] # Solo un elemento
del lista[] # Elimina la lista
```

<a name="10-copiar"></a>

### 10. Copiar una lista

Es posible copiar una lista y reasignarla a una nueva variable de la siguiente manera: lista_2 = lista_1, Dado que lista_2 hace referencia a lista_1, cualquier cambio que se haga a lista_2, se modificará también en lista_1. Sin embargo, queremos tener una copia en lugar de modificar la original, para eso usaremos el método copy(), por ejemplo:
```python
# Sintaxis
lista_1 = ["elemento_1", "elemento_2", "elemento_3"]
lista_2 = lista_1.copy()
```
```python
alumnos = ["pedro","Juan","pepe","maria","ana"]
alumnos_2 = alumnos.copy()
print(alumnos_2) # ['pedro', 'Juan', 'pepe', 'maria', 'ana']
```
<a name="11-unir-listas"></a>

### 11. Unir listas

Hay varias formas de unir listas, las más comunes son:
- Operador (+)
```python
# Sintaxis
lista_1 = ["elemento_1", "elemento_2", "elemento_3"]
lista_2 = ["elemento_4", "elemento_5", "elemento_6"]
lista_3 = lista_1 + lista_2 # ['elemento_1', 'elemento_2', 'elemento_3', 'elemento_4', 'elemento_5', 'elemento_6']
# Ejemplo
alumnos_1 = ["pedro","Juan","pepe","maria","ana"]
alumnos_2 = ["juan","pepe","maria","ana"]
alumnos_3 =  alumnos_1 + alumnos_2
print(alumnos_3) # ['pedro', 'Juan', 'pepe', 'maria', 'ana', 'juan', 'pepe', 'maria', 'ana']
```

- Método append(), que permite añadir una lista a otra, por ejemplo:
```python
# Sintaxis
lista.append(lista_2)
# Visualización
lista_1 = ["elemento_1", "elemento_2", "elemento_3"]
lista_2 = ["elemento_4", "elemento_5", "elemento_6"]
lista_1.append(lista_2) # ["elemento_1", "elemento_2", "elemento_3", "elemento_4", "elemento_5", "elemento_6"]
# Ejemplo
alumnos_1 = ["pedro","Juan","pepe","maria","ana"]
alumnos_2 = ["Jose", "Sebas", "Alfredo"]
alumnos_1.append(alumnos_2)
print(alumnos_1) # ['pedro', 'Juan', 'pepe', 'maria', 'ana', ['Jose', 'Sebas', 'Alfredo']]
```

- Método extend(), que permite añadir una lista a otra, por ejemplo:
```python
#Sintaxis
lista.extend(lista_2)
# Visualización
lista_1 = ["elemento_1", "elemento_2", "elemento_3"]
lista_2 = ["elemento_4", "elemento_5", "elemento_6"]
lista_1.extend(lista_2)
# Ejemplo
alumnos_1 = ["pedro","Juan","pepe","maria","ana"]
alumnos_2 = ["Jose", "Sebas", "Alfredo"]
alumnos_1.extend(alumnos_2)
print(alumnos_1) # ['pedro', 'Juan', 'pepe', 'maria', 'ana', 'Jose', 'Sebas', 'Alfredo']
```

<a name="12-Contar"></a>

### 12. Contar elementos de una lista

El método count() devuelve el número de veces que un elemento aparece en una lista, por ejemplo:
```python
# Sintaxis
lista.count(elemento)
# Visualización
lista_1 = ["elemento_1", "elemento_2", "elemento_3", "elemento_2", "elemento_1"]
print(lista_1.count("elemento_2")) # 2
# Ejemplo
lista_1 = [1, 2, 3, 4, 1, 6, 7, 8, 1, 10]
print(lista_1.count(1)) # 3
```
<a name="13-encontrar-indice"></a>

### 13. Encontrar índice de un elemento de una lista

Para encontrar el índice de un elemento usamos el método index() que devuelve el índice del elemento, por ejemplo:
```python
# Sintaxis
lista = ["elemento_1", "elemento_2", "elemento_3", "elemento_2", "elemento_1"]
lista.index(elemento)
# Ejemplo
alumnos = ["pedro","Juan","pepe","maria","ana"]
print(alumnos.index("Juan")) # 1
```

<a name="14-invertir-lista"></a>

### 14. Invertir una lista

Para invertir una lista usamos el método reverse(), que realiza la inversión de los elementos que tiene la misma, por ejemplo:

```python
# Sintaxis
lista = ["elemento_1", "elemento_2", "elemento_3"]
lista.reverse()
# Ejemplo
alumnos = ["Anselmo", "Mario", "Raul", "Maria", "Tamara"]
alumnos.reverse()
print(alumnos)  # ['Tamara', 'Maria', 'Raul', 'Mario', 'Anselmo']
```

<a name="15-ordenar"></a>

### 15. Ordenar elementos de una lista

Para ordenar listas podemos usar el método sort(), o las funciones integradas sorted(). El método sort() reordena los elementos en orden ascendente y modifica la lista original. Si un argumento dentro del método sort() reverse es verdadero se ordena la lista descendetemente, ejemplo:
```python
# Sintaxis
lista = ["elemento_1", "elemento_2"]
lista.sort() # ascendente
lista.sort(reverse=True) # descendente
# Ejemplo
alumnos = ["Maria", "Pedro", "Juan", "Luis", "Manuela"]
asignaturas = ["Mates", "lengua", "ingles", "geografia"]
alumnos.sort()
asignaturas.sort(reverse=True)
print(alumnos) # ['Juan', 'Luis', 'Manuela', 'Maria', 'Pedro']
print(asignaturas) # ['lengua', 'ingles', 'geografia', 'Mates']
```

la función sorted(), devuelve la lista ordenada, habría que usar reverse para que la desordenara.
```python
alumnos = ["Pedro", "Juan", "Maria", "Zaida"]
print(sorted(alumnos)) # ['Juan', 'Maria', 'Pedro', 'Zaida']
alumnos = sorted(alumnos,reverse=True)
print(alumnos) # ['Zaida', 'Pedro', 'Maria', 'Juan']
```

<a name="16-buscar"></a>

### 16. Buscar elementos en una lista

Buscar elementos en una lista es una tarea común en programación. En Python, existen varias formas de buscar un elemento en una lista dependiendo de tus necesidades. A continuación, te explico los métodos más comunes para realizar búsquedas.

- Mediante el operador in, ejemplo.
```python
lista = ["elemento_1", "elemento_2", "elemento_3"]
print("elemento_1" in lista) # Devolvera True si está o False si no.
```
- Buscando su indice en la lista con el método index, ejemplo.
```python
lista = ["elemento_1", "elemento_2", "elemento_3"]
print(lista.index("elemento_1")) # devolverá el índice del elemento o sino está un error que deberemos 
# para que el programa no falle.
```

#### ¡Enhorabuena! Si has llegado hasta aquí y comprendido las listas estas un paso más cerca, vamos ahora con unos ejercicios.

<a name = "16-ejercicios"></a>

## 16. Ejercicios

### Nivel 1

- Declarar una lista vacía
- Declarar una lista con más de 5 elementos
- Encuentra la longitud de tu lista
- Obtenga el primer elemento, el elemento del medio y el último elemento de la lista.
- Declare una lista llamada datos, coloque su (nombre, edad, altura, estado civil, dirección)
- Declare una variable de lista llamada companias y asigne valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
- Imprima la lista usando print()
- Imprima el número de empresas en la lista
- Imprima la primera, la segunda y la última empresa.
- Imprimir la lista después de modificar una de las empresas
- Agregar una empresa a companias al final de la lista.
- Insertar una empresa en el medio de la lista de empresas
- Cambie uno de los nombres de companias a mayúsculas (¡IBM excluido!)
- Unir companias con una cadena '-; '
- Comprueba si una determinada empresa existe en la lista companias.
- Ordenar la lista usando el método sort()
- Invierta la lista en orden descendente utilizando el método reverse()
- Elimina las primeras 3 empresas de la lista
- Elimina las últimas 3 empresas de la lista.
- Elimina de la lista a Google
- Eliminar la primera empresa que queda de companias
- Eliminar todas las empresas de TI de la lista
- Una a las siguientes listas:
- copie la lista unida y asígnela a una variable full_stack, luego 
- inserte Python y SQL.
- La siguiente es una lista de edades de los alumnos
```python
edad = [19,23,23,54,19,37,32,26,28,22,45]
```
- Ordena la lista y encuentra la edad mínima y máxima
- Encuentra el alumno que está en el medio de las edades (es decir el elemento del centro)
- Guarda las edades pares en una nueva lista llamada edades_pares.
- Añade dos edades más y ordenalo de menor a mayor.





<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/03_Cadenas/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/05_Tuplas/readme.md">Siguiente Capítulo</a>
</h4>


<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/listas.png">
</h1>