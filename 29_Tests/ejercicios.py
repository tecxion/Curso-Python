"""
Ejercicios de Tests

Aquí usamos unittest (incluido en Python) para que puedas ejecutarlo
directamente con:   python ejercicios.py
Al final tienes, comentada, la versión equivalente en pytest.
"""
import unittest


# ---------- Funciones que vamos a probar ----------

def es_par(n):
    return n % 2 == 0

def multiplicar(a, b):
    return a * b

def mayor_de_lista(lista):
    return max(lista)

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def invertir_texto(texto):
    return texto[::-1]


# 1. Comprobación rápida con assert (antes de los tests formales).
assert es_par(4) is True
assert es_par(7) is False
print("Los assert iniciales han pasado correctamente.")


# 2-8. Tests con unittest.
class TestEjercicios(unittest.TestCase):

    # 2. Dos tests para multiplicar.
    def test_multiplicar_positivos(self):
        self.assertEqual(multiplicar(3, 4), 12)

    def test_multiplicar_por_cero(self):
        self.assertEqual(multiplicar(5, 0), 0)

    # 3. assertTrue con es_par.
    def test_es_par_verdadero(self):
        self.assertTrue(es_par(10))

    def test_es_par_falso(self):
        self.assertFalse(es_par(9))

    # 4. assertEqual con mayor_de_lista.
    def test_mayor_de_lista(self):
        self.assertEqual(mayor_de_lista([3, 9, 1]), 9)

    # 5. assertIn.
    def test_letra_en_palabra(self):
        self.assertIn("o", "python")

    # 6. assertRaises con dividir.
    def test_division_entre_cero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

    def test_division_normal(self):
        self.assertEqual(dividir(10, 2), 5)

    # 8. invertir_texto: caso normal y caso límite (texto vacío).
    def test_invertir_normal(self):
        self.assertEqual(invertir_texto("hola"), "aloh")

    def test_invertir_vacio(self):
        self.assertEqual(invertir_texto(""), "")


if __name__ == "__main__":
    unittest.main(verbosity=2)


# ----------------------------------------------------------------------
# 7. La MISMA idea en pytest (guárdalo en un fichero 'test_matematicas.py'
#    y ejecútalo con el comando 'pytest'):
#
# import pytest
#
# def multiplicar(a, b):
#     return a * b
#
# def test_multiplicar_positivos():
#     assert multiplicar(3, 4) == 12
#
# def test_multiplicar_por_cero():
#     assert multiplicar(5, 0) == 0
#
# def test_division_entre_cero():
#     with pytest.raises(ValueError):
#         dividir(10, 0)
# ----------------------------------------------------------------------
