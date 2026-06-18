<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/21_Regex/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/23_Decoradores_Avanzados/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/type_hints.png">
</h1>


<h1 align="center">Anotaciones de Tipo y Dataclasses</h1><br>

<h3>Índice</h3>

- [1. Tipado dinámico vs anotaciones](#1-tipado-dinámico-vs-anotaciones)
- [2. Anotar variables](#2-anotar-variables)
- [3. Anotar funciones](#3-anotar-funciones)
- [4. Tipos de colecciones](#4-tipos-de-colecciones)
- [5. Optional y valores que pueden faltar](#5-optional-y-valores-que-pueden-faltar)
- [6. Las dataclasses](#6-las-dataclasses)
- [7. Dataclasses con valores por defecto y métodos](#7-dataclasses-con-valores-por-defecto-y-métodos)
- [8. Ejercicios](#8-ejercicios)

<a name = "1-tipado-dinámico-vs-anotaciones"></a>

## 1. Tipado dinámico vs anotaciones

Python es un lenguaje de **tipado dinámico**: una variable puede guardar un número y luego un texto, sin avisar. Eso es cómodo, pero en proyectos grandes provoca errores difíciles de encontrar.

Las **anotaciones de tipo** (*type hints*) nos permiten **indicar** qué tipo esperamos en una variable, un parámetro o lo que devuelve una función. Es una forma de documentar y de que los editores (como VS Code) nos avisen de errores antes de ejecutar.

>[!IMPORTANT]
>Las anotaciones son **solo informativas**: Python NO las comprueba al ejecutar. Si anotas que algo es un `int` y le pasas un `str`, el programa no falla por ello. Sirven para ti, para tu equipo y para las herramientas de análisis. Aun así, escribir código anotado es señal de profesionalidad.

<a name = "2-anotar-variables"></a>

## 2. Anotar variables

Se anota con dos puntos y el tipo después del nombre:

```python
nombre: str = "Ana"
edad: int = 30
altura: float = 1.75
activo: bool = True
```

Es muy parecido a lo que hacías en otros lenguajes que ya conoces, como Java o Dart.

<a name = "3-anotar-funciones"></a>

## 3. Anotar funciones

Aquí es donde las anotaciones brillan. Indicamos el tipo de cada parámetro y, tras la flecha `->`, el tipo que devuelve la función:

```python
def sumar(a: int, b: int) -> int:
    return a + b

def saludar(nombre: str) -> str:
    return f"Hola, {nombre}"

def es_mayor(edad: int) -> bool:
    return edad >= 18
```

Cuando una función no devuelve nada, se anota con `-> None`:

```python
def imprimir_titulo(texto: str) -> None:
    print(texto.upper())
```

Solo con leer la firma `def sumar(a: int, b: int) -> int:` ya sabes exactamente cómo se usa la función, sin mirar su contenido.

<a name = "4-tipos-de-colecciones"></a>

## 4. Tipos de colecciones

Podemos detallar qué contienen las listas, diccionarios, etc. A partir de Python 3.9 se usan directamente `list`, `dict`, `tuple`, `set`:

```python
def media(notas: list[float]) -> float:
    return sum(notas) / len(notas)

def contar_palabras(texto: str) -> dict[str, int]:
    conteo: dict[str, int] = {}
    for palabra in texto.split():
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

coordenadas: tuple[int, int] = (10, 20)
nombres: list[str] = ["Ana", "Luis"]
```

`list[float]` significa "una lista de números decimales"; `dict[str, int]` significa "un diccionario cuyas claves son texto y sus valores enteros".

<a name = "5-optional-y-valores-que-pueden-faltar"></a>

## 5. Optional y valores que pueden faltar

A veces un valor puede ser de un tipo **o** ser `None`. Para eso se usa `| None` (en versiones modernas) o `Optional` del módulo `typing`:

```python
def buscar_usuario(id: int) -> str | None:
    usuarios = {1: "Ana", 2: "Luis"}
    return usuarios.get(id)   # devuelve el nombre o None si no existe

resultado = buscar_usuario(3)
if resultado is None:
    print("No encontrado")
```

`str | None` significa "un texto o nada". Es muy habitual en funciones que buscan algo que puede no estar.

>[!NOTE]
>La sintaxis `tipo | None` necesita Python 3.10 o superior. Si usas una versión más antigua, añade `from __future__ import annotations` al principio del archivo (como verás en los ejercicios) o usa `Optional[str]` importándolo con `from typing import Optional`.

<a name = "6-las-dataclasses"></a>

## 6. Las dataclasses

¿Recuerdas las clases del día 15? Cuando una clase solo sirve para **guardar datos**, escribir el `__init__` y el `__str__` a mano es repetitivo. Las **dataclasses** automatizan todo eso con un decorador.

Compara la versión clásica con la dataclass:

```python
# Versión clásica (día 15)
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"
```

```python
# La MISMA clase con una dataclass
from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: int

p = Persona("Ana", 30)
print(p)            # Persona(nombre='Ana', edad=30)  ¡__str__ gratis!
print(p.nombre)     # Ana
print(p == Persona("Ana", 30))   # True  ¡comparación gratis!
```

Con `@dataclass`, Python genera **automáticamente** el `__init__`, el `__str__` (en realidad `__repr__`) y el `__eq__` a partir de los atributos anotados. Mucho menos código.

<a name = "7-dataclasses-con-valores-por-defecto-y-métodos"></a>

## 7. Dataclasses con valores por defecto y métodos

Las dataclasses admiten valores por defecto y también pueden tener sus propios métodos, igual que cualquier clase:

```python
from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    precio: float
    stock: int = 0          # valor por defecto

    def valor_total(self) -> float:
        return self.precio * self.stock

camiseta = Producto("Camiseta", 19.99, 10)
print(camiseta)                 # Producto(nombre='Camiseta', precio=19.99, stock=10)
print(camiseta.valor_total())   # 199.9
```

>[!NOTE]
>Igual que con las funciones normales, en las dataclasses los atributos con valor por defecto deben ir **después** de los que no lo tienen.

<a name = "8-ejercicios"></a>

## 8. Ejercicios

1. Anota una función `multiplicar(a, b)` que reciba dos enteros y devuelva un entero.

2. Anota una función `nombre_completo(nombre, apellido)` que reciba dos textos y devuelva un texto.

3. Anota una función `promedio(numeros)` que reciba una lista de `float` y devuelva un `float`.

4. Anota una función `inicial(nombre)` que devuelva la primera letra, y otra `buscar(id)` que devuelva un `str` o `None`.

5. Crea una dataclass `Libro` con `titulo` (str), `autor` (str) y `año` (int). Crea un objeto y muéstralo.

6. Añade a la dataclass `Libro` un atributo `prestado` (bool) con valor por defecto `False` y un método `prestar()` que lo ponga a `True`.

7. Crea una dataclass `Punto` con `x` e `y` (int) y un método `distancia_al_origen()` que devuelva la distancia (raíz cuadrada de x² + y²).

8. Crea una dataclass `CuentaBancaria` con `titular` (str) y `saldo` (float, por defecto 0). Añade métodos `ingresar()` y `retirar()` (sin permitir negativos).

> [!NOTE]
> Pistas para los ejercicios:
> - La sintaxis es `def funcion(parametro: tipo) -> tipo_que_devuelve:`.
> - Si no devuelve nada, anota `-> None`.
> - Para "texto o nada" usa `str | None`.
> - Para usar dataclasses: `from dataclasses import dataclass` y pon `@dataclass` encima de la clase.
> - En una dataclass los atributos se declaran anotados: `nombre: tipo`.
> - Para la distancia: `(self.x ** 2 + self.y ** 2) ** 0.5`.

<h3 align = "center">
¡Tu código ahora es más claro y profesional! Mañana volvemos a los decoradores, pero esta vez a fondo: functools y decoradores con parámetros.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/21_Regex/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/23_Decoradores_Avanzados/readme.md">Día siguiente</a>
</h4>
