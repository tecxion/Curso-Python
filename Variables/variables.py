# Tipos de variables en python.
nombre = "Pepe"        #string
apellido = "Gómez"     #string
edad = 23              #int
mayor_edad = True      #bool
asignaturas = {"programación", "bases de datos", "contenedores", "lenguaje de marcas"}

# Ahora imprimimos por pantalla el tipo de dato
print(type('Jesus'))   # Esto dará un string
print(type(nombre))    # String
print(type(edad))      # int
print(type(3.14))      # float
print(type(2 + 4j))     # Complejo
print(type(mayor_edad))    # booleano
print(type({"referencia": "LS2341"}))  # diccionario
print(type((1,2)))     # tupla
print(type(zip([1,2],[3,4])))   # zip
print(type(asignaturas)) # set