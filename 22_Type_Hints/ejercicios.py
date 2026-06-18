"""
Ejercicios de Anotaciones de Tipo y Dataclasses
"""
# Esta línea hace que las anotaciones no se evalúen al ejecutar.
# Permite usar la sintaxis moderna "str | None" aunque tengas una
# versión de Python anterior a la 3.10. Es una práctica habitual.
from __future__ import annotations
from dataclasses import dataclass

# 1. multiplicar(a, b) -> int
def multiplicar(a: int, b: int) -> int:
    return a * b
print(multiplicar(3, 4))   # 12


# 2. nombre_completo(nombre, apellido) -> str
def nombre_completo(nombre: str, apellido: str) -> str:
    return f"{nombre} {apellido}"
print(nombre_completo("Ana", "García"))


# 3. promedio(numeros) -> float
def promedio(numeros: list[float]) -> float:
    return sum(numeros) / len(numeros)
print(promedio([8.0, 6.5, 9.0]))


# 4. inicial(nombre) -> str  y  buscar(id) -> str | None
def inicial(nombre: str) -> str:
    return nombre[0]

def buscar(id: int) -> str | None:
    usuarios = {1: "Ana", 2: "Luis"}
    return usuarios.get(id)

print(inicial("Python"))   # P
print(buscar(1))           # Ana
print(buscar(9))           # None


# 5. Dataclass Libro.
@dataclass
class Libro:
    titulo: str
    autor: str
    año: int
    # 6. atributo con valor por defecto + método prestar()
    prestado: bool = False

    def prestar(self) -> None:
        self.prestado = True

libro = Libro("El Quijote", "Cervantes", 1605)
print(libro)
libro.prestar()
print(f"¿Prestado? {libro.prestado}")


# 7. Dataclass Punto con distancia_al_origen().
@dataclass
class Punto:
    x: int
    y: int

    def distancia_al_origen(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

punto = Punto(3, 4)
print(f"Distancia al origen: {punto.distancia_al_origen()}")   # 5.0


# 8. Dataclass CuentaBancaria.
@dataclass
class CuentaBancaria:
    titular: str
    saldo: float = 0

    def ingresar(self, cantidad: float) -> None:
        if cantidad > 0:
            self.saldo += cantidad

    def retirar(self, cantidad: float) -> None:
        if cantidad > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= cantidad

cuenta = CuentaBancaria("Ana")
cuenta.ingresar(100)
cuenta.retirar(30)
print(cuenta)   # CuentaBancaria(titular='Ana', saldo=70)
