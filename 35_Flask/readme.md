<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/34_Web_Scraping/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/36_API_REST/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/flask.png">
</h1>


<h1 align="center">Desarrollo Web con Flask</h1><br>

<h3>Índice</h3>

- [1. ¿Qué es Flask?](#1-qué-es-flask)
- [2. Tu primera aplicación web](#2-tu-primera-aplicación-web)
- [3. Rutas y vistas](#3-rutas-y-vistas)
- [4. Rutas con parámetros](#4-rutas-con-parámetros)
- [5. Plantillas HTML con Jinja2](#5-plantillas-html-con-jinja2)
- [6. Pasar datos a la plantilla](#6-pasar-datos-a-la-plantilla)
- [7. Estructura de un proyecto Flask](#7-estructura-de-un-proyecto-flask)
- [8. Ejercicios](#8-ejercicios)

<a name = "1-qué-es-flask"></a>

## 1. ¿Qué es Flask?

**Flask** es un *framework* (un conjunto de herramientas) para crear **aplicaciones web** con Python. Con él, tu programa deja de vivir solo en la consola y pasa a tener **páginas web** que cualquiera puede abrir en su navegador.

Flask es **minimalista**: te da lo esencial y tú añades lo demás. Eso lo hace perfecto para aprender. Con él podrás crear desde una web sencilla hasta una API completa (lo veremos mañana).

```bash
pip install flask
```

<a name = "2-tu-primera-aplicación-web"></a>

## 2. Tu primera aplicación web

Esta es una aplicación web completa en Flask. Apenas 7 líneas:

```python
# fichero: app.py
from flask import Flask

app = Flask(__name__)        # creamos la aplicación

@app.route("/")              # cuando alguien visite "/"...
def inicio():
    return "<h1>¡Hola, mundo web!</h1>"   # ...se ejecuta esto

if __name__ == "__main__":
    app.run(debug=True)      # arranca el servidor de desarrollo
```

Para ejecutarla:

```bash
python app.py
```

Verás un mensaje con una dirección como `http://127.0.0.1:5000`. Ábrela en tu navegador y verás tu página. `127.0.0.1` (o `localhost`) es **tu propio ordenador**: el servidor corre en tu máquina.

>[!NOTE]
>`debug=True` activa el modo desarrollo: la página se recarga sola al cambiar el código y muestra errores detallados. Quítalo cuando publiques la app de verdad.

<a name = "3-rutas-y-vistas"></a>

## 3. Rutas y vistas

Una **ruta** es una URL de tu web; la función que se ejecuta para esa URL se llama **vista**. Se conectan con el decorador `@app.route` (¡los decoradores del día 13 y 23 en acción!):

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def inicio():
    return "Página de inicio"

@app.route("/sobre-mi")
def sobre_mi():
    return "<h1>Sobre mí</h1><p>Soy estudiante de Python.</p>"

@app.route("/contacto")
def contacto():
    return "Escríbeme a correo@ejemplo.com"
```

Cada `@app.route("/ruta")` define una página distinta: `/`, `/sobre-mi`, `/contacto`.

<a name = "4-rutas-con-parámetros"></a>

## 4. Rutas con parámetros

Las rutas pueden tener **partes variables** entre `<>`, que llegan como argumento a la vista. Así una sola función sirve muchas páginas:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/usuario/<nombre>")
def saludar(nombre):
    return f"<h1>¡Hola, {nombre}!</h1>"

# Indicando el tipo del parámetro
@app.route("/cuadrado/<int:numero>")
def cuadrado(numero):
    return f"El cuadrado de {numero} es {numero ** 2}"
```

Visitar `/usuario/Ana` mostrará "¡Hola, Ana!"; `/cuadrado/5` mostrará "El cuadrado de 5 es 25".

<a name = "5-plantillas-html-con-jinja2"></a>

## 5. Plantillas HTML con Jinja2

Devolver HTML como texto se queda corto enseguida. Flask usa **Jinja2** para separar el HTML en ficheros **plantilla**, que van en una carpeta llamada `templates/`. Se cargan con `render_template`:

```
mi_web/
├── app.py
└── templates/
    └── inicio.html
```

```html
<!-- templates/inicio.html -->
<!DOCTYPE html>
<html>
<head><title>Mi web</title></head>
<body>
    <h1>Bienvenido a mi web</h1>
</body>
</html>
```

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")
```

<a name = "6-pasar-datos-a-la-plantilla"></a>

## 6. Pasar datos a la plantilla

Lo potente: podemos enviar **datos de Python** a la plantilla, y Jinja2 los pinta con `{{ }}` y permite bucles y condiciones con `{% %}`:

```python
@app.route("/")
def inicio():
    return render_template("inicio.html", nombre="Ana", tareas=["Estudiar", "Entrenar"])
```

```html
<!-- templates/inicio.html -->
<h1>Hola, {{ nombre }}</h1>
<ul>
    {% for tarea in tareas %}
        <li>{{ tarea }}</li>
    {% endfor %}
</ul>
```

¿Ves cómo Jinja2 usa los bucles que ya conoces (día 9)? El resultado es una lista HTML generada a partir de datos de Python. Esto es la base de cualquier web dinámica.

<a name = "7-estructura-de-un-proyecto-flask"></a>

## 7. Estructura de un proyecto Flask

Recuperando lo del día 19 (organización de proyectos), una app Flask sencilla se estructura así:

```
mi_web/
├── venv/                 # entorno virtual
├── app.py                # la aplicación y sus rutas
├── templates/            # los .html (Jinja2)
│   ├── base.html
│   └── inicio.html
├── static/               # CSS, imágenes, JavaScript
│   └── estilo.css
└── requirements.txt
```

- **`templates/`**: el HTML.
- **`static/`**: lo que no cambia (estilos, imágenes).
- **`app.py`**: la lógica y las rutas.

<a name = "8-ejercicios"></a>

## 8. Ejercicios

> Para estos ejercicios crea un fichero `app.py`. Pruébalo con `python app.py` y abre las URLs en el navegador. Recuerda terminar con `app.run(debug=True)`.

### Nivel 1 — Básico
1. Crea una app Flask con una ruta `/` que devuelva `"<h1>Mi primera web</h1>"`.
2. Añade una ruta `/sobre-mi` que devuelva una breve presentación tuya en HTML.
3. Añade una ruta `/contacto` con tu forma de contacto.
4. Ejecuta la app y comprueba las tres rutas en el navegador.

### Nivel 2 — Aplicado
5. Crea una ruta `/saludo/<nombre>` que salude a la persona por su nombre.
6. Crea una ruta `/suma/<int:a>/<int:b>` que muestre la suma de los dos números.
7. Crea una carpeta `templates/` con un `inicio.html` y haz que la ruta `/` lo muestre con `render_template`.
8. Pasa tu nombre desde la vista a la plantilla y muéstralo con `{{ nombre }}`.

### Nivel 3 — Reto
9. Pasa una lista de tareas a la plantilla y muéstrala como una lista HTML usando un bucle `{% for %}`.
10. En la plantilla, usa un `{% if %}` para mostrar "No hay tareas" si la lista está vacía.
11. Crea una pequeña web de 3 páginas (inicio, lista de productos desde una lista de Python, y "sobre mí") enlazadas entre sí con etiquetas `<a href="...">`.

> [!NOTE]
> Pistas:
> - Toda app empieza con `app = Flask(__name__)` y termina con `app.run(debug=True)`.
> - Cada página es una función con su `@app.route("/ruta")` encima.
> - Parámetros en la ruta: `<nombre>` o `<int:numero>`; llegan como argumento de la función.
> - Las plantillas van en `templates/` y se cargan con `render_template("archivo.html", dato=valor)`.
> - En Jinja2: `{{ variable }}` pinta un valor y `{% for x in lista %} ... {% endfor %}` hace un bucle.

<h3 align = "center">
¡Ya tienes tu primera web! Mañana convertimos Flask en una API REST para que otras aplicaciones (¡incluido tu móvil!) puedan hablar con ella.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/34_Web_Scraping/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/36_API_REST/readme.md">Día siguiente</a>
</h4>
