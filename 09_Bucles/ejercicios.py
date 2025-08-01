"""
Ejercicios de Bucles
"""

# Genera una cuenta del 0 al 10 con el bucle for
for i in range(11):
    print(i)

# Genera una cuenta del 0 al 10 con el bucle while
i = 0
while i < 11:
    print(i)
    i += 1

# Crea un programa que genere la siguiente salida por pantalla.
aspa = "#"
for i in range(7):
    print(aspa)
    aspa += "#"

# Crea la tabla de multiplicar del 5
del_5 = 5
for tabla in range(11):
    resultado = tabla * del_5
    print(f"{del_5} x {del_5} = {resultado} " )


# Usa el bucle for para imprimir por pantalla los números pares del 0 al 50
for par in range(51):
    if par % 2 == 0:
        print(par)

# Usa el bucle while para imprimir por pantalla los números impares del 0 al 50
impar = 0
while impar < 50:
    if impar % 2 != 0:
        print(impar)
    impar += 1


# Imprime por pantalla la suma de todos los números del 0 al 100. Usa el bucle que quieras
# el resultado debe ser 5050.
# Bucle for
total = 0
for numero in range(101):
    total = total + numero
print(total)

# Bucle while
control = 0
total = 0
while control < 101:
    total = total + control
    control += 1
print(total)


# En el siguiente diccionario usa el bucle for para imprimir los paises que están en 
# "América" y en que continente está "Japón"

paises_por_continente = {
    "América": ["Estados Unidos", "Canadá", "México", "Brasil", "Argentina"],
    "Europa": ["España", "Francia", "Alemania", "Italia", "Reino Unido"],
    "África": ["Nigeria", "Egipto", "Sudáfrica", "Kenia", "Etiopía"],
    "Asia": ["China", "Japón", "India", "Corea del Sur", "Rusia"],
    "Oceanía": ["Australia", "Nueva Zelanda", "Fiyi", "Papúa Nueva Guinea"]
}


for pais in paises_por_continente["América"]:
    print(f"{pais}")

pais_buscado = "Japón"
for continente, paises in paises_por_continente.items():
    if pais_buscado in paises:
        print(f"{pais_buscado} está en {continente}")
        break