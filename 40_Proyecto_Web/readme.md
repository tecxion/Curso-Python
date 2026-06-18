<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/39_Proyecto_Consola/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/proyecto_web.png">
</h1>


<h1 align="center">Proyecto 2: Gestor de Tareas Web (full-stack)</h1><br>

<h3>Índice</h3>

- [1. El gran final](#1-el-gran-final)
- [2. Qué vamos a construir](#2-qué-vamos-a-construir)
- [3. Estructura del proyecto](#3-estructura-del-proyecto)
- [4. La base de datos: models.py](#4-la-base-de-datos-modelspy)
- [5. La aplicación: app.py](#5-la-aplicación-apppy)
- [6. Las plantillas HTML](#6-las-plantillas-html)
- [7. Los estilos (CSS)](#7-los-estilos-css)
- [8. Ejecutar el proyecto en local](#8-ejecutar-el-proyecto-en-local)
- [9. Desplegar en internet](#9-desplegar-en-internet)
- [10. ¡Fin del curso!](#10-fin-del-curso)

<a name = "1-el-gran-final"></a>

## 1. El gran final

Has llegado al **último día**. En el día 39 construiste un gestor de tareas de **consola**; hoy vas a construir el **mismo gestor pero como aplicación web full-stack** y lo dejarás **funcionando en internet** con una URL que podrás compartir.

Este proyecto reúne casi todo el bloque avanzado:
- **Flask** y rutas (día 35).
- **Plantillas** con Jinja2 (día 35).
- **API REST** en JSON (día 36).
- **Base de datos** con SQLAlchemy (día 37).
- **Despliegue** en la nube (día 38).
- Y, por debajo, todo lo de los días 1-29: clases, funciones, comprensiones, manejo de errores…

>[!IMPORTANT]
>Tienes el proyecto **completo y funcionando** en la carpeta [`gestor_web`](./gestor_web). Te recomiendo escribirlo tú desde cero siguiendo esta guía, y usar esa carpeta solo para comparar si te atascas.

<a name = "2-qué-vamos-a-construir"></a>

## 2. Qué vamos a construir

Una página web donde el usuario puede:
- **Ver** su lista de tareas.
- **Añadir** una tarea con un formulario.
- **Marcar** una tarea como completada (y desmarcarla).
- **Eliminar** una tarea.

Además, una **API** en `/api/tareas` que devuelve las tareas en JSON, para que otros programas (¡o tu app de móvil del futuro!) puedan consumirlas.

<a name = "3-estructura-del-proyecto"></a>

## 3. Estructura del proyecto

Aplicamos la organización en varios ficheros del día 19:

```
gestor_web/
├── app.py              # la aplicación y sus rutas
├── models.py           # la base de datos y el modelo Tarea
├── templates/          # el HTML (Jinja2)
│   ├── base.html       # plantilla base (cabecera, pie)
│   └── index.html      # la página principal
├── static/
│   └── estilo.css      # los estilos
├── requirements.txt    # dependencias
└── .gitignore
```

<a name = "4-la-base-de-datos-modelspy"></a>

## 4. La base de datos: models.py

Separamos el modelo en su propio fichero. Definimos el objeto `db` y la tabla `Tarea` (día 37):

```python
# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    hecha = db.Column(db.Boolean, default=False)

    def a_diccionario(self):
        return {"id": self.id, "titulo": self.titulo, "hecha": self.hecha}
```

<a name = "5-la-aplicación-apppy"></a>

## 5. La aplicación: app.py

El corazón del proyecto. Configura la base de datos, conecta el modelo y define las rutas. Fíjate en que cada acción (añadir, completar, eliminar) **modifica la base de datos y redirige** de vuelta a la página principal:

```python
# app.py
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, Tarea

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tareas.db"
db.init_app(app)

@app.route("/")
def index():
    tareas = Tarea.query.all()
    pendientes = [t for t in tareas if not t.hecha]
    return render_template("index.html", tareas=tareas, pendientes=len(pendientes))

@app.route("/agregar", methods=["POST"])
def agregar():
    titulo = request.form.get("titulo", "").strip()
    if titulo:
        db.session.add(Tarea(titulo=titulo))
        db.session.commit()
    return redirect(url_for("index"))

@app.route("/completar/<int:id>")
def completar(id):
    tarea = Tarea.query.get(id)
    if tarea:
        tarea.hecha = not tarea.hecha
        db.session.commit()
    return redirect(url_for("index"))

@app.route("/eliminar/<int:id>")
def eliminar(id):
    tarea = Tarea.query.get(id)
    if tarea:
        db.session.delete(tarea)
        db.session.commit()
    return redirect(url_for("index"))

@app.route("/api/tareas")
def api_tareas():
    return jsonify([t.a_diccionario() for t in Tarea.query.all()])

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=puerto, debug=True)
```

- `request.form.get("titulo")` lee el dato del **formulario** (no JSON, porque viene de una web).
- `redirect(url_for("index"))` reenvía al usuario a la página principal tras cada acción.
- La ruta `/api/tareas` ofrece los mismos datos en **JSON**.

<a name = "6-las-plantillas-html"></a>

## 6. Las plantillas HTML

Usamos **herencia de plantillas**: `base.html` define la estructura común y `index.html` rellena el contenido. Es el mismo concepto de herencia del día 16, aplicado al HTML.

`base.html` (lo esencial):
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{% block titulo %}Gestor de Tareas{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='estilo.css') }}">
</head>
<body>
    <div class="contenedor">
        <header><h1>📝 Gestor de Tareas</h1></header>
        {% block contenido %}{% endblock %}
    </div>
</body>
</html>
```

`index.html` (el formulario y la lista, con bucle y condición de Jinja2):
```html
{% extends "base.html" %}
{% block contenido %}
<form action="{{ url_for('agregar') }}" method="POST">
    <input type="text" name="titulo" placeholder="¿Qué tienes que hacer?" required>
    <button type="submit">Añadir</button>
</form>

{% if tareas %}
<ul>
    {% for tarea in tareas %}
    <li class="{{ 'hecha' if tarea.hecha else '' }}">
        <a href="{{ url_for('completar', id=tarea.id) }}">{{ '✅' if tarea.hecha else '⬜' }}</a>
        {{ tarea.titulo }}
        <a href="{{ url_for('eliminar', id=tarea.id) }}">🗑️</a>
    </li>
    {% endfor %}
</ul>
{% else %}
<p>No hay tareas todavía. ¡Añade la primera!</p>
{% endif %}
{% endblock %}
```

<a name = "7-los-estilos-css"></a>

## 7. Los estilos (CSS)

El fichero `static/estilo.css` da el aspecto visual. No necesitas dominar CSS para este curso (es otro mundo), pero ten claro lo esencial: los ficheros estáticos (CSS, imágenes) van en la carpeta `static/` y se enlazan con `url_for('static', filename='...')`. Tienes el CSS completo en la carpeta del proyecto para que lo uses tal cual.

<a name = "8-ejecutar-el-proyecto-en-local"></a>

## 8. Ejecutar el proyecto en local

```bash
cd gestor_web
python3 -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Abre `http://127.0.0.1:5000`: ya puedes añadir, completar y borrar tareas. Y si visitas `http://127.0.0.1:5000/api/tareas` verás los datos en JSON.

<a name = "9-desplegar-en-internet"></a>

## 9. Desplegar en internet

Aplica lo del día 38 para que el mundo lo use:

1. Sube `gestor_web/` a un repositorio de GitHub.
2. En [Render](https://render.com): **New + → Web Service**, conecta el repo.
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `gunicorn app:app`
5. Plan **Free** → Create.

En un par de minutos tendrás una URL pública tipo `https://gestor-tareas.onrender.com`. **¡Compártela!** Esa web la hiciste tú, de cero, con Python.

>[!NOTE]
>Idea para subir de nivel: une los dos proyectos. Haz que tu app de **consola** (día 39) lea las tareas de tu **API web** (día 40) con `requests` (día 27). Tendrías una misma información accesible desde el terminal y desde el navegador.

<a name = "10-fin-del-curso"></a>

## 10. ¡Fin del curso!

Lo has conseguido: **40 días, de cero a avanzado**. Repasa el camino:

- **Días 1-13**: los fundamentos (variables, estructuras de datos, condicionales, bucles, funciones, módulos).
- **Días 14-19**: Python intermedio (errores, POO, ficheros, comprensiones, entornos).
- **Días 20-29**: Python avanzado (fechas, regex, type hints, decoradores, itertools, context managers, SQLite, APIs, logging, tests).
- **Días 30-34**: ciencia de datos (NumPy, Pandas, análisis, visualización, scraping).
- **Días 35-38**: desarrollo web (Flask, API REST, base de datos, despliegue).
- **Días 39-40**: dos proyectos finales completos, uno de consola y uno web desplegado.

Ya no eres principiante. Sabes pensar un problema, estructurar un proyecto en varios ficheros, manejar datos, construir y publicar una aplicación. El siguiente paso es el mejor: **construir tus propias ideas**. Coge un proyecto que te ilusione y láncate; ahí es donde de verdad se aprende.

Gracias por recorrer estos 40 días. ¡Nos vemos en el código! 🚀🐍

<h3 align = "center">
"No tienes que ser un experto para empezar, pero tienes que empezar para llegar a ser un experto."
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/39_Proyecto_Consola/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">🏠 Volver al Inicio</a>
</h4>
