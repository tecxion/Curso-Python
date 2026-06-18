"""
Ejercicios de Context Managers (la sentencia with)

NOTA: el ejercicio 7 y 8 crean ficheros de texto en la carpeta.
"""
import time
from contextlib import contextmanager


# 1. Context manager Saludo (con clase).
class Saludo:
    def __enter__(self):
        print("Hola")
        return self

    def __exit__(self, tipo, valor, traza):
        print("Adiós")

with Saludo():
    print("Estoy dentro del bloque")


# 2. Context manager Marco.
class Marco:
    def __enter__(self):
        print("=" * 30)
        return self

    def __exit__(self, tipo, valor, traza):
        print("=" * 30)

with Marco():
    print("Contenido enmarcado")


# 3. Context manager Temporizador (con clase).
class Temporizador:
    def __enter__(self):
        self.inicio = time.time()
        return self

    def __exit__(self, tipo, valor, traza):
        print(f"Tardó {time.time() - self.inicio:.4f} segundos")

with Temporizador():
    total = sum(range(1_000_000))


# 4. Context manager que captura errores.
class CapturarErrores:
    def __enter__(self):
        return self

    def __exit__(self, tipo, valor, traza):
        if tipo is not None:
            print(f"Error capturado: {valor}")
        return True   # no relanza el error

with CapturarErrores():
    print("Voy a provocar un error...")
    raise ValueError("¡fallo controlado!")
print("El programa sigue funcionando")


# 5. Saludo pero con @contextmanager.
@contextmanager
def saludo():
    print("Hola (versión contextlib)")
    yield
    print("Adiós (versión contextlib)")

with saludo():
    print("Dentro del bloque")


# 6. seccion(titulo) con @contextmanager.
@contextmanager
def seccion(titulo):
    print(f"--- {titulo} ---")
    yield
    print("--- fin ---")

with seccion("Resultados"):
    print("Dato 1")
    print("Dato 2")


# 7. Un único with para leer un fichero y escribir en otro.
with open("origen.txt", "w", encoding="utf-8") as preparar:
    preparar.write("contenido original")

with open("origen.txt", "r", encoding="utf-8") as entrada, \
     open("copia.txt", "w", encoding="utf-8") as salida:
    salida.write(entrada.read())
print("Fichero copiado correctamente")


# 8. Context manager propio que abre y cierra un fichero.
@contextmanager
def abrir_fichero(ruta, modo):
    fichero = open(ruta, modo, encoding="utf-8")
    try:
        yield fichero
    finally:
        fichero.close()
        print("Fichero cerrado por nuestro context manager")

with abrir_fichero("prueba.txt", "w") as f:
    f.write("Hecho con nuestro propio with")
