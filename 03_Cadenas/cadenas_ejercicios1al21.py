"""
EJERCICIOS DE CADENAS
"""

# 1. Une las palabras 'Aprendiendo', 'Programar', 'Con', 'Python' para formar una única cadena: 'Aprendiendo Programar Con Python'.
cadena_1 = 'Aprendiendo' + ' ' + 'Programar' + ' ' + 'Con' + ' ' + 'Python'
print(cadena_1)
# 2. Crea una cadena concatenando 'Programar', 'Es', 'Genial' para obtener 'Programar Es Genial'.
palabra1 = "Programar"
palabra2 = "Es"
palabra3 = "Genial"
cadena_2 = ("{} {} {}" .format(palabra1, palabra2, palabra3))
print(cadena_2)

# 3. Declara una variable llamada 'organizacion' y asígnale el valor 'Programar Es Genial'.
organizacion = "Programar Es Genial"
# 4. Muestra el contenido de la variable 'organizacion' usando la función 'print()'.
print(organizacion)
# 5. Imprime la cantidad de caracteres que contiene la variable 'organizacion' usando 'len()'.
print(len(organizacion))
# 6. Convierte la cadena almacenada en 'organizacion' a mayúsculas usando '.upper()'.
print(organizacion.upper())
# 7. Transforma todos los caracteres de 'organizacion' a minúsculas utilizando '.lower()'.
print(organizacion.lower())
# 8. Aplica los métodos '.capitalize()', '.title()' y '.swapcase()' a la cadena 'Python para todos'.
print("Python para todos".capitalize())
print("Python para todos".title())
print("Python para todos".swapcase())
# 9. Extrae la palabra 'Programar' de la frase 'Programar Es Genial' mediante slicing.
print(organizacion)
# 10. Verifica si la palabra 'Programar' aparece en la cadena 'Programar Es Genial' utilizando '.find()' o 'in'.
print(organizacion.find("Programar"))
# 11. Sustituye `'Programar'` por `'Python'` en la frase `'Programar Es Genial
print(organizacion.replace("Programar", "Python"))
# 12 Remplaza Python es Genial por Python es Increible.
print(organizacion.replace("Genial", "Increible" ))
# 13. Divide la cadena `'Aprender Python Juntos'` en una lista de palabras usando `.split()`
print("Aprender Python Juntos".split())
# 14. Divide la cadena `'Twitter, LinkedIn, Reddit, TikTok'` utilizando la coma como delimitador.
cadena_3 = "Twitter, LinkedIn, Reddit, TikTok"
print(cadena_3.split(", "))
"""
En este ejercicio si quieres comprueba haciendo esto:
cadena_3 = "Twitter, LinkedIn, Reddit, TikTok"
print(type(cadena_3))
print(type(cadena_3.split(", ")))
"""
# 15. ¿Qué carácter se encuentra en el índice 0 de la cadena `'Programar Es Genial'`?
print(organizacion[0])
# 16. ¿Cuál es el índice del último carácter en `'Programar Es Genial'`?
print(len("Progarmar es genial"))
# 17. ¿Qué carácter ocupa el índice 11 en `'Programar Es Genial'`?
print(organizacion[11])
# 18. Crea una sigla con la frase `'Python Es Para Todos'`.
lista = "Python es para todos"
palabras = lista.split()
print(palabras)
# 19. Genera una abreviación para `'Code With Me'`.
frase1 = "Code With Me"
print(frase1[0:12:2]) # puedes elegir la combinación que quieras.
# 20. Usa `.index()` para saber dónde aparece por primera vez la letra `'P'` en `'Programar Es Genial'`.
print(organizacion.index("P"))
# 21. Usa `.index()` para encontrar la primera ocurrencia de `'E'` en `'Programar Es Genial'`.
frase2 = "Programar Es Genial"
print(frase2.index("E"))