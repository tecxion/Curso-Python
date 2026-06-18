<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/31_Pandas/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/33_Visualizacion/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/analisis_datos.png">
</h1>


<h1 align="center">Análisis de Datos</h1><br>

<h3>Índice</h3>

- [1. ¿Qué es analizar datos?](#1-qué-es-analizar-datos)
- [2. Detectar valores nulos](#2-detectar-valores-nulos)
- [3. Limpiar datos](#3-limpiar-datos)
- [4. Estadística descriptiva](#4-estadística-descriptiva)
- [5. Agrupar con groupby](#5-agrupar-con-groupby)
- [6. Tablas dinámicas y conteos](#6-tablas-dinámicas-y-conteos)
- [7. Aplicar funciones con apply](#7-aplicar-funciones-con-apply)
- [8. Un mini-análisis completo](#8-un-mini-análisis-completo)
- [9. Ejercicios](#9-ejercicios)

<a name = "1-qué-es-analizar-datos"></a>

## 1. ¿Qué es analizar datos?

**Analizar datos** es el proceso de coger un montón de datos en bruto y sacarles **conclusiones**: medias, tendencias, grupos, valores raros… En el mundo real los datos llegan **sucios** (con huecos, errores, duplicados), así que primero hay que **limpiarlos** y luego **resumirlos**.

Hoy juntamos Pandas (día 31) con la estadística para hacer un análisis de principio a fin. El flujo típico es:

1. **Cargar** los datos.
2. **Limpiarlos** (nulos, duplicados, tipos).
3. **Explorar y resumir** (estadística, agrupaciones).
4. **Sacar conclusiones**.

<a name = "2-detectar-valores-nulos"></a>

## 2. Detectar valores nulos

Los **valores nulos** (huecos, `NaN`) son lo primero que hay que vigilar. Pandas los detecta así:

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "nombre": ["Ana", "Luis", "Marta", "Pedro"],
    "edad": [25, np.nan, 22, 35],
    "ciudad": ["Madrid", "Sevilla", None, "Bilbao"]
})

print(df.isnull())            # tabla de True/False
print(df.isnull().sum())      # cuántos nulos por columna
```

<a name = "3-limpiar-datos"></a>

## 3. Limpiar datos

Las dos estrategias básicas con los nulos: **eliminarlos** o **rellenarlos**:

```python
# Eliminar filas que tengan algún nulo
df_limpio = df.dropna()

# Rellenar los nulos con un valor
df["edad"] = df["edad"].fillna(df["edad"].mean())   # rellena con la media
df["ciudad"] = df["ciudad"].fillna("Desconocida")

# Eliminar filas duplicadas
df = df.drop_duplicates()
```

>[!IMPORTANT]
>No hay una regla universal: a veces conviene eliminar las filas con nulos y a veces rellenarlas. Depende de cuántas sean y de qué representen. Pensar esto es parte del trabajo de analista.

<a name = "4-estadística-descriptiva"></a>

## 4. Estadística descriptiva

La **estadística descriptiva** resume los datos con unos pocos números. Pandas los da casi todos hechos:

```python
import pandas as pd
df = pd.DataFrame({"salario": [1800, 2200, 1500, 2800, 2000, 1900]})

print(df["salario"].mean())      # media
print(df["salario"].median())    # mediana (valor central)
print(df["salario"].std())       # desviación estándar (cuánto varían)
print(df["salario"].max())       # máximo
print(df["salario"].min())       # mínimo
print(df["salario"].describe())  # ¡todo de golpe!
```

- La **media** se ve afectada por valores extremos; la **mediana** no.
- La **desviación estándar** mide cómo de dispersos están los datos respecto a la media.

<a name = "5-agrupar-con-groupby"></a>

## 5. Agrupar con groupby

**`groupby`** es la herramienta más potente del análisis: agrupa las filas que comparten un valor y aplica un cálculo a cada grupo. Es responder preguntas del tipo *"¿cuál es la media POR categoría?"*.

```python
import pandas as pd
df = pd.DataFrame({
    "departamento": ["Ventas", "IT", "Ventas", "IT", "RRHH"],
    "salario": [1800, 2500, 2000, 2700, 1900]
})

# Salario medio por departamento
print(df.groupby("departamento")["salario"].mean())

# Varias operaciones a la vez
print(df.groupby("departamento")["salario"].agg(["mean", "max", "count"]))
```

<a name = "6-tablas-dinámicas-y-conteos"></a>

## 6. Tablas dinámicas y conteos

```python
import pandas as pd
df = pd.DataFrame({
    "ciudad": ["Madrid", "Madrid", "Sevilla", "Bilbao", "Madrid"]
})

# Contar cuántas veces aparece cada valor
print(df["ciudad"].value_counts())
# Madrid     3
# Sevilla    1
# Bilbao     1

# Valores únicos
print(df["ciudad"].unique())   # ['Madrid' 'Sevilla' 'Bilbao']
print(df["ciudad"].nunique())  # 3
```

<a name = "7-aplicar-funciones-con-apply"></a>

## 7. Aplicar funciones con apply

Con **`apply`** aplicamos nuestra propia función a cada valor de una columna. Aquí se nota todo lo que aprendiste de funciones (día 10) y lambdas (día 13):

```python
import pandas as pd
df = pd.DataFrame({"nombre": ["ana", "luis", "marta"], "edad": [25, 17, 30]})

# Poner los nombres con la inicial en mayúscula
df["nombre"] = df["nombre"].apply(lambda x: x.capitalize())

# Crear una columna a partir de una condición
df["mayor_edad"] = df["edad"].apply(lambda x: "Sí" if x >= 18 else "No")
print(df)
```

<a name = "8-un-mini-análisis-completo"></a>

## 8. Un mini-análisis completo

Juntémoslo todo en un análisis de ventas de principio a fin:

```python
import pandas as pd

ventas = pd.DataFrame({
    "producto": ["Camiseta", "Pantalón", "Camiseta", "Zapatos", "Pantalón"],
    "categoria": ["Ropa", "Ropa", "Ropa", "Calzado", "Ropa"],
    "precio": [20, 40, 20, 60, 40],
    "unidades": [3, 1, 5, 2, 2]
})

# 1. Columna con el ingreso de cada venta
ventas["ingreso"] = ventas["precio"] * ventas["unidades"]

# 2. Ingreso total
print(f"Ingreso total: {ventas['ingreso'].sum()}€")

# 3. Ingreso por categoría
print(ventas.groupby("categoria")["ingreso"].sum())

# 4. Producto más vendido (por unidades)
top = ventas.groupby("producto")["unidades"].sum().idxmax()
print(f"Producto más vendido: {top}")
```

<a name = "9-ejercicios"></a>

## 9. Ejercicios

Parte de este DataFrame de empleados (algunos datos están sucios a propósito):

```python
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "nombre": ["Ana", "Luis", "Marta", "Pedro", "Sara", "Juan"],
    "departamento": ["IT", "Ventas", "IT", "Ventas", "RRHH", "IT"],
    "edad": [25, 30, np.nan, 35, 28, 41],
    "salario": [2500, 1800, 2700, 2000, 1900, np.nan]
})
```

### Nivel 1 — Básico
1. Cuenta cuántos valores nulos hay en cada columna.
2. Rellena los nulos de `edad` con la media de la edad.
3. Rellena los nulos de `salario` con la mediana del salario.
4. Muestra las estadísticas descriptivas (`describe`) de la columna `salario`.

### Nivel 2 — Aplicado
5. Calcula el salario medio por departamento.
6. Cuenta cuántos empleados hay en cada departamento (`value_counts`).
7. Crea una columna `categoria_edad` que ponga "joven" si la edad es menor de 30 y "senior" si no (usa `apply`).
8. ¿Cuál es el departamento con el salario medio más alto?

### Nivel 3 — Reto
9. Para cada departamento, muestra a la vez la media, el máximo y el número de empleados del salario (usa `agg`).
10. Crea una columna `salario_subido` que aumente un 10% el salario solo de los empleados de IT (el resto igual).
11. Haz un mini-informe que imprima: total de empleados, salario medio global, y el nombre del empleado mejor pagado.

> [!NOTE]
> Pistas:
> - Nulos: `df.isnull().sum()`; rellenar: `df["col"].fillna(valor)`.
> - Media y mediana: `.mean()` y `.median()`.
> - Agrupar: `df.groupby("col")["otra"].mean()`.
> - `apply(lambda x: ...)` transforma cada valor de una columna.
> - El nombre del mejor pagado: `df.loc[df["salario"].idxmax(), "nombre"]`.

<h3 align = "center">
¡Ya sabes sacar conclusiones de los datos! Pero un número solo no convence: mañana aprenderemos a contar la historia con gráficos.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/31_Pandas/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/33_Visualizacion/readme.md">Día siguiente</a>
</h4>
