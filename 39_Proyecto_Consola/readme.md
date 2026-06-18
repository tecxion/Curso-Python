<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/38_Despliegue/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/40_Proyecto_Web/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/proyecto_consola.png">
</h1>


<h1 align="center">Proyecto 1: Gestor de Tareas de Consola</h1><br>

<h3>Índice</h3>

- [1. ¿Qué vamos a construir?](#1-qué-vamos-a-construir)
- [2. Preparar el proyecto](#2-preparar-el-proyecto)
- [3. Paso 1: la clase Tarea (tarea.py)](#3-paso-1-la-clase-tarea-tareapy)
- [4. Paso 2: guardar y leer en disco (almacenamiento.py)](#4-paso-2-guardar-y-leer-en-disco-almacenamientopy)
- [5. Paso 3: la lógica (gestor.py)](#5-paso-3-la-lógica-gestorpy)
- [6. Paso 4: el menú de consola (main.py)](#6-paso-4-el-menú-de-consola-mainpy)
- [7. Ejecutar el proyecto (¡tu despliegue!)](#7-ejecutar-el-proyecto-tu-despliegue)
- [8. Distribuir el proyecto](#8-distribuir-el-proyecto)
- [9. Crear un ejecutable (.exe / app) con PyInstaller](#9-crear-un-ejecutable-exe--app-con-pyinstaller)
- [10. Ideas para seguir mejorándolo](#10-ideas-para-seguir-mejorándolo)
- [11. ¡Enhorabuena!](#11-enhorabuena)

<a name = "1-qué-vamos-a-construir"></a>

## 1. ¿Qué vamos a construir?

¡Hemos llegado al final! Es el momento de juntar **todo** lo aprendido en un proyecto de verdad. Vamos a crear un **Gestor de Tareas** que funciona enteramente desde la consola y que permite:

- Añadir tareas con prioridad (alta, media, baja).
- Ver todas las tareas o solo las pendientes.
- Marcar tareas como completadas.
- Eliminar tareas.
- **Guardar todo en un fichero**, de modo que al cerrar y volver a abrir el programa, tus tareas sigan ahí.

Este proyecto repasa de golpe casi todo el curso:

| Lo que usamos | Día |
| ------------------------------------ | ----------------- |
| Clases y objetos (`Tarea`, `GestorTareas`) | 15 y 16 (POO) |
| Lectura/escritura de ficheros JSON | 17 (Ficheros) |
| `try / except` para no romperse | 14 (Errores) |
| Comprensiones de listas | 18 (Comprensiones) |
| Varios `.py` que se importan entre sí | 12 y 19 (Módulos) |
| Bucles, condicionales, funciones, diccionarios… | ¡todo el resto! |

>[!NOTE]
>Tienes el proyecto **completo y funcionando** en la carpeta [`gestor_tareas`](./gestor_tareas) de este mismo día. Te recomiendo escribirlo tú desde cero siguiendo la guía, y usar esa carpeta solo para comparar si te atascas.

<a name = "2-preparar-el-proyecto"></a>

## 2. Preparar el proyecto

Vamos a aplicar lo del día anterior. Abre una terminal y crea la estructura:

```bash
mkdir gestor_tareas
cd gestor_tareas

# Creamos y activamos el entorno virtual
python3 -m venv venv
source venv/bin/activate        # En Windows: venv\Scripts\activate
```

Nuestro proyecto se repartirá en **cuatro ficheros**, cada uno con una responsabilidad clara (a esto se le llama *separación de responsabilidades*):

```
gestor_tareas/
├── tarea.py            # QUÉ es una tarea
├── almacenamiento.py   # CÓMO se guardan y leen las tareas
├── gestor.py           # La LÓGICA: añadir, completar, eliminar...
└── main.py             # La INTERFAZ: el menú con el que habla el usuario
```

<a name = "3-paso-1-la-clase-tarea-tareapy"></a>

## 3. Paso 1: la clase Tarea (tarea.py)

Empezamos por lo más pequeño: representar **una** tarea. Una tarea tiene un título, una prioridad, si está o no completada, y una fecha de creación. Además necesita saber convertirse a diccionario (para poder guardarse en JSON) y volver a crearse desde un diccionario.

```python
# tarea.py
from datetime import datetime

PRIORIDADES_VALIDAS = ("alta", "media", "baja")


class Tarea:
    def __init__(self, titulo, prioridad="media", completada=False, fecha=None):
        self.titulo = titulo
        self.prioridad = prioridad if prioridad in PRIORIDADES_VALIDAS else "media"
        self.completada = completada
        # Si no nos pasan fecha, usamos la actual
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
```

Fíjate en `@classmethod`: es un método que se llama sobre la **clase** (`Tarea.desde_diccionario(...)`) en vez de sobre un objeto, y sirve aquí como "fábrica" de tareas a partir de datos guardados.

<a name = "4-paso-2-guardar-y-leer-en-disco-almacenamientopy"></a>

## 4. Paso 2: guardar y leer en disco (almacenamiento.py)

Este fichero se encarga **solo** de hablar con el disco duro. Así, si el día de mañana quisiéramos guardar en una base de datos en vez de en un JSON, solo cambiaríamos este archivo.

```python
# almacenamiento.py
import os
import json

# Guardamos el JSON junto a este fichero, así funciona ejecutes desde donde ejecutes.
RUTA = os.path.join(os.path.dirname(__file__), "tareas.json")


def guardar_tareas(lista_de_diccionarios):
    with open(RUTA, "w", encoding="utf-8") as fichero:
        json.dump(lista_de_diccionarios, fichero, indent=4, ensure_ascii=False)


def cargar_tareas():
    try:
        with open(RUTA, "r", encoding="utf-8") as fichero:
            return json.load(fichero)
    except FileNotFoundError:
        return []          # primera ejecución: aún no hay fichero
    except json.JSONDecodeError:
        print("Aviso: el fichero de tareas estaba dañado. Se empieza de cero.")
        return []
```

¿Ves cómo aquí aparece el manejo de errores del día 14? Si el fichero no existe (la primera vez que ejecutas el programa) no nos rompemos: devolvemos una lista vacía y a funcionar.

<a name = "5-paso-3-la-lógica-gestorpy"></a>

## 5. Paso 3: la lógica (gestor.py)

La clase `GestorTareas` es el **cerebro**: mantiene la lista de tareas en memoria y ofrece los métodos para manipularla. Conecta las dos piezas anteriores: usa la clase `Tarea` y las funciones de `almacenamiento`.

```python
# gestor.py
from tarea import Tarea
from almacenamiento import guardar_tareas, cargar_tareas


class GestorTareas:
    def __init__(self):
        # Cargamos los diccionarios guardados y los convertimos en objetos Tarea.
        self.tareas = [Tarea.desde_diccionario(d) for d in cargar_tareas()]

    def agregar(self, titulo, prioridad):
        self.tareas.append(Tarea(titulo, prioridad))
        self.guardar()

    def completar(self, indice):
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
        return [tarea for tarea in self.tareas if not tarea.completada]

    def guardar(self):
        guardar_tareas([tarea.a_diccionario() for tarea in self.tareas])
```

¡Mira cuánto del curso hay aquí! Una **clase** (cap. 15), una **comprensión de listas** en `__init__` y en `pendientes()` (cap. 18), y la conexión entre varios **módulos** (cap. 12). Cada vez que cambiamos algo llamamos a `self.guardar()` para que el JSON esté siempre actualizado.

<a name = "6-paso-4-el-menú-de-consola-mainpy"></a>

## 6. Paso 4: el menú de consola (main.py)

Por último, `main.py` es lo único que ve el usuario: un menú en bucle que lee opciones por teclado y llama al gestor. Aquí va el bloque `if __name__ == "__main__":` que vimos en el día anterior.

```python
# main.py
from gestor import GestorTareas


def mostrar_menu():
    print("\n========== GESTOR DE TAREAS TECXION ==========")
    print("1. Ver todas las tareas")
    print("2. Ver solo pendientes")
    print("3. Añadir tarea")
    print("4. Marcar tarea como completada")
    print("5. Eliminar tarea")
    print("6. Salir")
    print("==============================================")


def mostrar_tareas(tareas):
    if not tareas:
        print("\n  (No hay tareas para mostrar)")
        return
    print()
    for numero, tarea in enumerate(tareas, start=1):
        print(f"  {numero}. {tarea}")


def main():
    gestor = GestorTareas()
    print("¡Bienvenido a tu gestor de tareas!")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ").strip()

        if opcion == "1":
            mostrar_tareas(gestor.tareas)
        elif opcion == "2":
            mostrar_tareas(gestor.pendientes())
        elif opcion == "3":
            titulo = input("Título de la tarea: ").strip()
            prioridad = input("Prioridad (alta/media/baja): ").strip().lower()
            gestor.agregar(titulo, prioridad)
            print(f"Tarea '{titulo}' añadida.")
        elif opcion == "4":
            mostrar_tareas(gestor.tareas)
            try:
                numero = int(input("Número de la tarea a completar: "))
                gestor.completar(numero - 1)
            except ValueError:
                print("Debes escribir un número.")
        elif opcion == "5":
            mostrar_tareas(gestor.tareas)
            try:
                numero = int(input("Número de la tarea a eliminar: "))
                gestor.eliminar(numero - 1)
            except ValueError:
                print("Debes escribir un número.")
        elif opcion == "6":
            print("¡Hasta pronto! Tus tareas quedan guardadas.")
            break
        else:
            print("Opción no válida. Elige un número del 1 al 6.")


if __name__ == "__main__":
    main()
```

>[!NOTE]
>La versión que tienes en la carpeta [`gestor_tareas`](./gestor_tareas) está un poco más pulida (valida títulos vacíos, avisa si el número no existe, etc.). Compárala cuando termines la tuya: verás pequeñas mejoras que puedes incorporar.

<a name = "7-ejecutar-el-proyecto-tu-despliegue"></a>

## 7. Ejecutar el proyecto (¡tu despliegue!)

Llegó el momento de **desplegarlo en tu propia máquina**. Con el entorno activado y dentro de la carpeta del proyecto:

```bash
python3 main.py        # En Windows: python main.py
```

Verás aparecer el menú. Prueba a añadir un par de tareas, marca una como completada y **cierra el programa**. Si vuelves a ejecutarlo, ¡tus tareas siguen ahí! Esa es la magia de haber aprendido a guardar en ficheros: aparecerá un fichero `tareas.json` en la carpeta con tus datos.

```bash
# Una sesión de ejemplo:
# 1) Añades "Estudiar Python" con prioridad alta
# 2) Añades "Comprar pan" con prioridad baja
# 3) Marcas la primera como completada
# 4) Cierras y vuelves a abrir -> ¡siguen guardadas!
```

>[!IMPORTANT]
>Esto es, literalmente, un **despliegue local**: tu aplicación ejecutándose de verdad en tu ordenador, lista para usarse desde la terminal cuantas veces quieras.

<a name = "8-distribuir-el-proyecto"></a>

## 8. Distribuir el proyecto

Un proyecto no está terminado hasta que otra persona puede usarlo. Para compartirlo bien, añade estos tres ficheros (todos vistos en el día 19):

- **`requirements.txt`** → las dependencias. Nuestro proyecto solo usa la librería estándar, así que no necesita paquetes externos, pero lo incluimos porque es el estándar:
  ```bash
  pip freeze > requirements.txt
  ```
- **`.gitignore`** → para no subir basura al repositorio:
  ```
  venv/
  __pycache__/
  tareas.json
  ```
- **`README.md`** → explica qué hace el proyecto y cómo ejecutarlo.

Con esto puedes subirlo a GitHub (como este mismo curso) y cualquiera podrá descargarlo, crear su entorno y ejecutarlo con tres comandos:

```bash
git clone <url-de-tu-repo>
cd gestor_tareas
python3 main.py
```

<a name = "9-crear-un-ejecutable-exe--app-con-pyinstaller"></a>

## 9. Crear un ejecutable (.exe / app) con PyInstaller

¿Y si quieres dárselo a alguien que **no tiene Python instalado**? Puedes empaquetar el proyecto en un **único ejecutable** con la librería **PyInstaller**. Esto convierte tu programa en un archivo que se abre con doble clic (un `.exe` en Windows, un binario en Mac/Linux).

```bash
# Con el entorno virtual activado, instala PyInstaller
pip install pyinstaller

# Genera el ejecutable a partir de main.py
pyinstaller --onefile main.py
```

Cuando termine, encontrarás tu programa dentro de una carpeta llamada **`dist/`**. Ese archivo ya no necesita Python: se puede ejecutar en cualquier ordenador del mismo sistema operativo.

>[!NOTE]
>El ejecutable que genera PyInstaller es específico de cada sistema operativo: si lo creas en Windows obtienes un `.exe` para Windows; si lo creas en Mac, uno para Mac. Para distribuir a varios sistemas, hay que generarlo en cada uno.

<a name = "10-ideas-para-seguir-mejorándolo"></a>

## 10. Ideas para seguir mejorándolo

El proyecto funciona, pero la mejor forma de aprender es ampliarlo. Aquí tienes retos, de más fácil a más difícil:

- **Fácil:** añade una opción para editar el título de una tarea.
- **Fácil:** ordena las tareas por prioridad al listarlas (`sorted` con `key`, cap. 13).
- **Media:** añade una fecha límite a cada tarea y avisa de las que ya han vencido (`datetime`).
- **Media:** colorea la salida con la librería `colorama` (rojo = alta, verde = completada). Ahí sí tendrá sentido tu `requirements.txt`.
- **Difícil:** crea una excepción propia `TareaNoEncontradaError` (cap. 14) y úsala en el gestor.
- **Difícil:** permite tener varias listas (trabajo, casa, estudios) guardadas en ficheros distintos.

<a name = "11-enhorabuena"></a>

## 11. ¡Enhorabuena!

Has construido una aplicación de consola completa, organizada en varios ficheros, con clases, persistencia de datos y manejo de errores: todo lo aprendido desde el día 1 puesto en práctica. Eso ya **no es de principiante**.

Pero aún queda un último reto, el más ambicioso del curso. Mañana, en el **día 40**, construirás el **segundo proyecto final**: una aplicación **web full-stack** (Flask + API + base de datos) y la **desplegarás en internet** con una URL pública. Llevarás esta misma idea (un gestor de tareas) del terminal a la web.

<h3 align = "center">
"No tienes que ser un experto para empezar, pero tienes que empezar para llegar a ser un experto."
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/38_Despliegue/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/40_Proyecto_Web/readme.md">Día siguiente</a>
</h4>
