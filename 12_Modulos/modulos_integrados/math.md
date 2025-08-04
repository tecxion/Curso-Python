# Módulo math

A continuación están las funciones más utilizadas del módulo math y una breve descripción.

## 2. Constantes útiles

| Constante | Valor aproximado  | Descripción                           |
| --------- | ----------------- | ------------------------------------- |
| math.pi   | 3.141592653589793 | Número π (pi)                         |
| math.e    | 2.718281828459045 | Número e (base del logaritmo natural) |
| math.tau  | 6.283185307179586 | 2π (tau)                              |
| math.inf  | ∞                 | Infinito                              |
| math.nan  | NaN               | No es un número (Not a Number)        |

## 3. Funciones principales (compatibles en Windows/Linux/macOS)

- Funciones básicas

| Función             | Ejemplo                         | Resultado | Descripción                     |
| ------------------- | ------------------------------- | --------- | ------------------------------- |
| math.sqrt(x)        | math.sqrt(16)	4.0	Raíz cuadrada |
| math.pow(x, y)      | math.pow(2, 3)                  | 8.0       | Potencia (x elevado a y)        |
| math.exp(x)         | math.exp(1)                     | ~2.718    | e elevado a x                   |
| math.log(x[, base]) | math.log(100, 10)               | 2.0       | Logaritmo (base 10 si se omite) |
| math.fabs(x)        | math.fabs(-5.2)                 | 5.2       | Valor absoluto (float)          |


## Funciones trigonométricas

| Función         | Ejemplo               | Resultado (radianes) |
| --------------- | --------------------- | -------------------- |
| math.sin(x)     | math.sin(math.pi/2)   | 1.0                  |
| math.cos(x)     | math.cos(math.pi)     | -1.0                 |
| math.tan(x)     | math.tan(math.pi/4)   | ~1.0                 |
| math.degrees(x) | math.degrees(math.pi) | 180.0                |
| math.radians(x) | math.radians(180)     | 3.14159 (π)          |

## Funciones de redondeo y discretas

| Función           | Ejemplo           | Resultado | Descripción                |
| ----------------- | ----------------- | --------- | -------------------------- |
| math.ceil(x)      | math.ceil(3.2)    | 4         | Redondeo hacia arriba      |
| math.floor(x)     | math.floor(3.9)   | 3         | Redondeo hacia abajo       |
| math.trunc(x)     | math.trunc(-3.7)  | -3        | Trunca el decimal          |
| math.factorial(n) | math.factorial(5) | 120       | Factorial (5! = 5×4×3×2×1) |
| math.gcd(a, b)    | math.gcd(36, 60)  | 12        | Máximo común divisor       |


[Volver al Readme de módulos](../readme.md)