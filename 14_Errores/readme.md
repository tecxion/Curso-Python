<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/13_Funciones_2/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/15_POO/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/errores.png">
</h1>


<h1 align="center">Manejo de Errores y Excepciones</h1><br>

<h3>Índice</h3>

- [1. ¿Qué es una excepción?](#1-qué-es-una-excepción)
- [2. Tipos de errores más comunes](#2-tipos-de-errores-más-comunes)
- [3. try y except](#3-try-y-except)
- [4. Capturar varias excepciones](#4-capturar-varias-excepciones)
- [5. else y finally](#5-else-y-finally)
- [6. Lanzar errores con raise](#6-lanzar-errores-con-raise)
- [7. Crear tus propias excepciones](#7-crear-tus-propias-excepciones)
- [8. Buenas prácticas](#8-buenas-prácticas)
- [9. Ejercicios](#9-ejercicios)

<a name = "1-qué-es-una-excepción"></a>

## 1. ¿Qué es una excepción?

Hasta ahora, cuando algo iba mal en nuestro programa, Python paraba la ejecución y nos mostraba un mensaje rojo de error. A ese mensaje se le llama **excepción**.

Una **excepción** es un evento que ocurre durante la ejecución de un programa y que interrumpe el flujo normal de las instrucciones. Por ejemplo, si intentamos dividir entre cero o convertir la palabra `"hola"` en un número, Python no sabe qué hacer y "lanza" (en inglés *raise*) una excepción.

```python
numero = int("hola")  # ValueError: invalid literal for int() with base 10: 'hola'
```

El **manejo de errores** consiste en preparar nuestro programa para que, en lugar de romperse, sepa **reaccionar** ante estos imprevistos y siga funcionando o avise al usuario de forma controlada.

>[!IMPORTANT]
>No es lo mismo un **error de sintaxis** (escribiste mal el código y Python ni siquiera puede ejecutarlo) que una **excepción** (el código es correcto, pero algo falla mientras se ejecuta). En este día trabajamos con las excepciones.

<a name = "2-tipos-de-errores-más-comunes"></a>

## 2. Tipos de errores más comunes

Python tiene muchas excepciones ya definidas. Estas son las que más te vas a encontrar mientras aprendes:

| Excepción | Cuándo ocurre |
| ----------------- | ------------------------------------------------- |
| `ValueError` | El valor no es del tipo esperado (`int("hola")`) |
| `TypeError` | Operación entre tipos incompatibles (`"2" + 2`) |
| `ZeroDivisionError` | Dividir entre cero (`10 / 0`) |
| `IndexError` | Acceder a un índice que no existe en una lista |
| `KeyError` | Acceder a una clave que no existe en un diccionario |
| `FileNotFoundError` | Intentar abrir un fichero que no existe |
| `NameError` | Usar una variable que no ha sido definida |

```python
lista = [1, 2, 3]
print(lista[10])   # IndexError: list index out of range

datos = {"nombre": "Ana"}
print(datos["edad"])  # KeyError: 'edad'
```

<a name = "3-try-y-except"></a>

## 3. try y except

La estructura básica para controlar errores son las palabras reservadas **`try`** y **`except`**:

- En el bloque **`try`** colocamos el código que *puede* fallar.
- En el bloque **`except`** colocamos lo que queremos hacer *si* falla.

```python
try:
    numero = int(input("Introduce un número: "))
    print(f"El doble es {numero * 2}")
except ValueError:
    print("Eso no es un número válido.")
```

Si el usuario escribe `5`, el programa imprime `El doble es 10`. Si escribe `hola`, en lugar de romperse muestra `Eso no es un número válido` y continúa.

```python
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
        return None

print(dividir(10, 2))  # 5.0
print(dividir(10, 0))  # No se puede dividir entre cero. -> None
```

>[!NOTE]
>Conviene capturar el tipo de error concreto (`except ValueError:`) en lugar de un `except:` "a secas". Así controlas solo lo que esperas que falle y no escondes otros errores que sí deberías ver.

<a name = "4-capturar-varias-excepciones"></a>

## 4. Capturar varias excepciones

Un mismo bloque `try` puede tener varios `except` para reaccionar de forma distinta según el error:

```python
try:
    lista = [1, 2, 3]
    indice = int(input("¿Qué posición quieres ver? "))
    print(lista[indice])
except ValueError:
    print("Debes introducir un número entero.")
except IndexError:
    print("Esa posición no existe en la lista.")
```

También podemos agrupar varias excepciones en un solo `except` usando una tupla, y guardar el mensaje del error en una variable con `as`:

```python
try:
    resultado = 10 / int(input("Divisor: "))
except (ValueError, ZeroDivisionError) as error:
    print(f"Ha ocurrido un problema: {error}")
```

<a name = "5-else-y-finally"></a>

## 5. else y finally

La estructura completa tiene cuatro bloques. `else` y `finally` son opcionales:

- **`try`**: el código que puede fallar.
- **`except`**: qué hacer si falla.
- **`else`**: se ejecuta **solo si NO hubo ningún error**.
- **`finally`**: se ejecuta **siempre**, haya error o no (ideal para "limpiar": cerrar ficheros, conexiones, etc.).

```python
try:
    numero = int(input("Introduce un número: "))
except ValueError:
    print("No era un número.")
else:
    print(f"Perfecto, el cuadrado es {numero ** 2}")
finally:
    print("Fin del programa. ¡Gracias!")
```

<a name = "6-lanzar-errores-con-raise"></a>

## 6. Lanzar errores con raise

A veces somos nosotros quienes queremos **provocar** un error a propósito, porque detectamos algo que no debería pasar. Para ello usamos la palabra reservada **`raise`**:

```python
def comprobar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    if edad < 18:
        raise ValueError("Debes ser mayor de edad.")
    return "Acceso permitido"

try:
    print(comprobar_edad(15))
except ValueError as error:
    print(f"Error: {error}")  # Error: Debes ser mayor de edad.
```

`raise` "lanza" la excepción hacia arriba para que quien llamó a la función decida cómo manejarla.

<a name = "7-crear-tus-propias-excepciones"></a>

## 7. Crear tus propias excepciones

Cuando los errores que trae Python no describen bien tu problema, puedes crear los tuyos. Una excepción personalizada es simplemente una **clase** que hereda de `Exception` (las clases las verás en profundidad en el siguiente día, aquí solo necesitas la idea):

```python
class SaldoInsuficienteError(Exception):
    """Se lanza cuando se intenta retirar más dinero del disponible."""
    pass

def retirar(saldo, cantidad):
    if cantidad > saldo:
        raise SaldoInsuficienteError("No tienes saldo suficiente.")
    return saldo - cantidad

try:
    nuevo_saldo = retirar(100, 250)
except SaldoInsuficienteError as error:
    print(f"Operación rechazada: {error}")
```

Usar nombres claros como `SaldoInsuficienteError` hace que tu código sea mucho más fácil de leer y mantener.

<a name = "8-buenas-prácticas"></a>

## 8. Buenas prácticas

- Captura **excepciones concretas**, no uses `except:` vacío salvo casos muy puntuales.
- No uses `try/except` para tapar errores de programación: si una variable está mal escrita, arréglala, no la escondas.
- Los mensajes de error deben ser **útiles** para quien usa el programa.
- Usa `finally` para liberar recursos (ficheros, conexiones).
- Validar primero (con `if`) y manejar la excepción después son técnicas que se complementan.

>[!IMPORTANT]
>Un programa profesional **no se rompe** delante del usuario. El manejo de errores es lo que separa un script de prácticas de una aplicación de verdad.

<a name = "9-ejercicios"></a>

## 9. Ejercicios

1. Crea un programa que pida un número por teclado y muestre su raíz cuadrada. Si el usuario escribe algo que no es un número, debe mostrar un mensaje amable en lugar de romperse.

2. Escribe una función `division_segura(a, b)` que devuelva la división de `a` entre `b`. Si `b` es 0, debe capturar el `ZeroDivisionError` y devolver el texto `"No se puede dividir entre cero"`.

3. Dada la siguiente lista, pide al usuario una posición y muestra el elemento. Controla tanto que escriba un número como que la posición exista.
```python
colores = ["rojo", "verde", "azul", "amarillo"]
```

4. Crea una función `acceder(diccionario, clave)` que devuelva el valor de una clave. Si la clave no existe, debe capturar el `KeyError` y devolver `"Clave no encontrada"`.

5. Escribe un programa con `try`, `except`, `else` y `finally` que pida la edad del usuario:
    - Si no es un número → mensaje en `except`.
    - Si es un número → en `else` di si es mayor o menor de edad.
    - En `finally` despídete siempre con un mensaje.

6. Crea una función `validar_password(password)` que lance (`raise`) un `ValueError` si la contraseña tiene menos de 8 caracteres, y otro si no contiene ningún número. Si está bien, devuelve `"Contraseña válida"`.

7. Crea una excepción personalizada llamada `TemperaturaInvalidaError`. Después, escribe una función `registrar_temperatura(grados)` que la lance si la temperatura es menor de -90 o mayor de 60 (valores imposibles en la Tierra).

8. Programa una pequeña calculadora por consola que pida dos números y una operación (`+`, `-`, `*`, `/`) y use manejo de errores para controlar entradas no numéricas y la división entre cero.

> [!NOTE]
> Pistas para los ejercicios:
> - Recuerda la estructura mínima: `try:` con el código peligroso y `except TipoDeError:` con la reacción.
> - Para la raíz cuadrada puedes usar `numero ** 0.5` o `import math` y `math.sqrt(numero)`.
> - Para lanzar un error usa `raise ValueError("mensaje")`.
> - Para crear tu excepción: `class MiError(Exception): pass`.
> - Guarda el mensaje del error con `except ValueError as error:` y úsalo con `print(error)`.

<h3 align = "center">
¡Ya sabes hacer que tus programas no se rompan! En el siguiente día damos un salto importante: la Programación Orientada a Objetos.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/13_Funciones_2/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/15_POO/readme.md">Día siguiente</a>
</h4>
