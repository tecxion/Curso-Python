"""
Ejercicios de Flask (3 niveles)

Requisito:  pip install flask
Ejecuta con:  python ejercicios.py   y abre http://127.0.0.1:5000

NOTA: en el día de hoy las plantillas se enseñan con la carpeta templates/.
Aquí, para que todo quepa en UN archivo y sea fácil de probar, usamos
render_template_string (el HTML va en un texto). En tu proyecto real usa
render_template con ficheros .html dentro de templates/.
"""
from flask import Flask, render_template_string

app = Flask(__name__)


# ===== NIVEL 1 - BÁSICO =====
@app.route("/")
def inicio():
    return "<h1>Mi primera web</h1>"

@app.route("/sobre-mi")
def sobre_mi():
    return "<h1>Sobre mí</h1><p>Soy estudiante de Python y esto es mi web.</p>"

@app.route("/contacto")
def contacto():
    return "<p>Escríbeme a correo@ejemplo.com</p>"


# ===== NIVEL 2 - APLICADO =====
@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"<h1>¡Hola, {nombre}!</h1>"

@app.route("/suma/<int:a>/<int:b>")
def suma(a, b):
    return f"<p>{a} + {b} = {a + b}</p>"


PLANTILLA_INICIO = """
<!DOCTYPE html>
<html>
<head><title>Inicio</title></head>
<body>
    <h1>Hola, {{ nombre }}</h1>
    <!-- NIVEL 3: lista de tareas con bucle y condición -->
    {% if tareas %}
        <ul>
        {% for tarea in tareas %}
            <li>{{ tarea }}</li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No hay tareas</p>
    {% endif %}
    <p><a href="/productos">Ver productos</a> | <a href="/sobre-mi">Sobre mí</a></p>
</body>
</html>
"""

@app.route("/bienvenida")
def bienvenida():
    return render_template_string(PLANTILLA_INICIO, nombre="Ana",
                                  tareas=["Estudiar", "Entrenar", "Programar"])


# ===== NIVEL 3 - RETO =====
@app.route("/productos")
def productos():
    lista = ["Camiseta", "Pantalón", "Zapatos"]
    plantilla = """
    <h1>Productos</h1>
    <ul>{% for p in productos %}<li>{{ p }}</li>{% endfor %}</ul>
    <a href="/bienvenida">Volver</a>
    """
    return render_template_string(plantilla, productos=lista)


if __name__ == "__main__":
    app.run(debug=True)
