"""
Solución ejercicios Condicionales.
"""
# Escribe tu edad en una variable y si tienes más de 18 años que imprima 
# `("eres mayor de edad")` en caso contrario que imprima `("eres menor, que suerte.")`
mi_edad = 26
if mi_edad > 18:
    print("eres mayor de edad")
else:
    print("eres menor, que suerte")


# Pide al usuario mediante input("igresa tu edad: ") y almacénalo en una variable. 
# Si tiene más de 18 imprime por pantalla `Puedes sacarte el carnet` en caso contrario `aún no puedes sacarte el carnet` y que diga los años que le faltan 'Te faltan años`.
edad_user = int(input("ingresa tu edad:"))
if edad_user > 18:
    print("Puedes sacarte el carnet!")
else:
    carnet = 18 - edad_user
    print("aún no puedes sacarte el carnet! te faltan", carnet, "años")


# Con la variable de edad compara tu edad y la mia (38) `tecxion_edad = 38` y si yo soy mayor que tú que imprima `tecxion es mayor` en caso contrario
#  `tú eres mayor que tecxion` y si tenemos la misma edad `tenéis la misma edad, ¡genial!`.
tecxion_edad = 38
if tecxion_edad > mi_edad:
    print("Tecxion es mayor")
elif tecxion_edad < mi_edad:
    print("Tú eres mayor que tecxion")
else:
    print("tenéis la misma edad, ¡genial!")



# Pide al usuario que ingrese dos números y compáralos, que imprima si a es mayor 
# que b `a es mayor que b` en caso contrario `b es mayor que a` y si son iguales 
# `a es igual a b`
a = int(input("Ingresa un número: "))
b = int(input("Ingresa otro número: "))
if a > b:
    print(a, "es mayor que", b)
elif a < b:
    print(a, "es menor que ", b)
else:
    print(a, " es igual ", b)



# Pide al usuario que ingrese la nota del examen y clasifica la nota. `de 0 a 5 Suspenso, 
# de 5 a 6 suficiente, de 6 a 7 bien, de 7 a 8 Notable, de 8 a 9 Sobresaliente y 
# de 9 a 10 Matrícula`
nota = float(input("Ingresa la nota: "))
if nota > 0 and nota < 5:
    print("Estás suspenso")
elif nota >= 5 and nota <= 6:
    print("Suficiente")
elif nota > 6 and nota <= 7:
    print("Bien")
elif nota > 7 and nota <= 8:
    print("Notable")
elif nota > 8 and nota <= 9:
    print("Sobresaliente")
elif nota > 9 and nota <= 10:
    print("Matrícula")
else:
    print("Nota no computable")

# Vamos a crear un pequeño programa que recomiende películas según el género que elija el usuario. Pide al usuario que ingrese un género, si el género existe que muestre las películas de ese género, si no existe que muestre un mensaje tipo `género no encontrado`
  # Diccionario. 
peliculas = {
    "acción": ["Misión Imposible", "John Wick", "Mad Max"],
    "comedia": ["Supercool", "Los Hangover", "Scary Movie"],
    "terror": ["El Exorcista", "It", "El Conjuro"]
}

eleccion = input("Elige un género (acción, comedia, terror: )")
if eleccion == "acción":
    print(peliculas["acción"])
elif eleccion == "comedia":
    print(peliculas["comedia"])
elif eleccion == "terror":
    print(peliculas["terror"])
else:
    print("Género no encontrado.")
