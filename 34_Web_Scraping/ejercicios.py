"""
Ejercicios de Web Scraping (3 niveles)

Requisito:  pip install requests beautifulsoup4 pandas
El ejercicio 9 necesita internet (está protegido con try/except).
El ejercicio 11 crea un fichero catalogo.csv.
"""
from bs4 import BeautifulSoup
import pandas as pd

html = """
<html><body>
  <h1>Catálogo</h1>
  <div class="producto">
    <p class="nombre">Camiseta</p>
    <p class="precio">19.99</p>
  </div>
  <div class="producto">
    <p class="nombre">Pantalón</p>
    <p class="precio">39.99</p>
  </div>
  <div class="producto">
    <p class="nombre">Zapatos</p>
    <p class="precio">59.99</p>
  </div>
  <a href="https://tienda.com/ofertas">Ver ofertas</a>
</body></html>
"""

sopa = BeautifulSoup(html, "html.parser")

print("===== NIVEL 1 - BÁSICO =====")

# 1. Texto del h1.
print(sopa.find("h1").text)

# 2. Primer producto.
print(sopa.find("p", class_="nombre").text)

# 3. Todos los nombres.
for nombre in sopa.find_all("p", class_="nombre"):
    print(nombre.text)

# 4. href del enlace.
print(sopa.find("a")["href"])


print("\n===== NIVEL 2 - APLICADO =====")

# 5. Precios como float.
precios = [float(p.text) for p in sopa.find_all("p", class_="precio")]
print(precios)

# 6. Precio medio.
print(f"Precio medio: {sum(precios) / len(precios):.2f}")

# 7. Recorrer cada producto.
for producto in sopa.find_all("div", class_="producto"):
    nombre = producto.find("p", class_="nombre").text
    precio = producto.find("p", class_="precio").text
    print(f"Nombre: {nombre} — Precio: {precio}")

# 8. Producto más caro.
productos = sopa.find_all("div", class_="producto")
mas_caro = max(productos, key=lambda p: float(p.find("p", class_="precio").text))
print(f"Más caro: {mas_caro.find('p', class_='nombre').text}")


print("\n===== NIVEL 3 - RETO =====")

# 9. Petición real (protegida por si no hay internet).
try:
    import requests
    respuesta = requests.get("https://example.com", timeout=5)
    sopa_real = BeautifulSoup(respuesta.text, "html.parser")
    print(f"H1 de example.com: {sopa_real.find('h1').text}")
except Exception as error:
    print(f"(Sin conexión o error: {error})")

# 10. Lista de diccionarios.
catalogo = []
for producto in sopa.find_all("div", class_="producto"):
    catalogo.append({
        "nombre": producto.find("p", class_="nombre").text,
        "precio": float(producto.find("p", class_="precio").text)
    })
print(catalogo)

# 11. A DataFrame y a CSV.
df = pd.DataFrame(catalogo)
df.to_csv("catalogo.csv", index=False)
print("Guardado catalogo.csv:")
print(df)
