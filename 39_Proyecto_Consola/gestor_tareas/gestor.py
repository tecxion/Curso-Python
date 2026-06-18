"""
gestor.py
Define la clase GestorTareas, el "cerebro" de la aplicación.
Conecta las Tareas (tarea.py) con el almacenamiento (almacenamiento.py).
"""
from tarea import Tarea
from almacenamiento import guardar_tareas, cargar_tareas


class GestorTareas:
    def __init__(self):
        # Al arrancar, cargamos las tareas guardadas y las convertimos en objetos Tarea.
        self.tareas = [Tarea.desde_diccionario(d) for d in cargar_tareas()]

    def agregar(self, titulo, prioridad):
        self.tareas.append(Tarea(titulo, prioridad))
        self.guardar()

    def completar(self, indice):
        # indice es el número que ve el usuario (empezando en 1)
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].marcar_completada()
            self.guardar()
            return True
        return False

    def eliminar(self, indice):
        if 0 <= indice < len(self.tareas):
            eliminada = self.tareas.pop(indice)
            self.guardar()
            return eliminada
        return None

    def pendientes(self):
        # Comprensión de listas (día 18)
        return [tarea for tarea in self.tareas if not tarea.completada]

    def completadas(self):
        return [tarea for tarea in self.tareas if tarea.completada]

    def guardar(self):
        # Convertimos cada Tarea de nuevo a diccionario antes de guardar.
        guardar_tareas([tarea.a_diccionario() for tarea in self.tareas])
