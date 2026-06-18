<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/26_SQLite/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/28_Logging/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/apis.png">
</h1>


<h1 align="center">Consumir APIs Web (requests)</h1><br>

<h3>Índice</h3>

- [1. ¿Qué es una API?](#1-qué-es-una-api)
- [2. La librería requests](#2-la-librería-requests)
- [3. Tu primera petición GET](#3-tu-primera-petición-get)
- [4. Códigos de estado](#4-códigos-de-estado)
- [5. Leer la respuesta JSON](#5-leer-la-respuesta-json)
- [6. Parámetros en la petición](#6-parámetros-en-la-petición)
- [7. Manejar errores de red](#7-manejar-errores-de-red)
- [8. Ejercicios](#8-ejercicios)

<a name = "1-qué-es-una-api"></a>

## 1. ¿Qué es una API?

Una **API** (*Application Programming Interface*) es una forma de que dos programas **se comuniquen** entre sí. Cuando hablamos de **APIs web**, nos referimos a servicios en internet a los que tu programa puede pedirle datos: el tiempo, la cotización de una moneda, información de películas, etc.

Funciona como un restaurante: tú (tu programa) haces un **pedido** a una dirección (URL), y el servidor te devuelve una **respuesta** con los datos, normalmente en formato **JSON** (el que aprendiste en el día 17).

Casi todas las apps que usas (el tiempo, mapas, redes sociales) consumen APIs por debajo. Aprender a usarlas abre un mundo enorme de posibilidades.

<a name = "2-la-librería-requests"></a>

## 2. La librería requests

Python puede hacer peticiones web con la librería estándar, pero es algo incómoda. La comunidad usa **`requests`**, una librería externa que lo hace sencilísimo. Como es externa, hay que instalarla (¡aquí se nota lo del día 19!):

```bash
# Con tu entorno virtual activado
pip install requests
```

Y luego se importa como cualquier módulo:

```python
import requests
```

>[!NOTE]
>Como `requests` es una dependencia externa, este es un buen momento para añadirla a tu `requirements.txt` con `pip freeze > requirements.txt`.

<a name = "3-tu-primera-petición-get"></a>

## 3. Tu primera petición GET

La operación más común es **GET**: pedir datos a una URL. Usaremos una API gratuita de pruebas, [JSONPlaceholder](https://jsonplaceholder.typicode.com), que devuelve datos de ejemplo.

```python
import requests

respuesta = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(respuesta.text)
# {
#   "userId": 1,
#   "id": 1,
#   "title": "delectus aut autem",
#   "completed": false
# }
```

`requests.get(url)` devuelve un objeto **respuesta** con toda la información de lo que nos contestó el servidor.

<a name = "4-códigos-de-estado"></a>

## 4. Códigos de estado

Cada respuesta trae un **código de estado** que indica si todo fue bien. Lo consultamos con `.status_code`:

| Código | Significado |
| ------ | ------------------------------------ |
| `200` | OK, todo correcto |
| `404` | No encontrado (la URL no existe) |
| `401` | No autorizado (falta una credencial) |
| `500` | Error del servidor |

```python
import requests

respuesta = requests.get("https://jsonplaceholder.typicode.com/todos/1")

if respuesta.status_code == 200:
    print("¡Petición correcta!")
else:
    print(f"Algo falló: {respuesta.status_code}")
```

<a name = "5-leer-la-respuesta-json"></a>

## 5. Leer la respuesta JSON

Lo más útil: el método **`.json()`** convierte la respuesta directamente en un **diccionario** (o lista) de Python, listo para usar:

```python
import requests

respuesta = requests.get("https://jsonplaceholder.typicode.com/users/1")
datos = respuesta.json()        # ¡ya es un diccionario!

print(datos["name"])            # Leanne Graham
print(datos["email"])           # Sincere@april.biz
print(datos["address"]["city"]) # Gwenborough
```

Fíjate cómo todo lo del curso encaja: la respuesta es un diccionario (día 7), con valores anidados a los que accedemos con claves.

<a name = "6-parámetros-en-la-petición"></a>

## 6. Parámetros en la petición

Muchas APIs aceptan **parámetros** para filtrar lo que pides. Se pasan con el argumento `params` y un diccionario, y `requests` los añade a la URL por ti:

```python
import requests

# Pedimos solo las tareas (todos) del usuario nº 1
respuesta = requests.get(
    "https://jsonplaceholder.typicode.com/todos",
    params={"userId": 1}
)

tareas = respuesta.json()       # una lista de diccionarios
print(f"El usuario 1 tiene {len(tareas)} tareas")

# ¿Cuántas ha completado? (comprensión de listas del día 18)
completadas = [t for t in tareas if t["completed"]]
print(f"Completadas: {len(completadas)}")
```

<a name = "7-manejar-errores-de-red"></a>

## 7. Manejar errores de red

Internet falla: no hay conexión, el servidor tarda, la URL no existe… Por eso, **siempre** que trabajes con APIs debes usar el manejo de errores del día 14. `requests` lanza excepciones que podemos capturar:

```python
import requests

try:
    respuesta = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=5)
    respuesta.raise_for_status()    # lanza error si el código no es 200
    datos = respuesta.json()
    print(datos["title"])
except requests.exceptions.ConnectionError:
    print("No hay conexión a internet.")
except requests.exceptions.Timeout:
    print("El servidor tardó demasiado.")
except requests.exceptions.HTTPError as error:
    print(f"Error en la respuesta: {error}")
```

- `timeout=5` evita que el programa se quede colgado esperando para siempre.
- `raise_for_status()` convierte un código de error (como 404) en una excepción que puedes capturar.

>[!IMPORTANT]
>Nunca confíes en que una petición web vaya a funcionar. Envuélvela siempre en `try/except`: es la diferencia entre un programa que se cuelga y uno robusto.

<a name = "8-ejercicios"></a>

## 8. Ejercicios

> Necesitas conexión a internet y haber instalado `requests` (`pip install requests`). Usaremos la API gratuita `https://jsonplaceholder.typicode.com`.

1. Haz una petición GET a `https://jsonplaceholder.typicode.com/todos/1` e imprime el código de estado.

2. De esa misma petición, convierte la respuesta a JSON e imprime el campo `title`.

3. Pide el usuario `https://jsonplaceholder.typicode.com/users/2` y muestra su nombre, email y ciudad.

4. Pide la lista completa de `https://jsonplaceholder.typicode.com/posts` e imprime cuántos posts hay (pista: `len()`).

5. Usando `params`, pide los posts del usuario con `userId=1` e imprime cuántos son.

6. Escribe una función `obtener_post(id)` que reciba un número, pida `.../posts/{id}` y devuelva su título. Controla el caso de que no exista (status 404).

7. Pide los `todos` del usuario 1 (con `params`) y cuenta cuántos ha completado (campo `completed`).

8. Envuelve una petición en un `try/except` completo que controle la falta de conexión y un `timeout` de 5 segundos.

> [!NOTE]
> Pistas para los ejercicios:
> - Instala antes con `pip install requests` (en tu entorno virtual).
> - `respuesta.json()` te da un diccionario o una lista directamente.
> - Para filtrar usa `params={"clave": valor}`.
> - Usa `respuesta.raise_for_status()` para detectar respuestas con error.
> - Pon siempre `timeout=5` y captura `requests.exceptions.ConnectionError` y `Timeout`.

<h3 align = "center">
¡Tu programa ya habla con internet! Mañana aprenderemos a dejar rastro de lo que hace nuestro código con el logging.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/26_SQLite/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/28_Logging/readme.md">Día siguiente</a>
</h4>
