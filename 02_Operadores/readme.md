<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/operadores.png">
</h1>

# Capítulo 2: Operadores.

- [Capítulo 2: Operadores.](#capítulo-2-operadores)
  - [1. Operadores de Asignación](#1-operadores-de-asignación)
  - [2. Operadores aritméticos](#2-operadores-aritméticos)
  - [3. Operadores de comparación](#3-operadores-de-comparación)
  - [4. Operadores Lógicos](#4-operadores-lógicos)
  - [5. Booleanos](#5-booleanos)
    - [Conversión a Booleanos:](#conversión-a-booleanos)
  - [6. Ejercicios](#6-ejercicios)


En este capítulo, exploraremos los **operadores** en Python, que son símbolos especiales utilizados para realizar operaciones entre valores o variables. Los operadores son fundamentales en la programación, ya que nos permiten manipular datos y tomar decisiones dentro de nuestros programas.

Python incluye varios tipos de operadores, que se clasifican en las siguientes categorías:


---
<a name="operadoresasignacion"></a>

## 1. Operadores de Asignación

Los **operadores de asignación** se utilizan para asignar valores a variables. Además de la asignación básica (`=`), existen operadores combinados que realizan una operación y asignan el resultado en un solo paso.

| Operador | Descripción                     | Ejemplo     | Equivalente    |
| -------- | ------------------------------- | ----------- | -------------- |
| =        | Asigna un valor                 | x = 5       | x = 5          |
| +=       | Suma y asigna                   | x += 3      | x = x + 3      |
| -=       | Resta y asigna                  | x -= 2      | x = x - 2      |
| *=       | Multiplica y asigna             | x *= 4      | x = x * 4      |
| /=       | Divide y asigna                 | x /= 2      | x = x / 2      |
| %=       | Calcula el módulo y asigna      | x %= 3      | x = x % 3      |
| //=      | Divide de forma entera y asigna | x //= 2     | x = x // 2     |
| **=      | Potencia y asigna               | x **= 3     | x = x ** 3     |
| <<=      | Desplaza bits a la izquierda    | x <<= 2     | x = x << 2     |
| >>=      | Desplaza bits a la derecha      | x >>= 1     | x = x >> 1     |
| &=       | Realiza operación AND bit a bit | x &= 0b1010 | x = x & 0b1010 |
| ^=       | Realiza operación XOR bit a bit | x ^= 0b1100 | x = x ^ 0b100  |

- Ejemplo:
```python
x = 10
x += 5  # x ahora es 15
x *= 2  # x ahora es 30

```

<a name="operadoresaritmeticos"></a>

## 2. Operadores aritméticos

Los operadores aritméticos se utilizan para realizar operaciones matemáticas básicas.


| Operador | Descripción     | Ejemplo | Resultado |
| -------- | --------------- | ------- | --------- |
| +        | Suma            | 3 + 1   | 4         |
| -        | Resta           | 3 - 1   | 2         |
| *        | Multiplicación  | 3 * 2   | 6         |
| /        | División        | 4 / 2   | 2         |
| %        | Módulo          | 10 % 3  | 1         |
| **       | Potencia        | 2 ** 3  | 8         |
| //       | División entera | 10 // 3 | 3         |

- Ejemplo:
```python
a = 5
b = 3
print(a + b)  # suma es 8
print(a - b)  # resta es 2
print(a * b)  # multiplicacion es 15
print(a / b)  # division es 1.6666666666666667
print(a % b)  # modulo es 2
print(a ** b)  # potencia es 125
print(a // b)  # division_entera es 1
```


<a name="operadoresdecomparacion"></a>

## 3. Operadores de comparación

Los operadores de comparación se utilizan para comparar dos valores. Devuelven un valor booleano (True o False) como resultado.


| OPERADOR | DESCRIPCIÓN       | EJEMPLO | RESULTADO |
| -------- | ----------------- | ------- | --------- |
| ==       | Igualdad          | 3 == 2  | False     |
| !=       | Desigualdad       | 3 != 2  | True      |
| >        | Mayor que         | 3 > 2   | True      |
| <        | Menor que         | 3 < 2   | False     |
| >=       | Mayor o igual que | 3 >= 2  | True      |
| <=       | Menor o igual que | 3 <= 2  | False     |

- Ejemplo:
```python
a = 5
b = 3
print(a == b)  # igualdad es False
print(a != b)  # desigualdad es True
print(a > b)  # mayor que es True
print(a < b)  # menor que es False
print(a >= b)  # mayor o igual que es True
print(a <= b)  # menor o igual que es False
```

<a name="operadoreslogicos"></a>

## 4. Operadores Lógicos

Los operadores lógicos se utilizan para combinar expresiones booleanas y devolver un resultado basado en la lógica.

| OPERADOR | DESCRIPCIÓN | EJEMPLO        | RESULTADO |
| -------- | ----------- | -------------- | --------- |
| and      | AND         | True and False | False     |
| or       | OR          | True or False  | True      |
| not      | NOT         | not True       | False     |

- Ejemplo:
```python
a = True
b = False
print(a and b)  # and es False
print(a or b)  # or es True
print(not a)  # not es False
```

## 5. Booleanos

Los booleanos son un tipo de dato que puede tener solo dos valores: True o False. Son útiles para representar estados lógicos, como encendido/apagado, verdadero/falso, etc.

- Características:
    - Se utilizan comúnmente en estructuras condicionales (if, while) y en operaciones lógicas.
    - También pueden ser el resultado de una comparación o una operación lógica.
```python
# Ejemplo de uso de booleanos en una estructura condicional
encendido = True
apagado = False

print(encendido)  # Salida: True
print(apagado)    # Salida: False

# Combinando con operadores lógicos
print(encendido and apagado)  # Salida: False
print(encendido or apagado)   # Salida: True
```

<a name="conversion-a-booleanos"></a>

### Conversión a Booleanos:

Cualquier valor en Python puede convertirse implícitamente a un booleano. Por ejemplo:

Valores como 0, None, "" (cadena vacía), [] (lista vacía) se consideran False. Cualquier otro valor se considera True.

- Ejemplo:
```python
print(bool(0))        # Salida: False
print(bool("Hola"))   # Salida: True
print(bool([]))       # Salida: False
```

<a name="6-ejercicios"></a>

## 6. Ejercicios

- Ejercicio 1: 
    - Pide al usuario que ingrese dos números, y el programa automáticamente debe calcular la suma, la resta, la multiplicación y la división de estos números.
    - Haz que el programa compare esos dos números y muestre si son o no iguales de diferentes formas.
    - Comprueba cual de los números es mayor o menor de diferentes formas.
    - Suma al número 1 del usuario el valor de 4 y almacénalo en la misma variable y muestra el resultado.
    - Potencia el número al cubo (3) y asígnalo a la misma variable y muestra el resultado.