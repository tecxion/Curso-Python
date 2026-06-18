<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/30_NumPy/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/32_Analisis_Datos/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/pandas.png">
</h1>


<h1 align="center">Pandas: trabajar con datos</h1><br>

<h3>Índice</h3>

- [1. ¿Qué es Pandas?](#1-qué-es-pandas)
- [2. Series: la columna](#2-series-la-columna)
- [3. DataFrame: la tabla](#3-dataframe-la-tabla)
- [4. Explorar un DataFrame](#4-explorar-un-dataframe)
- [5. Seleccionar columnas y filas](#5-seleccionar-columnas-y-filas)
- [6. Filtrar con condiciones](#6-filtrar-con-condiciones)
- [7. Crear y modificar columnas](#7-crear-y-modificar-columnas)
- [8. Leer y escribir CSV](#8-leer-y-escribir-csv)
- [9. Ejercicios](#9-ejercicios)

<a name = "1-qué-es-pandas"></a>

## 1. ¿Qué es Pandas?

**Pandas** es la librería más usada para **analizar y manipular datos** en Python. Si NumPy (día 30) es el motor numérico, Pandas es la herramienta cómoda que pone encima: trabaja con **tablas** (como una hoja de Excel) y permite filtrar, agrupar, ordenar y resumir datos con muy poco código.

Tiene dos estructuras principales:
- **Series**: una columna de datos con etiquetas.
- **DataFrame**: una tabla completa (varias columnas).

```bash
pip install pandas
```

```python
import pandas as pd    # alias universal
```

<a name = "2-series-la-columna"></a>

## 2. Series: la columna

Una **Series** es como una lista con "etiquetas" (un índice) para cada valor:

```python
import pandas as pd

notas = pd.Series([8, 6, 9, 7], index=["Ana", "Luis", "Marta", "Pedro"])
print(notas)
# Ana      8
# Luis     6
# Marta    9
# Pedro    7

print(notas["Marta"])    # 9   -> acceso por etiqueta
print(notas.mean())      # 7.5 -> hereda lo estadístico de NumPy
```

<a name = "3-dataframe-la-tabla"></a>

## 3. DataFrame: la tabla

El **DataFrame** es la estrella de Pandas: una tabla con filas y columnas. La forma más común de crearlo es a partir de un **diccionario** (día 7), donde cada clave es una columna:

```python
import pandas as pd

datos = {
    "nombre": ["Ana", "Luis", "Marta", "Pedro"],
    "edad": [25, 30, 22, 35],
    "ciudad": ["Madrid", "Sevilla", "Madrid", "Bilbao"]
}

df = pd.DataFrame(datos)
print(df)
#   nombre  edad   ciudad
# 0    Ana    25   Madrid
# 1   Luis    30  Sevilla
# 2  Marta    22   Madrid
# 3  Pedro    35   Bilbao
```

<a name = "4-explorar-un-dataframe"></a>

## 4. Explorar un DataFrame

Lo primero al recibir unos datos es **echarles un vistazo**. Estos métodos son tus mejores amigos:

```python
df.head()        # las primeras 5 filas
df.tail(3)       # las últimas 3 filas
df.shape         # (filas, columnas)
df.columns       # nombres de las columnas
df.info()        # resumen: tipos y valores nulos
df.describe()    # estadísticas de las columnas numéricas
```

`describe()` es especialmente útil: te da de golpe la media, el mínimo, el máximo y los percentiles de cada columna numérica.

<a name = "5-seleccionar-columnas-y-filas"></a>

## 5. Seleccionar columnas y filas

```python
import pandas as pd
df = pd.DataFrame({
    "nombre": ["Ana", "Luis", "Marta"],
    "edad": [25, 30, 22]
})

# Una columna (devuelve una Series)
print(df["nombre"])

# Varias columnas (lista de nombres)
print(df[["nombre", "edad"]])

# Filas por POSICIÓN con iloc
print(df.iloc[0])      # primera fila

# Filas por ETIQUETA de índice con loc
print(df.loc[0])       # fila con índice 0
```

>[!NOTE]
>Recuerda la diferencia: **`iloc`** selecciona por posición numérica (como en las listas) y **`loc`** por la etiqueta del índice. Con índices por defecto (0, 1, 2…) coinciden, pero no siempre es así.

<a name = "6-filtrar-con-condiciones"></a>

## 6. Filtrar con condiciones

Igual que las máscaras booleanas de NumPy, pero sobre la tabla. Es lo que más vas a usar:

```python
import pandas as pd
df = pd.DataFrame({
    "nombre": ["Ana", "Luis", "Marta", "Pedro"],
    "edad": [25, 30, 22, 35],
    "ciudad": ["Madrid", "Sevilla", "Madrid", "Bilbao"]
})

# Mayores de 25
print(df[df["edad"] > 25])

# Los de Madrid
print(df[df["ciudad"] == "Madrid"])

# Combinando condiciones (& es "y", | es "o"). ¡Cada condición entre paréntesis!
print(df[(df["edad"] > 23) & (df["ciudad"] == "Madrid")])
```

<a name = "7-crear-y-modificar-columnas"></a>

## 7. Crear y modificar columnas

Crear una columna nueva es tan fácil como asignarla:

```python
import pandas as pd
df = pd.DataFrame({
    "producto": ["Camiseta", "Pantalón", "Zapatos"],
    "precio": [20, 40, 60],
    "cantidad": [3, 2, 1]
})

# Columna nueva calculada a partir de otras
df["total"] = df["precio"] * df["cantidad"]
print(df)

# Ordenar por una columna
print(df.sort_values("total", ascending=False))
```

<a name = "8-leer-y-escribir-csv"></a>

## 8. Leer y escribir CSV

Aquí Pandas brilla: leer un fichero de datos es **una línea**. Esto conecta con lo que viste de CSV en el día 17, pero infinitamente más cómodo:

```python
import pandas as pd

# Leer un CSV a un DataFrame
df = pd.read_csv("ventas.csv")

# Guardar un DataFrame en un CSV (index=False evita una columna extra)
df.to_csv("resultado.csv", index=False)
```

Pandas también lee Excel (`read_excel`), JSON (`read_json`) y muchos formatos más. Por eso es la puerta de entrada a casi cualquier análisis de datos.

<a name = "9-ejercicios"></a>

## 9. Ejercicios

Trabaja con este DataFrame de partida (créalo al principio de tus ejercicios):

```python
import pandas as pd
df = pd.DataFrame({
    "nombre": ["Ana", "Luis", "Marta", "Pedro", "Sara"],
    "edad": [25, 30, 22, 35, 28],
    "ciudad": ["Madrid", "Sevilla", "Madrid", "Bilbao", "Sevilla"],
    "salario": [1800, 2200, 1500, 2800, 2000]
})
```

### Nivel 1 — Básico
1. Muestra las primeras 3 filas del DataFrame.
2. Muestra la forma (`shape`) y los nombres de las columnas.
3. Muestra solo la columna `nombre`.
4. Calcula la media de la columna `salario`.

### Nivel 2 — Aplicado
5. Filtra y muestra las personas mayores de 25 años.
6. Muestra solo las personas que viven en Madrid.
7. Crea una columna nueva `salario_anual` que sea el salario por 14 pagas.
8. Ordena el DataFrame por salario de mayor a menor.

### Nivel 3 — Reto
9. Muestra las personas de Sevilla **con** salario mayor de 1900 (dos condiciones combinadas).
10. Calcula el salario medio **por ciudad** (pista: `df.groupby("ciudad")["salario"].mean()`).
11. Guarda en un CSV llamado `empleados.csv` solo las columnas `nombre` y `salario`, y vuelve a leerlo para comprobar que se guardó bien.

> [!NOTE]
> Pistas:
> - `import pandas as pd` al principio.
> - Para filtrar: `df[df["columna"] > valor]`.
> - Combinar condiciones: `df[(cond1) & (cond2)]`, cada una entre paréntesis.
> - `groupby` agrupa filas que comparten valor y luego aplicas una operación (`.mean()`, `.sum()`...).
> - Al guardar usa `df.to_csv("archivo.csv", index=False)`.

<h3 align = "center">
¡Ya sabes manejar tablas de datos! Mañana las exprimimos: limpieza, agrupaciones y estadística para sacar conclusiones de datos reales.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/30_NumPy/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/32_Analisis_Datos/readme.md">Día siguiente</a>
</h4>
