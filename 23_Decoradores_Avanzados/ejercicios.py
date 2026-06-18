"""
Ejercicios de Decoradores Avanzados y functools
"""
import functools
import time


# 1. Decorador mayusculas (con functools.wraps).
def mayusculas(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@mayusculas
def saludar(nombre):
    """Devuelve un saludo."""
    return f"hola {nombre}"

print(saludar("ana"))   # HOLA ANA


# 2. Comprobar que conserva el nombre.
print(saludar.__name__)   # saludar  (no 'wrapper')


# 3. Decorador con parámetro repetir(veces).
def repetir(veces):
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(veces):
                resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorador

@repetir(3)
def ladrar():
    print("¡Guau!")
ladrar()


# 4. Decorador con parámetro mensaje(texto).
def mensaje(texto):
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(texto)
            return func(*args, **kwargs)
        return wrapper
    return decorador

@mensaje("Ejecutando suma...")
def suma(a, b):
    return a + b
print(suma(2, 3))   # Ejecutando suma... \n 5


# 5. factorial con @lru_cache.
@functools.lru_cache(maxsize=None)
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)
print(factorial(100))


# 6. partial para crear hola(nombre).
def saludar_con(saludo, nombre):
    return f"{saludo}, {nombre}"

hola = functools.partial(saludar_con, "Hola")
print(hola("Luis"))   # Hola, Luis


# 7. reduce para el número mayor (sin max).
mayor = functools.reduce(lambda x, y: x if x > y else y, [3, 9, 1, 7, 5])
print(f"El mayor es: {mayor}")   # 9


# 8. Decorador medir_tiempo.
def medir_tiempo(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"{func.__name__} tardó {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def sumar_muchos():
    return sum(range(1_000_000))
print(sumar_muchos())
