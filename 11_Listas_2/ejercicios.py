"""
Ejercicios Listas 2
"""
# Filtra solo números pares de esta lista usando comprensión de listas.
numeros = [-3, - 6, -1, -8, 2, 4, 6, 1, 7, 11, 83, 56]
pares = [num for num in numeros if num % 2 == 0]
print(pares)



# Aplana el siguiente array en una lista usando comprensión de listas.
array_lista = [[[1, 2, 3], [4, 5, 6], [7, 8, 0]]]
lista = [num for sublista in array_lista for subsublista in sublista for num in subsublista]
print(lista)



# Aplana la siguiente lista.
lenguajes = [[("Python", "Java")], [("C++", "C#")], [("Ensamblador", "Maquina")]]
aplanar = [prog for sublist in lenguajes for sublist_2 in sublist for prog in sublist_2]
print(aplanar) # Salida ["Python", "Java", "C++", "C#", "Ensamblador", "Maquina"]

# Cambia la siguiente lista a una lista de Diccionarios.
provincias = [[("La Rioja", "Logroño")], [("Alava", "Vitoria")], [("Madrid", "Madrid")]]
diccionario = [{"Provincia": provincia, "Ciudad": ciudad} for [(provincia, ciudad)] in provincias]
print(diccionario) # [{"Provincia": "La Rioja", "Ciudad": "Logroño"}, {"Provincia": "Alava", "Ciudad": "Vitoria"}, {"Provincia": "Madrid", "Ciudad": "Madrid"}]


# Crea una función lambda que calcule el área de un triángulo.
area = lambda base, altura: (base*altura)/2
print(area(2, 5))
