"""
Ejercicios de Bases de Datos con SQLite

NOTA: al ejecutar este archivo se crea una base de datos 'agenda.db'
en la misma carpeta. Es el comportamiento esperado.
"""
import sqlite3

# 1. Crear la base de datos y la tabla contactos.
conexion = sqlite3.connect("agenda.db")
cursor = conexion.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS contactos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT
    )
""")
# Vaciamos la tabla para que el script se pueda ejecutar varias veces limpio.
cursor.execute("DELETE FROM contactos")
conexion.commit()


# 2. Insertar tres contactos.
cursor.execute("INSERT INTO contactos (nombre, telefono) VALUES ('Ana', '600111222')")
cursor.execute("INSERT INTO contactos (nombre, telefono) VALUES ('Alberto', '600333444')")
cursor.execute("INSERT INTO contactos (nombre, telefono) VALUES ('Luis', '600555666')")
conexion.commit()


# 3. Consultar y mostrar todos los contactos.
print("--- Todos los contactos ---")
cursor.execute("SELECT * FROM contactos")
for fila in cursor.fetchall():
    print(fila)


# 4. Consultar los que empiezan por "A".
print("--- Contactos que empiezan por A ---")
cursor.execute("SELECT nombre, telefono FROM contactos WHERE nombre LIKE 'A%'")
for nombre, telefono in cursor.fetchall():
    print(f"{nombre}: {telefono}")


# 5. Actualizar el teléfono de un contacto.
cursor.execute("UPDATE contactos SET telefono = '699999999' WHERE nombre = 'Luis'")
conexion.commit()


# 6. Borrar un contacto por su nombre.
cursor.execute("DELETE FROM contactos WHERE nombre = 'Alberto'")
conexion.commit()


# 7. Función añadir_contacto (segura, con parámetros ?).
def añadir_contacto(nombre, telefono):
    cursor.execute(
        "INSERT INTO contactos (nombre, telefono) VALUES (?, ?)",
        (nombre, telefono)
    )
    conexion.commit()
    print(f"Contacto '{nombre}' añadido.")

añadir_contacto("Marta", "611222333")


# 8. Función buscar_contacto.
def buscar_contacto(nombre):
    cursor.execute("SELECT telefono FROM contactos WHERE nombre = ?", (nombre,))
    resultado = cursor.fetchone()
    if resultado is None:
        return f"No existe el contacto '{nombre}'"
    return f"Teléfono de {nombre}: {resultado[0]}"

print(buscar_contacto("Ana"))       # existe
print(buscar_contacto("Pedro"))     # no existe


print("--- Estado final de la agenda ---")
cursor.execute("SELECT nombre, telefono FROM contactos ORDER BY nombre")
for nombre, telefono in cursor.fetchall():
    print(f"{nombre}: {telefono}")

conexion.close()
