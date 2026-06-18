<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/24_Itertools/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/26_SQLite/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/context_managers.png">
</h1>


<h1 align="center">Context Managers (la sentencia with)</h1><br>

<h3>Índice</h3>

- [1. El problema de los recursos](#1-el-problema-de-los-recursos)
- [2. ¿Qué es un context manager?](#2-qué-es-un-context-manager)
- [3. Crear uno con una clase: __enter__ y __exit__](#3-crear-uno-con-una-clase-__enter__-y-__exit__)
- [4. Gestionar errores dentro del with](#4-gestionar-errores-dentro-del-with)
- [5. Crear uno con contextlib y yield](#5-crear-uno-con-contextlib-y-yield)
- [6. Abrir varios recursos a la vez](#6-abrir-varios-recursos-a-la-vez)
- [7. Ejercicios](#7-ejercicios)

<a name = "1-el-problema-de-los-recursos"></a>

## 1. El problema de los recursos

Algunos recursos hay que **abrirlos y cerrarlos**: ficheros, conexiones a bases de datos, conexiones de red… Si se nos olvida cerrarlos, provocamos fugas de memoria y errores. Y si el programa falla a mitad, el recurso puede quedar abierto para siempre.

```python
# Forma peligrosa: ¿y si write() falla? El fichero queda abierto.
fichero = open("datos.txt", "w")
fichero.write("hola")
fichero.close()   # fácil de olvidar
```

En el día 17 ya usaste la solución: la sentencia **`with`**. Hoy aprenderás **cómo funciona por dentro** y a crear tus propios `with`.

<a name = "2-qué-es-un-context-manager"></a>

## 2. ¿Qué es un context manager?

Un **context manager** (gestor de contexto) es un objeto preparado para usarse con `with`. Garantiza que algo se ejecute **al entrar** y, sobre todo, algo **al salir** (¡aunque haya un error!).

```python
with open("datos.txt", "w") as fichero:
    fichero.write("hola")
# Al salir del bloque, el fichero se cierra SOLO, pase lo que pase
```

La idea clave: el `with` se encarga de la "limpieza" por ti. Vamos a construir los nuestros.

<a name = "3-crear-uno-con-una-clase-__enter__-y-__exit__"></a>

## 3. Crear uno con una clase: __enter__ y __exit__

Cualquier clase se convierte en context manager si implementa dos métodos especiales (¿recuerdas los *dunder* del día 16?):

- **`__enter__`**: se ejecuta al **entrar** en el `with`. Lo que devuelva es lo que recibe el `as`.
- **`__exit__`**: se ejecuta al **salir**, siempre.

```python
class Temporizador:
    def __enter__(self):
        import time
        self.inicio = time.time()
        print("⏱ Empieza la medición...")
        return self            # esto es lo que recibe el 'as'

    def __exit__(self, tipo_error, valor_error, traza):
        import time
        self.fin = time.time()
        print(f"⏱ Tardó {self.fin - self.inicio:.4f} segundos")

with Temporizador():
    total = sum(range(1_000_000))
# ⏱ Empieza la medición...
# ⏱ Tardó 0.03 segundos
```

Lo importante: el código de `__exit__` se ejecuta **garantizado** al terminar el bloque.

<a name = "4-gestionar-errores-dentro-del-with"></a>

## 4. Gestionar errores dentro del with

Lo más potente de `__exit__` es que se ejecuta **incluso si hay una excepción** dentro del `with`. Recibe información del error (tipo, valor y traza), por lo que puede reaccionar a él:

```python
class ConexionSegura:
    def __enter__(self):
        print("Abriendo conexión...")
        return self

    def __exit__(self, tipo_error, valor_error, traza):
        print("Cerrando conexión (pase lo que pase)")
        if tipo_error is not None:
            print(f"Hubo un error: {valor_error}")
        return True   # True = "ya he gestionado el error, no lo relances"

with ConexionSegura():
    print("Trabajando...")
    raise ValueError("¡algo salió mal!")

print("El programa continúa")   # se ejecuta gracias al return True
```

Si `__exit__` devuelve `True`, le dice a Python "el error ya está controlado". Si devuelve `False` (o nada), la excepción se propaga normalmente.

<a name = "5-crear-uno-con-contextlib-y-yield"></a>

## 5. Crear uno con contextlib y yield

Escribir una clase entera para algo sencillo es mucho. El módulo **`contextlib`** permite crear un context manager con una simple **función generadora** y el decorador `@contextmanager`:

- Todo lo que va **antes** del `yield` es el `__enter__`.
- Todo lo que va **después** del `yield` es el `__exit__`.

```python
from contextlib import contextmanager

@contextmanager
def temporizador():
    import time
    inicio = time.time()
    print("Empieza...")
    yield                       # aquí se ejecuta el cuerpo del with
    fin = time.time()
    print(f"Tardó {fin - inicio:.4f} segundos")

with temporizador():
    total = sum(range(1_000_000))
```

Mucho más corto que la versión con clase, y muy legible.

<a name = "6-abrir-varios-recursos-a-la-vez"></a>

## 6. Abrir varios recursos a la vez

Un mismo `with` puede gestionar varios recursos separándolos por comas. Es habitual al, por ejemplo, leer de un fichero y escribir en otro:

```python
with open("origen.txt", "r", encoding="utf-8") as entrada, \
     open("copia.txt", "w", encoding="utf-8") as salida:
    salida.write(entrada.read())
# Los dos ficheros se cierran solos al terminar
```

>[!NOTE]
>La barra invertida `\` al final de la línea solo sirve para partir una línea muy larga en dos y que se lea mejor. No es obligatoria.

<a name = "7-ejercicios"></a>

## 7. Ejercicios

1. Crea una clase context manager `Saludo` que imprima "Hola" al entrar y "Adiós" al salir. Pruébala con un `with`.

2. Crea un context manager con clase `Marco` que imprima una línea de `=` antes y después del bloque (para enmarcar lo que se imprime dentro).

3. Crea un context manager `Temporizador` (con clase) que mida y muestre cuánto tarda el código de su bloque.

4. Crea un context manager con clase que, en `__exit__`, capture cualquier error producido dentro del `with` y lo muestre sin que el programa se rompa (devuelve `True`).

5. Repite el ejercicio 1 (`Saludo`) pero ahora usando `@contextmanager` y `yield` en lugar de una clase.

6. Crea con `@contextmanager` un gestor `seccion(titulo)` que imprima `--- titulo ---` al entrar y `--- fin ---` al salir.

7. Usa un único `with` para abrir un fichero de texto en modo lectura y otro en modo escritura a la vez (puedes crear primero el de lectura).

8. Crea un context manager con `@contextmanager` que abra un fichero, lo entregue con `yield` y se asegure de cerrarlo al final (reimplementa, de forma sencilla, lo que hace `open`).

> [!NOTE]
> Pistas para los ejercicios:
> - Con clase necesitas los métodos `__enter__(self)` y `__exit__(self, tipo, valor, traza)`.
> - Lo que devuelvas en `__enter__` (o tras el `yield`) es lo que recibe el `as`.
> - Para que `__exit__` "trague" un error, haz que devuelva `True`.
> - Con `contextlib`: importa `from contextlib import contextmanager` y usa `yield` para separar el antes del después.
> - Para medir tiempo, recuerda `import time` y `time.time()`.

<h3 align = "center">
¡Ya sabes gestionar recursos como es debido! Mañana damos un gran salto: guardar datos de verdad en una base de datos con SQLite.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/24_Itertools/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/26_SQLite/readme.md">Día siguiente</a>
</h4>
