"""
Ejercicio

    - Pide al usuario que ingrese dos números, y el programa automáticamente debe calcular la suma, la resta, 
la multiplicación y la división de estos números e imprimelos en la consola.
    - Haz que el programa compare esos dos números y muestre si son o no iguales de diferentes formas.
    - Comprueba cual de los números es mayor o menor de diferentes formas.
    - Suma al número 1 del usuario el valor de 4 y almacénalo en la misma variable y muestra el resultado.
    - Potencia el número al cubo (3) y asígnalo a la misma variable y muestra el resultado.
"""

numero1 = int(input("Ingrese un número: ")) # usamos int para que el usuario ingrese un número y no tenga decimales
numero2 = int(input("Ingrese otro número: "))
print(f"La suma de los dos números es: {numero1 + numero2}")  # vamos a usar la f-string para concatenar una variable con un texto
print(f"la resta de los dos números es: {numero1 - numero2}")
print("la multiplicación de los dos números es:", numero1 * numero2) # también podemos usar una coma para concatenar
print("La división de los dos números es:", numero1 / numero2)


# comparación de los números
print("Comparación de los números:")
print(f"¿Los números son iguales? {numero1 == numero2}")
print(f"¿Los números son diferentes? {numero1 !=  numero2}")
print(f"¿El número 1 es mayor que el número 2? {numero1 >= numero2}")
print(f"¿El número 1 es menor que el número 2? {numero1 <= numero2}")

# suma y potencia
print("Suma y potencia de los números:")
numero1 += 4
print(f"El resultado de la suma es: {numero1}")
numero1 **= 3
print(f"El resultado de la potencia es: {numero1}")