<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/01_Variables">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/03_Cadenas">Siguiente Capítulo</a>
</h4>


<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/cadenas.png">
</h1>

## Índice del Capítulo
- [Cadenas](#cadenas)
  - [1. Definición de cadenas (String)](#1-definición-de-cadenas-string)
  - [2. Longitud de una cadena](#2-longitud-de-una-cadena)
  - [3. Concatenación de cadenas](#3-concatenación-de-cadenas)
  - [4. Secuencias de escape](#4-secuencias-de-escape)
  - [5. Formateo de cadenas](#5-formateo-de-cadenas)
    - [Nuevo formato de Strings](#nuevo-formato-de-strings)
    - [Interpolación de cadenas / f-Strings (Python 3.6+)](#interpolación-de-cadenas--f-strings-python-36)
  - [6. Cadenas de python como secuencias de caracteres](#6-cadenas-de-python-como-secuencias-de-caracteres)
    - [6.1 Segmentación de cadenas.](#61-segmentación-de-cadenas)
    - [6.2 Invertir una cadena](#62-invertir-una-cadena)
    - [6.3 Saltar caracteres](#63-saltar-caracteres)
  - [7. Metodos de cadenas](#7-metodos-de-cadenas)
  - [8. Ejercicios.](#8-ejercicios)


<a name = "Cadenas"></a>

# Cadenas

<a name = "1-definición-de-cadenas-string"></a>

## 1. Definición de cadenas (String)
Las cadenas son una secuencia de caracteres, que pueden contener letras, números, símbolos, etc. Las cadenas se pueden definir utilizando comillas simples ('') o comillas dobles ("") o triples (''' '''). Las cadenas pueden contener cualquier tipo de datos, incluyendo números, booleanos, listas, diccionarios, etc.
En esta lección siempre que hablemos de cadenas estamos haciendo referencia a los Strings para que no haya confusión.

- Ejemplo de cadena
```python
cadena = "Hola, mundo!"
print(cadena)
letra = "P"   # Esto también es una cadena
print(letra)
```

Las cadenas multilínea se crean usando comillas simples triples (''') o comillas dobles triples (""").
- Ejemplo de cadena multilínea
```python
cadena_multilinea = '''
Este es un ejemplo de cadena multilínea.
Puede contener cualquier tipo de datos.
'''
print(cadena_multilinea)
```

<a name="2-longitud-de-una-cadena"></a>

## 2. Longitud de una cadena
La longitud de una cadena se puede obtener utilizando la función len(). La función len() devuelve el número de caracteres en una cadena.


<a name="3-concatenación-de-cadenas"></a>

## 3. Concatenación de cadenas
La concatenación de cadenas se realiza utilizando el operador +. El operador + concatena dos cadenas y devuelve una nueva cadena que contiene los caracteres de ambas cadenas.

- Ejemplo:
```python
cadena1 = "Hola"
cadena2 = "mundo"
cadena3 = cadena1 + " " + cadena2
print(cadena3)
```
<a name ="4-secuencias-de-escape"></a>

## 4. Secuencias de escape
Las secuencias de escape se utilizan para representar caracteres especiales en una cadena. Por ejemplo:
- \n: nueva línea
- \t: Tabulador significa (8 espacios)
- \\: Barra invertida
- \': Comilla simple (')
- \": Comillas dobles (")

-Ejemplo:
```python
cadena = "Hola \n mundo"
print(cadena)
print("Si queremos escribir \"Comillas\" en una cadena")
print("O para tabular 8 espacios: \t y así \tdar formato")
```

<a name="5-formateo-de-cadenas"></a>

## 5. Formateo de cadenas
En python existen muchas formas de dar formato a una cadena, en las siguientes líneas aprenderemos a manejar algunas de ellas, por ejemplo:
- %s - Cadena (o cualquier objeto que sea un String)
- %d - Número entero
- %f - Número de punto flotante
- %o - Número en octal
- %x - Número en hexadecimal
- %e - Número en notación exponencial
- %c - Caracter
- %r - Representación de objeto
- %a - Cadena de formato de Python

Estos son muchos de los formateadores disponibles en Python, pero puedes encontrar más en la documentación oficial de Python, a continuación un ejemplo de cómo usarlos:

```python
nombre = "Juan"
apellido = "Pérez"
edad = 25
asignatura = "Python"
nota_media = 8.3

print("Mi nombre es %s y mi apellido es %s." % (nombre, apellido))
print("y tengo %d años." % edad)
print("Mi asignatura favorita es %s y mi nota media es %f." % (asignatura, nota_media))
```
>[!NOTE]
>Como podemos observar para el formateo de cadenas en python existen muchas pero su uso es siempre el mismo, insertamos "%" seguido del tipo de dato que queremos formatear y posteriormente definimos la variable/es que queremos formatear precedido de "%".


<a name ="nuevo-formato-de-strings"></a>

### Nuevo formato de Strings
En python 3 se introduce una nueva forma de formatear cadenas, la cual es más legible y fácil de leer, para usarla debemos importar el modulo "format" y luego definir la cadena y los valores que queremos formatear, por ejemplo:
```python
import format
nombre = "Juan"
apellido = "Pérez"
edad = 25
asignatura = "Python"
nota_media = 8.3
print("Mi nombre es {} y mi apellido es {}.".format(nombre, apellido))
print("y tengo {} años.".format(edad))
print("Mi asignatura favorita es {} y mi nota media es {}" .format(asignatura, nota_media))

# También podemos hacer diferentes operaciones matemáticas.
a = 6
b = 3

print("{} + {} = {}".format(a, b, a + b))
print("{:d} - {:d} = {:d}".format(a, b, a - b)) # En este caso indicamos de que se trata de un int si las variables fueran float daría error.

c = 4.3
d = 9.2
print("{:.2f} + {:.2f} = {:.2f}".format(c, d, c + d)) # para declarar el float usamos :.2f para que solo ponga 2 decimales
e = ("{} + {} = {}".format(c, d, c + d)) # Si no declaramos el tipo de dato de la variable el resultado será un string
print(e)
print(type(e)) #Esto dará como salida un str
```
>[!NOTE]
>En este caso se usa la palabra reservada "format" las llaves {} es donde va insertada la variable, posteriormente designamos con .format las variables que queremos formatear en el orden que queremos que aparezcan.

<a name ="interpolación-de-cadenas--f-strings-python-36"></a>

### Interpolación de cadenas / f-Strings (Python 3.6+)
En python 3.6 se introdujo una nueva forma de formatear cadenas, la cual es más legible y fácil de leer, para usarla debemos importar el modulo "format" y luego definir la cadena y los valores que queremos formatear, por ejemplo:
```python
import format
nombre = "Juan"
apellido = "Pérez"
edad = 25
asignatura = "Python"
nota_media = 8.3
print(f"Mi nombre es {nombre} y mi apellido es {apellido}.")
print(f"y tengo {edad} años.")
print(f"Mi asignatura favorita es {asignatura} y mi nota media es {nota_media}")
```

>[!NOTE]
>En este caso se usa la palabra reservada "f" y las llaves {} es donde va insertada la variable.

<a name ="6-cadenas-de-python-como-secuencias-de-caracteres"></a>

## 6. Cadenas de python como secuencias de caracteres
Las cadenas de python son secuencias de caracteres y comparten métodos básicos de acceso con otras secuencias ordenadas de objetos de Python: listas o tuplas. La forma más sencilla de extraer caracteres individuales es descomprimirlos en las variables que correspondan.

- Ejemplo:
```python
cadena = "Python"
a, b, c, d, e, f = cadena
print(a, b, c, d, e, f)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
```

También podríamos acceder a los caracteres individuales de una cadena utilizando índices, comenzando desde el 0. Los índices negativos se usan para recorrer la cadena en sentido inverso. Por ejemplo:
```python
cadena = "Python"
print(cadena[0]) # P
print(cadena[-5]) # y
print(cadena[-4]) # t
print(cadena[3]) # h
print(cadena[-2]) # o
print(cadena[-1]) # n
```

<a name="61-segmentación-de-cadenas"></a>

### 6.1 Segmentación de cadenas.

En python podemos segmentar cadenas, es decir, convertir una cadena en otra cadena.

- Ejemplo:
```python
cadena = "Python"
print(cadena[0:2]) # Py
print(cadena[2:5]) # tho
print(cadena[5:]) # n
print(cadena[:3]) # Pyt
print(cadena[2:]) # thon
print(cadena[-3:]) # hon
print(cadena[:-3]) # Pyt
print(cadena[-5:-2]) # tho
print(cadena[-5:]) # Python
print(cadena[:-5]) # ''
```

<a name="62-invertir-una-cadena"></a>

### 6.2 Invertir una cadena
Para invertir una cadena en python podemos utilizar el método reverse() o podemos escribir el nombre_variable[::-1]

- Ejemplo:
```python
cadena = "Hola Mundo!"
print(cadena[::-1]) #!odnuM aloH 
```

<a name="63-saltar-caracteres"></a>

### 6.3 Saltar caracteres
Para saltar caracteres en una cadena podemos utilizar el método replace() o podemos escribir el nombre_variable[::2], esto lo vamos a entender mejor con esta explicación:


Desglose de la sintaxis [inicio:fin:paso]
asignatura = Python
print(asignatura[0:6:2]) #Pho
P y t h o n
0 1 2 3 4 5
- Primer número (0): Índice de inicio (incluido) - Empieza en el carácter 0 ('P')
- Segundo número (6): Índice de fin (excluido) - Termina antes del índice 6 (que sería el 7mo carácter, pero como 'Python' tiene 6 caracteres, llega hasta el final)
- Tercer número (2): Paso (saltos) -Toma cada 2 caracteres

- Ejemplo:
```python
cadena = "Hola Mundo!"
print(cadena[0:10:2]) # Hl ud
```

>[!NOTE]
> El Slicing como es conocido en Python es una herramienta muy poderosa para manipular secuencias.


<a name="7-metodos-de-cadenas"></a>

## 7. Metodos de cadenas

Existen multitud de métodos de cadenas en Python, algunos de los más importantes son:
- capitalize(): Devuelve la cadena con la primera letra en mayúscula.
   ```python
   cadena = "hola mundo"
   print(cadena.capitalize()) # Hola mundo
   ```
- upper(): Devuelve la cadena en mayúsculas.
   ```python
     cadena = "hola mundo"
     print(cadena.upper()) # HOLA MUNDO
     ```
- lower(): Devuelve la cadena en minúsculas.
    ```python
    cadena = "Hola Mundo"
    print(cadena.lower()) # hola mundo
    ```
- swapcase(): Devuelve la cadena con las letras en mayúsculas y minúsculas intercambiadas.
    ```python
    cadena = "Hola Mundo"
    print(cadena.swapcase()) # hOLA mUNDO
    ```
- count(): Devuelve el número de veces que aparece una subcadena en la cadena.
  ```python
    cadena = "Hola Mundo"
    print(cadena.count("o")) # 2
    ```
- endswith(): Devuelve True si la cadena termina con la subcadena especificada.
    ```python
    cadena = "Hola Mundo"
    print(cadena.endswith("o")) # True
    ```
- startswith(): Devuelve True si la cadena empieza con la subcadena especificada.
    ```python
    cadena = "Hola Mundo"
    print(cadena.startswith("H")) # True
    ```
- find(): Devuelve el índice de la primera aparición de la subcadena especificada en la cadena.
    ```python
    cadena = "Hola Mundo"
    print(cadena.find("o")) # 4
    ```
- index(): Devuelve el índice de la primera aparición de la subcadena especificada en la cadena.
    ```python
    cadena = "Hola Mundo"
    print(cadena.index("o")) # 4
    ```
- replace(): Reemplaza una subcadena por otra en la cadena.
    ```python
    cadena = "Hola Mundo"
    print(cadena.replace("o", "x")) # Hxla Mxdn
    ```
- split(): Divide la cadena en una lista de subcadenas, utilizando el separador especificado.
    ```python
    cadena = "Hola Mundo"
    print(cadena.split(" ")) # ['Hola', 'Mundo']
    ```
- join(): Une una lista de cadenas en una única cadena, utilizando el separador 
  ```python
  cadena = "Hola Mundo"
    print("-".join(cadena)) # H-o-l-a-M-u-n-d-o
    ```
- strip(): Elimina los caracteres especificados del principio y del final de la cadena.
    ```python
    cadena = "Hola Mundo"
    print(cadena.strip("o")) # Hla Mundo
    ```
- lstrip(): Elimina los caracteres especificados del principio de la cadena.
    ```python
    cadena = "Hola Mundo"
    print(lstrip(cadena, "o")) # Hla Mundo
    ```
- rstrip(): Elimina los caracteres especificados del final de la cadena.
    ```python
    cadena = "Hola Mundo"
    print(cadena.rstrip("o")) # Hola Mundo

- title(): Convierte la primera letra de cada palabra en la cadena en mayúscula.
    ```python
    cadena = "hola mundo"
    print(cadena.title()) # Hola Mundo
    ```
- isalnum(): Devuelve True si todos los caracteres en la cadena son alfanuméricos, False en caso contrario.
    ```python
    cadena = "hola mundo"
    print(cadena.isalnum()) # False
    prueba = "hola123"
    print(prueba.isalnum()) # True
    ```
- isalpha(): Devuelve True si todos los caracteres en la cadena son alfabéticos, False en caso contrario.
  ```python
  cadena = "hola mundo"
  print(cadena.isalpha()) # False
  prueba = "hola"
  print(prueba.isalpha()) # True
  ```
- isdigit(): Devuelve True si todos los caracteres en la cadena son dígitos, False en caso contrario.
    ```python
    cadena = "123"
    print(cadena.isdigit()) # True
    prueba = "hola"
    print(cadena.isdigit()) # False
    ```
- islower(): Devuelve True si todos los caracteres en la cadena están en minúsculas, False en caso contrario.
    ```python
    cadena = "hola mundo"
    print(cadena.islower()) # False ya que coge el espacio y devuelve False
    prueba = "holamundo"
    print(prueba.islower()) # True
    ```
- isidentifier(): Devuelve True si la cadena es un identificador válido en Python, False en caso contrario.
    ```python
    cadena = "hola mundo"
    print(cadena.isidentifier()) # False ya que empieza con letra pero contiene un espacio
    prueba = "hola_mundo"
    print(prueba.isidentifier()) # True
    ```
- isnumeric(): Devuelve True si todos los caracteres en la cadena son numéricos, False en caso contrario.
    ```python
    cadena = "123"
    print(cadena.isnumeric()) # True
    prueba = "hola"
    print(prueba.isnumeric()) # False
    ```
- isspace(): Devuelve True si todos los caracteres en la cadena son espacios en blanco, False en caso contrario.
    ```python
    cadena = " "
    print(cadena.isspace()) # True
    prueba = "hola"
    print(prueba.isspace()) # False
    ```
- swapcase(): Convierte la cadena a su versión en minúsculas o mayúsculas según sea el caso.
    ```python
    cadena = "Hola Mundo"
    print(cadena.swapcase()) # hOLA mUNDO
    ```
- startswith(): Devuelve True si la cadena comienza con la subcadena especificada, False en caso contrario.
    ```python
    cadena = "Hola Mundo"
    print(cadena.startswith("Ho")) # True
    ```

Hay alrededor de 50 métodos de strings, por lo que te recomiendo que te vayas leyendo y practicando, ya que es muy importante conocerlos, además aquí te dejo el enlace a esta parte de la documentación oficial con todos los métodos.

[Ver todos los métodos](https://docs.python.org/es/3.13/library/stdtypes.html#string-methods)

<a name = "8-ejercicios"></a>

## 8. Ejercicios.

A continuación te dejo una serie de ejercicios para que practiques lo aprendido en este capítulo.

1. Une las palabras `'Aprendiendo'`, `'Programar'`, `'Con'`, `'Python'` para formar una única cadena: `'Aprendiendo Programar Con Python'`.
2. Crea una cadena concatenando `'Programar'`, `'Es'`, `'Genial'` para obtener `'Programar Es Genial'`.
3. Declara una variable llamada `organizacion` y asígnale el valor `'Programar Es Genial'`.
4. Muestra el contenido de la variable `organizacion` usando la función `print()`.
5. Imprime la cantidad de caracteres que contiene la variable `organizacion` usando `len()`.
6. Convierte la cadena almacenada en `organizacion` a mayúsculas usando `.upper()`.
7. Transforma todos los caracteres de `organizacion` a minúsculas utilizando `.lower()`.
8. Aplica los métodos `.capitalize()`, `.title()` y `.swapcase()` a la cadena `'Python para todos'`.
9. Extrae la palabra `'Programar'` de la frase `'Programar Es Genial'` mediante slicing.
10. Verifica si la palabra `'Programar'` aparece en la cadena `'Programar Es Genial'` utilizando `.find()` o `in`.
11. Sustituye `'Programar'` por `'Python'` en la frase `'Programar Es Genial'`.
12. Reemplaza `'Python Es Genial'` por `'Python Es Increíble'` utilizando el método `.replace()`.
13. Divide la cadena `'Aprender Python Juntos'` en una lista de palabras usando `.split()`.
14. Divide la cadena `'Twitter, LinkedIn, Reddit, TikTok'` utilizando la coma como delimitador.
15. ¿Qué carácter se encuentra en el índice 0 de la cadena `'Programar Es Genial'`?
16. ¿Cuál es el índice del último carácter en `'Programar Es Genial'`?
17. ¿Qué carácter ocupa el índice 11 en `'Programar Es Genial'`?
18. Crea una sigla con la frase `'Python Es Para Todos'`.
19. Genera una abreviación para `'Code With Me'`.
20. Usa `.index()` para saber dónde aparece por primera vez la letra `'P'` en `'Programar Es Genial'`.
21. Usa `.index()` para encontrar la primera ocurrencia de `'E'` en `'Programar Es Genial'`.
22. Utiliza `.rfind()` para encontrar la última posición de la letra `'o'` en `'Code With All People'`.
23. Halla la posición de la palabra `'porque'` usando `.find()` en la oración:  
   `'Es difícil explicar porque porque porque es confuso.'`
24. Usa `.rindex()` para localizar la última aparición de `'porque'` en:  
   `'Es difícil explicar porque porque porque es confuso.'`
25. Elimina la sección `'porque porque porque'` en la frase:  
   `'Es difícil explicar porque porque porque es confuso.'`
26. ¿La cadena `'Aprender Con Python'` comienza con `'Aprender'`?
27. ¿La cadena `'Aprender Con Python'` termina en `'python'`?
28. Elimina los espacios al inicio y al final de `'  Programar Es Genial  '`.
29. ¿Cuál de las siguientes cadenas es un identificador válido con `.isidentifier()`?  
   - `1_programar`  
   - `programar`
30. Dada la lista `['NumPy', 'Pandas', 'Matplotlib', 'Scikit-learn']`, únelas en una sola cadena separadas por `###`.
31. Imprime las siguientes frases en líneas separadas usando `\n`:  
   - Estoy aprendiendo Python.  
   - ¡Y me está gustando mucho!
32. Usa `\t` para tabular los siguientes datos:  
    | Name | Age | Country | City      |
    | ---- | --- | ------- | --------- |
    | Juan | 23  | España  | Barcelona |

33. Utiliza f-strings o `.format()` para mostrar:  
- `radio = 7`  
- `área = 3.14 * radio ** 2`  
- Resultado: `El área de un círculo con radio 7 es 153.86 metros cuadrados.`
34.    Muestra las siguientes operaciones usando formato de cadena:  
- `9 + 5 = 14`  
- `9 - 5 = 4`  
- `9 * 5 = 45`  
- `9 / 5 = 1.80`  
- `9 % 5 = 4`  
- `9 // 5 = 1`  
- `9 ** 5 = 59049`

[Solución Ejercicios del 1 al 21](./cadenas_ejercicios1al21.py)
[Solución Ejercicios del 22 al 34](./cadenas_ejercicios22al34.py)



