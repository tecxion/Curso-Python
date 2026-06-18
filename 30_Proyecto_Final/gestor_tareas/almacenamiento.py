"""
almacenamiento.py
Responsable de leer y escribir las tareas en disco (día 17: ficheros + JSON).
Aísla todo lo relacionado con el fichero para que el resto del programa no se
preocupe de cómo se guardan los datos.
"""
import os
import json

# Guardamos el JSON junto a este fichero, así funciona ejecutes desde donde ejecutes.
RUTA = os.path.join(os.path.dirname(__file__), "tareas.json")


def guardar_tareas(lista_de_diccionarios):
    """Guarda la lista de tareas (ya convertidas a diccionario) en el fichero JSON."""
    with open(RUTA, "w", encoding="utf-8") as fichero:
        json.dump(lista_de_diccionarios, fichero, indent=4, ensure_ascii=False)


def cargar_tareas():
    """
    Carga las tareas guardadas. Si el fichero no existe todavía
    (primera ejecución) o está corrupto, devuelve una lista vacía.
    """
    try:
        with open(RUTA, "r", encoding="utf-8") as fichero:
            return json.load(fichero)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Aviso: el fichero de tareas estaba dañado. Se empieza de cero.")
        return []
