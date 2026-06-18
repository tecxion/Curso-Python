<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/20_Fechas/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/22_Type_Hints/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/regex.png">
</h1>


<h1 align="center">Expresiones Regulares (Regex)</h1><br>

<h3>Índice</h3>

- [1. ¿Qué son las expresiones regulares?](#1-qué-son-las-expresiones-regulares)
- [2. El módulo re](#2-el-módulo-re)
- [3. Funciones principales](#3-funciones-principales)
- [4. Metacaracteres básicos](#4-metacaracteres-básicos)
- [5. Clases de caracteres](#5-clases-de-caracteres)
- [6. Cuantificadores](#6-cuantificadores)
- [7. Grupos y extracción de datos](#7-grupos-y-extracción-de-datos)
- [8. Sustituir texto con sub](#8-sustituir-texto-con-sub)
- [9. Ejercicios](#9-ejercicios)

<a name = "1-qué-son-las-expresiones-regulares"></a>

## 1. ¿Qué son las expresiones regulares?

Una **expresión regular** (o *regex*) es un **patrón** que describe un conjunto de textos. Sirven para **buscar**, **validar** y **extraer** información de cadenas de texto de forma muy potente.

Por ejemplo, en lugar de escribir un montón de `if` para comprobar si un texto "parece" un email, definimos un patrón que describe cómo es un email y lo comprobamos de una vez. Las regex se usan para validar formularios (emails, teléfonos, DNIs), buscar palabras en textos enormes, extraer datos, etc.

>[!IMPORTANT]
>Las expresiones regulares cuestan un poco al principio porque parecen "jeroglíficos". No intentes memorizarlas: entiende las piezas y ten esta página a mano como chuleta. Con la práctica se vuelven naturales.

<a name = "2-el-módulo-re"></a>

## 2. El módulo re

En Python las regex se manejan con el módulo **`re`** (de *regular expressions*), incluido en la librería estándar:

```python
import re
```

Un detalle importante: los patrones se escriben como **cadenas "raw"**, poniendo una `r` delante (`r"..."`). Esto evita que Python interprete las barras invertidas `\` de forma rara.

```python
patron = r"\d+"     # la r delante es muy recomendable en regex
```

<a name = "3-funciones-principales"></a>

## 3. Funciones principales

Estas son las funciones del módulo `re` que más usarás:

| Función | Qué hace |
| ------------------ | --------------------------------------------------- |
| `re.search()` | Busca el patrón en cualquier parte del texto |
| `re.match()` | Comprueba si el texto **empieza** por el patrón |
| `re.findall()` | Devuelve una **lista** con todas las coincidencias |
| `re.sub()` | **Sustituye** las coincidencias por otro texto |
| `re.fullmatch()` | Comprueba si el texto **entero** encaja con el patrón |

```python
import re

texto = "Mi teléfono es 600123456 y mi código postal 28080"

resultado = re.search(r"\d+", texto)
print(resultado.group())   # 600123456  (la primera coincidencia)

numeros = re.findall(r"\d+", texto)
print(numeros)             # ['600123456', '28080']
```

`re.search()` devuelve un objeto *match* (o `None` si no encuentra nada); con `.group()` obtenemos el texto encontrado.

<a name = "4-metacaracteres-básicos"></a>

## 4. Metacaracteres básicos

Los **metacaracteres** son símbolos con significado especial dentro de un patrón:

| Símbolo | Significado |
| ------- | -------------------------------------------- |
| `.` | Cualquier carácter (menos el salto de línea) |
| `^` | Principio del texto |
| `$` | Final del texto |
| `\|` | "O" lógico (una cosa u otra) |
| `\` | Escapa un metacarácter para buscarlo literal |

```python
import re

print(bool(re.search(r"^Hola", "Hola mundo")))   # True  (empieza por "Hola")
print(bool(re.search(r"mundo$", "Hola mundo")))   # True  (termina en "mundo")
print(re.findall(r"gato|perro", "tengo un gato y un perro"))  # ['gato', 'perro']
```

<a name = "5-clases-de-caracteres"></a>

## 5. Clases de caracteres

Las **clases de caracteres** representan tipos de caracteres. Son de lo más usado:

| Clase | Significa | Equivale a |
| ----- | ----------------------------- | ------------- |
| `\d` | Un dígito | `[0-9]` |
| `\D` | Lo que NO es un dígito | |
| `\w` | Letra, número o guion bajo | `[a-zA-Z0-9_]` |
| `\W` | Lo que NO es `\w` | |
| `\s` | Un espacio en blanco | espacio, tab… |
| `[abc]` | Una a, b o c | |
| `[a-z]` | Una letra minúscula | |
| `[^abc]` | Cualquier cosa MENOS a, b o c | |

```python
import re

texto = "El pedido A-123 cuesta 45 euros"
print(re.findall(r"\d", texto))       # ['1', '2', '3', '4', '5'] (dígito a dígito)
print(re.findall(r"[A-Z]", texto))    # ['E', 'A']  (mayúsculas)
```

<a name = "6-cuantificadores"></a>

## 6. Cuantificadores

Los **cuantificadores** indican **cuántas veces** se repite lo anterior:

| Símbolo | Significa |
| ------- | ----------------------------- |
| `*` | 0 o más veces |
| `+` | 1 o más veces |
| `?` | 0 o 1 vez (opcional) |
| `{n}` | Exactamente n veces |
| `{n,m}`| Entre n y m veces |

```python
import re

print(re.findall(r"\d+", "casa 12 y 345"))   # ['12', '345']  (grupos de dígitos)
print(re.findall(r"\d{2}", "1 22 333"))       # ['22', '33']   (de dos en dos)

# Validar un código postal español (exactamente 5 dígitos)
codigo = "28080"
print(bool(re.fullmatch(r"\d{5}", codigo)))   # True
```

<a name = "7-grupos-y-extracción-de-datos"></a>

## 7. Grupos y extracción de datos

Los **paréntesis** crean **grupos**, que sirven para extraer trozos concretos de una coincidencia. Cada grupo se recupera con `.group(1)`, `.group(2)`, etc.

```python
import re

fecha = "Hoy es 18/03/2025"
patron = r"(\d{2})/(\d{2})/(\d{4})"
resultado = re.search(patron, fecha)

print(resultado.group())    # 18/03/2025  (todo el patrón)
print(resultado.group(1))   # 18   (primer grupo: día)
print(resultado.group(2))   # 03   (segundo grupo: mes)
print(resultado.group(3))   # 2025 (tercer grupo: año)
```

Esto es la base de la **extracción de datos**: defines un patrón con grupos y vas sacando justo lo que te interesa.

<a name = "8-sustituir-texto-con-sub"></a>

## 8. Sustituir texto con sub

`re.sub()` reemplaza todas las coincidencias de un patrón por otro texto. Es como un "buscar y reemplazar" con superpoderes:

```python
import re

texto = "Llama al 600-123-456 o al 700-999-888"

# Ocultar los teléfonos
censurado = re.sub(r"\d", "*", texto)
print(censurado)   # Llama al ***-***-*** o al ***-***-***

# Quitar los espacios de más
sucio = "Hola     mundo    Python"
limpio = re.sub(r"\s+", " ", sucio)
print(limpio)      # Hola mundo Python
```

<a name = "9-ejercicios"></a>

## 9. Ejercicios

1. Usa `re.findall` para extraer todos los números del texto `"Compré 3 manzanas, 12 peras y 7 plátanos"`.

2. Comprueba con una regex si el texto `"Python3"` contiene algún dígito.

3. Escribe una función `es_codigo_postal(texto)` que devuelva `True` si el texto son exactamente 5 dígitos.

4. Escribe una función `es_email(texto)` que valide un email sencillo (algo, una arroba, algo, un punto y al menos dos letras). Pista: `r"\w+@\w+\.\w{2,}"`.

5. Del texto `"El partido acabó 3-2 en el minuto 89"`, extrae con grupos los dos goles (el `3` y el `2`) por separado.

6. Usa `re.sub` para sustituir todos los espacios de un texto por guiones bajos.

7. Extrae todas las palabras que empiecen por mayúscula del texto `"Ana y Luis fueron a Madrid en Marzo"`.

8. Escribe una función `validar_telefono(numero)` que acepte teléfonos españoles de 9 dígitos que empiecen por 6, 7, 8 o 9.

> [!NOTE]
> Pistas para los ejercicios:
> - Importa siempre `import re` y escribe los patrones como `r"..."`.
> - Para validar el texto ENTERO usa `re.fullmatch`; para buscar dentro, `re.search`.
> - `re.search` y `re.fullmatch` devuelven `None` si no hay coincidencia: úsalo con `bool(...)`.
> - Para "una o más veces" usa `+`; para "exactamente 5" usa `{5}`.
> - Palabra que empieza por mayúscula: `r"[A-Z]\w*"`.
> - Teléfono español: empieza por `[6-9]` y luego 8 dígitos más → `r"[6-9]\d{8}"`.

<h3 align = "center">
¡Las regex ya no te dan miedo! Mañana hacemos tu código más claro y robusto con las anotaciones de tipo y las dataclasses.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/20_Fechas/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/22_Type_Hints/readme.md">Día siguiente</a>
</h4>
