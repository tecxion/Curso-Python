<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/22_Type_Hints/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/24_Itertools/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/decoradores.png">
</h1>


<h1 align="center">Decoradores Avanzados y functools</h1><br>

<h3>Índice</h3>

- [1. Repaso rápido de decoradores](#1-repaso-rápido-de-decoradores)
- [2. El problema de los metadatos: functools.wraps](#2-el-problema-de-los-metadatos-functoolswraps)
- [3. Decoradores con parámetros](#3-decoradores-con-parámetros)
- [4. functools.lru_cache: memoización gratis](#4-functoolslru_cache-memoización-gratis)
- [5. functools.reduce y functools.partial](#5-functoolsreduce-y-functoolspartial)
- [6. Un caso real: decorador de reintentos](#6-un-caso-real-decorador-de-reintentos)
- [7. Ejercicios](#7-ejercicios)

<a name = "1-repaso-rápido-de-decoradores"></a>

## 1. Repaso rápido de decoradores

En el día 13 viste los decoradores: funciones que **envuelven** a otra para añadirle comportamiento sin tocar su código. Recordemos la estructura base:

```python
def mi_decorador(func):
    def wrapper(*args, **kwargs):
        # algo antes
        resultado = func(*args, **kwargs)
        # algo después
        return resultado
    return wrapper

@mi_decorador
def saludar(nombre):
    return f"Hola {nombre}"
```

Hoy vamos un paso más allá: arreglaremos un problema que tienen los decoradores "caseros" y conoceremos el módulo **`functools`**, una caja de herramientas para trabajar con funciones.

<a name = "2-el-problema-de-los-metadatos-functoolswraps"></a>

## 2. El problema de los metadatos: functools.wraps

Cuando decoramos una función, esta "pierde" su identidad: su nombre y su documentación pasan a ser los del `wrapper`. Míralo:

```python
def mi_decorador(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@mi_decorador
def sumar(a, b):
    """Suma dos números."""
    return a + b

print(sumar.__name__)   # wrapper  ❌  (¡debería ser 'sumar'!)
print(sumar.__doc__)    # None      ❌  (perdimos la documentación)
```

La solución es decorar el `wrapper` con **`@functools.wraps(func)`**, que copia el nombre, la documentación y demás metadatos de la función original:

```python
import functools

def mi_decorador(func):
    @functools.wraps(func)          # ✅ conserva la identidad de func
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@mi_decorador
def sumar(a, b):
    """Suma dos números."""
    return a + b

print(sumar.__name__)   # sumar  ✅
print(sumar.__doc__)    # Suma dos números.  ✅
```

>[!IMPORTANT]
>Usa **siempre** `@functools.wraps(func)` al crear decoradores. Es la marca de un decorador bien hecho y evita errores raros al depurar.

<a name = "3-decoradores-con-parámetros"></a>

## 3. Decoradores con parámetros

¿Y si queremos un decorador al que poder pasarle opciones, como `@repetir(3)`? Necesitamos **una capa más**: una función que recibe los parámetros y devuelve el decorador.

Son **tres niveles** de funciones anidadas:

```python
import functools

def repetir(veces):                     # 1) recibe el parámetro
    def decorador(func):                 # 2) recibe la función
        @functools.wraps(func)
        def wrapper(*args, **kwargs):    # 3) recibe los argumentos
            for _ in range(veces):
                resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorador

@repetir(3)
def saludar():
    print("¡Hola!")

saludar()
# ¡Hola!
# ¡Hola!
# ¡Hola!
```

Léelo de fuera hacia dentro: `repetir(3)` devuelve un decorador, y ese decorador envuelve a `saludar`.

<a name = "4-functoolslru_cache-memoización-gratis"></a>

## 4. functools.lru_cache: memoización gratis

La **memoización** consiste en **recordar** el resultado de una función para no recalcularlo si la vuelves a llamar con los mismos argumentos. `functools` nos lo regala con el decorador **`@lru_cache`**.

El ejemplo clásico es Fibonacci recursivo, que sin caché es lentísimo porque repite millones de cálculos:

```python
import functools

@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))   # 12586269025  -> instantáneo gracias a la caché
```

Sin `@lru_cache`, calcular `fibonacci(50)` tardaría una eternidad. Con él, cada valor se calcula **una sola vez**. La caché funciona como un diccionario interno: "argumentos → resultado".

<a name = "5-functoolsreduce-y-functoolspartial"></a>

## 5. functools.reduce y functools.partial

`functools` trae más utilidades muy prácticas:

- **`reduce`** (ya lo viste en el día 13): combina todos los elementos de un iterable en un único valor.
- **`partial`**: crea una versión "pre-rellenada" de una función, fijando algunos de sus argumentos.

```python
from functools import reduce, partial

# reduce: multiplicar todos los números
producto = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(producto)   # 24

# partial: a partir de una función general, creamos otras más concretas
def potencia(base, exponente):
    return base ** exponente

cuadrado = partial(potencia, exponente=2)   # fijamos exponente=2
cubo = partial(potencia, exponente=3)       # fijamos exponente=3

print(cuadrado(5))   # 25
print(cubo(2))       # 8
```

`partial` es útil cuando llamas muchas veces a una función con los mismos argumentos: te ahorras repetirlos.

<a name = "6-un-caso-real-decorador-de-reintentos"></a>

## 6. Un caso real: decorador de reintentos

Juntemos todo en un decorador útil de verdad: uno que **reintenta** una función si lanza una excepción (algo habitual al trabajar con internet o ficheros).

```python
import functools

def reintentar(intentos):
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for intento in range(1, intentos + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    print(f"Intento {intento} falló: {error}")
            print("Se agotaron los intentos.")
        return wrapper
    return decorador

@reintentar(3)
def operacion_inestable(numero):
    if numero < 0:
        raise ValueError("Número negativo")
    return numero * 2

print(operacion_inestable(5))    # 10  (a la primera)
operacion_inestable(-1)          # reintenta 3 veces y se rinde
```

Fíjate cuánto del curso hay aquí: decoradores con parámetros, `*args/**kwargs`, manejo de errores (día 14) y `functools.wraps`.

<a name = "7-ejercicios"></a>

## 7. Ejercicios

1. Crea un decorador `mayusculas` que convierta a mayúsculas el texto que devuelva la función decorada. Usa `functools.wraps`.

2. Comprueba que tu decorador conserva el nombre original: imprime `func.__name__` de una función decorada y verifica que NO dice "wrapper".

3. Crea un decorador con parámetro `repetir(veces)` que ejecute la función el número de veces indicado.

4. Crea un decorador con parámetro `mensaje(texto)` que imprima ese texto antes de ejecutar la función.

5. Usa `@lru_cache` en una función `factorial(n)` recursiva y calcula `factorial(100)`.

6. Usa `functools.partial` para crear, a partir de una función `saludar(saludo, nombre)`, una función `hola(nombre)` que siempre salude con "Hola".

7. Usa `functools.reduce` para encontrar el número mayor de una lista sin usar la función `max`.

8. Crea un decorador `medir_tiempo` (con `functools.wraps` y el módulo `time`) que imprima cuánto tarda la función decorada.

> [!NOTE]
> Pistas para los ejercicios:
> - Empieza siempre por `import functools` (o `from functools import ...`).
> - Recuerda los TRES niveles para un decorador con parámetros: parámetro → función → wrapper.
> - `@lru_cache` se importa con `from functools import lru_cache` y se pone encima de la función.
> - `partial(funcion, argumento_fijo=valor)` crea una nueva función con ese argumento ya puesto.
> - Para medir tiempo: `import time`, guarda `time.time()` antes y después.

<h3 align = "center">
¡Ahora sí dominas los decoradores de verdad! Mañana exprimimos los iterables con el módulo itertools.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/22_Type_Hints/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/24_Itertools/readme.md">Día siguiente</a>
</h4>
