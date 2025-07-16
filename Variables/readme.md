# Variables y Funciones Built-in

- En la siguiente sección se explica cómo se pueden utilizar variables y funciones built-in en Python.
  * [Variables](#variables)
  * [Tipos de variables](#tiposdevariables)
  * 

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
```python
numero_complejo = 3 + 4j
```
