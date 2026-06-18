<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/37_Flask_BBDD/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/39_Proyecto_Consola/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/despliegue.png">
</h1>


<h1 align="center">Despliegue en la Nube</h1><br>

<h3>Índice</h3>

- [1. ¿Qué es desplegar?](#1-qué-es-desplegar)
- [2. Servidor de desarrollo vs producción](#2-servidor-de-desarrollo-vs-producción)
- [3. Preparar la app para producción](#3-preparar-la-app-para-producción)
- [4. requirements.txt y Procfile](#4-requirementstxt-y-procfile)
- [5. Subir el proyecto a GitHub](#5-subir-el-proyecto-a-github)
- [6. Desplegar en Render paso a paso](#6-desplegar-en-render-paso-a-paso)
- [7. Variables de entorno y secretos](#7-variables-de-entorno-y-secretos)
- [8. Ejercicios](#8-ejercicios)

<a name = "1-qué-es-desplegar"></a>

## 1. ¿Qué es desplegar?

Hasta ahora tu web (días 35-37) solo funcionaba en `http://127.0.0.1:5000`, es decir, **en tu ordenador**. **Desplegar** (*deploy*) es ponerla en un **servidor en internet** para que tenga una URL pública y cualquiera pueda usarla desde cualquier sitio.

Usaremos **Render** (https://render.com), una plataforma con un **plan gratuito** ideal para aprender, sin tarjeta de crédito. La idea sirve para otras (Railway, PythonAnywhere, Fly.io…).

<a name = "2-servidor-de-desarrollo-vs-producción"></a>

## 2. Servidor de desarrollo vs producción

El `app.run(debug=True)` que usábamos es el **servidor de desarrollo** de Flask: cómodo para programar, pero **no apto** para internet (es lento e inseguro). En producción se usa un servidor de verdad como **Gunicorn**:

```bash
pip install gunicorn
```

Gunicorn arranca tu app así (donde `app` es el fichero `app.py` y `app` el objeto Flask):

```bash
gunicorn app:app
```

>[!IMPORTANT]
>Regla de oro: `debug=True` **nunca** en producción. Muestra detalles internos que un atacante podría aprovechar.

<a name = "3-preparar-la-app-para-producción"></a>

## 3. Preparar la app para producción

Un detalle clave: el servidor en la nube te dice en **qué puerto** debe escuchar tu app a través de una **variable de entorno** llamada `PORT`. Hay que leerla en vez de fijar el 5000:

```python
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return {"mensaje": "¡Mi API está en internet!"}

if __name__ == "__main__":
    # Render (u otro) nos pasa el puerto en la variable PORT
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=puerto)
```

`host="0.0.0.0"` hace que la app acepte conexiones desde fuera, no solo desde tu máquina.

<a name = "4-requirementstxt-y-procfile"></a>

## 4. requirements.txt y Procfile

El servidor necesita saber **qué instalar** y **cómo arrancar** tu app. Dos ficheros (¿recuerdas el `requirements.txt` del día 19?):

`requirements.txt` — las dependencias:
```
flask
flask-sqlalchemy
gunicorn
```

Genéralo automáticamente con:
```bash
pip freeze > requirements.txt
```

Y el comando de arranque (en Render se pone en su panel, o en un `Procfile` en otras plataformas):
```
web: gunicorn app:app
```

<a name = "5-subir-el-proyecto-a-github"></a>

## 5. Subir el proyecto a GitHub

Render despliega desde un repositorio de GitHub. Si no lo has hecho aún, sube tu proyecto:

```bash
git init
git add .
git commit -m "Mi app lista para desplegar"
git branch -M main
git remote add origin https://github.com/tu_usuario/mi-app.git
git push -u origin main
```

>[!IMPORTANT]
>Asegúrate de tener un `.gitignore` (día 19) que excluya `venv/` y `__pycache__/`. No subas el entorno virtual ni datos sensibles.

<a name = "6-desplegar-en-render-paso-a-paso"></a>

## 6. Desplegar en Render paso a paso

1. Crea una cuenta gratis en [render.com](https://render.com) (puedes entrar con tu cuenta de GitHub).
2. Pulsa **New + → Web Service**.
3. Conecta tu repositorio de GitHub.
4. Render detecta que es Python. Configura:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Elige el plan **Free** y pulsa **Create Web Service**.
6. Espera unos minutos: Render instala, arranca y te da una **URL pública** tipo `https://mi-app.onrender.com`.

¡Tu app ya está en internet! Cada vez que hagas `git push`, Render la **vuelve a desplegar** sola.

>[!NOTE]
>En el plan gratuito, la app "se duerme" tras un rato sin visitas y tarda unos segundos en despertar en la siguiente. Es normal y suficiente para aprender y enseñar tu proyecto.

<a name = "7-variables-de-entorno-y-secretos"></a>

## 7. Variables de entorno y secretos

Nunca escribas contraseñas, claves de API o secretos **dentro del código** (acabarían en GitHub a la vista de todos). Se guardan en **variables de entorno** y se leen con `os.environ`:

```python
import os
clave_secreta = os.environ.get("SECRET_KEY", "valor-por-defecto-solo-local")
```

En Render las defines en **Environment → Add Environment Variable**. Así tu código es público pero tus secretos no.

<a name = "8-ejercicios"></a>

## 8. Ejercicios

> Estos ejercicios son **prácticos**: el objetivo es dejar una API tuya funcionando en internet. En la carpeta del día tienes `app.py` y `requirements.txt` de ejemplo, ya listos para desplegar.

### Nivel 1 — Básico
1. Coge la API que hiciste el día 37 y modifícala para leer el puerto de `os.environ.get("PORT", 5000)`.
2. Quita el `debug=True` y pon `host="0.0.0.0"`.
3. Crea su `requirements.txt` con `pip freeze > requirements.txt`.
4. Instala `gunicorn` y arranca tu app localmente con `gunicorn app:app` para comprobar que funciona.

### Nivel 2 — Aplicado
5. Crea un `.gitignore` que excluya `venv/`, `__pycache__/` y `*.db`.
6. Sube el proyecto a un repositorio nuevo de GitHub.
7. Crea una cuenta en Render y despliega el servicio web siguiendo los pasos de la sección 6.
8. Abre la URL pública que te da Render y comprueba que tu API responde.

### Nivel 3 — Reto
9. Añade una variable de entorno `SECRET_KEY` en Render y léela en tu app con `os.environ`.
10. Haz un cambio en el código, haz `git push` y comprueba que Render redespliega automáticamente.
11. Comparte la URL con alguien y pídele que cree datos a través de tu API (por ejemplo con la web del día 40). ¡Tu app ya la usa otra persona desde otro ordenador!

> [!NOTE]
> Pistas:
> - Lee el puerto SIEMPRE de `os.environ.get("PORT", 5000)`; nunca lo fijes en producción.
> - El comando de arranque es `gunicorn fichero:objeto` → con `app.py` y `app = Flask(...)` es `gunicorn app:app`.
> - `pip freeze > requirements.txt` captura tus dependencias exactas.
> - Si Render falla, mira los **Logs** en su panel: casi siempre es una dependencia que falta en `requirements.txt`.

<h3 align = "center">
¡Felicidades, ya sabes llevar una app de tu ordenador a todo el mundo! Solo quedan los dos proyectos finales. Mañana, el primero: tu app de consola completa.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/37_Flask_BBDD/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/39_Proyecto_Consola/readme.md">Día siguiente</a>
</h4>
