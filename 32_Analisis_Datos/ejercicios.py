"""
Ejercicios de Análisis de Datos (3 niveles)

Requisito:  pip install pandas numpy
"""
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "nombre": ["Ana", "Luis", "Marta", "Pedro", "Sara", "Juan"],
    "departamento": ["IT", "Ventas", "IT", "Ventas", "RRHH", "IT"],
    "edad": [25, 30, np.nan, 35, 28, 41],
    "salario": [2500, 1800, 2700, 2000, 1900, np.nan]
})

print("===== NIVEL 1 - BÁSICO =====")

# 1. Nulos por columna.
print(df.isnull().sum())

# 2. Rellenar edad con la media.
df["edad"] = df["edad"].fillna(df["edad"].mean())

# 3. Rellenar salario con la mediana.
df["salario"] = df["salario"].fillna(df["salario"].median())

# 4. describe() del salario.
print(df["salario"].describe())


print("\n===== NIVEL 2 - APLICADO =====")

# 5. Salario medio por departamento.
print(df.groupby("departamento")["salario"].mean())

# 6. Empleados por departamento.
print(df["departamento"].value_counts())

# 7. Columna categoria_edad.
df["categoria_edad"] = df["edad"].apply(lambda x: "joven" if x < 30 else "senior")
print(df[["nombre", "edad", "categoria_edad"]])

# 8. Departamento con salario medio más alto.
mejor_depto = df.groupby("departamento")["salario"].mean().idxmax()
print(f"Departamento mejor pagado: {mejor_depto}")


print("\n===== NIVEL 3 - RETO =====")

# 9. agg con media, máximo y conteo por departamento.
print(df.groupby("departamento")["salario"].agg(["mean", "max", "count"]))

# 10. Subir 10% el salario solo de IT.
df["salario_subido"] = df.apply(
    lambda fila: fila["salario"] * 1.1 if fila["departamento"] == "IT" else fila["salario"],
    axis=1
)
print(df[["nombre", "departamento", "salario", "salario_subido"]])

# 11. Mini-informe.
print("\n--- INFORME ---")
print(f"Total de empleados: {len(df)}")
print(f"Salario medio global: {df['salario'].mean():.2f}€")
mejor_pagado = df.loc[df["salario"].idxmax(), "nombre"]
print(f"Empleado mejor pagado: {mejor_pagado}")
