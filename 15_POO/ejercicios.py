"""
Ejercicios de Programación Orientada a Objetos (POO)
"""

# 1. Clase Persona con nombre y edad. Crea dos objetos y muestra sus datos.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # 2. Método saludar()
    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

persona1 = Persona("Ana", 25)
persona2 = Persona("Luis", 40)
print(persona1.nombre, persona1.edad)   # Ana 25
print(persona2.nombre, persona2.edad)   # Luis 40
persona1.saludar()
persona2.saludar()


# 3. Clase CuentaBancaria con ingresar y retirar (sin saldo negativo).
class CuentaBancaria:
    def __init__(self):
        self.saldo = 0

    def ingresar(self, cantidad):
        self.saldo += cantidad
        print(f"Ingresados {cantidad}€. Saldo: {self.saldo}€")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("No tienes saldo suficiente.")
        else:
            self.saldo -= cantidad
            print(f"Retirados {cantidad}€. Saldo: {self.saldo}€")

cuenta = CuentaBancaria()
cuenta.ingresar(100)
cuenta.retirar(30)
cuenta.retirar(200)


# 4. Clase Rectangulo con area() y perimetro().
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

rectangulo = Rectangulo(4, 3)
print(f"Área: {rectangulo.area()}")          # 12
print(f"Perímetro: {rectangulo.perimetro()}") # 14


# 5. Clase Circulo con atributo de clase PI y método area().
class Circulo:
    PI = 3.1416   # atributo de clase

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return Circulo.PI * self.radio ** 2

circulo = Circulo(5)
print(f"Área del círculo: {circulo.area()}")  # 78.54


# 6. Clase Producto con vender() y __str__.
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad > self.stock:
            print(f"No hay stock suficiente de {self.nombre}.")
        else:
            self.stock -= cantidad
            print(f"Vendidas {cantidad} unidades de {self.nombre}.")

    def __str__(self):
        return f"{self.nombre} | {self.precio}€ | stock: {self.stock}"

camiseta = Producto("Camiseta", 19.99, 10)
camiseta.vender(3)
camiseta.vender(20)
print(camiseta)


# 7. Clase Coche con acelerar, frenar y __str__.
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self, cantidad):
        self.velocidad += cantidad

    def frenar(self):
        self.velocidad = 0

    def __str__(self):
        return f"{self.marca} {self.modelo} a {self.velocidad} km/h"

coche = Coche("Seat", "Ibiza")
coche.acelerar(60)
print(coche)        # Seat Ibiza a 60 km/h
coche.frenar()
print(coche)        # Seat Ibiza a 0 km/h


# 8. Clase Estudiante con agregar_nota() y media().
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

estudiante = Estudiante("Marta")
estudiante.agregar_nota(8)
estudiante.agregar_nota(6)
estudiante.agregar_nota(10)
print(f"Media de {estudiante.nombre}: {estudiante.media()}")  # 8.0
