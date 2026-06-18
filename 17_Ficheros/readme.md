<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/16_POO_2/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/18_Comprehensions/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/ficheros.png">
</h1>


<h1 align="center">Manejo de Ficheros</h1><br>

<h3>Índice</h3>

- [1. ¿Por qué leer y escribir ficheros?](#1-por-qué-leer-y-escribir-ficheros)
- [2. Abrir un fichero: open() y los modos](#2-abrir-un-fichero-open-y-los-modos)
- [3. La sentencia with (la forma recomendada)](#3-la-sentencia-with-la-forma-recomendada)
- [4. Leer ficheros de texto](#4-leer-ficheros-de-texto)
- [5. Escribir en ficheros de texto](#5-escribir-en-ficheros-de-texto)
- [6. Trabajar con JSON](#6-trabajar-con-json)
- [7. Trabajar con CSV](#7-trabajar-con-csv)
- [8. Rutas y errores al trabajar con ficheros](#8-rutas-y-errores-al-trabajar-con-ficheros)
- [9. Ejercicios](#9-ejercicios)

<a name = "1-por-qué-leer-y-escribir-ficheros"></a>

## 1. ¿Por qué leer y escribir ficheros?

Hasta ahora, toda la información de nuestros programas (listas, diccionarios, objetos…) **desaparecía** al cerrarlos, porque vivía solo en la memoria. Para que los datos **persistan** necesitamos guardarlos en un **fichero** del disco duro.

Saber manejar ficheros nos permite, por ejemplo:
- Guardar la lista de tareas de un usuario y recuperarla mañana.
- Leer un fichero de configuración.
- Exportar resultados a un `.csv` que se abra en Excel.

>[!IMPORTANT]
>Para que un programa lea o escriba en una ruta, esa ruta debe ser accesible. Mientras aprendes, trabaja con ficheros que estén **en la misma carpeta** que tu `.py` para no complicarte con las rutas.

<a name = "2-abrir-un-fichero-open-y-los-modos"></a>

## 2. Abrir un fichero: open() y los modos

La función integrada **`open()`** abre un fichero. Recibe la ruta y un **modo** que indica qué queremos hacer:

| Modo | Significado | Si el fichero no existe |
| ----- | --------------------------------------- | ----------------------- |
| `"r"` | Lectura (*read*). Es el modo por defecto | Da error |
| `"w"` | Escritura (*write*). **Borra el contenido anterior** | Lo crea |
| `"a"` | Añadir (*append*). Escribe al final | Lo crea |
| `"x"` | Crear. Falla si ya existe | Lo crea |
| `"r+"`| Lectura y escritura | Da error |

>[!NOTE]
>Es muy importante recordar que **`"w"` borra todo lo que hubiera** en el fichero. Si solo quieres añadir contenido sin perder lo anterior, usa `"a"`.

También conviene indicar la **codificación** con `encoding="utf-8"` para que las tildes y la "ñ" se guarden bien.

<a name = "3-la-sentencia-with-la-forma-recomendada"></a>

## 3. La sentencia with (la forma recomendada)

Cuando abrimos un fichero hay que **cerrarlo** después con `.close()`. Es fácil olvidarlo, y si el programa falla a mitad, el fichero queda abierto. Por eso la forma recomendada es la sentencia **`with`**, que **cierra el fichero automáticamente** al terminar el bloque (incluso si hay un error):

```python
# Forma NO recomendada (hay que acordarse de cerrar)
fichero = open("notas.txt", "w", encoding="utf-8")
fichero.write("Hola")
fichero.close()

# Forma RECOMENDADA con with (se cierra solo)
with open("notas.txt", "w", encoding="utf-8") as fichero:
    fichero.write("Hola")
# aquí el fichero ya está cerrado automáticamente
```

A partir de ahora usaremos siempre `with`.

<a name = "4-leer-ficheros-de-texto"></a>

## 4. Leer ficheros de texto

Hay varias formas de leer, según lo que necesites:

```python
# Leer TODO el contenido como un único string
with open("notas.txt", "r", encoding="utf-8") as fichero:
    contenido = fichero.read()
    print(contenido)

# Leer todas las líneas en una LISTA
with open("notas.txt", "r", encoding="utf-8") as fichero:
    lineas = fichero.readlines()
    print(lineas)   # ['línea 1\n', 'línea 2\n', ...]

# Recorrer el fichero línea a línea (lo más eficiente)
with open("notas.txt", "r", encoding="utf-8") as fichero:
    for linea in fichero:
        print(linea.strip())   # strip() quita el salto de línea \n
```

>[!NOTE]
>Cada línea de texto termina con un carácter de salto de línea `\n`. El método `.strip()` es muy útil para eliminarlo al leer.

<a name = "5-escribir-en-ficheros-de-texto"></a>

## 5. Escribir en ficheros de texto

Usamos `.write()` para escribir un texto, o `.writelines()` para escribir una lista de textos. Recuerda añadir tú el salto de línea `\n`:

```python
# Escribir (CUIDADO: "w" borra lo anterior)
with open("compra.txt", "w", encoding="utf-8") as fichero:
    fichero.write("Pan\n")
    fichero.write("Leche\n")

# Añadir al final sin borrar ("a")
with open("compra.txt", "a", encoding="utf-8") as fichero:
    fichero.write("Huevos\n")

# Escribir una lista entera
tareas = ["Estudiar\n", "Entrenar\n", "Programar\n"]
with open("tareas.txt", "w", encoding="utf-8") as fichero:
    fichero.writelines(tareas)
```

<a name = "6-trabajar-con-json"></a>

## 6. Trabajar con JSON

El **JSON** es un formato de texto muy usado para guardar datos estructurados (listas y diccionarios). Es ideal para guardar el estado de un programa, porque se parece muchísimo a los diccionarios de Python. Se usa con el módulo **`json`** (que ya viene incluido):

```python
import json

usuario = {
    "nombre": "Ana",
    "edad": 30,
    "hobbies": ["leer", "programar"]
}

# Guardar un diccionario en un fichero .json  (dump = volcar)
with open("usuario.json", "w", encoding="utf-8") as fichero:
    json.dump(usuario, fichero, indent=4, ensure_ascii=False)

# Leer un fichero .json y convertirlo de nuevo en diccionario (load = cargar)
with open("usuario.json", "r", encoding="utf-8") as fichero:
    datos = json.load(fichero)

print(datos["nombre"])   # Ana
print(datos["hobbies"])  # ['leer', 'programar']
```

- `indent=4` hace que el fichero quede bien formateado y legible.
- `ensure_ascii=False` permite guardar tildes y "ñ" tal cual.

<a name = "7-trabajar-con-csv"></a>

## 7. Trabajar con CSV

Un **CSV** (*Comma-Separated Values*) es un fichero de texto con datos separados por comas, como una tabla. Es el formato típico para hojas de cálculo. Usamos el módulo **`csv`**:

```python
import csv

# Escribir un CSV
with open("personas.csv", "w", newline="", encoding="utf-8") as fichero:
    escritor = csv.writer(fichero)
    escritor.writerow(["nombre", "edad", "ciudad"])   # cabecera
    escritor.writerow(["Ana", 30, "Madrid"])
    escritor.writerow(["Luis", 25, "Sevilla"])

# Leer un CSV
with open("personas.csv", "r", encoding="utf-8") as fichero:
    lector = csv.reader(fichero)
    for fila in lector:
        print(fila)   # ['nombre', 'edad', 'ciudad'], ['Ana', '30', 'Madrid'], ...
```

>[!NOTE]
>El parámetro `newline=""` al escribir evita que aparezcan líneas en blanco entre filas. También existe `csv.DictReader` para leer cada fila como un diccionario, muy cómodo.

<a name = "8-rutas-y-errores-al-trabajar-con-ficheros"></a>

## 8. Rutas y errores al trabajar con ficheros

Trabajar con ficheros es uno de los sitios donde más conviene aplicar lo que aprendiste en el **día 14**: si intentamos leer un fichero que no existe, Python lanza `FileNotFoundError`.

```python
try:
    with open("no_existe.txt", "r", encoding="utf-8") as fichero:
        print(fichero.read())
except FileNotFoundError:
    print("El fichero no existe todavía.")
```

Un patrón muy habitual: intentar **cargar** los datos guardados y, si el fichero aún no existe (primera vez que se ejecuta), empezar con datos vacíos.

```python
import json

def cargar_datos():
    try:
        with open("datos.json", "r", encoding="utf-8") as fichero:
            return json.load(fichero)
    except FileNotFoundError:
        return []   # primera ejecución: lista vacía
```

<a name = "9-ejercicios"></a>

## 9. Ejercicios

1. Crea un programa que escriba en un fichero `frases.txt` tres frases motivadoras (una por línea). Luego ábrelo y muestra su contenido por pantalla.

2. Crea un programa que añada (sin borrar lo anterior) una nueva línea al fichero `frases.txt` cada vez que se ejecute.

3. Escribe una función `contar_lineas(ruta)` que reciba la ruta de un fichero y devuelva cuántas líneas tiene. Controla el caso de que el fichero no exista.

4. Crea un pequeño "diario": un programa que pida al usuario una entrada de texto y la añada al fichero `diario.txt` precedida de un guion.

5. Crea un diccionario con tus datos (nombre, edad, lenguajes que conoces) y guárdalo en un fichero `perfil.json`. Después léelo y muestra los datos.

6. Escribe una función `guardar_tareas(lista)` y otra `cargar_tareas()` que guarden y lean una lista de tareas en un fichero `tareas.json`. Si el fichero no existe, `cargar_tareas()` debe devolver una lista vacía.

7. Crea un fichero `notas.csv` con las columnas `alumno` y `nota`, y añade tres alumnos. Después léelo y calcula e imprime la nota media de la clase.

8. Crea un programa de "agenda de contactos" sencillo que guarde nombres y teléfonos en un fichero JSON. Debe permitir añadir un contacto nuevo y listar todos los contactos guardados (aprovecha lo aprendido sobre cargar datos existentes).

> [!NOTE]
> Pistas para los ejercicios:
> - Usa siempre `with open(...) as fichero:` para no tener que cerrarlo a mano.
> - Recuerda el modo: `"w"` borra, `"a"` añade, `"r"` lee.
> - Añade `\n` al final de cada línea que escribas en texto.
> - Para JSON: `json.dump(dato, fichero)` para guardar y `json.load(fichero)` para leer.
> - Para contar líneas o leer todo, recuerda `.read()`, `.readlines()` o recorrer el fichero con un `for`.
> - Envuelve la lectura en `try / except FileNotFoundError` para la primera ejecución.

<h3 align = "center">
¡Ahora tus programas pueden recordar información! Este día será clave para el proyecto final. Seguimos con una de las herramientas más elegantes de Python: las comprensiones y los generadores.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/16_POO_2/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/18_Comprehensions/readme.md">Día siguiente</a>
</h4>
