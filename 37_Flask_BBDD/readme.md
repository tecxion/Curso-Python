<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/36_API_REST/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/38_Despliegue/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/bbdd_web.png">
</h1>


<h1 align="center">Flask + Base de Datos (SQLAlchemy)</h1><br>

<h3>Índice</h3>

- [1. El problema: los datos se pierden](#1-el-problema-los-datos-se-pierden)
- [2. ¿Qué es un ORM?](#2-qué-es-un-orm)
- [3. Configurar Flask-SQLAlchemy](#3-configurar-flask-sqlalchemy)
- [4. Definir un modelo](#4-definir-un-modelo)
- [5. Crear la base de datos](#5-crear-la-base-de-datos)
- [6. Operaciones CRUD con el ORM](#6-operaciones-crud-con-el-orm)
- [7. Una API conectada a la base de datos](#7-una-api-conectada-a-la-base-de-datos)
- [8. Otras bases de datos (MongoDB y compañía)](#8-otras-bases-de-datos-mongodb-y-compañía)
- [9. Ejercicios](#9-ejercicios)

<a name = "1-el-problema-los-datos-se-pierden"></a>

## 1. El problema: los datos se pierden

La API de ayer guardaba las tareas en una **lista en memoria**. Eso tiene un problema enorme: en cuanto reinicias el servidor, **todo desaparece**. Una aplicación de verdad necesita guardar los datos en una **base de datos** que persista (como viste en el día 26 con SQLite).

Hoy conectamos Flask con una base de datos de forma elegante, usando un **ORM**.

<a name = "2-qué-es-un-orm"></a>

## 2. ¿Qué es un ORM?

Un **ORM** (*Object-Relational Mapping*) es una librería que te deja trabajar con la base de datos usando **objetos de Python** (clases, día 15) en lugar de escribir SQL a mano. Cada **clase** es una tabla y cada **objeto** es una fila.

Usaremos **SQLAlchemy**, integrado en Flask con `Flask-SQLAlchemy`:

```bash
pip install flask flask-sqlalchemy
```

Ventajas frente a escribir SQL (día 26) directamente:
- Trabajas con objetos Python en vez de cadenas SQL.
- Es más seguro (evita la inyección SQL).
- Puedes cambiar de base de datos (SQLite, PostgreSQL, MySQL) casi sin tocar el código.

<a name = "3-configurar-flask-sqlalchemy"></a>

## 3. Configurar Flask-SQLAlchemy

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Usamos SQLite: la base de datos será un fichero llamado datos.db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datos.db"
db = SQLAlchemy(app)
```

La línea `sqlite:///datos.db` dice "usa SQLite y guárdalo en el fichero `datos.db`". Para cambiar a PostgreSQL en producción, solo cambiarías esa cadena.

<a name = "4-definir-un-modelo"></a>

## 4. Definir un modelo

Un **modelo** es una clase que representa una tabla. Hereda de `db.Model` y cada atributo es una columna:

```python
class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    hecha = db.Column(db.Boolean, default=False)

    def a_diccionario(self):
        return {"id": self.id, "titulo": self.titulo, "hecha": self.hecha}
```

Fíjate: es una clase normal (día 15) con un método `a_diccionario` para poder devolverla como JSON, igual que hicimos en el proyecto de consola.

<a name = "5-crear-la-base-de-datos"></a>

## 5. Crear la base de datos

Para que se cree el fichero y las tablas, ejecutamos una vez `db.create_all()` dentro del **contexto** de la app:

```python
with app.app_context():
    db.create_all()
```

Esto crea `datos.db` con la tabla `tarea` si no existían.

<a name = "6-operaciones-crud-con-el-orm"></a>

## 6. Operaciones CRUD con el ORM

**CRUD** son las cuatro operaciones básicas: *Create, Read, Update, Delete*. Con el ORM se hacen con objetos:

```python
# CREATE - crear
nueva = Tarea(titulo="Estudiar SQLAlchemy")
db.session.add(nueva)
db.session.commit()

# READ - leer
todas = Tarea.query.all()                 # todas las filas
una = Tarea.query.get(1)                   # por id
pendientes = Tarea.query.filter_by(hecha=False).all()   # con filtro

# UPDATE - actualizar
tarea = Tarea.query.get(1)
tarea.hecha = True
db.session.commit()

# DELETE - borrar
db.session.delete(tarea)
db.session.commit()
```

>[!IMPORTANT]
>Igual que con SQLite (día 26), los cambios no se guardan hasta que haces `db.session.commit()`. Es el equivalente al `commit()` de antes.

<a name = "7-una-api-conectada-a-la-base-de-datos"></a>

## 7. Una API conectada a la base de datos

Ahora juntamos la API REST de ayer (día 36) con la base de datos. Las tareas ya **no se pierden** al reiniciar:

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datos.db"
db = SQLAlchemy(app)

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    hecha = db.Column(db.Boolean, default=False)

    def a_diccionario(self):
        return {"id": self.id, "titulo": self.titulo, "hecha": self.hecha}

@app.route("/api/tareas", methods=["GET"])
def listar():
    return jsonify([t.a_diccionario() for t in Tarea.query.all()])

@app.route("/api/tareas", methods=["POST"])
def crear():
    datos = request.get_json()
    tarea = Tarea(titulo=datos["titulo"])
    db.session.add(tarea)
    db.session.commit()
    return jsonify(tarea.a_diccionario()), 201

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
```

<a name = "8-otras-bases-de-datos-mongodb-y-compañía"></a>

## 8. Otras bases de datos (MongoDB y compañía)

Lo que has usado (SQLite, PostgreSQL, MySQL) son bases de datos **relacionales** (tablas con filas y columnas, lenguaje SQL). Existe otra familia, las **NoSQL**, que guardan los datos de otra forma:

- **MongoDB**: guarda **documentos** parecidos a diccionarios/JSON. En Python se usa con la librería `pymongo`. Es muy popular para datos flexibles que no encajan bien en tablas.

```python
# Idea general de MongoDB con pymongo (no hace falta que lo ejecutes hoy)
from pymongo import MongoClient
cliente = MongoClient("mongodb://localhost:27017")
db = cliente["mi_app"]
db.tareas.insert_one({"titulo": "Aprender Mongo", "hecha": False})
```

>[!NOTE]
>Para empezar, las bases relacionales con SQLAlchemy te cubren casi todo. MongoDB es una herramienta más para cuando tus datos no tengan una estructura fija. Lo importante hoy es que entiendas el concepto de **persistir** los datos de tu web.

<a name = "9-ejercicios"></a>

## 9. Ejercicios

> Crea un `app.py`. Usarás SQLite a través de Flask-SQLAlchemy (se creará un fichero `.db`). Puedes probar la API con `curl`, Postman o `requests`.

### Nivel 1 — Básico
1. Configura Flask-SQLAlchemy con una base de datos SQLite (`sqlite:///datos.db`).
2. Define un modelo `Libro` con `id`, `titulo` (texto) y `autor` (texto).
3. Crea la base de datos con `db.create_all()`.
4. Añade un método `a_diccionario()` al modelo `Libro`.

### Nivel 2 — Aplicado
5. Crea la ruta `GET /api/libros` que devuelva todos los libros de la base de datos.
6. Crea la ruta `POST /api/libros` que cree un libro nuevo a partir del JSON recibido.
7. Crea `GET /api/libros/<int:id>` que devuelva un libro por id (o 404).
8. Comprueba que, al reiniciar el servidor, los libros **siguen ahí** (esa es la gracia).

### Nivel 3 — Reto
9. Añade `DELETE /api/libros/<int:id>` y `PUT /api/libros/<int:id>` con SQLAlchemy.
10. Añade una ruta que devuelva solo los libros de un autor concreto (`filter_by`).
11. Crea un segundo modelo `Autor` y haz que cada libro tenga un autor (relación). Devuelve el nombre del autor en el JSON del libro.

> [!NOTE]
> Pistas:
> - El modelo hereda de `db.Model` y sus columnas son `db.Column(...)`.
> - Crear: `db.session.add(obj)` y luego `db.session.commit()`.
> - Leer: `Modelo.query.all()`, `Modelo.query.get(id)`, `Modelo.query.filter_by(campo=valor).all()`.
> - Para devolver JSON, recorre los objetos con una comprensión: `[obj.a_diccionario() for obj in ...]`.
> - Acuérdate de `with app.app_context(): db.create_all()` para crear las tablas.

<h3 align = "center">
¡Tu API ya guarda los datos de verdad! Solo queda una cosa para que el mundo la use: sacarla de tu ordenador. Mañana, el despliegue.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/36_API_REST/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/38_Despliegue/readme.md">Día siguiente</a>
</h4>
