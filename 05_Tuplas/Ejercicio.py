"""
Ejercicios Tuplas
"""
# Crear una tupla vacía
tupla_vacia = ()

# Crea una tupla que contenga los nombres de 4 paises de 
# Europa y otra de América que tenga nombres tanto del Norte como del Sur.
europa = ("España", "Francia", "Portugal","Italia")
america = ("Mexico", "Argentina", "Canada", "Nicaragua")

  # Comprueba si dentro de Europa está `España` y `Alemania`
print("España" in europa)
print("Alemania" in europa)

  # Comprueba si dentro de América está `Argentina` y `Colombia`
print("Argentina" in america)
print("Colombia" in america)

# Une ambas tuplas en una que se llame mundo.
mundo = europa + america

# ¿Cuántos paises hay en la tupla mundo?
print(len(mundo))

# Modifica la tupla América y añade dos paises más.
dos_paises = ("Brasil", "Cuba")
america = america + dos_paises
print(america)

# Camiba la tupla america a una lista.
america = list(america)

# Separa el primer y el último elemento de la tupla europa.
primer = europa[0:1]
print(primer)
ultimo = europa [3:4]
print(ultimo)

# Elimina la tupla europa.
del europa