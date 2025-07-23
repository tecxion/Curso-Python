"""
Solución Ejercicios Listas.
"""
# Declarar una lista vacía
lista_vacia = []

# Declarar una lista con más de 5 elementos
alumnos = ["Pepe", "Maria", "Luis", "Ana","Zaida", "Noelia"]

# Encuentra la longitud de tu lista
print(len(alumnos))

# Obtenga el primer elemento, el elemento del medio y el último elemento de la lista.
print(alumnos[0])
indice_medio = int(len(alumnos) / 2)
print(alumnos[indice_medio])
print(alumnos[-1])

# Declare una lista llamada datos, coloque su (nombre, edad, altura, estado civil, dirección)
datos = ["Pepe", 43, 193, "soltero", "Calle Falsa 123"]
# Declare una variable de lista llamada companias y asigne valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
companias = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon" ]

# Imprima la lista usando print()
print(companias)

# Imprima el número de empresas en la lista
print(len(companias))

# Imprima la primera, la segunda y la última empresa.
print(companias[0])
print(companias[1])
print(companias[-1])

# Imprimir la lista después de modificar una de las empresas
companias[3] = "Mercadona"
print(companias)

# Agregar una empresa a companias al final de la lista.
companias.append("Zara")
print(companias)

# Insertar una empresa en el medio de la lista de empresas
compania_medio = int(len(companias)/2)
companias.insert(compania_medio, "El Corte Ingles")
print(companias)

# Cambie uno de los nombres de companias a mayúsculas (¡IBM excluido!)
compania = companias[2]
print(compania.upper())

# Unir companias con una cadena '#; '
companias_enlace = "#;".join(companias)
print(companias_enlace)

# Comprueba si una determinada empresa existe en la lista companias.
print("Google" in companias)

# Ordenar la lista usando el método sort()
companias.sort()
print(companias)

# Invierta la lista en orden descendente utilizando el método reverse()
companias.sort(reverse=True)
print(companias)

# Elimina las primeras 3 empresas de la lista
del companias[0:3]
print(companias)

# También podemos hacerlo con la indexación companias_1 = companias[0:3] // print(companias_1) 
# generando una nueva lista y no perdiendo la primera

# Elimina las últimas 3 empresas de la lista.
del companias[-3:-1]
print(companias)
# También podríamos hacerlo con la indexación negativa companias_2 = companias[-3:-1]
# generando una nueva lista y no perdiendo la primera

# Elimina de la lista a Google
companias.remove("Google")
print(companias)

# Eliminar la primera empresa que queda de companias
companias.pop(0)
print(companias)

# Eliminar todas las empresas de TI de la lista
companias.clear()
print(companias)

# Una a las siguientes listas:
"""
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
"""
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# copie la lista unida y asígnela a una variable full_stack, luego 
# inserte Python y SQL.
full_stack.append("Python")
full_stack.insert(0,"SQL")
print(full_stack)

# Edades
edad = [19,23,23,54,19,37,32,26,28,22,45]
# Ordena la lista y encuentra la edad mínima y máxima
edad.sort()
print(edad)

# Encuentra el alumno que está en el medio de las edades (es decir el elemento del centro)
edad_medio = int(len(edad)/2)
print(edad[edad_medio])

# Añade dos edades más y ordenalo de mayor a menor.
edad.append(23)
edad.insert(5,21)
edad.sort(reverse=True)
print(edad)
