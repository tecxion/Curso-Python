"""
app.py — Aplicación de ejemplo LISTA PARA DESPLEGAR.

Diferencias clave con una app de desarrollo:
  - Lee el puerto de la variable de entorno PORT (la pone el servidor).
  - Escucha en host 0.0.0.0 (acepta conexiones desde fuera).
  - Sin debug=True.

Arranque local de desarrollo:   python app.py
Arranque de producción:         gunicorn app:app
"""
import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def inicio():
    return jsonify({"mensaje": "¡Mi API está en internet!", "ok": True})


@app.route("/api/saludo/<nombre>")
def saludo(nombre):
    return jsonify({"saludo": f"Hola, {nombre}"})


if __name__ == "__main__":
    # Render (y otras plataformas) indican el puerto con la variable PORT.
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=puerto)
