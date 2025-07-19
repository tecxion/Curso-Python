<h3 align="center">
<a href="https://github.com/tecxion/Curso-Python">Inicio del Curso</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/02_Operadores">Siguiente Cápitulo</a>
</h3>


<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/variables1.png">

</h1>



# Variables y Funciones Built-in

- En la siguiente sección se explica cómo se pueden utilizar variables y funciones built-in en Python.
  * [Comentarios](#comentarios)
  * [Variables](#variables)
    * [Tipos de variables](#tiposdevariables)
    * [Declarar múltiples variables en una línea](#multiplesvariableslinea)
  * [Tipos de dato y conversión](#tiposdato)
    * [Tipos](#tipos)
    * [conversion](#conversion)
  * [Funciones Built-in](#builtin)
  * [Ejercicios](#ejercicios)
    * [Ejercicio 1](#ejercicio1)
    * [Ejercicio 2](#ejercicio2)

---

<a name="comentarios"></a>

## Comentarios

Como en todo lenguaje de programación los comentarios son muy importantes siempre pero siempre sin excedernos, en python los comentarios se escriben con el símbolo "#" y para hacer comentarios multilínea se ponen tres comillas simples o dobles.

Ejemplo:
```python
# Esto es un comentario en 
# varias líneas usando el símbolo "#"
''' 
Este es un comentario
multilínea usando
triples comillas simples.
''' 
```

#### Importante:

- Los docstrings (''' o """) son accesibles en tiempo de ejecución (como atributo __doc__), mientras que los comentarios con # son ignorados por el intérprete.

- Para comentarios temporales o desactivar bloques de código, es mejor usar #.


---

<a name="variables"></a>

## Variables

### ¿Qué son las Variables?

En programación, una **variable** es un contenedor que se utiliza para almacenar datos. Los datos pueden ser números, texto, valores booleanos, entre otros. Las variables permiten reutilizar estos datos a lo largo del programa y simplifican el manejo de la información.

En Python, las variables son **dinámicas**, lo que significa que no necesitas declarar explícitamente el tipo de dato que almacenarán. Python asigna automáticamente el tipo de dato según el valor que se le asigne.

#### Reglas de nombres de variables de Python

- Un nombre de variable **debe** comenzar con una *letra o el carácter de guión bajo*
- Un nombre de variable **no puede** comenzar con un número
- Un nombre de variable **solo** puede contener *caracteres alfanuméricos y guiones bajos* (Az, 0-9 y _)
- Los nombres de las variables **distinguen** entre *mayúsculas y minúsculas* (firstname, Firstname, FirstName y FIRSTNAME) son variables diferentes.

>[!NOTE]
>En python como en otros muchos lenguajes existen las palabras reservadas por lo que no pueden usarse como nombre de variables. Ejemplos: if, for, while, def, class, etc.(debemos tenerlo en cuenta a la hora de escribir nuestro código)

<a name="tiposdevariables"></a>

## Tipos de Variables en Python

A continuación, se describen los principales **tipos** de variables en Python:

1. **Enteros (int)**: Representan números enteros sin decimales.
```python
edad = 25
```
2. **Números de punto flotante (float)**: Representan números con decimales.
```python
pi = 3.14159
```
3. **Cadenas de texto (str)**: Representan secuencias de caracteres.
```python
nombre = "Juan"
```
4. **Booleanos (bool)**: Representan valores lógicos (verdadero o falso).
```python
es_estudiante = True
```
5. **Listas (list)**: Representan colecciones ordenadas de elementos.
```python
colores = ["rojo", "verde", "azul"]
```
6. **Tuplas (tuple)**: Representan colecciones ordenadas de elementos, similar a las listas, pero inmutables.
```python
coordenadas = (10, 20)
```
7. **Diccionarios (dict)**: Representan colecciones desordenadas de pares clave-valor.
```python
alumno = {"nombre": "Juan", "edad": 25}
```
8. **Conjuntos (set)**: Representan colecciones desordenadas de elementos únicos (sin duplicados).
```python
numeros = {1, 2, 3, 4, 5}
```
9. **NonType (None)**: Representa un valor nulo o sin valor.
```python
resultado = None
```
10. **Números complejos (complex)**: Representan números complejos con parte real y parte imaginaria.
- Los números complejos tienen su aplicación en ciencia y matemáticas entonces como programadores puede ser que no le veamos al 100% la utilidad pero la tienen.
```python
numero_complejo = 3 + 4j
```
11. **ZIP**: En Python, _zip_ es una función incorporada que combina elementos de dos o más iterables (como listas, tuplas o cadenas) en pares ordenados. Estos pares se devuelven como un objeto de tipo _zip_, que es un **iterador**.
```python
print(type(zip([1, 2], [3, 4])))
```
- ¿Para qué se usa zip?
La función zip es útil cuando necesitas combinar datos de diferentes iterables para procesarlos juntos. Algunos casos de uso comunes incluyen:

- Combinar Datos Relacionados:
Si tienes dos listas relacionadas (por ejemplo, nombres y edades), puedes usar zip para emparejar sus elementos.
- Iterar sobre Múltiples Iterables Simultáneamente:
En lugar de iterar sobre cada iterable por separado, puedes usar zip para recorrerlos en paralelo.
- Crear Diccionarios a Partir de Listas:
Puedes usar zip para combinar dos listas en pares clave-valor y crear un diccionario.

>[!NOTE]
>Creo que los tipos de datos zip necesitaban una aclaración mejor para no confundirlos con ficheros zip sobre todo ahora que estamos comenzando.

<a name="multiplesvariableslinea"></a>

### Declarar múltiples variables en una líne

También se pueden declarar variables en una única línea de código
**Ejemplo**:
```python
nombre, apellido, ciudad, edad = 'Jorge', 'Gomez', 'Cordoba', 30
print('nombre:', nombre)
print("apellido:", apellido)
print("ciidad:", ciudad)
print("edad:", edad)
```

<a name="tiposdato"></a>

### Tipos de datos

En python como en el resto de lenguajes de programación existen diferentes tipos de datos, aunque no hace falta declarar el tipo como podría ser java, siempre tenemos que tener en cuenta que tipo de dato es para evitar errores en el código.

#### Comprobación del tipo de dato y conversión

<a name="tipos"></a>

- En las siguientes líneas de código puedes ver declaradas unas variables y su impresión por pantalla del tipo de dato que guardan (Copia el código y comprueba a ver que te dice la consola).
```python
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
print(type(asignaturas)) # lista
```

<a name="conversion"></a>

- Conversión: En muchas ocasiones para evitar errores debemos convertir una variable en otra ya que si tenemos un float almacenado en memoria ese dato no puede trabajarse como un int a pesar que los dos sean números, para ello se usa la conversión de datos con las funciones de conversión, esto se usa en todos los lenguajes de programación para evitar errores.
   - Las diferentes funciones que existen para convertir datos y las más utilizadas seran, float(), str(), bool(), list(), tuple(), set(), a continuación os dejo unos ejemplos:
```python
numero = int("42")       # Convierte una cadena a entero
decimal_a_entero = int(3.9)  # Trunca el decimal: 3
numero = float("3.14")   # Convierte una cadena a float
entero_a_decimal = float(5)  # Convierte un entero a float: 5.0
verdadero = bool(1)      # Cualquier número distinto de 0 es True
falso = bool(0)          # 0 es False
cadena_vacia = bool("")  # Una cadena vacía es False
tupla = (1, 2, 3)
lista = list(tupla)      # Convierte una tupla a lista: [1, 2, 3]
cadena = "hola"
conjunto = set(cadena)   # Convierte una cadena a conjunto: {'h', 'o', 'l', 'a'}
# Ejemplo práctio:
entrada = input("Introduce un número: ")  # Entrada del usuario (cadena)
numero = int(entrada)                     # Convierte la entrada a entero
print(numero + 10)                        # Realiza una operación matemática
```

- También debemos tener en cuenta que se pueden cometer errores en la conversión y por ello debemos tener en cuenta estas consideraciones:
   1. Errores de Conversión: Intentar convertir un valor inapropiado puede generar errores. Por ejemplo:
    ```python
    int("abc")  # ValueError: invalid literal for int() with base 10: 'abc'
    ```
    2. Pérdida de Información: Algunas conversiones pueden resultar en pérdida de información. Por ejemplo:
    ```python
    int(3.9)  # Resultado: 3 (se trunca el decimal)
    ```
    3. Valores Vacíos o Nulos: Los valores vacíos (como "", 0, None) generalmente se convierten a False en contextos booleanos.

- ¿Qué son las f-strings?

Las f-strings (formateo de cadenas) permiten insertar variables, expresiones o llamadas a funciones directamente dentro de una cadena de texto. Son una forma clara y concisa de combinar texto y datos dinámicos, esto debemos tenerlo en cuenta si queremos poner variables en una cadena de texto. f"Texto {variable_o_expresión}"

Ejemplo:
```python
nombre = "Juan"
edad = 30
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")
```

---

<a name="builtin"></a>

## Funciones Built-in 

En python tenemos muchas funciones que nos ayudan a realizar muchas tareas, estas funciones son llamadas funciones built-in ya que son funciones que ya están definidas en el lenguaje y que podemos utilizar sin importar que el lenguaje este instalado en nuestro sistema, estas funciones son muy útiles y nos ayudan a realizar muchas tareas de forma rápida y sencilla, las funciones built-in son las siguientes:

![funciones Built-in](/Media/funcionesbuiltin.png)

Yo estoy usando ahora mismo windows pero se puede hacer desde cualquier terminal, solo hay que abrir python en la misma e introducir la funcion que queramos usar.

![powershell](/Media/powershell.png)

Puedes practicar con la función que quieras para ello puedes leer la documentación oficial y ver que hace cada función.

[Funciones Built-in](https://docs.python.org/es/3.9/library/functions.html)


- Dentro de las funciones built-in podrás encontrar la de entrada de datos por parte del usuario, en este caso usaremos la función input(), esta función nos permite pedir al usuario que introduzca un valor, este valor se guarda en una variable que se puede utilizar después.
```python
nombre = input("Introduce tu nombre: ")
print("Hola", nombre)
```

--- 

<a name="ejercicios"></a>

### Ejercicios de variables y funciones built-in

Para realizar los ejercicios abre tu IDE, crea una carpeta en su interior que se llame "python" y dentro de esa carpeta crea un archivo llamado "01_Variables.py". Abre el archivo y escribe el código de los ejercicios.

<a name="ejercicio1"></a>

#### Ejercicio 1: Variables
1. Escribe un comentario en una línea que diga *"esto es un comentario en una línea".*
2. Escribe un comentario en varias líneas que diga *"esto es un comentario multilínea y estoy usando varias líneas"* usando el comentario multilínea.
3. Declara una variable llamada nombre_usuario y asígnale un valor.
4. Declara una variable llamada profesion y asígnale un valor.
5. Declara una variable llamada lenguaje_favorito y asígnale un valor.
6. Declara una variable llamada edad_actual y asígnale un valor.
7. Declara una variable llamada año_nacimiento y asígnale un valor.
8. Declara una variable llamada es_estudiante y asígnale un valor booleano.
9. Declara una variable llamada tiene_trabajo y asígnale un valor booleano.
10. Declara una variable llamada es_de_dia y asígnale un valor booleano.
11. Declara múltiples variables en una sola línea (ejemplo: x, y, z = 10, 20, 30).

[Solucion](ejercicio1.py)


<a name="ejercicios2"></a>

#### Ejercicio 2: funciones Built-in

1. Usa la función type() para verificar el tipo de datos de todas las variables declaradas en el ejercicio 1.
2. Usa la función len() para encontrar la longitud de tu nombre_usuario.
3. Compara la longitud de tu nombre_usuario con la longitud de tu profesion.
4. Declara dos variables: numero_a = 7 y numero_b = 3.
5. Suma numero_a y numero_b, y asigna el resultado a una variable llamada suma_total.
6. Imprime por pantalla el número más alto de los dos números anteriores.
7. Crea una lista llamada palabras con las siguientes cadenas ["manzana", "plátano", "cereza", "naranja", "uva"]
8. Usa la función len() para encontrar la longitud de cada palabra en la lista y almacena los resultados en
 una nueva lista llamada longitudes_palabras
9. Usa la función max() para encontrar la palabra más larga en la lista (basándote en su longitud) y almacena
 el resultado en una variable llamada palabra_mas_larga
10. Usa la función min() para encontrar la palabra más corta en la lista (basándote en su longitud) y almacena
 el resultado en una variable llamada palabra_mas_corta
12. Usa la función sorted() para ordenar la lista de palabras alfabéticamente y almacena el resultado en una variable
 llamada palabras_ordenadas


[Solución](ejercicio2.py)

#### Ejercicio adicional

- Solicita al usuario que ingrese el lado del cuadrado.
  - Calcula el área del cuadrado y asigna el valor a una variable llamada area_cuadrado. (ladoxlado)
  - Calcula el perímetro del cuadrado y asigna el valor a una variable llamada perimetro_cuadrado. (4xlado)
- Ejecuta help('keywords') en el shell de Python para revisar las palabras reservadas.

[Solución](ejercicioadicional.py)

>![NOTE]
>Para este ejercicio tendrás que ejecutar el código desde la terminal de Python y no desde el editor de código.