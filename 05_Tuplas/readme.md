<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/04_Listas/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/07_Conjuntos/readme.md">Siguiente Capítulo</a>
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


