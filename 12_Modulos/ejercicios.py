"""
EJERCICIOS MÓDULOS
"""

#  Escribe una función que genere una contraseña aleatoria.
import random
import string
def contrasena(tamano):
    caracteres = string.ascii_letters + string.digits
    password = "".join(random.choices(caracteres, k=tamano))
    return password

print(contrasena(10))


# Escribe una función que genere un color aleatorio rgb que son tres valores entre 0 y 255, ej. rgb(243,34,234).
# import random

def colores():
    color = []
    for i in range(3):
        color.append(random.randint(0, 255))
        i += 1
    return color

print(f"color rgb {colores()}")


# Escribe un script que cree una carpeta con el nombre introducido por el usuario, y luego pregunte si quiere borrarla y si contesta "sí" que se borre.
# PUEDES AÑADIRLE MÁS FUNCIONALIDAD SI DESEAS.
import os

def carpeta(nombre):
    os.mkdir(nombre)
    return "Carpeta creada"

def borrar(eleccion, nombre_c):
    eleccion = eleccion.upper()
    if eleccion == "S":
        os.rmdir(nombre_c)
        return "Carpeta borrada"
    else:
        return "no se ha borrado la carpeta"

nombre_carpeta = input("Ingresa el nombre de la carpeta: ")
print(carpeta(nombre_carpeta))
elec = input("Desea borrar la carpeta creada? (S/N)")
print(borrar(elec, nombre_carpeta))


# Usa el módulo math y crea una función que haga el cuadrado de un número y lo rendonde al alza si es mas de 0,5 y a la baja si es menos de 0,5.
import math

def cuadrado(numero):
    total = 0
    total = math.pow(numero,2)
    parte_entera = int(total)
    parte_decimal = total - parte_entera
    if parte_decimal >= 0.5:
        return math.ceil(total)
    else:
        return math.floor(total)
    
print(cuadrado(3)) # 9
print(cuadrado(3.2)) # 10.24
print(cuadrado(3.6)) # 12.96


# crea una función que saque la media de notas de esta lista importando el módulo statistics.
# notas = [5.4, 7, 8.5, 1.2, 6, 8.8, 4.7]

import statistics

notas = [5.4, 7, 8.5, 1.2, 6, 8.8, 4.7]

def nota_media(lista):
    notas_medias = statistics.median(lista)
    return notas_medias

print(nota_media(notas))


# crea un script con el módulo sys que imprima.
# print(f"Hola {argumento 1}. Tu nota media del examen de {argumento 2} es de {argumento 3}")

import sys
print(f"Hola {sys.argv[1]}. Tu nota media del examen de {sys.argv[2]} es de {sys.argv[3]}")