<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/operadores.png">
</h1>

# Capítulo 2: Operadores.

- [Capítulo 2: Operadores.](#capítulo-2-operadores)
  - [1. Operadores de Asignación](#1-operadores-de-asignación)
    - [Ejemplo:](#ejemplo)
  - [Operadores aritméticos](#operadores-aritméticos)
    - [Ejemplo:](#ejemplo-1)
  - [Operadores de comparación](#operadores-de-comparación)
    - [Ejemplo:](#ejemplo-2)
  - [Operadores Lógicos](#operadores-lógicos)


En este capítulo, exploraremos los **operadores** en Python, que son símbolos especiales utilizados para realizar operaciones entre valores o variables. Los operadores son fundamentales en la programación, ya que nos permiten manipular datos y tomar decisiones dentro de nuestros programas.

Python incluye varios tipos de operadores, que se clasifican en las siguientes categorías:


---
<a name="operadoresasignacion"></a>

## 1. Operadores de Asignación

Los **operadores de asignación** se utilizan para asignar valores a variables. Además de la asignación básica (`=`), existen operadores combinados que realizan una operación y asignan el resultado en un solo paso.

| Operador                                                                                   | Descripción                     | Ejemplo                        | Equivalente      |
| ------------------------------------------------------------------------------------------ | ------------------------------- | ------------------------------ | ---------------- |
| `=`                                                                                        | Asigna un valor                 | `x = 5`                        | `x = 5`          |
| `+=`                                                                                       | Suma y asigna                   | `x += 3`                       | `x = x + 3`      |
| `-=`                                                                                       | Resta y asigna                  | `x -= 2`                       | `x = x - 2`      |
| `*=`                                                                                       | Multiplica y asigna             | `x *= 4`                       | `x = x * 4`      |
| `/=`                                                                                       | Divide y asigna                 | `x /= 2`                       | `x = x / 2`      |
| `%=`                                                                                       | Calcula el módulo y asigna      | `x %= 3`                       | `x = x % 3`      |
| `//=`                                                                                      | Divide de forma entera y asigna | `x //= 2`                      | `x = x // 2`     |
| `**=`                                                                                      | Potencia y asigna               | `x **= 3`                      | `x = x ** 3`     |
| <<=                                                                                        | Desplaza bits a la izquierda    | `x <<= 2`                      | `x = x << 2`     |
| >>=                                                                                        | Desplaza bits a la derecha      | `x >>= 1`                      | `x = x >> 1`     |
| &=                                                                                         | Realiza operación AND bit a bit | `x &= 0b1010`                  | `x = x & 0b1010` |
| ^=                                                                                         | Realiza operación XOR bit a bit | `x ^= 0b1100`                  | `x = x ^ 0b100`  |
|                                                                                            | =                               | Realiza operación OR bit a bit | `x               | = 0b1111` | `x = x | 0b1111` |
| __________________________________________________________________________________________ |

### Ejemplo:
```python
x = 10
x += 5  # x ahora es 15
x *= 2  # x ahora es 30

```

<a name="operadoresaritmeticos"></a>

## Operadores aritméticos

Los operadores aritméticos se utilizan para realizar operaciones matemáticas básicas.

______________________________________________________________________________________
| OPERADOR                                                                             | DESCRIPCIÓN     | EJEMPLO | RESULTADO |
| ------------------------------------------------------------------------------------ | --------------- | ------- | --------- |
| +                                                                                    | Suma            | 3 + 1   | 4         |
| -                                                                                    | Resta           | 3 - 1   | 2         |
| *                                                                                    | Multiplicación  | 3 * 2   | 6         |
| /                                                                                    | División        | 4 / 2   | 2         |
| %                                                                                    | Módulo          | 10 % 3  | 1         |
| **                                                                                   | Potencia        | 2 ** 3  | 8         |
| //                                                                                   | División entera | 10 // 3 | 3         |
| ____________________________________________________________________________________ |

### Ejemplo:
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

## Operadores de comparación

Los operadores de comparación se utilizan para comparar dos valores. Devuelven un valor booleano (True o False) como resultado.

______________________________________________________________________________________
| OPERADOR                                                                              | DESCRIPCIÓN       | EJEMPLO | RESULTADO |
| ------------------------------------------------------------------------------------- | ----------------- | ------- | --------- |
| ==                                                                                    | Igualdad          | 3 == 2  | False     |
| !=                                                                                    | Desigualdad       | 3 != 2  | True      |
| >                                                                                     | Mayor que         | 3 > 2   | True      |
| <                                                                                     | Menor que         | 3 < 2   | False     |
| >=                                                                                    | Mayor o igual que | 3 >= 2  | True      |
| <=                                                                                    | Menor o igual que | 3 <= 2  | False     |
| _____________________________________________________________________________________ |

### Ejemplo:
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

<a name="operadoresaritmeticos"></a>

## Operadores Lógicos

Los operadores lógicos se utilizan para combinar expresiones booleanas y devolver un resultado basado en la lógica.