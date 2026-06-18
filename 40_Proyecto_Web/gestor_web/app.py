"""
app.py
Gestor de Tareas Web — el segundo proyecto final del curso.

Es la versión WEB del gestor de tareas del día 39: en vez de un menú de
consola, una página web donde añadir, completar y borrar tareas, con los
datos guardados en una base de datos (Flask + SQLAlchemy, días 35-37) y
lista para desplegar en internet (día 38).

Arranque local:        python app.py   ->   http://127.0.0.1:5000
Arranque producción:    gunicorn app:app
"""
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, Tarea

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tareas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


# ---------- Vistas web (devuelven HTML) ----------

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
        tarea.hecha = not tarea.hecha     # alterna hecha/pendiente
        db.session.commit()
    return redirect(url_for("index"))


@app.route("/eliminar/<int:id>")
def eliminar(id):
    tarea = Tarea.query.get(id)
    if tarea:
        db.session.delete(tarea)
        db.session.commit()
    return redirect(url_for("index"))


# ---------- API JSON (para que otros programas usen los datos, día 36) ----------

@app.route("/api/tareas")
def api_tareas():
    return jsonify([t.a_diccionario() for t in Tarea.query.all()])


# Creamos las tablas al arrancar si no existen.
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=puerto, debug=True)
