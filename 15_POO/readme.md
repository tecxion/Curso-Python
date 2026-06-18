<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/14_Errores/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/16_POO_2/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/poo.png">
</h1>


<h1 align="center">Programación Orientada a Objetos (POO)</h1><br>

<h3>Índice</h3>

- [1. ¿Qué es la Programación Orientada a Objetos?](#1-qué-es-la-programación-orientada-a-objetos)
- [2. Clases y objetos](#2-clases-y-objetos)
- [3. El método __init__ y self](#3-el-método-__init__-y-self)
- [4. Atributos](#4-atributos)
- [5. Métodos](#5-métodos)
- [6. Atributos de clase vs atributos de instancia](#6-atributos-de-clase-vs-atributos-de-instancia)
- [7. El método __str__](#7-el-método-__str__)
- [8. Ejercicios](#8-ejercicios)

<a name = "1-qué-es-la-programación-orientada-a-objetos"></a>

## 1. ¿Qué es la Programación Orientada a Objetos?

Hasta ahora hemos programado de forma **estructurada**: variables sueltas y funciones que las manipulan. La **Programación Orientada a Objetos** (POO, o *OOP* en inglés) es otra forma de organizar el código que consiste en **agrupar en un mismo sitio los datos y las acciones que trabajan con esos datos**.

Piensa en un coche del mundo real:
- Tiene **características**: marca, color, velocidad… → en POO los llamamos **atributos**.
- Puede hacer **cosas**: arrancar, acelerar, frenar… → en POO los llamamos **métodos**.

La POO nos permite crear nuestros propios "tipos de dato" a medida. Es la base de casi todo el software moderno, así que este día es uno de los más importantes del curso.

>[!NOTE]
>De hecho ya has usado objetos sin saberlo: una lista es un objeto y `.append()` es uno de sus métodos. Ahora aprenderás a crear los tuyos.

<a name = "2-clases-y-objetos"></a>

## 2. Clases y objetos

Hay dos conceptos clave que no debes confundir:

- Una **clase** es la **plantilla** o el molde. Define cómo serán los objetos. Por ejemplo, el plano de una casa.
- Un **objeto** (o *instancia*) es algo **concreto** creado a partir de esa plantilla. Por ejemplo, tu casa construida a partir del plano.

A partir de **una sola clase** podemos crear **muchos objetos**.

Las clases se crean con la palabra reservada **`class`** y por convención su nombre se escribe en **MayúsculaInicial** (estilo `CamelCase`):

```python
class Perro:
    pass   # de momento vacía

# Creamos dos objetos (instancias) de la clase Perro
mi_perro = Perro()
otro_perro = Perro()

print(type(mi_perro))   # <class '__main__.Perro'>
```

<a name = "3-el-método-__init__-y-self"></a>

## 3. El método __init__ y self

El método **`__init__`** es un método especial llamado **constructor**. Python lo ejecuta **automáticamente** cada vez que creamos un objeto, y sirve para darle sus valores iniciales.

El parámetro **`self`** representa **al propio objeto** que se está creando. Gracias a `self` cada objeto guarda sus propios datos. **Siempre** es el primer parámetro de los métodos.

```python
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre   # guardamos los datos dentro del objeto
        self.raza = raza

# Al crear el objeto pasamos los datos que pide __init__
mi_perro = Perro("Toby", "Labrador")
otro_perro = Perro("Luna", "Pastor Alemán")

print(mi_perro.nombre)   # Toby
print(otro_perro.raza)   # Pastor Alemán
```

>[!IMPORTANT]
>`__init__` lleva **doble guion bajo** delante y detrás (se les llama métodos *dunder*, de *double underscore*). No lo llamamos nosotros directamente: Python lo llama solo al crear el objeto.

<a name = "4-atributos"></a>

## 4. Atributos

Los **atributos** son las variables que viven dentro de un objeto y guardan su información. Accedemos a ellos con un **punto**: `objeto.atributo`.

```python
class Coche:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        self.velocidad = 0   # un atributo con valor inicial fijo

mi_coche = Coche("Seat", "rojo")

# Leer un atributo
print(mi_coche.marca)        # Seat

# Modificar un atributo
mi_coche.color = "azul"
print(mi_coche.color)        # azul
```

<a name = "5-métodos"></a>

## 5. Métodos

Los **métodos** son funciones definidas **dentro** de una clase. Representan las acciones que puede hacer el objeto. Su primer parámetro siempre es `self`, que les permite acceder y modificar los atributos del objeto.

```python
class Coche:
    def __init__(self, marca):
        self.marca = marca
        self.velocidad = 0

    def acelerar(self, cantidad):
        self.velocidad += cantidad
        print(f"El {self.marca} ahora va a {self.velocidad} km/h")

    def frenar(self):
        self.velocidad = 0
        print(f"El {self.marca} se ha detenido")

mi_coche = Coche("Toyota")
mi_coche.acelerar(50)   # El Toyota ahora va a 50 km/h
mi_coche.acelerar(30)   # El Toyota ahora va a 80 km/h
mi_coche.frenar()       # El Toyota se ha detenido
```

Fíjate en que al llamar al método (`mi_coche.acelerar(50)`) **no pasamos `self`**: Python lo hace por nosotros automáticamente.

<a name = "6-atributos-de-clase-vs-atributos-de-instancia"></a>

## 6. Atributos de clase vs atributos de instancia

- **Atributo de instancia**: pertenece a cada objeto concreto (se define con `self.` dentro de `__init__`). Cada objeto tiene el suyo.
- **Atributo de clase**: se define directamente dentro de la clase y es **compartido por todos** los objetos.

```python
class Empleado:
    empresa = "TecXion"   # atributo de CLASE (igual para todos)

    def __init__(self, nombre, sueldo):
        self.nombre = nombre   # atributos de INSTANCIA (propios de cada uno)
        self.sueldo = sueldo

emp1 = Empleado("Ana", 1800)
emp2 = Empleado("Luis", 2200)

print(emp1.empresa)   # TecXion
print(emp2.empresa)   # TecXion (compartido)
print(emp1.nombre)    # Ana
print(emp2.nombre)    # Luis
```

<a name = "7-el-método-__str__"></a>

## 7. El método __str__

Si imprimimos un objeto directamente, Python nos muestra algo poco útil como `<__main__.Coche object at 0x104f...>`. El método especial **`__str__`** nos permite definir **cómo se ve** un objeto cuando lo imprimimos con `print()`:

```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} -> {self.precio}€"

camiseta = Producto("Camiseta", 19.99)
print(camiseta)   # Camiseta -> 19.99€
```

Sin `__str__` obtendríamos un texto ilegible; con él, nuestros objetos se imprimen de forma clara.

<a name = "8-ejercicios"></a>

## 8. Ejercicios

1. Crea una clase `Persona` con los atributos `nombre` y `edad`. Crea dos objetos y muestra sus datos por pantalla.

2. Añade a la clase `Persona` un método `saludar()` que imprima `"Hola, me llamo X y tengo Y años"`.

3. Crea una clase `CuentaBancaria` con un atributo `saldo` (que empiece en 0) y los métodos `ingresar(cantidad)` y `retirar(cantidad)`. `retirar` no debe permitir dejar el saldo en negativo (avisa con un mensaje).

4. Crea una clase `Rectangulo` con atributos `base` y `altura`, y métodos `area()` y `perimetro()` que devuelvan sus valores.

5. Crea una clase `Circulo` con un atributo `radio` y un método `area()` (usa `3.1416 * radio ** 2`). Añade un atributo de clase `PI = 3.1416` y úsalo dentro del método.

6. Crea una clase `Producto` con `nombre`, `precio` y `stock`. Añade el método `vender(cantidad)` que reste del stock (controlando que haya suficiente) y un método `__str__` que muestre el producto bonito.

7. Crea una clase `Coche` con `marca`, `modelo` y `velocidad` (inicial 0). Añade `acelerar()`, `frenar()` y un `__str__`. Crea un coche y prueba sus métodos.

8. Crea una clase `Estudiante` con `nombre` y una lista de `notas` (vacía al principio). Añade `agregar_nota(nota)` y `media()` que devuelva la nota media (cuidado con la lista vacía).

> [!NOTE]
> Pistas para los ejercicios:
> - Toda clase empieza por `class NombreClase:` y casi siempre lleva un `def __init__(self, ...):`.
> - Recuerda guardar los datos con `self.atributo = valor` dentro de `__init__`.
> - El primer parámetro de **todos** los métodos es `self`.
> - Para crear un objeto: `p = Persona("Ana", 25)` y para usar un método `p.saludar()`.
> - Una lista vacía de notas se crea con `self.notas = []`.
> - Para la media: `sum(self.notas) / len(self.notas)` (comprueba antes que la lista no esté vacía).

<h3 align = "center">
¡Acabas de aprender el pilar de la programación moderna! En el siguiente día veremos cómo unas clases pueden heredar de otras: herencia, encapsulación y polimorfismo.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/14_Errores/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/16_POO_2/readme.md">Día siguiente</a>
</h4>
