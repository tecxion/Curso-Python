"""
Ejercicios de API REST con Flask (3 niveles)

Requisito:  pip install flask
Ejecuta con:  python ejercicios.py
Pruébala con curl, Postman o un script con requests.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

libros = [
    {"id": 1, "titulo": "El Quijote"},
    {"id": 2, "titulo": "La Odisea"},
]


# ===== NIVEL 1 - BÁSICO =====
@app.route("/api/ping")
def ping():
    return jsonify({"mensaje": "pong"})

@app.route("/api/libros", methods=["GET"])
def listar_libros():
    # NIVEL 3 (10): ordenar opcionalmente por título con ?orden=titulo
    if request.args.get("orden") == "titulo":
        return jsonify(sorted(libros, key=lambda libro: libro["titulo"]))
    return jsonify(libros)

@app.route("/api/libros/<int:id>", methods=["GET"])
def obtener_libro(id):
    for libro in libros:
        if libro["id"] == id:
            return jsonify(libro)
    return jsonify({"error": "Libro no encontrado"}), 404


# ===== NIVEL 2 - APLICADO =====
@app.route("/api/libros", methods=["POST"])
def crear_libro():
    datos = request.get_json()
    if not datos or "titulo" not in datos:
        return jsonify({"error": "Falta el título"}), 400      # validación (6)
    nuevo = {"id": (max([l["id"] for l in libros]) + 1) if libros else 1,
             "titulo": datos["titulo"]}
    libros.append(nuevo)
    return jsonify(nuevo), 201

@app.route("/api/libros/<int:id>", methods=["DELETE"])
def borrar_libro(id):
    global libros
    libros = [libro for libro in libros if libro["id"] != id]
    return jsonify({"mensaje": "Libro borrado"})

@app.route("/api/libros/<int:id>", methods=["PUT"])
def actualizar_libro(id):
    datos = request.get_json()
    for libro in libros:
        if libro["id"] == id:
            libro["titulo"] = datos.get("titulo", libro["titulo"])
            return jsonify(libro)
    return jsonify({"error": "Libro no encontrado"}), 404


# ===== NIVEL 3 - RETO =====
@app.route("/api/libros/buscar")
def buscar_libros():
    texto = request.args.get("titulo", "").lower()
    resultado = [libro for libro in libros if texto in libro["titulo"].lower()]
    return jsonify(resultado)


if __name__ == "__main__":
    app.run(debug=True)
