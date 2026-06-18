<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/27_APIs/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/29_Tests/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/logging.png">
</h1>


<h1 align="center">Logging y Depuración</h1><br>

<h3>Índice</h3>

- [1. ¿Por qué no usar siempre print?](#1-por-qué-no-usar-siempre-print)
- [2. El módulo logging](#2-el-módulo-logging)
- [3. Los niveles de logging](#3-los-niveles-de-logging)
- [4. Configurar el formato](#4-configurar-el-formato)
- [5. Guardar los logs en un fichero](#5-guardar-los-logs-en-un-fichero)
- [6. Registrar excepciones](#6-registrar-excepciones)
- [7. Depurar: print, logging y el debugger](#7-depurar-print-logging-y-el-debugger)
- [8. Ejercicios](#8-ejercicios)

<a name = "1-por-qué-no-usar-siempre-print"></a>

## 1. ¿Por qué no usar siempre print?

Durante todo el curso hemos usado `print()` para ver qué pasa en nuestros programas. Está bien para aprender, pero tiene problemas en proyectos serios:

- No distingue entre un mensaje informativo y un error grave.
- Hay que borrarlos a mano antes de entregar el programa.
- No guardan ninguna información de **cuándo** ocurrió cada cosa.

El **logging** (registro de eventos) resuelve todo esto. Es la forma profesional de que un programa cuente lo que está haciendo, y se puede **activar o silenciar** sin tocar el código.

<a name = "2-el-módulo-logging"></a>

## 2. El módulo logging

Python trae el módulo **`logging`** en su librería estándar:

```python
import logging

logging.warning("Esto es un aviso")
logging.error("Esto es un error")
```

```
WARNING:root:Esto es un aviso
ERROR:root:Esto es un error
```

A diferencia de `print`, cada mensaje lleva su **nivel de importancia** (WARNING, ERROR…), lo que nos permite filtrarlos.

<a name = "3-los-niveles-de-logging"></a>

## 3. Los niveles de logging

Hay cinco niveles, de menor a mayor gravedad. Sirven para clasificar cada mensaje:

| Nivel | Cuándo usarlo |
| ---------- | ------------------------------------------------- |
| `DEBUG` | Detalles para depurar (solo durante el desarrollo) |
| `INFO` | Información de que todo va según lo previsto |
| `WARNING` | Algo inesperado, pero el programa sigue |
| `ERROR` | Un problema que impidió hacer algo |
| `CRITICAL` | Un error grave que puede tumbar el programa |

```python
import logging

logging.debug("Mensaje de depuración")
logging.info("Mensaje informativo")
logging.warning("Mensaje de aviso")
logging.error("Mensaje de error")
logging.critical("Mensaje crítico")
```

>[!IMPORTANT]
>Por defecto, `logging` solo muestra los mensajes de nivel **WARNING o superior**. Por eso, en el ejemplo de arriba, `debug` e `info` NO aparecerían hasta que bajemos el nivel mínimo (lo vemos en la siguiente sección).

<a name = "4-configurar-el-formato"></a>

## 4. Configurar el formato

Con `logging.basicConfig()` decidimos **qué nivel** mostrar y **con qué formato**. Podemos incluir la fecha, el nivel y el mensaje:

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,        # ahora se muestran TODOS los niveles
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("Empezando el programa")
logging.info("Usuario conectado")
logging.warning("Memoria al 80%")
```

```
2025-03-18 18:05:12,345 - DEBUG - Empezando el programa
2025-03-18 18:05:12,346 - INFO - Usuario conectado
2025-03-18 18:05:12,346 - WARNING - Memoria al 80%
```

- `%(asctime)s` → fecha y hora.
- `%(levelname)s` → el nivel (DEBUG, INFO…).
- `%(message)s` → tu mensaje.

<a name = "5-guardar-los-logs-en-un-fichero"></a>

## 5. Guardar los logs en un fichero

Lo más útil del logging: en vez de mostrarse en la consola (y perderse), los mensajes se pueden **guardar en un fichero** para revisarlos después. Solo hay que indicar `filename`:

```python
import logging

logging.basicConfig(
    filename="registro.log",      # los mensajes van a este fichero
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("La aplicación ha arrancado")
logging.warning("Algo a vigilar")
```

Ahora aparecerá un fichero `registro.log` con todo lo ocurrido y su hora exacta. Imprescindible para saber qué pasó cuando un programa falla mientras no estabas mirando.

<a name = "6-registrar-excepciones"></a>

## 6. Registrar excepciones

Combinando el logging con el manejo de errores del día 14, podemos registrar los errores **con todo su detalle**. El método `logging.exception()` (o `exc_info=True`) guarda incluso la traza completa del error:

```python
import logging

logging.basicConfig(level=logging.DEBUG)

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logging.exception("Se intentó dividir entre cero")
        return None

dividir(10, 0)
```

Esto deja registrado el error sin que el programa se rompa, y con toda la información para entender qué pasó.

<a name = "7-depurar-print-logging-y-el-debugger"></a>

## 7. Depurar: print, logging y el debugger

**Depurar** (*debugging*) es buscar y arreglar errores. Tienes tres herramientas, de menos a más potente:

- **`print()`**: rápido para una comprobación puntual. Acuérdate de borrarlos luego.
- **`logging.debug()`**: como el print pero clasificado y silenciable sin borrar nada.
- **El depurador (debugger)**: en VS Code puedes poner un **punto de interrupción** (*breakpoint*) haciendo clic a la izquierda de un número de línea y ejecutar con la tecla `F5`. El programa se pausará ahí y podrás ver el valor de cada variable paso a paso. Es la forma más profesional de cazar errores escurridizos.

>[!NOTE]
>Python también tiene la función `breakpoint()`: si la escribes en una línea, el programa se detendrá ahí y te dará una consola para inspeccionar las variables. Pruébala.

<a name = "8-ejercicios"></a>

## 8. Ejercicios

1. Importa `logging` y emite un mensaje de cada uno de los cinco niveles (`debug`, `info`, `warning`, `error`, `critical`).

2. Configura el logging con `basicConfig` para que se muestren **todos** los niveles (nivel `DEBUG`).

3. Configura el formato para que cada mensaje incluya la fecha, el nivel y el texto.

4. Haz que los logs se guarden en un fichero llamado `mi_app.log` en lugar de en la consola.

5. Escribe una función `dividir(a, b)` que registre con `logging.error` (o `logging.exception`) si se intenta dividir entre cero.

6. Crea un pequeño programa que simule un inicio de sesión: registra con `info` cuando el login es correcto y con `warning` cuando falla.

7. Escribe una función que recorra una lista de números y registre con `warning` cada número negativo que encuentre.

8. Combina logging y manejo de errores: pide un número al usuario y registra un `error` si escribe algo que no es un número.

> [!NOTE]
> Pistas para los ejercicios:
> - Recuerda llamar a `logging.basicConfig(...)` al principio, antes de emitir mensajes.
> - Por defecto solo se ven WARNING o superior; baja a `level=logging.DEBUG` para verlos todos.
> - Para guardar en fichero usa el parámetro `filename="..."` en `basicConfig`.
> - `logging.exception("texto")` se usa DENTRO de un `except` y guarda la traza del error.
> - El formato útil es `"%(asctime)s - %(levelname)s - %(message)s"`.

<h3 align = "center">
¡Ya sabes dejar rastro de lo que hace tu código! Mañana, el último día de teoría antes del proyecto: aprenderemos a probar nuestro código con tests.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/27_APIs/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/29_Tests/readme.md">Día siguiente</a>
</h4>
