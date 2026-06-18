"""
Ejercicios de NumPy (3 niveles)

Requisito:  pip install numpy
"""
import numpy as np

print("===== NIVEL 1 - BÁSICO =====")

# 1. Array del 1 al 10.
a = np.arange(1, 11)
print(a)

# 2. Pares del 0 al 20.
pares = np.arange(0, 21, 2)
print(pares)

# 3. Multiplicar por 3.
print(np.array([5, 10, 15, 20]) * 3)   # [15 30 45 60]

# 4. Cinco ceros y cinco unos.
print(np.zeros(5))
print(np.ones(5))


print("\n===== NIVEL 2 - APLICADO =====")

datos = np.array([12, 7, 25, 4, 18, 9])

# 5. Estadísticas.
print(f"Suma: {datos.sum()}, Media: {datos.mean()}, Máx: {datos.max()}, Mín: {datos.min()}")

# 6. Máscara booleana: mayores que 10.
print(datos[datos > 10])   # [12 25 18]

# 7. 10 aleatorios y cuántos > 0.5.
np.random.seed(0)
aleatorios = np.random.rand(10)
print(f"Mayores que 0.5: {(aleatorios > 0.5).sum()}")

# 8. Celsius a Fahrenheit.
celsius = np.array([20, 22, 19, 24, 25, 23, 21])
fahrenheit = celsius * 9 / 5 + 32
print(fahrenheit)


print("\n===== NIVEL 3 - RETO =====")

# 9. Matriz 3x3 del 1 al 9, sumas por fila y columna.
matriz = np.arange(1, 10).reshape(3, 3)
print(matriz)
print(f"Suma por filas:    {matriz.sum(axis=1)}")   # [ 6 15 24]
print(f"Suma por columnas: {matriz.sum(axis=0)}")   # [12 15 18]

# 10. Notas de 4 alumnos en 3 exámenes.
notas = np.array([
    [8, 6, 7],
    [5, 9, 10],
    [7, 7, 8],
    [10, 9, 9]
])
print(f"Media por alumno: {notas.mean(axis=1)}")
print(f"Media por examen: {notas.mean(axis=0)}")

# 11. Porcentaje por debajo de 0.5 en 1000 aleatorios.
muchos = np.random.rand(1000)
porcentaje = (muchos < 0.5).mean() * 100
print(f"Porcentaje por debajo de 0.5: {porcentaje:.1f}%")
