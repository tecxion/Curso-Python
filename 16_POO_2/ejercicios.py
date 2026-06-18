"""
Ejercicios de POO 2: Herencia, Encapsulación y Polimorfismo
"""

# 1. Animal (padre) y Perro (hija) con herencia.
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def describir(self):
        print(f"Soy {self.nombre} y soy un animal.")

class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

mi_perro = Perro("Toby")
mi_perro.describir()   # heredado
mi_perro.ladrar()      # propio


# 2. Vehiculo con Moto y Camion usando super().__init__().
class Vehiculo:
    def __init__(self, marca, ruedas):
        self.marca = marca
        self.ruedas = ruedas

    def arrancar(self):
        print(f"El {self.marca} de {self.ruedas} ruedas arranca.")

class Moto(Vehiculo):
    def __init__(self, marca):
        super().__init__(marca, 2)

class Camion(Vehiculo):
    def __init__(self, marca):
        super().__init__(marca, 6)

Moto("Honda").arrancar()      # 2 ruedas
Camion("Volvo").arrancar()    # 6 ruedas


# 3 y 4. Figura con Cuadrado y Triangulo (sobrescritura + polimorfismo).
class Figura:
    def area(self):
        return 0

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

figuras = [Cuadrado(4), Triangulo(6, 3), Cuadrado(2)]
for figura in figuras:
    print(f"Área: {figura.area()}")   # polimorfismo: cada una calcula la suya


# 5. CuentaBancaria con atributo privado __saldo.
class CuentaBancaria:
    def __init__(self, saldo=0):
        self.__saldo = saldo

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            print("Saldo insuficiente.")
        else:
            self.__saldo -= cantidad

    def consultar_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria(100)
cuenta.ingresar(50)
cuenta.retirar(30)
print(f"Saldo: {cuenta.consultar_saldo()}€")  # 120


# 6. Temperatura con @property y setter (cero absoluto).
class Temperatura:
    def __init__(self, grados):
        self.__grados = grados

    @property
    def grados(self):
        return self.__grados

    @grados.setter
    def grados(self, valor):
        if valor < -273:
            print("Imposible: por debajo del cero absoluto.")
        else:
            self.__grados = valor

temp = Temperatura(20)
print(temp.grados)     # 20
temp.grados = 35
print(temp.grados)     # 35
temp.grados = -300     # mensaje de error


# 7. Empleado y Gerente (que gestiona un equipo).
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

class Gerente(Empleado):
    def __init__(self, nombre, sueldo):
        super().__init__(nombre, sueldo)
        self.equipo = []

    def añadir_empleado(self, empleado):
        self.equipo.append(empleado)
        print(f"{empleado.nombre} ahora trabaja con {self.nombre}.")

jefa = Gerente("Ana", 3000)
jefa.añadir_empleado(Empleado("Luis", 1800))
jefa.añadir_empleado(Empleado("Marta", 1900))
print(f"{jefa.nombre} tiene {len(jefa.equipo)} personas a cargo.")


# 8. Punto con __str__ y __add__.
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

p1 = Punto(1, 2)
p2 = Punto(3, 4)
print(p1)          # (1, 2)
print(p1 + p2)     # (4, 6)
