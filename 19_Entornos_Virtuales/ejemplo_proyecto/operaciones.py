"""
operaciones.py
Módulo con la lógica del programa. No se ejecuta solo:
está pensado para que otros ficheros importen sus funciones.
"""


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b
