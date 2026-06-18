"""
Ejercicios de Visualización de Datos (3 niveles)

Requisito:  pip install matplotlib numpy pandas
NOTA: cada ejercicio GUARDA una imagen .png en la carpeta (no usamos show()
para que funcione también desde la terminal). Ábrelas para ver el resultado.
"""
import matplotlib
matplotlib.use("Agg")   # backend sin ventana: permite guardar sin pantalla
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print("===== NIVEL 1 - BÁSICO =====")

# 1 y 2. Líneas con título y etiquetas.
dias = ["Lun", "Mar", "Mié", "Jue", "Vie"]
horas = [2, 3, 1, 4, 2]
plt.plot(dias, horas, marker="o")
plt.title("Horas de estudio por día")
plt.xlabel("Día")
plt.ylabel("Horas")
plt.savefig("estudio.png")
plt.close()
print("Guardado estudio.png")

# 3. Barras de productos.
plt.bar(["Camiseta", "Pantalón", "Zapatos"], [30, 20, 15])
plt.title("Ventas por producto")
plt.savefig("ventas_producto.png")
plt.close()
print("Guardado ventas_producto.png")

# 4. Tarta del reparto del día.
plt.pie([8, 6, 4, 6], labels=["Dormir", "Estudiar", "Ocio", "Otros"], autopct="%1.0f%%")
plt.title("Mi día")
plt.savefig("dia.png")
plt.close()
print("Guardado dia.png")


print("\n===== NIVEL 2 - APLICADO =====")

# 5. Dos líneas con leyenda.
meses = ["Ene", "Feb", "Mar", "Abr"]
plt.plot(meses, [100, 120, 90, 150], label="2023")
plt.plot(meses, [110, 130, 120, 160], label="2024")
plt.title("Ventas por año")
plt.legend()
plt.savefig("dos_anios.png")
plt.close()
print("Guardado dos_anios.png")

# 6. Histograma de 1000 aleatorios.
np.random.seed(0)
plt.hist(np.random.randn(1000), bins=20)
plt.title("Distribución normal")
plt.savefig("histograma.png")
plt.close()
print("Guardado histograma.png")

# 7. Línea personalizada.
plt.plot([1, 2, 3, 4], [10, 25, 18, 30], color="purple", linewidth=2, marker="s")
plt.title("Línea personalizada")
plt.savefig("personalizada.png")
plt.close()
print("Guardado personalizada.png")

# 8. Dispersión estudio vs nota.
plt.scatter([1, 2, 3, 4, 5], [4, 5, 6, 8, 9])
plt.title("Horas de estudio vs nota")
plt.xlabel("Horas")
plt.ylabel("Nota")
plt.savefig("dispersion.png")
plt.close()
print("Guardado dispersion.png")


print("\n===== NIVEL 3 - RETO =====")

# 9. Barras del total por categoría (con groupby).
ventas = pd.DataFrame({
    "categoria": ["Ropa", "Calzado", "Ropa", "Calzado", "Ropa"],
    "ingreso": [200, 150, 100, 80, 120]
})
totales = ventas.groupby("categoria")["ingreso"].sum()
totales.plot(kind="bar")
plt.title("Ingreso por categoría")
plt.tight_layout()
plt.savefig("por_categoria.png")
plt.close()
print("Guardado por_categoria.png")

# 10. Dos gráficos en una figura.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.bar(["A", "B", "C"], [30, 50, 20])
ax1.set_title("Barras")
ax2.pie([30, 50, 20], labels=["A", "B", "C"], autopct="%1.0f%%")
ax2.set_title("Tarta")
plt.savefig("dos_graficos.png")
plt.close()
print("Guardado dos_graficos.png")

# 11. Gráfico completo en alta calidad.
df = pd.DataFrame({
    "equipo": ["A", "A", "B", "B", "C"],
    "puntos": [10, 20, 15, 25, 30]
})
medias = df.groupby("equipo")["puntos"].mean()
medias.plot(kind="bar", color="teal", label="Media de puntos")
plt.title("Media de puntos por equipo")
plt.xlabel("Equipo")
plt.ylabel("Puntos")
plt.legend()
plt.tight_layout()
plt.savefig("informe.png", dpi=150)
plt.close()
print("Guardado informe.png (alta calidad)")
print("\n¡Listo! Abre los .png generados para ver los gráficos.")
