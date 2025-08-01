<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/08_Condicionales/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/10_Funciones/readme.md">Siguiente Capítulo</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/bucles.png">
</h1>


<h1 align="center">Bucles</h1><br>


<h4>Índice</h4>

- [1. Inicio Bucles](#1-inicio-bucles)
- [2. Bucle While](#2-bucle-while)
- [3. Break y Continue](#3-break-y-continue)
  - [3.1 Break con while](#31-break-con-while)
  - [3.2 Continue con while](#32-continue-con-while)
- [4. Bucle For](#4-bucle-for)
  - [4.1 Bucle for con cadenas](#41-bucle-for-con-cadenas)
  - [4.2 Bucle for con listas](#42-bucle-for-con-listas)
  - [4.3 Bucle for con tuplas](#43-bucle-for-con-tuplas)
  - [4.4 Bucle for con Conjuntos](#44-bucle-for-con-conjuntos)
  - [4.5 Bucle for con Diccionario](#45-bucle-for-con-diccionario)
- [4.6 Bucle for con break](#46-bucle-for-con-break)
- [4.7 Bucle for con Continue](#47-bucle-for-con-continue)
- [5. Función Range](#5-función-range)
- [6. Bucle For anidado](#6-bucle-for-anidado)
- [7. For Else](#7-for-else)
- [8. Palabra Pass](#8-palabra-pass)
- [9. Ejercicios.](#9-ejercicios)



<a name = "1-inicio-bucles" ></a>

## 1. Inicio Bucles

Los bucles permiten repetir bloques de código de manera controlada, python tiene dos tipos principales de bucles que te explico a continuación.
- El bucle **FOR** (for)
- el Bucle **WHILE** (while)

<a name = "2-bucle-while" ></a>

## 2. Bucle While

El bucle _while_. Este bucle se ejecutará mientras la condición siga siendo verdadera, es útil cuando no sabes cuántas repeticiones necesitas, pero conoces la condición para continuar.
```python
# Sintaxis
while condicion:
    # Bloque que se ejecutará.
#Ejemplo
contador = 6
while contador < 10:
    print(contador)
    contador = contador +1
```
>[!NOTE]
>En el ejemplo anterior, cuando el contador es menor que 10 el código se ejecuta hasta llegar a 9, si queremos que se ejecute cuando la condición deja de ser verdadera podemos usar un else.
```python
contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1
else:
    print(contador)
```
En este caso la condición cuando llega a 5 se vuelve falsa y la ejecución inicia el ese como resultado imprimirá 5.

<a name = "3-break-y-continue" ></a>

## 3. Break y Continue

* El break y el Continue se pueden usar tanto con _while_ como con _for_ la función es la misma pero su funcionalidad puede ser diferente, vamos primero a verlo con while y posteriormente con for.

<a name = "31-break-con-while"></a>

### 3.1 Break con while

Si queremos detener un bucle usaremos la palabra reservada **break**, del inglés Romper.
```python
# Sintaxis
while condicion:
    código
    if condicion:
        break
# Ejemplo
contador = 0
while contador < 5:
    print(contador)
    contador = contador +1
    if contador == 3:
        break
# En este caso cuando el contador sea igual a 3 saldrá del bucle, ¡pruébalo!
```
<a name="32-continue-con-while"></a>

### 3.2 Continue con while

Con la palabra reservada continue lo que conseguimos es que mita la iteración actual y continue con la siguiente, veamos un ejemplo.
```python
# Sintaxis
while condicion:
    código
    if condición:
        continue
# Ejemplo
contador = 0
while contador < 10:
    if contador == 5 or contador == 8:
        contador = contador + 1
        continue
    print(contador) # 0 1 2 3 4 6 7 9
    contador = contador + 1
# Como podemos ver en este caso cuando contador es igual a 5 o igual a 8 salta esos números.
```

<a name = "4-bucle-for" ></a>

## 4. Bucle For

El bucle for es perfecto cuando sabemos las veces que queremos repetir el bucle o para recorrer listas, tuplas, diccionarios o cadenas (String).

<a name = "41-bucle-for-con-cadenas" ></a>

### 4.1 Bucle for con cadenas 
```python
# Sintaxis
for elemento in secuencia:
    # Bloque de código a ejecutar
# Ejemplo
nombre = "Antonio"
for letra in nombre:
    print(letra)
```

<a name = "42-bucle-for-con-listas" ></a>

### 4.2 Bucle for con listas
```python
# Sintaxis
for elemento in lista:
    código a ejecutar # el elemento en java se suele usar i, en python se intenta hacer referencia
    #al elemento en cuestion.
# Ejemplo
numeros = [0, 1, 2, 3, 4, 5]
for numero in numeros: # numero solo es válido dentro del bucle.
    print(numero)
# Otro ejemplo
alumnos = ["Pepe", "Ana", "Luis", "Teresa"]
for alumno in alumnos:
    print(alumno) # Con este ejemplo es más visible.
```

<a name = "43-bucle-for-con-tuplas" ></a>

### 4.3 Bucle for con tuplas
```python
# Sintaxis
for elemento in tupla:
    código a ejecutar
# Ejemplo
alumnos = ("Trump", "Ronald", "Churchil", "Musk")
for alumno in alumnos:
    print(alumno)
# Como podemos comprobar recorre la lista completa, ya le veremos la utilidad posteriormente.
```

<a name = "44-bucle-for-con-conjuntos" ></a>

### 4.4 Bucle for con Conjuntos
```python
# Sintaxis
for elemento in conjunto:
    código a ejecutar
# Ejemplo
alumnos_1 = {"Pepe", "Tamara", "Luisa", "Antonia", "Miguel", "Francisco"}
for alumno in alumnos_1:
    print(alumno)
# Como podemos ver recorre el Conjunto y cada vez lo puede imprimir de manera diferente.

```

<a name = "45-bucle-for-con-diccionarios" ></a>

### 4.5 Bucle for con Diccionario

Al recorrer los Diccionarios con un bucle for obtenemos la clave del diccionario, ejemplo.
```python
# Sintaxis
for elemento in diccionario:
    código a ejecutar
# Ejemplo
alumno_1 = {
    "nombre":"Juan",
    "edad": 25,
    "ciudad": "Madrid",
    "curso" : "DAM",
    "asignaturas" : ["Bases de datos", "Programación", "Inglés"],
    "direccion" : {
        "Calle": "Falsa 123", 
        "cod_postal": "25878"
    }
}
for clave in alumno_1:
    print(clave)
# Si queremos clave y valor usamos esta forma
for clave, valor in alumno_1.items():
    print(clave, "-" valor)
```

<a name = "46-bucle-for-con-break" ></a>

## 4.6 Bucle for con break

Al igual que con el while, el break con el bucle for lo que hace es salir de la iteración.
```python
# Sintaxis
for elemento in secuencia:
    código
    if condicion:
        break
# Ejemplo
numeros = (1,2,3,4,5)
for numero in numeros:
    print(numero)
    if numero == 3:
        break
# El bucle se detiene al llegar a 3.
```

<a name ="47-bucle-for-con-continue"></a>

## 4.7 Bucle for con Continue

Usaremos _continue_ cuando queramos omitir alguno de los pasos del bucle for
```python
# Sintaxis
for elemento in secuencia:
    código
    if condicion:
        continue
# Ejemplo
numeros = (0,1,2,3,4,5)
for numero in numeros:
    print(numero)
    if numero == 3:
        print("estamos en ", numero)
        continue
    print("el siguiente numero sera: ", numero + 1) if numero != 5 else print("fin del bucle")
print("fuera del bucle")
```
>[!NOTE]
>Para que entendamos el ejemplo anterior, lo que realiza el bucle for es imprimir los números y si se cumple la condición del if vuelve al inicio del bucle por lo que en el 4 no imprime el siguiente número sera: pero si imprime el número ya que el bucle continua ejecutandose, si no me he explicado bien, id modificando el bucle y lo entenderéis.


<a name = "5-función-range" ></a>

## 5. Función Range

La función Range o función de Rango se utiliza una lista de números. _range(inicio, fin, paso)_ por defecto emieza en 0 y el incremento es 1. La secuencia de rango necesita al menos el argumento de fin, ejemplo.
```python
# Sintaxis
range(fin)
range(inicio, fin)
range(inicio, fin, paso)
# Ejemplo de sintaxis
range(11) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] con 1 parámetro
range(1,11) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] con 2 parámetros
range(1,11,2) # [1, 3, 5, 7, 9] # con los 3 parámetros
# Ejemplo
lista = list(range(10))
print(lista) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
conjunto = set(range(11))
print(conjunto) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

```

>[!NOTE]
>Puede ser que ahora no le veas sentido a los range, pero son eficaces por que no ocupan memoria, flexibes ya que permiten generar diferentes patrones numéricos y legibles ya que hacen el códig más fácil de entender.

* Con el bucle for se usan de la siguiente manera.
```python
# Sintaxis
for elemento in range(inicio, fin, paso):
    código a ejecutar en el rango definido.
# Ejemplo
for numero in range(11):
    print(numero) # Esto imprimirá los números
```

>[!NOTE]
>También podéis probar a poner el paso en negativo a ver que es lo que hace el range().


<a name = "6-bucle-for-anidado" ></a>

## 6. Bucle For anidado

Podemos escribir un bucle for dentro de otro bucle for, esto en JAVA es bastante utilizado, ejemplo.
```python
# Sintaxis
for i in z:
    for j in i:
        print(j)
# Ejemplo
alumno_1 = {
    "nombre":"Juan",
    "edad": 25,
    "ciudad": "Madrid",
    "curso" : "DAM",
    "asignaturas" : ["Bases de datos", "Programación", "Inglés"],
    "direccion" : {
        "Calle": "Falsa 123", 
        "cod_postal": "25878"
    }
}
for clave in alumno_1:
    if clave == "asignaturas":
        for asignatura in alumno_1["asignaturas"]:
            print(asignatura)
# Este bucle for lleva anidado otra bucle
```

<a name = "7-for-else" ></a>

## 7. For Else

El for, else se puede usar para cuando finaliza el bucle enviar un mensaje, ejemplo.
```python
# Sintaxis
for elemento in range(inicio,fin,paso):
    código
else:
    print("fin del bucle")
# Ejemplo
for numero in range(11):
    print(numero)
else:
    print("el bucle ha llegado a 10")
```

<a name = "8-palabra-pass" ></a>

##  8. Palabra Pass

- Si escribimos un bucle pero que en su interior no contiene ninguna sentencia y no queremos que nos devuelva un error, escribimos pass dentro del bucle, ejemplo.
```python
# Sintaxis
for i in z:
    pass
# Ejemplo
for numer in range(6):
    pass
# Esto hace que el bucle itere 6 veces pero no hace nada.
```

<h4 align="center">
⭐⭐⭐⭐⭐ <br>
La programación no es un camino de rosas pero ya estás un pasito más cerca. te recomiendo que repases conceptos para no olvidarlos, que a mí mientras escribo el manual se me van olvidando cosas de capítulos anteriores y tengo que volver a mirarlos.
</h4>

<a name = "9-ejercicios" ></a>

## 9. Ejercicios.

- Genera una cuenta del 0 al 10 con el bucle for
- Genera una cuenta del 0 al 10 con el bucle while
- Crea un programa que genere la siguiente salida por pantall.
```
#
##
###
####
#####
######
#######
```
- Crea la tabla de multiplicar del 5
- Usa el bucle for para imprimir por pantalla los números pares del 0 al 50
- Usa el bucle while para imprimir por pantalla los números impares del 0 al 50
- Imprime por pantalla la suma de todos los números del 0 al 100. Usa el bucle que quieras el resultado debe ser 5050.
- En el siguiente diccionario usa el bucle for para imprimir los paises que están en "América" y en que continente está "Japón"
```
paises_por_continente = {
    "América": ["Estados Unidos", "Canadá", "México", "Brasil", "Argentina"],
    "Europa": ["España", "Francia", "Alemania", "Italia", "Reino Unido"],
    "África": ["Nigeria", "Egipto", "Sudáfrica", "Kenia", "Etiopía"],
    "Asia": ["China", "Japón", "India", "Corea del Sur", "Rusia"],
    "Oceanía": ["Australia", "Nueva Zelanda", "Fiyi", "Papúa Nueva Guinea"]
}
```



<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/08_Condicionales/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/10_Funciones/readme.md">Siguiente Capítulo</a>
</h4>