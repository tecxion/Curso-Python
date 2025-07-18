# Ejercicio 2

"""
1. Usa la función type() para verificar el tipo de datos de todas las variables declaradas en el ejercicio 1.
2. Usa la función len() para encontrar la longitud de tu nombre_usuario.
3. Compara la longitud de tu nombre_usuario con la longitud de tu profesion.
4. Declara dos variables: numero_a = 7 y numero_b = 3.
5. Suma numero_a y numero_b, y asigna el resultado a una variable llamada suma_total.
6. Imprime por pantalla el número más alto de los dos números anteriores.
7. Crea una lista llamada palabras con las siguientes cadenas ["manzana", "platano", "cereza", "naranja", "uva"]
8. Usa la función len() para encontrar la longitud de cada palabra en la lista y almacena los resultados en
 una nueva lista llamada longitudes_palabras
9. Usa la función max() para encontrar la palabra más larga en la lista (basándote en su longitud) y almacena
 el resultado en una variable llamada palabra_mas_larga
10. Usa la función min() para encontrar la palabra más corta en la lista (basándote en su longitud) y almacena
 el resultado en una variable llamada palabra_mas_corta
12. Usa la función sorted() para ordenar la lista de palabras alfabéticamente y almacena el resultado en una variable
 llamada palabras_ordenadas
"""

nombre_usuario = "Juan"
profesion = "Estudiante"
lenguaje_favorito = "Python"
edad_actual = 25
año_nacimiento = 1997
es_estudiante = True
tiene_trabajo = False
es_de_dia = True
x, y, z = 10, 20, 30


print(type(nombre_usuario))
print(type(profesion))
print(type(lenguaje_favorito))
print(type(edad_actual))
print(type(año_nacimiento))
print(type(es_estudiante))
print(type(tiene_trabajo))
print(type(es_de_dia))
print(type([x, y, z]))

print(len(nombre_usuario))
print(len(profesion))

numero_a = 7
numero_b = 3

sum_total = sum([numero_a, numero_b])
print(sum_total)
print(max(numero_a, numero_b))

print("Ejercicio funciones built-in")
palabras = ["manzana", "platano", "cereza", "naranja", "uva"]
print(palabras)
longitudes_palabras = [len(palabra) for palabra in palabras]
palabra_mas_larga = max(palabras, key=len)
palabra_mas_corta = min(palabras, key=len)
palabras_ordenadas = sorted(palabras)
print(palabras_ordenadas)
print(palabra_mas_larga)
print(palabra_mas_corta)
print(longitudes_palabras)
