<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/12_Modulos/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/14_Errores/readme.md">Siguiente Capítulo</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/funciones_2.png">
</h1>


<h1 align="center">Funciones de Orden superior / Higher-Order Functions</h1><br>

<h3>Índice</h3>

- [1. Función de orden superior](#1-función-de-orden-superior)
  - [1.1 Función como parámetro](#11-función-como-parámetro)
  - [1.2 Función como valor de retorno](#12-función-como-valor-de-retorno)
- [2. Cierres de python o Python Closures](#2-cierres-de-python-o-python-closures)
- [3. Decoradores de Python](#3-decoradores-de-python)
  - [3.1 Creando decoradores](#31-creando-decoradores)
  - [3.2 Aplicación de multiples decoradores en una sola función](#32-aplicación-de-multiples-decoradores-en-una-sola-función)
  - [3.3 Aceptar parámetros en funciones decoradoras](#33-aceptar-parámetros-en-funciones-decoradoras)
- [4. Funciones de orden superior integradas](#4-funciones-de-orden-superior-integradas)
  - [4.1 Función de mapa](#41-función-de-mapa)
  - [4.2 Función de filtro](#42-función-de-filtro)
  - [4.3 Función de reducción](#43-función-de-reducción)
  - [4.4 Funcion Sorted con clave](#44-funcion-sorted-con-clave)
- [5. Ejercicios](#5-ejercicios)

<a name = "1-función-de-orden-superior"> </a>

## 1. Función de orden superior

Las funciones de orden superior (Higher-Order Functions) son un concepto fundamental en Python (y en programación funcional) que se refiere a funciones que pueden:

- Aceptar otras funciones como argumentos
- Retornar funciones como resultado.
- Una función se puede modificar
- Se puede asignar una función a una variable

Python trata las funciones como ciudadanos de primera clase (first-class citizens), lo que significa que pueden ser pasadas, almacenadas y manipuladas como cualquier otro objeto (números, strings, listas, etc.).

<a name = "11-función-como-parámetro"></a>

### 1.1 Función como parámetro

Ejemplo con map()
```python
def cuadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4]
resultado = list(map(cuadrado, numeros))
print(resultado)  # [1, 4, 9, 16]
# Otro ejemplo con una función personalizada
def aplicar_operacion(funcion, lista):
    return [funcion(x) for x in lista]
def doble(x):
    return x * 2
print(aplicar_operacion(doble, [1, 2, 3]))  # [2, 4, 6]
```
- *map()* es una función de orden superior porque acepta la _función_ cuadrado como argumento.

<a name = "12-función-como-valor-de-retorno" ></a>

### 1.2 Función como valor de retorno

Una función que retorna otra función es como una "fábrica de funciones" que puede generar diferentes comportamientos según sea necesario.
- Ejemplo.
```python
def crear_funcion_personalizada(potencia):
    def elevar(numero):
        return numero ** potencia
    return elevar
```
- ¿Cómo funciona?
    - La función externa (crear_funcion_personalizada) recibe parámetros de configuración
    - Define una función interna (elevar) que usa esos parámetros
    - Retorna la función interna lista para ser usada


```python
def crear_saludo(mensaje):
    def saludar(nombre):
        return f"{mensaje}, {nombre}!"
    return saludar
saludo_formal = crear_saludo("Buenos días")
print(saludo_formal("Ana"))  # "Buenos días, Ana!"
# Otro ejemplo
def generar_operacion(operador):
    def suma(a, b):
        return a + b
    def resta(a, b):
        return a - b
    
    if operador == '+':
        return suma
    elif operador == '-':
        return resta
    else:
        return lambda a, b: a * b  # Retornamos una lambda como default

# Uso:
operacion_suma = generar_operacion('+')
print(operacion_suma(5, 3))  # 8

operacion_default = generar_operacion('?')
print(operacion_default(5, 3))  # 15
```

<a name = "2-cierres-de-python-o-python-closures" ></a>

## 2. Cierres de python o Python Closures

Los closures (cierres) son un concepto fundamental en Python que permite a las funciones "recordar" el entorno en el que fueron creadas, incluso después de que ese entorno haya dejado de existir. Es una característica poderosa que combina funciones con estado.

- Un closure es una función que:
    - Se define dentro de otra función (función anidada).
    - Accede a variables de la función exterior (variables no globales).    
    - Sobrevive fuera del ámbito donde fue creada.

```python
def contador_factory():
    count = 0
    def contar():
        nonlocal count # nonlocal nos permite modificar la variable (sin esto, sería de solo lectura)
        count += 1
        return count
    return contar

mi_contador = contador_factory()
print(mi_contador())  # 1
print(mi_contador())  # 2
```

<a name = "3-decoradores-de-python" ></a>

## 3. Decoradores de Python

Los decoradores son una característica de Python que permite modificar o extender el comportamiento de funciones o clases sin cambiar su código directamente. Funcionan como "envolturas" que se ejecutan antes, después o alrededor de la función original.

>[!NOTE]
>Los decoradores es algo que cuesta ver al principio pero se que les cojerás el truco.

<a name = "31-creando-decoradores"></a>

### 3.1 Creando decoradores
```python
# Sintaxis
def mi_decorador(func):
    def wrapper():
        print("Algo antes de la función")
        resultado = func()
        print("Algo después de la función")
        return resultado
    return wrapper

# Forma manual de aplicar el decorador
def saludar():
    return "¡Hola Mundo!"

saludar_decorada = mi_decorador(saludar)
saludar_decorada()
# Sintaxis de @
@mi_decorador
def mi_funcion():
    pass
# esto equivale a:
mi_funcion = mi_decorador(mi_funcion)
# Ejemplo más detallado:
def mi_decorador(func):
    def wrapper():
        print("Antes de ejecutar la función")
        func()  # Ejecuta la función original
        print("Después de ejecutar la función")
    return wrapper

@mi_decorador
def saludar():
    print("¡Hola!")

saludar()
# Salida:
# Antes de ejecutar la función
# ¡Hola!
# Después de ejecutar la función
```


<a name = "32-aplicación-de-multiples-decoradores-en-una-sola-función" ></a>

### 3.2 Aplicación de multiples decoradores en una sola función
```python
@medir_tiempo
@cache
@validar_tipos(int)
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)

# Equivale a:
# factorial = medir_tiempo(cache(validar_tipos(int)(factorial)))
```




<a name = "33-aceptar-parámetros-en-funciones-decoradoras" ></a>

### 3.3 Aceptar parámetros en funciones decoradoras
```python
# Ejemplo
def mi_decorador(func):
    def wrapper(*args, **kwargs):  # Acepta cualquier número de argumentos
        print(f"Llamando a {func.__name__} con args: {args}, kwargs: {kwargs}")
        resultado = func(*args, **kwargs)
        print(f"Resultado: {resultado}")
        return resultado
    return wrapper

@mi_decorador
def sumar(a, b):
    return a + b

@mi_decorador
def saludar(nombre, apellido=""):
    return f"Hola {nombre} {apellido}"

sumar(3, 5)
saludar("Juan", apellido="Pérez")
```

- Puntos clave que debes recordar:
    - Concepto fundamental: Los decoradores son funciones que modifican otras funciones sin cambiar su código original.
    - Sintaxis: El símbolo @ es azúcar sintáctico para aplicar decoradores de forma elegante.
    - Flexibilidad: Usa *args, **kwargs para que tus decoradores funcionen con cualquier función.
    - Metadatos: Siempre usa @functools.wraps(func) para preservar información de la función original.
    - Casos de uso comunes: Logging, validación, autenticación, caching, medición de tiempo, etc.


<a name = "4-funciones-de-orden-superior-integradas"></a>

## 4. Funciones de orden superior integradas

Una función de orden superior (Higher-Order Function) es una función que cumple al menos una de estas condiciones:
- Recibe una o más funciones como argumentos
- Devuelve una función como resultado
Este concepto viene de la programación funcional y es fundamental en Python.


<a name = "41-función-de-mapa"></a>

### 4.1 Función de mapa

- map()
Aplica una función a cada elemento de un iterable:
```python
# Ejemplo básico
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # [1, 4, 9, 16, 25]

# Con función definida
def convertir_celsius_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperaturas_c = [0, 20, 30, 40]
temperaturas_f = list(map(convertir_celsius_fahrenheit, temperaturas_c))
print(temperaturas_f)  # [32.0, 68.0, 86.0, 104.0]

# Con múltiples iterables
def sumar(x, y):
    return x + y

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
sumas = list(map(sumar, lista1, lista2))
print(sumas)  # [5, 7, 9]
```

<a name = "42-función-de-filtro"></a>

### 4.2 Función de filtro

- filter()
Filtra elementos de un iterable usando una función predicado:
```python
# Filtrar números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8, 10]

# Filtrar palabras largas
palabras = ["hola", "mundo", "programación", "python", "a"]
palabras_largas = list(filter(lambda palabra: len(palabra) > 4, palabras))
print(palabras_largas)  # ['mundo', 'programación', 'python']

# Filtrar valores truthy
valores = [0, 1, "", "texto", None, [], [1, 2]]
valores_truthy = list(filter(None, valores))  # None es equivalente a bool
print(valores_truthy)  # [1, 'texto', [1, 2]]
```


<a name = "43-función-de-reducción"></a>

### 4.3 Función de reducción

- reduce()
Aplica una función de forma acumulativa a los elementos de un iterable:
```python
from functools import reduce

# Sumar todos los elementos
numeros = [1, 2, 3, 4, 5]
suma_total = reduce(lambda x, y: x + y, numeros)
print(suma_total)  # 15

# Encontrar el máximo
maximo = reduce(lambda x, y: x if x > y else y, numeros)
print(maximo)  # 5

# Multiplicar todos los elementos
def multiplicar(x, y):
    return x * y

factorial_5 = reduce(multiplicar, [1, 2, 3, 4, 5])
print(factorial_5)  # 120

# Con valor inicial
reduce(lambda x, y: x + y, [1, 2, 3], 10)  # 16 (10 + 1 + 2 + 3)
```

<a name = "" ></a>

### 4.4 Funcion Sorted con clave

- Sorted() con key
```python
# Ordenar por criterio personalizado
estudiantes = [
    {'nombre': 'Ana', 'edad': 22, 'nota': 8.5},
    {'nombre': 'Luis', 'edad': 20, 'nota': 9.0},
    {'nombre': 'María', 'edad': 21, 'nota': 7.5}
]

# Ordenar por nota (descendente)
por_nota = sorted(estudiantes, key=lambda x: x['nota'], reverse=True)
print([e['nombre'] for e in por_nota])  # ['Luis', 'Ana', 'María']

# Ordenar por edad
por_edad = sorted(estudiantes, key=lambda x: x['edad'])
print([e['nombre'] for e in por_edad])  # ['Luis', 'María', 'Ana']

# Ordenar strings por longitud
palabras = ["python", "java", "c++", "javascript", "go"]
por_longitud = sorted(palabras, key=len)
print(por_longitud)  # ['go', 'c++', 'java', 'python', 'javascript']
```


<a name = "5-ejercicios" ></a>

## 5. Ejercicios

1. Tienes una lista de temperaturas en grados Celsius. Usa map() para convertirlas todas a grados Fahrenheit. La fórmula es: F = (C * 9/5) + 32
```python
temperaturas_celsius = [0, 10, 20, 30, 40]
# Resultado esperado: [32.0, 50.0, 68.0, 86.0, 104.0]
```
2. Dada una lista de números, usa filter() para obtener solo los números pares.
```python
palabras = ["casa", "programacion", "python", "sol", "ordenador", "luz", "universidad"]
# Resultado esperado: ['programacion', 'ordenador', 'universidad']
```

3. Tienes una lista de diccionarios con información de estudiantes. Usa sorted() con key para ordenarlos por nota de mayor a menor.
```python
estudiantes = [
    {"nombre": "Ana", "nota": 8.5},
    {"nombre": "Luis", "nota": 7.2},
    {"nombre": "María", "nota": 9.1},
    {"nombre": "Pedro", "nota": 6.8}
]
# Resultado esperado: María (9.1), Ana (8.5), Luis (7.2), Pedro (6.8)
```

4. Dada una lista de números, usa filter() para obtener solo los números pares.
```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# Resultado esperado: [2, 4, 6, 8, 10, 12]
```

5. Dada una lista de números, usa filter() para obtener solo los números mayores a 5, y luego map() para elevarlos al cuadrado.
```python
numeros = [1, 3, 6, 8, 2, 9, 4, 7, 10]
# Resultado esperado: [36, 64, 81, 49, 100]
```

6. Crea un decorador llamado saludar que imprima "¡Hola!" antes de ejecutar cualquier función y "¡Adiós!" después de ejecutarla.
```python
@saludar
def decir_nombre(nombre):
    print(f"Mi nombre es {nombre}")

# Al llamar decir_nombre("Juan") debería imprimir:
# ¡Hola!
# Mi nombre es Juan
# ¡Adiós!
```

7. Crea un decorador llamado contar_llamadas que cuente cuántas veces se ha llamado a una función y lo imprima antes de ejecutarla.
```python
@contar_llamadas
def sumar(a, b):
    return a + b
# Primera llamada debería imprimir: "Llamada #1 a sumar"
# Segunda llamada debería imprimir: "Llamada #2 a sumar"
```

8. Crea un decorador llamado mostrar_tiempo que imprima cuánto tiempo tarda en ejecutarse una función. Usa el módulo time.
```python
import time

@mostrar_tiempo
def operacion_lenta():
    time.sleep(1)  # Simula una operación que tarda 1 segundo
    return "Operación completada"

# Debería imprimir algo como: "La función operacion_lenta tardó 1.001 segundos"
```

9. Crea un decorador llamado solo_positivos que solo permita ejecutar una función si todos sus argumentos son números positivos. Si hay algún número negativo o cero, debe imprimir "Error: Solo se permiten números positivos" y devolver None.
```python
@solo_positivos
def multiplicar(a, b):
    return a * b

@solo_positivos
def sumar_tres(a, b, c):
    return a + b + c

# multiplicar(3, 4) debería devolver 12
# multiplicar(-2, 5) debería imprimir error y devolver None
# sumar_tres(1, 2, 3) debería devolver 6
# sumar_tres(1, -2, 3) debería imprimir error y devolver None
```

10. Crea un decorador llamado repetir_tres_veces que haga que cualquier función se ejecute exactamente 3 veces seguidas.
```python

@repetir_tres_veces
def decir_algo(mensaje):
    print(mensaje)

# Al llamar decir_algo("Hola mundo") debería imprimir:
# Hola mundo
# Hola mundo
# Hola mundo
```

> [!NOTE]
> - Ya que este capítulo es algo dificil de entender te dejo estos consejos para que realices los ejercicios.
> - Recuerda que map() y filter() devuelven iteradores, usa list() para convertir a lista
> - En filter(), la función debe devolver True o False
> - En sorted() con key, especifica qué parte del elemento usar para ordenar
> - Puedes usar lambda para funciones simples: lambda x: x * 2
> - Un decorador básico tiene esta estructura:
> ```python
> def mi_decorador(func):
>     def wrapper(*args, **kwargs):
>         # Código antes de la función
>         resultado = func(*args, **kwargs)
>         # Código después de la función
>         return resultado
>     return wrapper
> ```
> - Usa *args, **kwargs para que tu decorador funcione con cualquier función
> - Para contar llamadas, puedes usar una variable global o usar wrapper.contador
> - Para medir tiempo: import time, guarda time.time() antes y después de la función

<h3 align = "center">
Este capítulo es interesante y dificil de entender por lo que te animo a que le des un par de vueltas para entenderlo que al final se consigue, te lo digo yo...
</h3>


<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/12_Modulos/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/14_Errores/readme.md">Siguiente Capítulo</a>
</h4>