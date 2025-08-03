"""
Ejercicios Funciones
"""
# Crea una función que obtenga dos números como parámetros y devuelva la suma.
def suma(a, b):
    total = a + b
    return total
print(suma(5, 8))

# Escribe una función que calcule el área de un triángulo (bxa)/2. 
# se le pasará como argumentos la base y la altura.
def area_triangulo(base, altura):
    total_area = (base*altura)/2
    return(total_area)
print(area_triangulo(3, 6))

# Crea una función que pase los metros a pulgadas (1m = 39,37 pulgadas).
def metros_pulgadas(metros):
    total_pulgadas = metros * 39,37
    return(total_pulgadas)
print(metros_pulgadas(45))


# Crea una función que pasado un mes devuelva la época del año que es.
def temporada(mes):
    if mes == "diciembre" or mes == "enero" or mes == "febrero":
        return ("Invierno")
    elif mes == "marzo" or mes == "abril" or mes == "Mayo" or mes == "Junio":
        return ("Primavera")
    elif mes == "julio" or mes == "agosto" or mes == "septiembre":
        return ("Verano")
    elif mes == "noviembre" or mes == "octubre":
        return ("Invierno")
    else:
        return("mes no válido")
print(temporada("julio"))


# Escribe una función que tome una lista como parámetro e imprima cada elemento.
lista = ["Apple", "Samsung", "Xiaomi", "Oppo"]
def imprimir(argumento):
    for elem in argumento:
        print(elem)
imprimir(lista)


# Crea una función que sume todos los números hasta llegar al número introducido.
def sumanum(num):
    total = 0 
    for i in range(num+1):
        total += i
    return (total)
print(f"el total de la suma es: {sumanum(23)}")



# Crea una función que diga el número de pares que hay entre el 0 y el número introducido.
def num_pares(num):
    pares = 0
    for n in range(num+1):
        if n % 2 == 0:
            pares += 1 
    return pares
print(f"el número de pares en tu número es {num_pares(34)}")


# Crea una función que diga el número de impares que hay entre el 0 y el número introducido.
def num_impares(num):
    impares = 0
    for n in range(num+1):
        if n % 2 != 0:
            impares += 1 
    return impares
print(f"el número de pares en tu número es {num_pares(30)}")


# Escribe una función que diga si todos los elementos de una lista son únicos.
alumnos_1 = ["Juan", "Almudena", "Carmen", "Manuel"]
alumnos_2 = ["Sancho", "Pedro", "Marta", "Pablo", "Sancho"]
def comprobar(lista):
    elementos = []
    for elem in lista:
        if elem in elementos:
            return False
        elementos.append(elem)
    return True
print(comprobar(alumnos_1))
print(comprobar(alumnos_2))



"""
Ejercicios de usuarios
"""

# Calculadora TecXion

def calculadora (a, b, operacion):
    total = 0
    if operacion == "+":
        total = a + b
        return total
    elif operacion == "-":
        total = a - b
        return total
    elif operacion == "*":
        total = a * b
        return total
    elif operacion == "/":
        total = a / b
        return total
    
def solicitar_numero():
    num = int(input("Introduce un número: "))
    return num

def solicitar_operacion():
    operacion = (input("Introduce operación (\"+, -, *, /\")"))
    return operacion

num_1 = solicitar_numero()
num_2 = solicitar_numero()
operador = solicitar_operacion()
print(f"El resultado de la operacion es: {calculadora(num_1, num_2, operador)}")

# ############################################################################################