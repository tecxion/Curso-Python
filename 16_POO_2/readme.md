<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/15_POO/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/17_Ficheros/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/poo_2.png">
</h1>


<h1 align="center">POO 2: Herencia, Encapsulación y Polimorfismo</h1><br>

<h3>Índice</h3>

- [1. Los pilares de la POO](#1-los-pilares-de-la-poo)
- [2. Herencia](#2-herencia)
  - [2.1 La función super()](#21-la-función-super)
  - [2.2 Sobrescribir métodos](#22-sobrescribir-métodos)
- [3. Polimorfismo](#3-polimorfismo)
- [4. Encapsulación](#4-encapsulación)
  - [4.1 Atributos privados](#41-atributos-privados)
  - [4.2 Getters, setters y @property](#42-getters-setters-y-property)
- [5. Otros métodos especiales (dunder)](#5-otros-métodos-especiales-dunder)
- [6. Ejercicios](#6-ejercicios)

<a name = "1-los-pilares-de-la-poo"></a>

## 1. Los pilares de la POO

En el día anterior aprendiste a crear clases y objetos. La POO tiene tres "pilares" que la hacen tan potente y que veremos aquí:

- **Herencia**: crear clases nuevas a partir de otras ya existentes, reaprovechando su código.
- **Encapsulación**: proteger los datos internos de un objeto para que no se modifiquen de cualquier manera.
- **Polimorfismo**: que objetos distintos respondan al mismo método cada uno a su manera.

>[!NOTE]
>A veces se menciona un cuarto pilar, la **abstracción** (centrarse en *qué* hace un objeto y no en *cómo* lo hace por dentro). Es una idea más que una herramienta concreta y la irás interiorizando con la práctica.

<a name = "2-herencia"></a>

## 2. Herencia

La **herencia** permite que una clase (**clase hija**) herede los atributos y métodos de otra (**clase padre**). Así no repetimos código: lo común se escribe una vez en el padre y cada hija añade lo suyo.

Para heredar, ponemos la clase padre entre paréntesis al definir la hija:

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

# Perro HEREDA de Animal
class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

mi_perro = Perro("Toby")
mi_perro.comer()    # heredado de Animal -> Toby está comiendo.
mi_perro.ladrar()   # propio de Perro   -> Toby dice: ¡Guau!
```

`Perro` no define `__init__` ni `comer`, pero los tiene porque los **hereda** de `Animal`.

<a name = "21-la-función-super"></a>

### 2.1 La función super()

A veces la clase hija necesita su propio `__init__` pero **además** quiere ejecutar el del padre. Para eso usamos **`super()`**, que hace referencia a la clase padre:

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)   # ejecuta el __init__ de Animal
        self.raza = raza           # y añade lo suyo

mi_perro = Perro("Luna", "Beagle")
print(mi_perro.nombre)   # Luna  (lo gestionó el padre)
print(mi_perro.raza)     # Beagle
```

<a name = "22-sobrescribir-métodos"></a>

### 2.2 Sobrescribir métodos

Una clase hija puede **redefinir** (sobrescribir) un método del padre para cambiar su comportamiento. Basta con declarar un método con el mismo nombre:

```python
class Animal:
    def hacer_sonido(self):
        print("Sonido genérico de animal")

class Gato(Animal):
    def hacer_sonido(self):     # sobrescribe el del padre
        print("¡Miau!")

Animal().hacer_sonido()   # Sonido genérico de animal
Gato().hacer_sonido()     # ¡Miau!
```

<a name = "3-polimorfismo"></a>

## 3. Polimorfismo

**Polimorfismo** significa "muchas formas". En la práctica: podemos tratar objetos de clases distintas de la misma manera si comparten un método con el mismo nombre, y cada uno responderá a su forma.

```python
class Perro:
    def hablar(self):
        return "Guau"

class Gato:
    def hablar(self):
        return "Miau"

class Vaca:
    def hablar(self):
        return "Muuu"

# El mismo bucle funciona con cualquier objeto que tenga hablar()
animales = [Perro(), Gato(), Vaca()]
for animal in animales:
    print(animal.hablar())   # Guau / Miau / Muuu
```

No nos importa de qué clase es cada animal: si tiene el método `hablar()`, funciona. Esto hace el código mucho más flexible.

<a name = "4-encapsulación"></a>

## 4. Encapsulación

La **encapsulación** consiste en **proteger** los datos internos de un objeto para que no se modifiquen desde fuera sin control, y obligar a usar los métodos que nosotros decidimos.

<a name = "41-atributos-privados"></a>

### 4.1 Atributos privados

En Python, por convención, un atributo que empieza por **doble guion bajo** (`__`) se considera **privado**: no debería tocarse directamente desde fuera de la clase.

```python
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo   # atributo privado

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def consultar_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria(100)
cuenta.ingresar(50)
print(cuenta.consultar_saldo())   # 150
# print(cuenta.__saldo)  -> AttributeError: no se accede directamente
```

Así nos aseguramos de que nadie ponga un saldo negativo "a mano": **solo** se puede modificar a través de los métodos que hemos definido.

<a name = "42-getters-setters-y-property"></a>

### 4.2 Getters, setters y @property

Los **getters** (obtener) y **setters** (modificar) son métodos para leer y escribir atributos privados de forma controlada. Python ofrece una forma elegante con el decorador **`@property`** (¿recuerdas los decoradores del día 13?):

```python
class Persona:
    def __init__(self, edad):
        self.__edad = edad

    @property              # getter: se usa como si fuera un atributo
    def edad(self):
        return self.__edad

    @edad.setter           # setter: validamos antes de asignar
    def edad(self, nueva_edad):
        if nueva_edad < 0:
            print("La edad no puede ser negativa.")
        else:
            self.__edad = nueva_edad

persona = Persona(30)
print(persona.edad)     # 30  (usa el getter, sin paréntesis)
persona.edad = 35       # usa el setter
print(persona.edad)     # 35
persona.edad = -5       # La edad no puede ser negativa.
```

<a name = "5-otros-métodos-especiales-dunder"></a>

## 5. Otros métodos especiales (dunder)

Además de `__init__` y `__str__`, existen muchos métodos especiales que personalizan cómo se comportan nuestros objetos con las operaciones de Python:

| Método | Para qué sirve | Se activa con |
| ----------- | --------------------------------- | ----------------- |
| `__init__` | Constructor | `Clase(...)` |
| `__str__` | Texto legible para el usuario | `print(obj)` |
| `__len__` | Longitud del objeto | `len(obj)` |
| `__eq__` | Comparar si dos objetos son iguales | `obj1 == obj2` |
| `__add__` | Sumar dos objetos | `obj1 + obj2` |

```python
class Carrito:
    def __init__(self):
        self.productos = []

    def añadir(self, producto):
        self.productos.append(producto)

    def __len__(self):
        return len(self.productos)

carrito = Carrito()
carrito.añadir("pan")
carrito.añadir("leche")
print(len(carrito))   # 2  (gracias a __len__)
```

<a name = "6-ejercicios"></a>

## 6. Ejercicios

1. Crea una clase `Animal` con un atributo `nombre` y un método `describir()`. Crea una clase `Perro` que herede de `Animal` y añada un método `ladrar()`.

2. Crea una clase `Vehiculo` con `marca` y `ruedas`, y un método `arrancar()`. Crea `Moto` y `Camion` que hereden de `Vehiculo` y usen `super().__init__()` para definir las ruedas (2 y 6).

3. Crea una clase `Figura` con un método `area()` que devuelva 0. Crea `Cuadrado` y `Triangulo` que hereden de ella y **sobrescriban** `area()` con su fórmula correcta.

4. Aprovechando el ejercicio anterior, crea una lista con varias figuras distintas y recórrela con un bucle imprimiendo el área de cada una (polimorfismo).

5. Crea una clase `CuentaBancaria` con un atributo **privado** `__saldo`. Añade `ingresar()`, `retirar()` (sin permitir negativos) y `consultar_saldo()`.

6. Crea una clase `Temperatura` con un atributo privado `__grados`. Usa `@property` para el getter y un setter que no permita valores por debajo de -273 (cero absoluto).

7. Crea una clase `Empleado` con `nombre` y `sueldo`, y una clase `Gerente` que herede de ella, añada el atributo `equipo` (lista de empleados a su cargo) y un método para añadir empleados.

8. Crea una clase `Punto` con coordenadas `x` e `y`. Implementa `__str__` para que se imprima como `(x, y)` y `__add__` para poder sumar dos puntos y obtener un nuevo `Punto`.

> [!NOTE]
> Pistas para los ejercicios:
> - Para heredar: `class Hija(Padre):`.
> - Para llamar al constructor del padre: `super().__init__(parametros)`.
> - Sobrescribir un método = definir en la hija uno con el mismo nombre.
> - Un atributo privado empieza por `__` (dos guiones bajos): `self.__saldo`.
> - El getter lleva `@property` encima; el setter lleva `@nombre.setter`.
> - En `__add__(self, otro)` devuelve un objeto nuevo: `return Punto(self.x + otro.x, self.y + otro.y)`.

<h3 align = "center">
¡Ya dominas las clases! Con esto tienes la base para organizar programas grandes. Ahora aprenderemos a guardar y leer información en ficheros para que no se pierda al cerrar el programa.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/15_POO/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/17_Ficheros/readme.md">Día siguiente</a>
</h4>
