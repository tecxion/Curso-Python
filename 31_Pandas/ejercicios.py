"""
Ejercicios de Pandas (3 niveles)

Requisito:  pip install pandas
NOTA: el ejercicio 11 crea un fichero empleados.csv en la carpeta.
"""
import pandas as pd

df = pd.DataFrame({
    "nombre": ["Ana", "Luis", "Marta", "Pedro", "Sara"],
    "edad": [25, 30, 22, 35, 28],
    "ciudad": ["Madrid", "Sevilla", "Madrid", "Bilbao", "Sevilla"],
    "salario": [1800, 2200, 1500, 2800, 2000]
})

print("===== NIVEL 1 - BÁSICO =====")

# 1. Primeras 3 filas.
print(df.head(3))

# 2. Forma y columnas.
print(f"Forma: {df.shape}")
print(f"Columnas: {list(df.columns)}")

# 3. Columna nombre.
print(df["nombre"])

# 4. Media del salario.
print(f"Salario medio: {df['salario'].mean()}")


print("\n===== NIVEL 2 - APLICADO =====")

# 5. Mayores de 25.
print(df[df["edad"] > 25])

# 6. Los de Madrid.
print(df[df["ciudad"] == "Madrid"])

# 7. Columna salario_anual (14 pagas).
df["salario_anual"] = df["salario"] * 14
print(df[["nombre", "salario_anual"]])

# 8. Ordenar por salario descendente.
print(df.sort_values("salario", ascending=False)[["nombre", "salario"]])


print("\n===== NIVEL 3 - RETO =====")

# 9. De Sevilla con salario > 1900.
print(df[(df["ciudad"] == "Sevilla") & (df["salario"] > 1900)][["nombre", "salario"]])

# 10. Salario medio por ciudad.
print(df.groupby("ciudad")["salario"].mean())

# 11. Guardar y releer un CSV.
df[["nombre", "salario"]].to_csv("empleados.csv", index=False)
releido = pd.read_csv("empleados.csv")
print("CSV releído:")
print(releido)
