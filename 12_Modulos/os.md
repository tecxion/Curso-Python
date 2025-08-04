# Módulo OS

## 📂 Comandos más usados


### Manejo de Archivos y directorios.

| Comando       | Descripción                     | Ejemplo                             |
| ------------- | ------------------------------- | ----------------------------------- |
| os.mkdir()    | Crea un directorio              | os.mkdir("nueva_carpeta")           |
| os.makedirs() | Crea directorios recursivamente | os.makedirs("ruta/con/subcarpetas") |
| os.remove()   | Elimina un archivo              | os.remove("archivo.txt")            |
| os.rmdir()    | Elimina un directorio vacío     | os.rmdir("carpeta_vacia")           |
| os.rename()   | Renombra/mueve archivos         | os.rename("viejo.txt", "nuevo.txt") |
| os.listdir()  | Lista archivos en un directorio | os.listdir(".") (directorio actual) |

### Información del sistema

| Comando          | Descripción                                       | Ejemplo                                |
| ---------------- | ------------------------------------------------- | -------------------------------------- |
| os.name          | Nombre del SO ('posix'=Linux/macOS, 'nt'=Windows) | print(os.name)                         |
| os.getcwd()      | Ruta del directorio actual                        | print(os.getcwd())                     |
| os.path.exists() | Verifica si existe una ruta                       | os.path.exists("archivo.txt")          |
| os.path.join()   | Une rutas de forma multiplataforma                | os.path.join("carpeta", "archivo.txt") |


### Variables de Entorno y Procesos

| Comando        | Descripción                                                   | Ejemplo                                                    |
| -------------- | ------------------------------------------------------------- | ---------------------------------------------------------- |
| os.environ     | Diccionario con variables de entorno                          | os.environ.get("HOME")                                     |
| os.system()    | Ejecuta comandos del sistema                                  | os.system("ls") (Linux/macOS) o os.system("dir") (Windows) |
| os.startfile() | Abre un archivo con su programa predeterminado (solo Windows) | os.startfile("documento.pdf")                              |

### 🔍 Funciones Avanzadas Útiles
| Comando           | Descripción                         |
| ----------------- | ----------------------------------- |
| os.walk()         | Recorre directorios recursivamente  |
| os.path.abspath() | Obtiene la ruta absoluta            |
| os.path.split()   | Separa ruta en directorio y archivo |
| os.stat()         | Obtiene metadatos de archivos       |


## ⚠️ Diferencias Clave entre sistemas.

- Rutas:
    - Windows usa \, Linux/macOS usan /.
    - Solución: Usa siempre os.path.join():
        ```python
        ruta = os.path.join("carpeta", "subcarpeta", "archivo.txt")
        ```
- Comandos del sistema:
    - os.system("ls") funciona en Linux/macOS, pero en Windows es dir.
    - Alternativa multiplataforma: Usa subprocess.run() en lugar de os.system().

- Permisos:
    - Linux/macOS usan permisos Unix (os.chmod()).
    - Windows maneja permisos de forma diferente.

### 📂 Ejemplo Práctico Multiplataforma
```python
import os

# Crear una estructura de carpetas multiplataforma
carpeta_principal = "proyecto"
subcarpetas = ["data", "src", "docs"]

os.makedirs(carpeta_principal, exist_ok=True)  # 'exist_ok=True' evita errores si ya existe

for carpeta in subcarpetas:
    ruta = os.path.join(carpeta_principal, carpeta)
    os.mkdir(ruta)

# Listar archivos en el directorio actual
print("Archivos en el directorio actual:")
for archivo in os.listdir("."):
    print(f"- {archivo}")

# Verificar si un archivo existe
ruta_archivo = os.path.join(carpeta_principal, "data", "datos.csv")
if not os.path.exists(ruta_archivo):
    print(f"\nEl archivo {ruta_archivo} no existe")
```