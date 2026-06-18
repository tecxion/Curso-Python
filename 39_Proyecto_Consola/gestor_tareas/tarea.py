"""
tarea.py
Define la clase Tarea (POO, días 15 y 16).
Cada Tarea sabe convertirse a/desde diccionario para poder guardarse en JSON.
"""
from datetime import datetime

PRIORIDADES_VALIDAS = ("alta", "media", "baja")


class Tarea:
    def __init__(self, titulo, prioridad="media", completada=False, fecha=None):
        self.titulo = titulo
        self.prioridad = prioridad if prioridad in PRIORIDADES_VALIDAS else "media"
        self.completada = completada
        # Si no nos pasan fecha, usamos la actual (datetime, día 20)
        self.fecha = fecha or datetime.now().strftime("%d/%m/%Y %H:%M")

    def marcar_completada(self):
        self.completada = True

    def a_diccionario(self):
        """Convierte la tarea en un diccionario para guardarla en JSON."""
        return {
            "titulo": self.titulo,
            "prioridad": self.prioridad,
            "completada": self.completada,
            "fecha": self.fecha,
        }

    @classmethod
    def desde_diccionario(cls, datos):
        """Crea una Tarea a partir de un diccionario leído del JSON."""
        return cls(
            titulo=datos["titulo"],
            prioridad=datos.get("prioridad", "media"),
            completada=datos.get("completada", False),
            fecha=datos.get("fecha"),
        )

    def __str__(self):
        estado = "X" if self.completada else " "
        return f"[{estado}] ({self.prioridad.upper():^5}) {self.titulo}  ·  {self.fecha}"
