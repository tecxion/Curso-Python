# Módulo String

```python
# Para importarlo
import string
```

## 1. Constantes más útiles

El módulo string incluye estas constantes predefinidas:
```python
import string

print(string.ascii_letters)    # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.ascii_lowercase)  # 'abcdefghijklmnopqrstuvwxyz'
print(string.ascii_uppercase)  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.digits)           # '0123456789'
print(string.hexdigits)        # '0123456789abcdefABCDEF'
print(string.octdigits)        # '01234567'
print(string.punctuation)      # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print(string.whitespace)       # ' \t\n\r\x0b\x0c' (espacios, tabs, saltos de línea)
```

## 2. Funciones principales

### 2.1. string.capwords() - Capitalizar palabras

- Capitaliza cada palabra de una cadena (similar a str.title() pero mejor):

```python
import string

texto = "hola   mundo python"
print(string.capwords(texto))  # "Hola   Mundo Python"
# Observa que respeta los espacios múltiples
```

### 2.2. Plantillas de texto (string.Template)

- Formateo seguro de cadenas (alternativa a f-strings):
```python
from string import Template

plantilla = Template("Hola, $nombre! Tu saldo es: $${monto}")
mensaje = plantilla.substitute(nombre="Ana", monto=100)
print(mensaje)  # "Hola, Ana! Tu saldo es: $100"
```

## 3. Comparación con métodos de str
Muchas operaciones pueden hacerse directamente con métodos de strings, pero las constantes de string son útiles para:

### 3.1 Validación de caracteres:
```python
def es_alfabetico(cadena):
    return all(c in string.ascii_letters for c in cadena)
```

### 3.2 Generación de contraseñas aleatorias.
```python
# Aquí usamos el módulo random que se explica a continuación.
import random
import string

def generar_contraseña(longitud=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))
```

## 4. Tabla de traducción (str.maketrans)

- Útil para reemplazar o eliminar caracteres:
```python
import string

# Crear tabla de traducción
trans = str.maketrans('aeiou', '12345', string.punctuation)

texto = "¡Hola, mundo!"
print(texto.translate(trans))  # "H4l2 m5nd2" (vocales reemplazadas y signos eliminados)
```

## 5. Rendimiento vs. Métodos nativos
- Para operaciones simples, los métodos de str suelen ser más rápidos:
```python
# Más rápido
"texto".upper()

# Más lento (pero útil para constantes)
string.ascii_uppercase
```

[Volver al Readme de módulos](../readme.md/#25-módulo-de-cadenas)