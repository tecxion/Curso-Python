"""
models.py
Define la base de datos y el modelo Tarea (ORM, día 37).
Separamos los modelos del resto de la app para mantener el orden (día 19).
"""
from flask_sqlalchemy import SQLAlchemy

# Creamos el objeto de base de datos aquí; en app.py lo conectaremos con la app.
db = SQLAlchemy()


class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    hecha = db.Column(db.Boolean, default=False)

    def a_diccionario(self):
        """Para devolver la tarea como JSON desde la API."""
        return {"id": self.id, "titulo": self.titulo, "hecha": self.hecha}
