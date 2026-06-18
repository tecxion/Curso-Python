<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/19_Entornos_Virtuales/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/21_Regex/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/fechas.png">
</h1>


<h1 align="center">Fechas y Tiempo (datetime)</h1><br>

<h3>Índice</h3>

- [1. El módulo datetime](#1-el-módulo-datetime)
- [2. La fecha y hora actual](#2-la-fecha-y-hora-actual)
- [3. Crear fechas concretas](#3-crear-fechas-concretas)
- [4. Acceder a las partes de una fecha](#4-acceder-a-las-partes-de-una-fecha)
- [5. Formatear fechas con strftime](#5-formatear-fechas-con-strftime)
- [6. De texto a fecha con strptime](#6-de-texto-a-fecha-con-strptime)
- [7. Operar con fechas: timedelta](#7-operar-con-fechas-timedelta)
- [8. El módulo time](#8-el-módulo-time)
- [9. Ejercicios](#9-ejercicios)

<a name = "1-el-módulo-datetime"></a>

## 1. El módulo datetime

Tarde o temprano todo programa necesita trabajar con **fechas y horas**: la fecha de creación de una tarea, calcular cuántos días faltan para un evento, registrar cuándo ocurrió algo… Python trae el módulo **`datetime`** (incluido en la librería estándar) justo para eso.

Dentro de `datetime` hay varias clases. Las que más usaremos:

| Clase | Para qué sirve |
| ------------ | ------------------------------------------ |
| `date` | Solo fecha (año, mes, día) |
| `time` | Solo hora (hora, minutos, segundos) |
| `datetime` | Fecha **y** hora juntas |
| `timedelta` | Una **duración** (para sumar/restar tiempo) |

```python
from datetime import date, time, datetime, timedelta
```

<a name = "2-la-fecha-y-hora-actual"></a>

## 2. La fecha y hora actual

Lo más habitual es preguntar "¿qué día/hora es ahora?":

```python
from datetime import date, datetime

hoy = date.today()
print(hoy)            # 2025-03-18  (año-mes-día)

ahora = datetime.now()
print(ahora)          # 2025-03-18 17:42:09.123456
```

<a name = "3-crear-fechas-concretas"></a>

## 3. Crear fechas concretas

También podemos construir una fecha u hora exacta pasando sus valores. El orden es **año, mes, día** (y luego hora, minuto, segundo):

```python
from datetime import date, datetime

cumple = date(2000, 5, 17)
print(cumple)                      # 2000-05-17

evento = datetime(2025, 12, 31, 23, 59, 0)
print(evento)                      # 2025-12-31 23:59:00
```

<a name = "4-acceder-a-las-partes-de-una-fecha"></a>

## 4. Acceder a las partes de una fecha

Cada fecha guarda sus partes como atributos a los que accedemos con el punto:

```python
from datetime import datetime

ahora = datetime.now()
print(ahora.year)     # 2025
print(ahora.month)    # 3
print(ahora.day)      # 18
print(ahora.hour)     # 17
print(ahora.minute)   # 42

# weekday() devuelve el día de la semana: 0 = lunes ... 6 = domingo
print(ahora.weekday())  # 1  (martes)
```

<a name = "5-formatear-fechas-con-strftime"></a>

## 5. Formatear fechas con strftime

Por defecto las fechas se imprimen en formato `año-mes-día`, que no siempre es lo que queremos. Con el método **`strftime()`** ("string from time") convertimos una fecha en **texto con el formato que elijamos**, usando códigos especiales:

| Código | Significado | Ejemplo |
| ------ | ------------------ | ------- |
| `%d` | Día (2 dígitos) | 18 |
| `%m` | Mes (2 dígitos) | 03 |
| `%Y` | Año (4 dígitos) | 2025 |
| `%H` | Hora (24h) | 17 |
| `%M` | Minutos | 42 |
| `%A` | Día de la semana | Tuesday |
| `%B` | Nombre del mes | March |

```python
from datetime import datetime

ahora = datetime.now()

print(ahora.strftime("%d/%m/%Y"))          # 18/03/2025
print(ahora.strftime("%H:%M"))             # 17:42
print(ahora.strftime("%d de %B de %Y"))    # 18 de March de 2025
```

>[!NOTE]
>Los nombres de mes y día (`%A`, `%B`) salen en inglés por defecto porque dependen del idioma del sistema. Para que salgan en español hay que configurar el `locale`, algo que de momento puedes dejar para más adelante.

<a name = "6-de-texto-a-fecha-con-strptime"></a>

## 6. De texto a fecha con strptime

Es la operación inversa: convertir un **texto** en un objeto fecha con el que poder operar. Usamos **`strptime()`** ("string parse time") y le indicamos en qué formato viene el texto:

```python
from datetime import datetime

texto = "25/12/2025"
fecha = datetime.strptime(texto, "%d/%m/%Y")
print(fecha)        # 2025-12-25 00:00:00
print(fecha.year)   # 2025  (ya es una fecha de verdad)
```

Esto es muy útil cuando leemos fechas de un fichero o de lo que escribe el usuario por teclado: llegan como texto y necesitamos convertirlas.

<a name = "7-operar-con-fechas-timedelta"></a>

## 7. Operar con fechas: timedelta

Un **`timedelta`** representa una **duración** (días, horas, etc.). Sumándolo o restándolo a una fecha obtenemos otra fecha. Y si **restamos dos fechas**, obtenemos el `timedelta` que las separa:

```python
from datetime import date, timedelta

hoy = date.today()

# ¿Qué día será dentro de 10 días?
dentro_de_10 = hoy + timedelta(days=10)
print(dentro_de_10)

# ¿Qué día fue hace una semana?
hace_una_semana = hoy - timedelta(weeks=1)
print(hace_una_semana)

# ¿Cuántos días faltan para fin de año?
fin_de_año = date(hoy.year, 12, 31)
diferencia = fin_de_año - hoy
print(f"Faltan {diferencia.days} días para fin de año")
```

<a name = "8-el-módulo-time"></a>

## 8. El módulo time

Aparte de `datetime`, existe el módulo **`time`**, útil sobre todo para **pausar** el programa o **medir** cuánto tarda algo:

```python
import time

print("Empezamos...")
time.sleep(2)          # pausa el programa 2 segundos
print("...2 segundos después")

# Medir cuánto tarda un trozo de código
inicio = time.time()           # marca de tiempo en segundos
total = sum(range(1_000_000))
fin = time.time()
print(f"Tardó {fin - inicio:.4f} segundos")
```

>[!IMPORTANT]
>`time.sleep()` lo usamos en el día de decoradores (día 13) sin explicarlo a fondo. Ahora ya sabes qué hacía: pausar la ejecución los segundos que le indiques.

<a name = "9-ejercicios"></a>

## 9. Ejercicios

1. Muestra por pantalla la fecha y la hora actuales por separado (usa `date.today()` y `datetime.now()`).

2. Crea una fecha con tu cumpleaños y muestra en qué **día de la semana** caíste al nacer (`weekday()`).

3. Muestra la fecha de hoy con el formato `dd/mm/aaaa` y también con el formato `aaaa-mm-dd` usando `strftime`.

4. Pide al usuario una fecha en formato `dd/mm/aaaa`, conviértela con `strptime` y dile en qué año está.

5. Escribe una función `dias_hasta(fecha_texto)` que reciba una fecha futura como texto (`dd/mm/aaaa`) y devuelva cuántos días faltan desde hoy.

6. Calcula y muestra qué día será dentro de 100 días a partir de hoy.

7. Crea una función `edad(fecha_nacimiento)` que, dada una fecha de nacimiento, calcule cuántos años tiene la persona (pista: resta años y ajusta si aún no ha sido su cumpleaños este año).

8. Mide cuánto tarda tu ordenador en sumar todos los números del 0 al 10.000.000 usando el módulo `time`.

> [!NOTE]
> Pistas para los ejercicios:
> - Importa lo que necesites: `from datetime import date, datetime, timedelta`.
> - `strftime` = de fecha A texto. `strptime` = de texto A fecha. No los confundas.
> - Para sumar/restar tiempo usa `timedelta(days=...)`.
> - Al restar dos fechas obtienes un `timedelta`; su atributo `.days` te da los días.
> - Para la edad: `hoy.year - nacimiento.year` y resta 1 si `(hoy.month, hoy.day) < (nacimiento.month, nacimiento.day)`.

<h3 align = "center">
¡Ya controlas el tiempo en tus programas! Mañana, una herramienta potentísima para buscar patrones en texto: las expresiones regulares.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/19_Entornos_Virtuales/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/21_Regex/readme.md">Día siguiente</a>
</h4>
