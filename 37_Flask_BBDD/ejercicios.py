"""
Ejercicios de Flask + Base de Datos (3 niveles)

Requisito:  pip install flask flask-sqlalchemy
Ejecuta con:  python ejercicios.py
Crea un fichero datos.db con la base de datos SQLite.
"""
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# NIVEL 1 (1): configuración de la base de datos SQLite.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datos.db"
db = SQLAlchemy(app)


# NIVEL 1 (2 y 4): modelo Libro con método a_diccionario().
class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100))

    def a_diccionario(self):
        return {"id": self.id, "titulo": self.titulo, "autor": self.autor}


# ===== NIVEL 2 - APLICADO =====
@app.route("/api/libros", methods=["GET"])
def listar():
    # NIVEL 3 (10): filtrar por autor con ?autor=...
    autor = request.args.get("autor")
    if autor:
        libros = Libro.query.filter_by(autor=autor).all()
    else:
        libros = Libro.query.all()
    return jsonify([libro.a_diccionario() for libro in libros])

@app.route("/api/libros", methods=["POST"])
def crear():
    datos = request.get_json()
    if not datos or "titulo" not in datos:
        return jsonify({"error": "Falta el título"}), 400
    libro = Libro(titulo=datos["titulo"], autor=datos.get("autor", "Desconocido"))
    db.session.add(libro)
    db.session.commit()
    return jsonify(libro.a_diccionario()), 201

@app.route("/api/libros/<int:id>", methods=["GET"])
def obtener(id):
    libro = Libro.query.get(id)
    if libro is None:
        return jsonify({"error": "No encontrado"}), 404
    return jsonify(libro.a_diccionario())


# ===== NIVEL 3 - RETO =====
@app.route("/api/libros/<int:id>", methods=["PUT"])
def actualizar(id):
    libro = Libro.query.get(id)
    if libro is None:
        return jsonify({"error": "No encontrado"}), 404
    datos = request.get_json()
    libro.titulo = datos.get("titulo", libro.titulo)
    libro.autor = datos.get("autor", libro.autor)
    db.session.commit()
    return jsonify(libro.a_diccionario())

@app.route("/api/libros/<int:id>", methods=["DELETE"])
def borrar(id):
    libro = Libro.query.get(id)
    if libro is None:
        return jsonify({"error": "No encontrado"}), 404
    db.session.delete(libro)
    db.session.commit()
    return jsonify({"mensaje": "Libro borrado"})


# NIVEL 1 (3): crear las tablas.
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
