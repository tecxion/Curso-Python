<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/25_Context_Managers/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/27_APIs/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/sqlite.png">
</h1>


<h1 align="center">Bases de Datos con SQLite</h1><br>

<h3>Índice</h3>

- [1. ¿Por qué una base de datos?](#1-por-qué-una-base-de-datos)
- [2. SQLite y el módulo sqlite3](#2-sqlite-y-el-módulo-sqlite3)
- [3. Conectar y crear una tabla](#3-conectar-y-crear-una-tabla)
- [4. Insertar datos (INSERT)](#4-insertar-datos-insert)
- [5. Consultar datos (SELECT)](#5-consultar-datos-select)
- [6. Actualizar y borrar (UPDATE y DELETE)](#6-actualizar-y-borrar-update-y-delete)
- [7. Consultas seguras: parámetros](#7-consultas-seguras-parámetros)
- [8. Ejercicios](#8-ejercicios)

<a name = "1-por-qué-una-base-de-datos"></a>

## 1. ¿Por qué una base de datos?

En el día 17 guardamos datos en ficheros JSON. Funciona genial para cosas pequeñas, pero cuando hay **muchos** datos y necesitamos **buscar, ordenar y filtrar** de forma rápida y fiable, lo suyo es una **base de datos**.

Una base de datos organiza la información en **tablas** (parecidas a una hoja de cálculo): filas y columnas. Para hablar con ellas se usa un lenguaje llamado **SQL** (*Structured Query Language*), que aprenderás de forma básica hoy.

<a name = "2-sqlite-y-el-módulo-sqlite3"></a>

## 2. SQLite y el módulo sqlite3

**SQLite** es una base de datos que cabe en **un solo fichero** y no necesita instalar ningún servidor. Es perfecta para aprender y para aplicaciones pequeñas. Lo mejor: Python la trae **incluida** con el módulo **`sqlite3`**, sin instalar nada.

```python
import sqlite3
```

Toda la base de datos vivirá en un archivo (por ejemplo `mi_base.db`) que se crea solo.

<a name = "3-conectar-y-crear-una-tabla"></a>

## 3. Conectar y crear una tabla

Para trabajar con SQLite seguimos siempre el mismo patrón:

1. **Conectar** a la base de datos (`connect`).
2. Crear un **cursor** (el objeto que ejecuta las órdenes SQL).
3. Ejecutar SQL con `execute`.
4. **Confirmar** los cambios con `commit`.
5. **Cerrar** la conexión con `close`.

```python
import sqlite3

# 1. Conectar (crea el fichero si no existe)
conexion = sqlite3.connect("tienda.db")

# 2. Crear el cursor
cursor = conexion.cursor()

# 3. Crear una tabla (si no existe ya)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL,
        stock INTEGER
    )
""")

# 4. Confirmar y 5. cerrar
conexion.commit()
conexion.close()
```

Cada columna tiene un **tipo**: `INTEGER` (entero), `REAL` (decimal), `TEXT` (texto). `PRIMARY KEY AUTOINCREMENT` hace que el `id` se genere solo y sea único para cada fila.

<a name = "4-insertar-datos-insert"></a>

## 4. Insertar datos (INSERT)

Para añadir filas usamos la orden SQL `INSERT INTO`:

```python
import sqlite3

conexion = sqlite3.connect("tienda.db")
cursor = conexion.cursor()

cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES ('Camiseta', 19.99, 10)")
cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES ('Pantalón', 39.99, 5)")

conexion.commit()   # ¡imprescindible para que se guarde!
conexion.close()
```

>[!IMPORTANT]
>Si te olvidas del `commit()`, los cambios NO se guardan. Es el error más típico al empezar con bases de datos.

<a name = "5-consultar-datos-select"></a>

## 5. Consultar datos (SELECT)

`SELECT` recupera información. Tras ejecutarlo, leemos los resultados con `fetchall()` (todas las filas) o `fetchone()` (una sola):

```python
import sqlite3

conexion = sqlite3.connect("tienda.db")
cursor = conexion.cursor()

# Todos los productos
cursor.execute("SELECT * FROM productos")
filas = cursor.fetchall()
for fila in filas:
    print(fila)   # (1, 'Camiseta', 19.99, 10)

# Solo algunos, con condición y orden
cursor.execute("SELECT nombre, precio FROM productos WHERE precio < 30 ORDER BY precio")
for nombre, precio in cursor.fetchall():
    print(f"{nombre}: {precio}€")

conexion.close()
```

Cada fila se devuelve como una **tupla** (¿recuerdas las tuplas del día 5?).

<a name = "6-actualizar-y-borrar-update-y-delete"></a>

## 6. Actualizar y borrar (UPDATE y DELETE)

```python
import sqlite3

conexion = sqlite3.connect("tienda.db")
cursor = conexion.cursor()

# Actualizar
cursor.execute("UPDATE productos SET stock = 20 WHERE nombre = 'Camiseta'")

# Borrar
cursor.execute("DELETE FROM productos WHERE nombre = 'Pantalón'")

conexion.commit()
conexion.close()
```

>[!IMPORTANT]
>Mucho cuidado con `UPDATE` y `DELETE` **sin** un `WHERE`: cambiarían o borrarían **todas** las filas de la tabla.

<a name = "7-consultas-seguras-parámetros"></a>

## 7. Consultas seguras: parámetros

Nunca metas datos del usuario directamente en la consulta con un f-string: es peligroso (existe un ataque llamado *inyección SQL*). En su lugar, usa **`?`** como hueco y pasa los valores en una tupla:

```python
import sqlite3

conexion = sqlite3.connect("tienda.db")
cursor = conexion.cursor()

nombre = input("Nombre del producto: ")
precio = float(input("Precio: "))

# ✅ Forma segura: los ? se rellenan con la tupla
cursor.execute(
    "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
    (nombre, precio, 0)
)

conexion.commit()
conexion.close()
```

>[!NOTE]
>Recuerda lo del día 25: una conexión es un recurso. Puedes usar `with sqlite3.connect("tienda.db") as conexion:` para que se confirme y cierre de forma más segura.

<a name = "8-ejercicios"></a>

## 8. Ejercicios

Para estos ejercicios crearás una base de datos `agenda.db` con una tabla de contactos.

1. Crea la base de datos `agenda.db` y una tabla `contactos` con columnas `id` (clave primaria autoincremental), `nombre` (texto) y `telefono` (texto).

2. Inserta tres contactos en la tabla.

3. Consulta y muestra todos los contactos por pantalla.

4. Consulta solo los contactos cuyo nombre empiece por "A" (pista: `WHERE nombre LIKE 'A%'`).

5. Actualiza el teléfono de uno de los contactos.

6. Borra uno de los contactos por su nombre.

7. Escribe una función `añadir_contacto(nombre, telefono)` que inserte un contacto usando parámetros `?` (forma segura).

8. Escribe una función `buscar_contacto(nombre)` que devuelva el teléfono de un contacto, o un mensaje si no existe.

> [!NOTE]
> Pistas para los ejercicios:
> - El patrón siempre es: `connect` → `cursor` → `execute` → `commit` → `close`.
> - No olvides el `commit()` tras insertar, actualizar o borrar.
> - Usa `fetchall()` para varias filas y `fetchone()` para una.
> - Para datos del usuario usa `?` y una tupla, nunca f-strings.
> - `CREATE TABLE IF NOT EXISTS` evita errores si vuelves a ejecutar el programa.

<h3 align = "center">
¡Ya sabes guardar datos en una base de datos de verdad! Mañana conectaremos tu programa con internet consumiendo APIs web.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/25_Context_Managers/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/27_APIs/readme.md">Día siguiente</a>
</h4>
