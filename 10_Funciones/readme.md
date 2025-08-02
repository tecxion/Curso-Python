<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/09_Bucles/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/11_Modulos/readme.md">Siguiente Capítulo</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/funciones.png">
</h1>


<h1 align="center">Funciones</h1><br>


<h4>Índice</h4>

- [1. Definición de función](#1-definición-de-función)
- [2. Declarar y llamar a una función](#2-declarar-y-llamar-a-una-función)
- [3. Función sin parámetros](#3-función-sin-parámetros)
- [4. Función con parámetros](#4-función-con-parámetros)
- [5. Función que devuelve un valor](#5-función-que-devuelve-un-valor)
- [6. Función con parámetros predeterminados](#6-función-con-parámetros-predeterminados)
- [7. Número arbitrario de argumentos](#7-número-arbitrario-de-argumentos)
- [8. Número predeterminado y arbitrario de parámetros](#8-número-predeterminado-y-arbitrario-de-parámetros)
- [9. Función como parámetro de otra función](#9-función-como-parámetro-de-otra-función)
- [10. Ejercicios.](#10-ejercicios)

>[!IMPORTANT]
>Para ejecutar las funciones no podrás hacerlo por la "SALIDA" tendrás que ejecutarlos por la terminal, navegando a la carpeta que tienes tu archivo .py o ejecutando una terminal en la misma carpeta. [ver comandos terminal](../comandos.md)

<a name = "1-definición-de-función"></a>

## 1. Definición de función

Las funciones son bloques de código reutilizables que realizan una tarea específica. Son fundamentales para organizar y estructurar programas en Python, está es la definición técnica de las funciones y como mejor se pueden explicar.

Para las funciones usaremos la palabra reservada **_def_**.

<a name = "2-declarar-y-llamar-a-una-función"></a>

## 2. Declarar y llamar a una función

Cuando creamos una función, la declaramos y posteriormente la llamamos a ejecución, las funciones se pueden declarar con parámetros o sin parámetros, si has visto otro lenguaje como JAVA no tendrás mas problema.

```python
# Sintaxis
# Declarar la función
def nombre_funcion(): # IMPORTANTE! Recordar siempre los dos puntos.
    el código de la función
# llamada de la función
nombre_funcion()
```

<a name ="3-función-sin-parámetros"></a>

## 3. Función sin parámetros

Como mencionamos antes una función se puede declarar sin parámetros, esto quiere decir que dentro del paréntesis no trae ningún parámetro que sea necesario para ejecutar esa función.
```python
# Ejemplo
# Definimos la función
def alumno(): # Función alumno sin parámetros
    nombre = "Paco"
    apellido = "Martinez"
    edad = 24
    nombre_completo = (f"Hola, mi nombre es {nombre} {apellido} y tengo {edad} años" )
    print(nombre_completo)
# llamamos a la función
alumno()
```

<a name = "4-función-con-parámetros" ></a>

## 4. Función con parámetros

- Las funciones com parámetros son funciones que para que se ejecuten tienen que recibir un valor, es decir si la función no recibe ese parámetro ya sea bien por introducción del usuario o de otra función no se ejecutará correctamente.
  

```python
# Sintaxis
## Declaración
def nombre_funcion(parámetros):
    codigo de la función
    return
## Llamada a la función
nombre_funcion(parámetros)
# Ejemplo
def sumar(a, b):
    return a + b
resultado = sumar(4, 5) # llama a la función sumar y suma 4 + 5 ya definidos
print(resultado) # 9

# Otro ejemplo
def saludar(nombre): # en este caso el parámetro viene introducido por el usuario.
    saludo = (f"Hola, {nombre}, ¿qué tal?")
    return saludo

nombre = input("Introduce tu nombre: ")
print(saludar(nombre))

```

- Una función puede tener varios parámetros, por ejemplo.
```python
# Sintaxis
def nombre_funcion(param_1, param_2):
    código función
    return
# Llamada a la función
nombre_funcion(param_1, param_2)

# Ejemplo
def nombre_completo(nombre, apellido):
    saludo = (f"Hola, {nombre} {apellido}, esto es una función con dos param.")
    return saludo

nombre_alumno = input("¿Cómo te llamas? ")
apellido_alumno = input("¿Y tu apellido? ")
print(nombre_completo(nombre_alumno, apellido_alumno))

```
<a name = "5-función-que-devuelve-un-valor" ></a>

## 5. Función que devuelve un valor

Las funciones también pueden devolver un valor concreto, si una función no tiene una instrucción de retorno, su valor es "None", para ello usamos la palabra reservada _return_, esto es util para cuando la función a la que se llama debe devolver un valor.
```python
# Ejemplo con las función anterior.
def alumno(): # Función alumno sin parámetros
    nombre = "Paco"
    apellido = "Martinez"
    edad = 24
    nombre_completo = (f"Hola, mi nombre es {nombre} {apellido} y tengo {edad} años" )
    return nombre_completo
```

- Las funciones pueden devolver diferentes tipos de datos, por ejemplo.

* Devolviendo una cadena.
```python
def imprimir_nombre(mi_nombre):
    return mi_nombre
imprimir_nombre("Pepito")

def imprimir_nombre_completo(nombre, apellido):
    nombre_completo = (f"{nombre} {apellido}")
    return nombre_completo
print(imprimir_nombre_completo(nombre="Marcos", apellido="Blanco"))

```

* Devolviendo un número
```python
# Ejemplo
def suma(a, b):
    total = a + b
    return total
print(suma(3, 5))
```

* Devolviendo un booleano
```python
def es_par(a):
    if a % 2 == 0:
        print("es par")
        return True
    return False
print("3 es par?", es_par(3))
print("6 es par?", es_par(6))
```

* Devolviendo una lista
```python
def num_pares(a):
    pares = []
    for i in range(a+1):
        if i % 2 == 0:
            pares.append(i)
    return pares
print(num_pares(20))
```

<a name = "6-función-con-parámetros-predeterminados" ></a>

## 6. Función con parámetros predeterminados

Hay veces que la función lleva parámetros asociados y a estos parámetros le damos unos valores predeterminados, sobre todo ya que si una función tiene un parámetro y no se le asigna un valor nos dará error, para eso se usan los parámetros predeterminados, ejemplo.
```python
# Sintaxis
# Declarando la función
def funcion(param = valor):
    código
# Llamada a la función, tenemos dos formas
funcion() # sin parámetro inicial que tomara el valor del parámetro predeterminado
funcion(param) # con un parámetro dado.
# Ejemplo
def saludo(nombre = "alumno"):
    mensaje = nombre + ", Bienvenido al Curso Python"
    return mensaje
print(saludo()) # Sin parámetro
print(saludo("Pedro")) # Con parámetro
```

>[!NOTE]
>Indicar que las funciones con parámetros predeterminados puede también tener uno predeterminado y otro no, dos predeterminados, etc. Dependerá de lo que realice esa función pero tener en cuenta que si los parámetros de la función no tienen valor y es requerido dará error.
>```python
>def funcion_error(a):
>    resta = 100 - a
>    return resta
>print(funcion_error()) # al no tener parámetro y ser necesario da error.

<a name = "7-número-arbitrario-de-argumentos" ></a>

## 7. Número arbitrario de argumentos

<a name = "8-número-predeterminado-y-arbitrario-de-parámetros" ></a>

## 8. Número predeterminado y arbitrario de parámetros


<a name = "9-función-como-parámetro-de-otra-función" ></a>

## 9. Función como parámetro de otra función


<a name = "10-ejercicios" ></a>

## 10. Ejercicios.





















<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/09_Bucles/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/11_Modulos/readme.md">Siguiente Capítulo</a>
</h4>