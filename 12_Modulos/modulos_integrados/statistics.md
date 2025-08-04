# Módulo Statistics

## 📌 Funciones Principales del Módulo statistics

### 📊 Medidas de Tendencia Central

| Función          | Descripción                | Ejemplo                         |
| ---------------- | -------------------------- | ------------------------------- |
| mean()           | Media aritmética           | mean([1, 2, 3, 4]) → 2.5        |
| median()         | Mediana (valor central)    | median([1, 3, 5]) → 3           |
| mode()           | Moda (valor más frecuente) | mode([1, 1, 2, 3]) → 1          |
| harmonic_mean()  | Media armónica             | harmonic_mean([2, 4, 8]) → 3.43 |
| geometric_mean() | Media geométrica           | geometric_mean([2, 8]) → 4.0    |

### 📈 Medidas de Dispersión

| Función     | Descripción                     | Ejemplo                      |
| ----------- | ------------------------------- | ---------------------------- |
| stdev()     | Desviación estándar (muestral)  | stdev([1, 2, 3]) → 1.0       |
| variance()  | Varianza (muestral)             | variance([1, 2, 3]) → 1.0    |
| pvariance() | Varianza poblacional            | pvariance([1, 2, 3]) → 0.666 |
| pstdev()    | Desviación estándar poblacional | pstdev([1, 2, 3]) → 0.816    |

### 📊 Otras Funciones Útiles

| Función       | Descripción                              | Ejemplo                                          |
| ------------- | ---------------------------------------- | ------------------------------------------------ |
| quantiles()   | Divide datos en cuartiles, deciles, etc. | quantiles([1, 2, 3, 4], n=4) → [1.25, 2.5, 3.75] |
| multimode()   | Devuelve todas las modas (si hay varias) | multimode([1, 1, 2, 2, 3]) → [1, 2]              |
| median_low()  | Mediana baja (valor real si hay paridad) | median_low([1, 3, 5, 7]) → 3                     |
| median_high() | Mediana alta (valor real si hay paridad) | median_high([1, 3, 5, 7]) → 5                    |

## Ejemplo
```python
import statistics

datos = [2, 4, 4, 4, 5, 5, 7, 9]

# Medidas de tendencia central
print("Media:", statistics.mean(datos))  # 5.0
print("Mediana:", statistics.median(datos))  # 4.5
print("Moda:", statistics.mode(datos))  # 4

# Medidas de dispersión
print("Desviación estándar:", statistics.stdev(datos))  # 2.138
print("Varianza:", statistics.variance(datos))  # 4.571
```

##  ¿Cuándo Usar statistics vs. numpy/pandas?

| Característica | statistics         | numpy/pandas                              |
| -------------- | ------------------ | ----------------------------------------- |
| Velocidad      | Más lento          | Optimizado para grandes datasets          |
| Funcionalidad  | Estadística básica | Análisis avanzado y manipulación de datos |
| Instalación    | Incluido en Python | Requiere pip install numpy pandas         |

- Recomendación:
✔ Usa statistics para cálculos rápidos y simples.
✔ Usa numpy/pandas para datos masivos o análisis complejos.

[Volver al Readme de módulos](../readme.md/#23-módulos-de-estadísticas)