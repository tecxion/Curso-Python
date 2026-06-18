<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/32_Analisis_Datos/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/34_Web_Scraping/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/visualizacion.png">
</h1>


<h1 align="center">Visualización de Datos (Matplotlib)</h1><br>

<h3>Índice</h3>

- [1. ¿Por qué visualizar?](#1-por-qué-visualizar)
- [2. Matplotlib y pyplot](#2-matplotlib-y-pyplot)
- [3. Tu primer gráfico de líneas](#3-tu-primer-gráfico-de-líneas)
- [4. Personalizar un gráfico](#4-personalizar-un-gráfico)
- [5. Tipos de gráficos](#5-tipos-de-gráficos)
- [6. Guardar el gráfico en una imagen](#6-guardar-el-gráfico-en-una-imagen)
- [7. Graficar directamente desde Pandas](#7-graficar-directamente-desde-pandas)
- [8. Ejercicios](#8-ejercicios)

<a name = "1-por-qué-visualizar"></a>

## 1. ¿Por qué visualizar?

Un dato es frío; un **gráfico** cuenta una historia de un vistazo. La **visualización de datos** convierte tablas de números en imágenes que muestran tendencias, comparaciones y valores raros que en una tabla pasarían desapercibidos.

Cierra el bloque de datos: ya sabes obtener (Pandas) y analizar (día 32) datos; hoy aprendes a **comunicarlos**.

<a name = "2-matplotlib-y-pyplot"></a>

## 2. Matplotlib y pyplot

**Matplotlib** es la librería de gráficos más usada de Python. Casi siempre se trabaja con su submódulo `pyplot`, que por convención se importa como `plt`:

```bash
pip install matplotlib
```

```python
import matplotlib.pyplot as plt
```

<a name = "3-tu-primer-gráfico-de-líneas"></a>

## 3. Tu primer gráfico de líneas

El flujo básico siempre es el mismo: preparas los datos, llamas a una función de dibujo y muestras (o guardas) el resultado.

```python
import matplotlib.pyplot as plt

meses = ["Ene", "Feb", "Mar", "Abr", "May"]
ventas = [100, 120, 90, 150, 200]

plt.plot(meses, ventas)     # dibuja una línea
plt.show()                  # muestra el gráfico en una ventana
```

>[!NOTE]
>`plt.show()` abre una ventana con el gráfico. Si ejecutas desde un script normal en la terminal, la ventana aparece y el programa espera a que la cierres. Más abajo verás cómo **guardarlo como imagen** en su lugar, que suele ser más práctico.

<a name = "4-personalizar-un-gráfico"></a>

## 4. Personalizar un gráfico

Un gráfico sin títulos ni etiquetas no comunica. Estos son los retoques imprescindibles:

```python
import matplotlib.pyplot as plt

meses = ["Ene", "Feb", "Mar", "Abr", "May"]
ventas = [100, 120, 90, 150, 200]

plt.plot(meses, ventas, color="green", marker="o", linestyle="--")
plt.title("Ventas por mes")        # título
plt.xlabel("Mes")                  # etiqueta del eje X
plt.ylabel("Ventas (€)")           # etiqueta del eje Y
plt.grid(True)                     # rejilla de fondo
plt.show()
```

<a name = "5-tipos-de-gráficos"></a>

## 5. Tipos de gráficos

Cada tipo de gráfico sirve para una cosa. Estos son los más usados:

```python
import matplotlib.pyplot as plt

categorias = ["A", "B", "C"]
valores = [30, 50, 20]

# Gráfico de BARRAS (comparar categorías)
plt.bar(categorias, valores)
plt.show()

# Gráfico de TARTA (proporciones de un total)
plt.pie(valores, labels=categorias, autopct="%1.1f%%")
plt.show()

# HISTOGRAMA (distribución de muchos datos)
import numpy as np
datos = np.random.randn(1000)   # 1000 números aleatorios
plt.hist(datos, bins=20)
plt.show()

# DISPERSIÓN (relación entre dos variables)
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 6]
plt.scatter(x, y)
plt.show()
```

| Gráfico | Para qué |
| ------------- | ----------------------------------- |
| Líneas (`plot`) | Evolución a lo largo del tiempo |
| Barras (`bar`) | Comparar categorías |
| Tarta (`pie`) | Proporciones de un total |
| Histograma (`hist`) | Distribución de datos |
| Dispersión (`scatter`) | Relación entre dos variables |

<a name = "6-guardar-el-gráfico-en-una-imagen"></a>

## 6. Guardar el gráfico en una imagen

En lugar de (o además de) mostrarlo, casi siempre querrás **guardar** el gráfico como un archivo PNG para usarlo en un informe:

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Mi gráfico")
plt.savefig("grafico.png")      # guarda la imagen en disco
plt.close()                     # cierra la figura para liberar memoria
```

>[!IMPORTANT]
>Llama a `savefig()` **antes** de `show()` (o en lugar de él). Si haces `show()` primero, la figura se vacía y el archivo saldría en blanco.

<a name = "7-graficar-directamente-desde-pandas"></a>

## 7. Graficar directamente desde Pandas

Lo mejor: Pandas (día 31) lleva Matplotlib integrado. Puedes graficar un DataFrame con `.plot()` directamente:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "mes": ["Ene", "Feb", "Mar", "Abr"],
    "ventas": [100, 120, 90, 150]
})

df.plot(x="mes", y="ventas", kind="bar")
plt.title("Ventas mensuales")
plt.savefig("ventas.png")
```

Así enlazas todo el bloque de datos: cargas con Pandas, analizas con groupby y visualizas con un `.plot()`.

<a name = "8-ejercicios"></a>

## 8. Ejercicios

> Para estos ejercicios, **guarda** cada gráfico con `plt.savefig("nombre.png")` en lugar de `plt.show()`: así podrás abrir las imágenes y comprobarlas, y los ejercicios funcionan aunque ejecutes desde la terminal.

### Nivel 1 — Básico
1. Dibuja un gráfico de líneas con los días de la semana en el eje X y las horas que estudiaste cada día en el eje Y. Guárdalo como `estudio.png`.
2. Añade título y etiquetas a los ejes del gráfico anterior.
3. Crea un gráfico de barras con tres productos y sus ventas.
4. Crea un gráfico de tarta con el reparto de tu tiempo en un día (dormir, estudiar, ocio, otros).

### Nivel 2 — Aplicado
5. Dibuja dos líneas en el mismo gráfico (ventas de dos años) y añade una leyenda con `plt.legend()`.
6. Crea un histograma de 1000 números aleatorios generados con NumPy.
7. Cambia el color, el grosor de línea y añade marcadores a un gráfico de líneas.
8. Crea un gráfico de dispersión que relacione horas de estudio con nota obtenida.

### Nivel 3 — Reto
9. A partir de un DataFrame de ventas por categoría, agrúpalo con `groupby` y dibuja un gráfico de barras con el total por categoría.
10. Crea una figura con **dos gráficos** uno al lado del otro usando `plt.subplots(1, 2)` (por ejemplo, barras y tarta de los mismos datos).
11. Carga unos datos en un DataFrame, calcula la media por grupo y genera un gráfico con título, etiquetas y leyenda, y guárdalo en alta calidad (`dpi=150`).

> [!NOTE]
> Pistas:
> - `import matplotlib.pyplot as plt` al principio.
> - Para varias líneas, llama a `plt.plot(...)` varias veces antes de guardar.
> - La leyenda necesita que cada `plot` lleve `label="..."` y luego llamar a `plt.legend()`.
> - Para dos gráficos: `fig, (ax1, ax2) = plt.subplots(1, 2)` y dibuja con `ax1.bar(...)`, `ax2.pie(...)`.
> - Guarda siempre con `plt.savefig("archivo.png")` y luego `plt.close()`.

<h3 align = "center">
¡Ya cuentas historias con datos! Cerramos el bloque de datos y abrimos el de la web: mañana, cómo extraer información de páginas con web scraping.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/32_Analisis_Datos/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/34_Web_Scraping/readme.md">Día siguiente</a>
</h4>
