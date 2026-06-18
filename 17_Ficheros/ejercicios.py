"""
Ejercicios de Manejo de Ficheros

NOTA: al ejecutar este archivo se crearán ficheros (.txt, .json, .csv)
en la misma carpeta. Es normal: es justo lo que estamos practicando.
"""
import json
import csv

# 1. Escribir tres frases en frases.txt y luego mostrarlas.
with open("frases.txt", "w", encoding="utf-8") as fichero:
    fichero.write("El que no arriesga, no gana.\n")
    fichero.write("Hoy es un buen día para programar.\n")
    fichero.write("Pequeños pasos, grandes resultados.\n")

with open("frases.txt", "r", encoding="utf-8") as fichero:
    print(fichero.read())


# 2. Añadir una línea nueva sin borrar lo anterior.
with open("frases.txt", "a", encoding="utf-8") as fichero:
    fichero.write("Una frase más cada vez que ejecuto.\n")


# 3. Función contar_lineas(ruta) con control de errores.
def contar_lineas(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as fichero:
            return len(fichero.readlines())
    except FileNotFoundError:
        return "El fichero no existe."
print(f"frases.txt tiene {contar_lineas('frases.txt')} líneas")
print(contar_lineas("no_existe.txt"))


# 4. Diario: añade una entrada al fichero diario.txt.
def escribir_diario(texto):
    with open("diario.txt", "a", encoding="utf-8") as fichero:
        fichero.write(f"- {texto}\n")
escribir_diario("Hoy he aprendido a manejar ficheros.")


# 5. Guardar y leer un perfil en perfil.json.
perfil = {
    "nombre": "Kiko",
    "edad": 30,
    "lenguajes": ["Java", "Dart", "Python"]
}
with open("perfil.json", "w", encoding="utf-8") as fichero:
    json.dump(perfil, fichero, indent=4, ensure_ascii=False)

with open("perfil.json", "r", encoding="utf-8") as fichero:
    datos = json.load(fichero)
print(f"{datos['nombre']} conoce {datos['lenguajes']}")


# 6. guardar_tareas() y cargar_tareas() con tareas.json.
def guardar_tareas(lista):
    with open("tareas.json", "w", encoding="utf-8") as fichero:
        json.dump(lista, fichero, indent=4, ensure_ascii=False)

def cargar_tareas():
    try:
        with open("tareas.json", "r", encoding="utf-8") as fichero:
            return json.load(fichero)
    except FileNotFoundError:
        return []

guardar_tareas(["Estudiar POO", "Practicar ficheros", "Repasar errores"])
print(f"Tareas guardadas: {cargar_tareas()}")


# 7. notas.csv con alumno y nota, y cálculo de la media.
with open("notas.csv", "w", newline="", encoding="utf-8") as fichero:
    escritor = csv.writer(fichero)
    escritor.writerow(["alumno", "nota"])
    escritor.writerow(["Ana", 8])
    escritor.writerow(["Luis", 6])
    escritor.writerow(["Marta", 10])

notas = []
with open("notas.csv", "r", encoding="utf-8") as fichero:
    lector = csv.DictReader(fichero)
    for fila in lector:
        notas.append(float(fila["nota"]))
print(f"Nota media de la clase: {sum(notas) / len(notas)}")


# 8. Agenda de contactos en JSON: añadir y listar.
def cargar_contactos():
    try:
        with open("agenda.json", "r", encoding="utf-8") as fichero:
            return json.load(fichero)
    except FileNotFoundError:
        return {}

def añadir_contacto(nombre, telefono):
    contactos = cargar_contactos()
    contactos[nombre] = telefono
    with open("agenda.json", "w", encoding="utf-8") as fichero:
        json.dump(contactos, fichero, indent=4, ensure_ascii=False)

def listar_contactos():
    contactos = cargar_contactos()
    for nombre, telefono in contactos.items():
        print(f"{nombre}: {telefono}")

añadir_contacto("Ana", "600111222")
añadir_contacto("Luis", "600333444")
print("--- Agenda ---")
listar_contactos()
