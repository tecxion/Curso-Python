# Módulo random


## Importar el módulo
```python
import random
```

## 2. Funciones Principales
- 🔢 Generación de Números Aleatorios

| Función                      | Descripción                      | Ejemplo                           |
| ---------------------------- | -------------------------------- | --------------------------------- |
| random()                     | Número float entre [0.0, 1.0)    | random.random() → 0.5487          |
| uniform(a, b)                | Float en [a, b]                  | random.uniform(1.5, 3.5) → 2.8731 |
| randint(a, b)                | Entero en [a, b] (incluye ambos) | random.randint(1, 10) → 7         |
| randrange(start, stop, step) | Como range() pero aleatorio      | random.randrange(0, 100, 5) → 35  |

- 🎲 Selecciones Aleatorias

| Función           | Descripción                            | Ejemplo                                 |
| ----------------- | -------------------------------------- | --------------------------------------- |
| choice(seq)       | Elemento aleatorio de una secuencia    | random.choice(['a', 'b', 'c']) → 'b'    |
| choices(seq, k=n) | Lista con n elementos (con repetición) | random.choices([1, 2, 3], k=2) → [3, 3] |
| sample(seq, k=n)  | Lista con n elementos únicos           | random.sample([1, 2, 3, 4], 2) → [4, 1] |
| shuffle(seq)      | Mezcla la secuencia in-place           | random.shuffle([1, 2, 3]) → [2, 1, 3]   |

- 📊 Distribuciones Estadísticas

| Función                  | Descripción                     |
| ------------------------ | ------------------------------- |
| gauss(mu, sigma)         | Distribución normal (gaussiana) |
| expovariate(lambd)       | Distribución exponencial        |
| betavariate(alpha, beta) | Distribución beta               |

## Ejemplos

- 🎯 Simulación de lanzamiento de moneda
```python
import random
resultado = random.choice(['Cara', 'Cruz'])
print(f"Salio: {resultado}")
```

- 🎲 Tirar un dado de 6 caras

```python
import random
dado = random.randint(1, 6)
print(f"El dado muestra: {dado}")
```

- 📊 Generar contraseña aleatoria
```python
import string
import random
caracteres = string.ascii_letters + string.digits + "!@#$%"
password = ''.join(random.choices(caracteres, k=12))
print(f"Contraseña: {password}")
```

## 5. Precauciones Importantes

- No es criptográficamente seguro: Para seguridad usa secrets (ej: contraseñas).
- No usar para muestreos científicos: En ciencia de datos prefiere numpy.random.

[Volver al Readme de módulos](../readme.md/#26-módulo-aleatorio)