<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/35_Flask/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/37_Flask_BBDD/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/api_rest.png">
</h1>


<h1 align="center">Construir una API REST con Flask</h1><br>

<h3>Índice</h3>

- [1. De web a API](#1-de-web-a-api)
- [2. Devolver JSON con jsonify](#2-devolver-json-con-jsonify)
- [3. Los métodos HTTP](#3-los-métodos-http)
- [4. GET: leer datos](#4-get-leer-datos)
- [5. POST: crear datos](#5-post-crear-datos)
- [6. PUT y DELETE: actualizar y borrar](#6-put-y-delete-actualizar-y-borrar)
- [7. Códigos de estado correctos](#7-códigos-de-estado-correctos)
- [8. Probar la API](#8-probar-la-api)
- [9. Ejercicios](#9-ejercicios)

<a name = "1-de-web-a-api"></a>

## 1. De web a API

Ayer (día 35) tu web devolvía **HTML** para que lo viera una persona. Una **API REST** hace algo distinto: devuelve **datos en JSON** para que los consuma **otro programa** (una app móvil, una web hecha con JavaScript, otro servidor…).

Es justo la otra cara del día 27: entonces *consumías* APIs de otros; hoy vas a *crear la tuya*. Una API REST organiza el acceso a unos datos (llamados **recursos**) mediante URLs y los métodos HTTP.

<a name = "2-devolver-json-con-jsonify"></a>

## 2. Devolver JSON con jsonify

Flask convierte diccionarios y listas de Python a JSON con **`jsonify`** (o devolviendo un `dict` directamente):

```python
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/api/saludo")
def saludo():
    return jsonify({"mensaje": "Hola desde la API", "ok": True})

# Desde Flask moderno, devolver un dict también funciona:
@app.route("/api/version")
def version():
    return {"version": "1.0"}
```

Si visitas `/api/saludo` verás JSON puro: `{"mensaje": "Hola desde la API", "ok": true}`.

<a name = "3-los-métodos-http"></a>

## 3. Los métodos HTTP

Una API REST usa los **métodos HTTP** para indicar qué quieres hacer con un recurso. Es una convención universal:

| Método | Significado | Ejemplo |
| ------ | --------------------- | -------------------------- |
| `GET` | **Leer** datos | Ver la lista de tareas |
| `POST` | **Crear** un dato | Añadir una tarea nueva |
| `PUT` | **Actualizar** un dato | Editar una tarea |
| `DELETE` | **Borrar** un dato | Eliminar una tarea |

En Flask, indicamos qué métodos acepta cada ruta con `methods=[...]`.

<a name = "4-get-leer-datos"></a>

## 4. GET: leer datos

Empecemos con una lista de tareas en memoria y dos rutas para leerlas: todas, o una por su `id`.

```python
from flask import Flask, jsonify
app = Flask(__name__)

tareas = [
    {"id": 1, "titulo": "Estudiar Python", "hecha": False},
    {"id": 2, "titulo": "Hacer ejercicio", "hecha": True},
]

@app.route("/api/tareas", methods=["GET"])
def listar_tareas():
    return jsonify(tareas)

@app.route("/api/tareas/<int:id>", methods=["GET"])
def obtener_tarea(id):
    for tarea in tareas:
        if tarea["id"] == id:
            return jsonify(tarea)
    return jsonify({"error": "No encontrada"}), 404
```

<a name = "5-post-crear-datos"></a>

## 5. POST: crear datos

Para **crear**, el cliente nos envía datos en el cuerpo de la petición en formato JSON. Los leemos con `request.get_json()`:

```python
from flask import Flask, jsonify, request
app = Flask(__name__)
tareas = []

@app.route("/api/tareas", methods=["POST"])
def crear_tarea():
    datos = request.get_json()          # lee el JSON que envía el cliente
    nueva = {
        "id": len(tareas) + 1,
        "titulo": datos["titulo"],
        "hecha": False
    }
    tareas.append(nueva)
    return jsonify(nueva), 201          # 201 = "creado"
```

<a name = "6-put-y-delete-actualizar-y-borrar"></a>

## 6. PUT y DELETE: actualizar y borrar

```python
@app.route("/api/tareas/<int:id>", methods=["PUT"])
def actualizar_tarea(id):
    datos = request.get_json()
    for tarea in tareas:
        if tarea["id"] == id:
            tarea["hecha"] = datos.get("hecha", tarea["hecha"])
            return jsonify(tarea)
    return jsonify({"error": "No encontrada"}), 404

@app.route("/api/tareas/<int:id>", methods=["DELETE"])
def borrar_tarea(id):
    global tareas
    tareas = [t for t in tareas if t["id"] != id]
    return jsonify({"mensaje": "Borrada"})
```

<a name = "7-códigos-de-estado-correctos"></a>

## 7. Códigos de estado correctos

¿Recuerdas los códigos de estado del día 27? Ahora eres tú quien los devuelve. Una buena API los usa bien:

- **200** OK (lectura/actualización correcta).
- **201** Created (algo se creó con éxito).
- **400** Bad Request (el cliente envió datos mal).
- **404** Not Found (el recurso no existe).

```python
return jsonify(nueva), 201        # devolver dato + código
return jsonify({"error": "Falta el título"}), 400
```

<a name = "8-probar-la-api"></a>

## 8. Probar la API

Una API no se prueba en el navegador (que solo hace GET fácilmente). Tienes varias opciones:

- Con la propia librería `requests` (día 27) desde otro script de Python.
- Con herramientas como **Postman** o **Thunder Client** (extensión de VS Code).
- Desde la terminal con `curl`:

```bash
# GET
curl http://127.0.0.1:5000/api/tareas

# POST enviando JSON
curl -X POST http://127.0.0.1:5000/api/tareas \
     -H "Content-Type: application/json" \
     -d '{"titulo": "Nueva tarea"}'
```

>[!NOTE]
>Flask trae un "cliente de pruebas" (`app.test_client()`) que permite probar la API sin arrancar el servidor. Es lo que usarás cuando combines esto con los tests del día 29.

<a name = "9-ejercicios"></a>

## 9. Ejercicios

> Construye una API en `app.py`. Usa una lista en memoria como "base de datos" provisional (mañana la haremos de verdad). Pruébala con `curl`, Postman o un script con `requests`.

### Nivel 1 — Básico
1. Crea una ruta `GET /api/ping` que devuelva `{"mensaje": "pong"}` en JSON.
2. Crea una lista de libros (diccionarios con `id` y `titulo`) y una ruta `GET /api/libros` que la devuelva.
3. Crea `GET /api/libros/<int:id>` que devuelva un libro por su id, o un error 404 si no existe.
4. Comprueba con el navegador o `curl` que `/api/libros` devuelve JSON.

### Nivel 2 — Aplicado
5. Crea `POST /api/libros` que reciba un JSON con `titulo` y añada un libro nuevo (genera el `id`). Devuelve 201.
6. Valida en el POST que venga el campo `titulo`; si falta, devuelve un error 400.
7. Crea `DELETE /api/libros/<int:id>` que elimine un libro.
8. Crea `PUT /api/libros/<int:id>` que cambie el título de un libro.

### Nivel 3 — Reto
9. Añade una ruta `GET /api/libros/buscar?titulo=...` que filtre los libros cuyo título contenga ese texto (pista: `request.args.get("titulo")`).
10. Haz que `GET /api/libros` acepte un parámetro opcional para ordenar los libros por título.
11. Escribe un pequeño script aparte con `requests` (día 27) que haga un POST para crear un libro y luego un GET para comprobar que se guardó.

> [!NOTE]
> Pistas:
> - `from flask import Flask, jsonify, request`.
> - Indica los métodos: `@app.route("/api/...", methods=["POST"])`.
> - Lee el cuerpo JSON con `request.get_json()` y los parámetros `?x=...` con `request.args.get("x")`.
> - Devuelve código de estado: `return jsonify(dato), 201`.
> - Para borrar, recuerda las comprensiones de listas (día 18): `[t for t in libros if t["id"] != id]`.

<h3 align = "center">
¡Ya tienes una API funcionando! Pero los datos en una lista se pierden al reiniciar. Mañana le damos una base de datos de verdad.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/35_Flask/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/37_Flask_BBDD/readme.md">Día siguiente</a>
</h4>
