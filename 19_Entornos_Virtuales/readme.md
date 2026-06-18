<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/18_Comprehensions/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/20_Fechas/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/entornos_virtuales.png">
</h1>


<h1 align="center">Entornos Virtuales y Gestión de Paquetes</h1><br>

<h3>Índice</h3>

- [1. ¿Qué es un entorno virtual y por qué usarlo?](#1-qué-es-un-entorno-virtual-y-por-qué-usarlo)
- [2. Crear un entorno virtual con venv](#2-crear-un-entorno-virtual-con-venv)
- [3. Activar y desactivar el entorno](#3-activar-y-desactivar-el-entorno)
- [4. Instalar paquetes con pip](#4-instalar-paquetes-con-pip)
- [5. requirements.txt](#5-requirementstxt)
- [6. El fichero .gitignore](#6-el-fichero-gitignore)
- [7. Cómo se organiza un proyecto Python](#7-cómo-se-organiza-un-proyecto-python)
- [8. Importar tus propios módulos](#8-importar-tus-propios-módulos)
- [9. Ejercicios](#9-ejercicios)

<a name = "1-qué-es-un-entorno-virtual-y-por-qué-usarlo"></a>

## 1. ¿Qué es un entorno virtual y por qué usarlo?

Cuando instalas paquetes (librerías que otros han escrito) con `pip`, por defecto se instalan **para todo tu ordenador**. El problema es que cada proyecto puede necesitar versiones **distintas** del mismo paquete, y eso acaba generando conflictos.

Un **entorno virtual** (*virtual environment*) es una **carpeta aislada** que contiene su propia copia de Python y sus propios paquetes, **independiente** del resto del sistema. Así, cada proyecto tiene exactamente lo que necesita, sin interferir con los demás.

Piensa en ello como una "burbuja" para cada proyecto:
- El proyecto A puede usar la versión 1.0 de una librería.
- El proyecto B puede usar la versión 2.0 de la misma librería.
- Y no se pelean entre ellos.

>[!IMPORTANT]
>Usar entornos virtuales es una **práctica estándar** en Python. Cualquier proyecto profesional los usa. Es uno de esos hábitos que conviene adquirir cuanto antes.

<a name = "2-crear-un-entorno-virtual-con-venv"></a>

## 2. Crear un entorno virtual con venv

Python incluye de serie la herramienta **`venv`** para crear entornos virtuales. Desde la terminal, dentro de la carpeta de tu proyecto, ejecuta:

```bash
# En Windows
python -m venv venv

# En macOS / Linux
python3 -m venv venv
```

Esto crea una carpeta llamada `venv` (el segundo `venv` es solo el nombre que le damos; podría ser otro, pero `venv` es lo habitual). Dentro está tu Python aislado.

<a name = "3-activar-y-desactivar-el-entorno"></a>

## 3. Activar y desactivar el entorno

Crear el entorno no basta: hay que **activarlo** para empezar a usarlo. El comando cambia según el sistema operativo:

```bash
# Windows (CMD)
venv\Scripts\activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate
```

Cuando está activado, verás `(venv)` al principio de la línea de la terminal. A partir de ahí, todo lo que instales con `pip` irá **solo** a este entorno.

Para salir del entorno, en cualquier sistema:

```bash
deactivate
```

>[!NOTE]
>El entorno virtual hay que activarlo **cada vez** que abres una terminal nueva para trabajar en el proyecto. No es algo permanente.

<a name = "4-instalar-paquetes-con-pip"></a>

## 4. Instalar paquetes con pip

**`pip`** es el gestor de paquetes de Python: sirve para instalar librerías que otras personas han publicado (hay miles, en [pypi.org](https://pypi.org)). Con el entorno activado:

```bash
# Instalar un paquete
pip install requests

# Instalar una versión concreta
pip install requests==2.31.0

# Ver los paquetes instalados
pip list

# Actualizar un paquete
pip install --upgrade requests

# Desinstalar
pip uninstall requests
```

`requests`, por ejemplo, es una librería famosísima para hacer peticiones a internet. Pero hay paquetes para casi todo: gráficos, datos, juegos, IA…

<a name = "5-requirementstxt"></a>

## 5. requirements.txt

Imagina que compartes tu proyecto con otra persona (o lo subes a GitHub). Esa persona necesita saber **qué paquetes** instalar. Para eso existe el fichero **`requirements.txt`**, que lista todas las dependencias del proyecto.

Lo generas automáticamente con:

```bash
pip freeze > requirements.txt
```

El fichero quedará con un contenido parecido a este:

```
requests==2.31.0
colorama==0.4.6
```

Y cualquiera que descargue tu proyecto puede instalar **todo de golpe** con:

```bash
pip install -r requirements.txt
```

>[!IMPORTANT]
>La carpeta `venv` **NO se sube a GitHub** (es enorme y se regenera). Lo que se comparte es el `requirements.txt`, para que cada persona se cree su propio entorno.

<a name = "6-el-fichero-gitignore"></a>

## 6. El fichero .gitignore

El fichero **`.gitignore`** le dice a Git qué archivos y carpetas debe **ignorar** (no subir al repositorio). En un proyecto Python casi siempre incluye, como mínimo:

```
# Entorno virtual
venv/

# Ficheros compilados de Python
__pycache__/
*.pyc

# Datos locales que no queremos compartir
*.log
```

Así evitas subir cosas pesadas o personales. Es uno de los primeros ficheros que se crean en un proyecto serio.

<a name = "7-cómo-se-organiza-un-proyecto-python"></a>

## 7. Cómo se organiza un proyecto Python

Hasta ahora cada día ha tenido un único `.py`. Pero un proyecto real se reparte en **varios ficheros**, cada uno con una responsabilidad. Una estructura típica y sencilla:

```
mi_proyecto/
│
├── venv/                  # entorno virtual (ignorado por git)
├── main.py                # punto de entrada: arranca el programa
├── funciones.py           # lógica del programa
├── datos.py               # carga y guardado de datos
├── requirements.txt       # dependencias
├── .gitignore             # qué ignora git
└── README.md              # explicación del proyecto
```

La idea clave es la **separación de responsabilidades**: cada fichero hace una cosa, y `main.py` los coordina. Esto es exactamente lo que montaremos en el proyecto final.

<a name = "8-importar-tus-propios-módulos"></a>

## 8. Importar tus propios módulos

Como ya viste en el día 12 (Módulos), un fichero `.py` puede importar funciones de otro fichero `.py` que esté en la misma carpeta:

```python
# fichero: funciones.py
def saludar(nombre):
    return f"Hola, {nombre}"
```

```python
# fichero: main.py
from funciones import saludar

print(saludar("Ana"))   # Hola, Ana
```

Un detalle profesional muy útil es el bloque **`if __name__ == "__main__":`**. El código que pongas dentro solo se ejecuta cuando el fichero se lanza **directamente**, no cuando se importa desde otro. Es la forma correcta de marcar "por aquí empieza el programa":

```python
# main.py
def main():
    print("¡Arranca el programa!")

if __name__ == "__main__":
    main()
```

>[!NOTE]
>`__name__` vale `"__main__"` cuando ejecutas el fichero directamente (`python main.py`), pero vale el nombre del módulo cuando lo importas. Así puedes tener ficheros que sirvan a la vez como programa y como módulo reutilizable.

<a name = "9-ejercicios"></a>

## 9. Ejercicios

Estos ejercicios son **prácticos de terminal**. La idea es que te familiarices con el flujo de trabajo real antes del proyecto final. En la carpeta del día tienes un ejemplo (`ejemplo_proyecto/`) que puedes usar como referencia.

1. Crea una carpeta nueva llamada `practica_entorno` y, dentro, crea un entorno virtual con `venv`.

2. Actívalo y comprueba que aparece `(venv)` en tu terminal. Luego desactívalo con `deactivate` y vuelve a activarlo.

3. Con el entorno activado, instala el paquete `colorama` (sirve para imprimir texto en color en la consola) con `pip install colorama`.

4. Ejecuta `pip list` y localiza `colorama` entre los paquetes instalados.

5. Genera un fichero `requirements.txt` con `pip freeze > requirements.txt` y ábrelo para ver su contenido.

6. Crea un fichero `.gitignore` que ignore la carpeta `venv/` y `__pycache__/`.

7. Crea dos ficheros: `operaciones.py` con una función `sumar(a, b)`, y `main.py` que la importe y la use. Ejecuta `python main.py`.

8. Añade a `main.py` el bloque `if __name__ == "__main__":` y comprueba que el programa solo arranca al ejecutarlo directamente y no al importarlo.

> [!NOTE]
> Pistas para los ejercicios:
> - Crear entorno: `python -m venv venv` (Windows) o `python3 -m venv venv` (Mac/Linux).
> - Activar: `venv\Scripts\activate` (Windows) o `source venv/bin/activate` (Mac/Linux).
> - Si en Mac/Linux `python3` no funciona, prueba `python`. Si `pip` falla, prueba `pip3`.
> - Recuerda: la carpeta `venv` no se sube nunca a GitHub.
> - Para importar tu módulo: `from operaciones import sumar`.

<h3 align = "center">
¡Ya tienes todas las piezas! Errores, clases, ficheros, comprensiones y el flujo de trabajo profesional. Ha llegado el momento de juntarlo todo en un proyecto real.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/18_Comprehensions/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/20_Fechas/readme.md">Día siguiente</a>
</h4>
