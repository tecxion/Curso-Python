"""
Ejercicios Cadenas parte 2

"""

# 22. Utiliza `.rfind()` para encontrar la última posición de la letra `'o'` en `'Code With All People'`.
print('Code With All People'.rfind('o'))

# 23. Halla la posición de la palabra `'porque'` usando `.find()` en la oración:  
#   `'Es difícil explicar porque porque porque es confuso.'`
frase1 = 'Es difícil explicar porque porque porque es confuso.'
print(frase1.find('porque'))

# 24. Usa `.rindex()` para localizar la última aparición de `'porque'` en:  
#  `'Es difícil explicar porque porque porque es confuso.'`
print(frase1.rindex('porque'))

# 25. Elimina la sección `'porque porque porque'` en la frase:  
#   `'Es difícil explicar porque porque porque es confuso.'`
print(frase1.replace('porque porque porque', ''))

# 26. ¿La cadena `'Aprender Con Python'` comienza con `'Aprender'`?
frase2 = 'Aprender Con Python'
print(frase2.startswith('Aprender'))

# 27. ¿La cadena `'Aprender Con Python'` termina en `'python'`?
print(frase2.endswith('python'))

# 28. Elimina los espacios al inicio y al final de `'  Programar Es Genial  '`.
frase3 = '  Programar Es Genial  '
print(frase3.strip())

# 29. ¿Cuál de las siguientes cadenas es un identificador válido con `.isidentifier()`?  
#   - `1_programar`  
#   - `programar`
cadena1 = '1_programar'
cadena2 = 'programar'
print(cadena1.isidentifier())
print(cadena2.isidentifier())

# 30. Dada la lista `['NumPy', 'Pandas', 'Matplotlib', 'Scikit-learn']`, únelas en una sola cadena separadas por `###`.
lista = ['NumPy', 'Pandas', 'Matplotlib', 'Scikit-learn']
print('###'.join(lista))

# 31. Imprime las siguientes frases en líneas separadas usando `\n`:  
#   - Estoy aprendiendo Python.  
#   - ¡Y me está gustando mucho!
frase4 = 'Estoy aprendiendo Python.\n¡Y me está gustando mucho!'
print(frase4)

# 32. Usa `\t` para tabular los siguientes datos:  
#    | Name | Age | Country | City      |
#    | ---- | --- | ------- | --------- |
#    | Juan | 23  | España  | Barcelona |

print(f'Name\tAge\tCountry\tCity')
print(f'Juan\t23\tEspaña\tBarcelona')

  # O en una sola línea.
print(f'Name\tAge\tCountry\tCity\nJuan\t23\tEspaña\tBarcelona')


# 33. Utiliza f-strings o `.format()` para mostrar:  
# - `radio = 7`  
# - `área = 3.14 * radio ** 2`  
# - Resultado: `El área de un círculo con radio 7 es 153.86 metros cuadrados.`

radio = 7
area = 3.14 * radio ** 2
print(f'El área de un círculo con radio {radio} es {area} metros cuadrados.')

# 34.    Muestra las siguientes operaciones usando formato de cadena:  
# - `9 + 5 = 14`  
# - `9 - 5 = 4`  
# - `9 * 5 = 45`  
# - `9 / 5 = 1.80`  
# - `9 % 5 = 4`  
# - `9 // 5 = 1`  
# - `9 ** 5 = 59049`

a = 9
b = 5
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(' %d * %d = %d' % (a, b, a*b))
print(" {} / {} = {:.2f}".format(a,b,a/b))
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')