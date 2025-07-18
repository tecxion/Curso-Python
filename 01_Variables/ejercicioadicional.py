"""
- Solicita al usuario que ingrese el lado del cuadrado.
  - Calcula el área del cuadrado y asigna el valor a una variable llamada area_cuadrado. (ladoxlado)
  - Calcula el perímetro del cuadrado y asigna el valor a una variable llamada perimetro_cuadrado. (4*lado)
- Ejecuta help('keywords') en el shell de Python para revisar las palabras reservadas.

"""

# Solicitamos al usuario que ingrese el lado del cuadrado
lado = float(input("Ingrese el lado del cuadrado: "))
# Se ve en el siguiente tema pero si sabes otro lenguaje no tendrás problema.

area_cuadrado = lado * lado
perimetro_cuadrado = 4 * lado
print(f"El área del cuadrado es: {area_cuadrado}")
print(f"El perímetro del cuadrado es: {perimetro_cuadrado}")



# Para este ejercicio tendrás que ejecutar el código desde la terminal de Python y no desde el editor de código. 