<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/04_Listas/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/06_Conjuntos/readme.md">Siguiente Capítulo</a>
</h4>


<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/tuplas.png">
</h1>

<h1 align="center">Tuplas</h1><br>

<h4>Índice</h4>

- [1. ¿Qué es una tupla?](#1-qué-es-una-tupla)
- [2. Sintaxis](#2-sintaxis)
- [3. Lóngitud de una tupla](#3-lóngitud-de-una-tupla)
- [4. Acceso a los elementos de una tupla](#4-acceso-a-los-elementos-de-una-tupla)
- [5. Cortar tuplas](#5-cortar-tuplas)
- [6. Cambiar tuplas a listas](#6-cambiar-tuplas-a-listas)
- [7. Como comprobar un elemento en una tupla](#7-como-comprobar-un-elemento-en-una-tupla)
- [8. Unir tuplas](#8-unir-tuplas)
- [9. Eliminar tuplas](#9-eliminar-tuplas)
- [10. Ejercicios.](#10-ejercicios)



<a name="1-qué-es-una-tupla"></a>

## 1. ¿Qué es una tupla?

Las tuplas son estructuras de datos, similar a las listas pero con una diferencia, son **Inmutables**, esto significa que una vez creadas no pueden ser modificadas.

- Características:
    - Son **Inmutables**, no se pueden cambiar después de su creación
    - **Ordenadas**, Mantienen el orden de los elementos.
    - **Pueden contener cualquier tipo de dato**, incluso otras tuplas.
    - **Permiten duplicados**, es decir pueden repetirse sus elementos.

>[!CAUTION]
>Las tuplas se forman con _( )_ mientras que las listas se forman con _[ ]_, tenedlo en cuenta para no confundirnos.

<a name = "2-sintaxis"></a>

## 2. Sintaxis 

Las tuplas se definen por paréntesis o simplemente separando los elementos por comas, ejemplo:
```python
tupla_1 = (1,2,3,4)
tupla_2 = 1,2,3,4 
tupla_3 = tuple([1,2,3,4]) #conversión desde lista
tupla_vacia = () # tupla vacia
tupla_un_elemento = (5,) # tupla de un elemento.
```

<a name = "3-lóngitud-de-una-tupla"></a>

## 3. Lóngitud de una tupla

Para saber la longitud de una tupla usamos como anteriormente en las listas el método _len()_, ejemplo:
```python
tupla = ("elemento_1", "elemento_2", "elemento_3")
len(tupla)
```

<a name = "4-Acceso-a-los-elementos-de-una-tupla"></a>

## 4. Acceso a los elementos de una tupla

En las tuplas al igual que en las listas se accede a sus elementos por indexación positiva o negativa, veamos un ejemplo:
- Indexación positiva.
```python
# Sintaxis
tupla_1 = ("elemento_1", "elemento_2", "elemento_3")
elem_1 = tupla_1[0]
elem_2 = tupla_1[1]
# Ejemplo
alumnos = ("Pedro","Maria","Juan","Ana")
pedro = alumnos[0]
ana = alumnos[3]
print(pedro) # Pedro
print(ana) # Ana
```

-Indexación negativa, significa comenzar por el final, es decir por el -1 se refiere al último y vamos sumando números negativos, ejemplo:
| elemento_1 | elemento_2 | elemento_3 | elemento_4 |
| ---------- | ---------- | ---------- | ---------- |
| -4         | -3         | -2         | -1         |

```python
# Sintaxis
tupla_1 = ("elemento_1", "elemento_2", "elemento_3", "elemento_4")
primer_ele = tupla_1[-4]
ultimo_ele = tupla_1[-1]
# Ejemplo
alumnos = ("Pedro","Maria","Luis","Ana")
pedro = alumnos[-4]
ana = alumnos[-1]
print(pedro) # Pedro
print(ana) # Ana
```

<a name = "5-Cortar-tuplas"></a>

## 5. Cortar tuplas

Podemos almacenar elementos de una tupla en otra usando los índices para generar así nuevas tuplas con los elementos que nosotros queramos solo debemos especificar el índice de inicio y el de fin, ejemplo:
```python
# Sintaxis
tupla_1 = ("elemento_1","elemento_2","elemento_3","elemento_4")
todos = tupla_1[0:4]
todos_1 = tupla_1[0:]
elemntos = [indice_inicio:indice_final]
# Ejemplo
alumnos = ("Pedro","Ana","Maria","Jesus")
todos = alumnos[0:4]
ana_maria = alumnos[1:3]
print(todos)
print(ana_maria)
```

- Rango con índices negativos.
```python
# Sintaxis
tupla_1 = ("elemento_1","elemento_2","elemento_3","elemento_4")
todos = tupla_1[-4:]
todos_1 = tupla_1[0:]
elemntos = [indice_inicio:indice_final]
# Ejemplo
alumnos = ("Pedro","Ana","Maria","Jesus")
todos = alumnos[0:4]
ana_maria = alumnos[1:3]
print(todos)
print(ana_maria)
```

<a name = "6-cambiar-tuplas-a-listas"></a>

## 6. Cambiar tuplas a listas

Podemos hacer cambios tanto de tuplas a listas como de listas a tuplas, como bien sabemos las tuplas son inmutables por lo que para modificarla debemos pasarla a una lista.

```python
# Sintaxis
tupla = ("elemento_1", "elemento_2", "elemento_3")
lista = list(tupla)

# Ejemplo
alumnos = ("Juan", "Maria", "Pedro", "Luis", "Ana")
print(alumnos)
print(type(alumnos))
alumnos = list(alumnos)
print(alumnos)
print(type(alumnos))
```

<a name="7-como-comprobar-un-elemento-en-una-tupla"></a>

## 7. Como comprobar un elemento en una tupla

Para comprobar si un elemento está contenido en una tupla usamos al igual que en las listas _in_, devuelve un valor booleano, ejemplo.

```python
# Sintaxis
tupla = ("elemento_1", "elemento_2", "elemento_3")
"elemento_2" in tupla # True
# Ejemplo
alumnos = ("Pepe", "Luis", "Alfredo")
print("Alfredo" in alumnos) #True
```

<a name="8-unir-tuplas"></a>

## 8. Unir tuplas

Si queremos unir tuplas en una tupla nueva podemos usar el operador _+_, ejemplo.
```python
# Sintaxis
tupla = ("elemento_1", "elemento_2")
tupla_2 = ("elemento_3", "elemento_4")
tupla_3 = tupla + tupla_2
# Ejemplo
alumnos = ("Pedro", "Ana")
alumnos_clase = ("Jorge", "Rodrigo", "Tamara")
todos_alumnos = alumnos + alumnos_clase
print(todos_alumnos) # ('Pedro', 'Ana', 'Jorge', 'Rodrigo', 'Tamara')
```

<a name = "9-eliminar-tuplas>

## 9. Eliminar tuplas

Como bien sabemos las tuplas son inmutables y no podemos modificar sus elementos, pero si podemos eliminar la tupla completa, para ello usamos _del_, ejemplo.
```python
# Sintaxis
tupla = ("elemento_1", "elemento_2")
del tupla
# Ejemplo
alumnos = ("Pedro", "Silvia")
del alumnos
print(alumnos) # Da error NameError: name 'alumnos' is not defined
```

<h3 align = "center">
👌 !Genial! Ya casi has acabado con las tuplas, vamos a por unos ejercicios.
</h3>

<a name = "10-ejercicios"></a>

## 10. Ejercicios.

- Crear una tupla vacía
- Crea una tupla que contenga los nombres de 4 paises de Europa y otra de América que tenga nombres tanto del Norte como del Sur.
  - Comprueba si dentro de Europa está `España` y `Alemania`
  - Comprueba si dentro de América está `Argentina` y `Colombia`
- Une ambas tuplas en una que se llame mundo.
- ¿Cuántos paises hay?
- Modifica la tupla América y añade dos paises más.
- Cambia la tupla america a una lista.
- Separa el primer y el último elemento de la tupla europa.
- Elimina la tupla europa.

[Solución a los ejercicios](./Ejercicio.py)


🤩 ¡Perfecto! Ya sabes mucho sobre tuplas, vamos a por lo siguiente, Conjuntos.

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/04_Listas/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/06_Conjuntos/readme.md">Siguiente Capítulo</a>
</h4>
