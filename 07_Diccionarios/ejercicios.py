"""
Soluciones ejercicios Diccionarios

"""

# Crea un diccionario vacio llamado casa.
casa = {}

# Agrega al diccionario casa, pais, ciudad, código postal, nombre de la casa. 
casa = {"pais":"España", "ciudad":"Barcelona", "cod_postal":15987, "nombre_casa":"chez Barna"}
print(casa)
# Crea un diccionario coche y añade la marca, modelo, cilindrada, 
# potencia, color, número de puertas, matrícula, extras, ciudad donde aparcas y código postal.
coche = {"marca":"nissan", "modelo":"GTR", "cilindara":3500, "potencia":540, "color":"negro", "num_puertas":2, "matricula":"1998STA", "extras":["AA/CC", "Llantas aleacion", "Pantalla 10\"", "Bacquets"], "ciudad_apar":"Sevilla", "cod_postal":45887}

# Obten la longitud del diccionario coche.
print(len(coche))

# Imprime el tipo de dato que es extras y los valores que tiene.
print(type(coche["extras"]))
print(coche["extras"])

# Agrega algún extra que quieres que tenga.
coche["extras"].extend(["elevalunas", "pintura metalizada"]) # usamos extend si queremos añadir
    # múltiples elementos a la lista sería como unir dos listas.
print(coche)

# Pasa el diccionario a una lista.
coche_lista = coche.items()

# Imprime por pantalla solo las claves del diccionario coche.
print("## Claves coche ##")
print(coche.keys())

# Almacena en una variable los valores del diccionario coche.
print("\n ## valores ## ")
valores_coche = coche.values()
print(valores_coche)

# Elimina la clave matrícula del diccionario.
coche.pop("matricula")
print("\n coche sin matrícula: ")
print(coche)

# Limpia el diccionario casa.
casa.clear()
print("\n el diccionario casa esta: ", casa)

# Elimina por completo uno de los dos diccionarios.
del coche
