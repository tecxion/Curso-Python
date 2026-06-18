<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/33_Visualizacion/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/35_Flask/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/web_scraping.png">
</h1>


<h1 align="center">Web Scraping</h1><br>

<h3>Índice</h3>

- [1. ¿Qué es el web scraping?](#1-qué-es-el-web-scraping)
- [2. Herramientas: requests y BeautifulSoup](#2-herramientas-requests-y-beautifulsoup)
- [3. Entender el HTML](#3-entender-el-html)
- [4. Buscar elementos: find y find_all](#4-buscar-elementos-find-y-find_all)
- [5. Extraer texto y atributos](#5-extraer-texto-y-atributos)
- [6. Buscar por clase y selectores CSS](#6-buscar-por-clase-y-selectores-css)
- [7. Scraping responsable y legal](#7-scraping-responsable-y-legal)
- [8. Ejercicios](#8-ejercicios)

<a name = "1-qué-es-el-web-scraping"></a>

## 1. ¿Qué es el web scraping?

El **web scraping** es la técnica de **extraer información de páginas web** de forma automática. Cuando una web no ofrece una API (día 27), el scraping nos permite "leer" su HTML y sacar los datos que nos interesan: precios, noticias, resultados, etc.

La idea es:
1. **Descargar** el HTML de la página (con `requests`).
2. **Analizarlo** para encontrar los datos (con `BeautifulSoup`).
3. **Extraer** lo que necesitamos.

Con esto empezamos el bloque de **desarrollo web** del curso.

<a name = "2-herramientas-requests-y-beautifulsoup"></a>

## 2. Herramientas: requests y BeautifulSoup

Usaremos dos librerías externas: **`requests`** (ya la conoces del día 27, para descargar) y **`BeautifulSoup`** (para analizar el HTML):

```bash
pip install requests beautifulsoup4
```

```python
import requests
from bs4 import BeautifulSoup

respuesta = requests.get("https://example.com")
sopa = BeautifulSoup(respuesta.text, "html.parser")
```

El objeto `sopa` ya tiene el HTML "masticado" y listo para buscar dentro de él.

<a name = "3-entender-el-html"></a>

## 3. Entender el HTML

Para extraer datos hay que entender un poco de **HTML**. Una página es un árbol de **etiquetas** (*tags*) anidadas:

```html
<html>
  <body>
    <h1>Título principal</h1>
    <p class="precio">19.99€</p>
    <a href="https://tienda.com">Comprar</a>
    <ul>
      <li>Producto 1</li>
      <li>Producto 2</li>
    </ul>
  </body>
</html>
```

- Cada etiqueta tiene un **nombre** (`h1`, `p`, `a`, `li`…).
- Puede tener **atributos** (`class="precio"`, `href="..."`).
- Y un **contenido** (el texto entre la apertura y el cierre).

>[!NOTE]
>En tu navegador, haz clic derecho sobre cualquier elemento de una web y elige "Inspeccionar". Verás el HTML real: es lo primero que hace todo el que va a hacer scraping, para saber qué etiquetas y clases buscar.

<a name = "4-buscar-elementos-find-y-find_all"></a>

## 4. Buscar elementos: find y find_all

Los dos métodos estrella de BeautifulSoup:
- **`find`**: devuelve el **primer** elemento que coincide.
- **`find_all`**: devuelve **todos** en una lista.

```python
from bs4 import BeautifulSoup

html = """
<html><body>
  <h1>Mi tienda</h1>
  <p>Producto 1</p>
  <p>Producto 2</p>
  <p>Producto 3</p>
</body></html>
"""
sopa = BeautifulSoup(html, "html.parser")

print(sopa.find("h1"))            # <h1>Mi tienda</h1>
print(sopa.find("p"))             # <p>Producto 1</p>  (solo el primero)

for parrafo in sopa.find_all("p"):
    print(parrafo)                # los tres <p>
```

<a name = "5-extraer-texto-y-atributos"></a>

## 5. Extraer texto y atributos

Normalmente no queremos la etiqueta entera, sino su **texto** o algún **atributo**:

```python
from bs4 import BeautifulSoup

html = '<a href="https://tienda.com" class="enlace">Comprar ahora</a>'
sopa = BeautifulSoup(html, "html.parser")

enlace = sopa.find("a")
print(enlace.text)          # Comprar ahora  -> el texto
print(enlace["href"])       # https://tienda.com  -> un atributo
print(enlace.get("class"))  # ['enlace']  -> .get() no falla si no existe
```

- `.text` (o `.get_text()`) → el texto de dentro.
- `elemento["atributo"]` → el valor de un atributo.

<a name = "6-buscar-por-clase-y-selectores-css"></a>

## 6. Buscar por clase y selectores CSS

Casi siempre necesitamos afinar la búsqueda por **clase** o **id**, porque hay muchas etiquetas iguales:

```python
from bs4 import BeautifulSoup

html = """
<div>
  <p class="precio">19.99€</p>
  <p class="descripcion">Camiseta de algodón</p>
  <p class="precio">39.99€</p>
</div>
"""
sopa = BeautifulSoup(html, "html.parser")

# Por clase con find_all
precios = sopa.find_all("p", class_="precio")
for precio in precios:
    print(precio.text)          # 19.99€ / 39.99€

# Con selectores CSS (select), como en hojas de estilo
print(sopa.select(".precio"))   # todos los de clase "precio"
print(sopa.select_one(".descripcion").text)  # Camiseta de algodón
```

>[!IMPORTANT]
>Fíjate en `class_` con guion bajo: como `class` es una palabra reservada de Python, BeautifulSoup usa `class_` para buscar por la clase del HTML.

<a name = "7-scraping-responsable-y-legal"></a>

## 7. Scraping responsable y legal

El scraping es poderoso, pero hay que usarlo con **responsabilidad**:

- Revisa los **términos de uso** de la web y su fichero `robots.txt` (`web.com/robots.txt`): indican qué se puede rastrear.
- **No satures** el servidor: añade pausas (`time.sleep(1)`, día 20) entre peticiones.
- Identifícate con una cabecera `User-Agent` y no hagas miles de peticiones por segundo.
- Si la web ofrece una **API** (día 27), úsala: siempre es preferible al scraping.
- No te apropies de contenido protegido por derechos de autor.

>[!IMPORTANT]
>Hacer scraping de forma agresiva puede bloquear tu IP o tener consecuencias legales. Sé respetuoso: extrae solo lo que necesitas y al ritmo de un humano.

<a name = "8-ejercicios"></a>

## 8. Ejercicios

> Para que practiques sin depender de internet, los Niveles 1 y 2 usan este HTML de ejemplo. Guárdalo en una variable al principio:
> ```python
> html = """
> <html><body>
>   <h1>Catálogo</h1>
>   <div class="producto">
>     <p class="nombre">Camiseta</p>
>     <p class="precio">19.99</p>
>   </div>
>   <div class="producto">
>     <p class="nombre">Pantalón</p>
>     <p class="precio">39.99</p>
>   </div>
>   <div class="producto">
>     <p class="nombre">Zapatos</p>
>     <p class="precio">59.99</p>
>   </div>
>   <a href="https://tienda.com/ofertas">Ver ofertas</a>
> </body></html>
> """
> ```

### Nivel 1 — Básico
1. Crea la `sopa` con BeautifulSoup y muestra el texto del `<h1>`.
2. Encuentra el primer producto (`find` con clase `nombre`) y muestra su texto.
3. Usa `find_all` para mostrar los nombres de todos los productos.
4. Extrae el atributo `href` del enlace `<a>`.

### Nivel 2 — Aplicado
5. Muestra todos los precios (clase `precio`) como números (convierte el texto a `float`).
6. Calcula el precio medio de los productos.
7. Recorre los `<div class="producto">` y muestra "Nombre: X — Precio: Y" de cada uno.
8. Encuentra el producto más caro y muestra su nombre.

### Nivel 3 — Reto
9. Haz una petición real con `requests` a `https://example.com`, créale la sopa y muestra el texto de su `<h1>` (envuélvelo en `try/except` por si no hay internet).
10. Construye una lista de diccionarios `[{"nombre": ..., "precio": ...}, ...]` a partir del HTML de ejemplo.
11. Convierte esa lista de diccionarios en un DataFrame de Pandas (día 31) y guárdalo en un CSV `catalogo.csv`.

> [!NOTE]
> Pistas:
> - `sopa = BeautifulSoup(html, "html.parser")`.
> - Texto de un elemento: `.text`; atributo: `elemento["href"]`.
> - Por clase: `sopa.find_all("p", class_="precio")`.
> - Para el más caro, puedes guardar los precios y usar `max()`, o construir la lista de diccionarios y ordenarla.
> - Para el CSV: `pd.DataFrame(lista).to_csv("catalogo.csv", index=False)`.

<h3 align = "center">
¡Ya sabes extraer datos de la web! Ahora damos la vuelta a la tortilla: en lugar de leer webs, mañana empezamos a CREARLAS con Flask.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/33_Visualizacion/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/35_Flask/readme.md">Día siguiente</a>
</h4>
