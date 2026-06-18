<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/28_Logging/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/30_Proyecto_Final/readme.md">Día siguiente</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/tests.png">
</h1>


<h1 align="center">Tests: probar tu código</h1><br>

<h3>Índice</h3>

- [1. ¿Qué es un test y por qué escribirlos?](#1-qué-es-un-test-y-por-qué-escribirlos)
- [2. assert: la base de todo test](#2-assert-la-base-de-todo-test)
- [3. unittest (incluido en Python)](#3-unittest-incluido-en-python)
- [4. Los métodos assert de unittest](#4-los-métodos-assert-de-unittest)
- [5. pytest (más sencillo)](#5-pytest-más-sencillo)
- [6. Probar que salta una excepción](#6-probar-que-salta-una-excepción)
- [7. Buenas prácticas al testear](#7-buenas-prácticas-al-testear)
- [8. Ejercicios](#8-ejercicios)

<a name = "1-qué-es-un-test-y-por-qué-escribirlos"></a>

## 1. ¿Qué es un test y por qué escribirlos?

Un **test** (o prueba) es un trozo de código cuyo único trabajo es **comprobar que otro código funciona** como debe. En lugar de ejecutar el programa y mirar a ojo si el resultado es correcto, escribimos pruebas que lo verifican **automáticamente**.

¿Por qué merece la pena?
- Detectas errores **antes** de que lleguen al usuario.
- Cuando cambias algo, los tests te avisan si **rompiste** lo que ya funcionaba.
- Te dan **confianza** para mejorar tu código sin miedo.

Es una de las prácticas que más diferencia a un programador aficionado de uno profesional.

<a name = "2-assert-la-base-de-todo-test"></a>

## 2. assert: la base de todo test

La pieza más simple es la palabra reservada **`assert`**: comprueba que una condición es verdadera. Si lo es, no pasa nada; si es falsa, lanza un error.

```python
def sumar(a, b):
    return a + b

assert sumar(2, 3) == 5      # correcto: no pasa nada
assert sumar(2, 2) == 5      # ❌ AssertionError: la condición es falsa
```

Los tests "de verdad" no son más que muchos `assert` organizados con herramientas que nos dicen claramente cuáles pasan y cuáles fallan.

<a name = "3-unittest-incluido-en-python"></a>

## 3. unittest (incluido en Python)

Python trae el módulo **`unittest`** en su librería estándar. Los tests se agrupan en una **clase** que hereda de `unittest.TestCase` (¡herencia del día 16!), y cada prueba es un método que empieza por `test_`:

```python
# fichero: test_calculadora.py
import unittest

def sumar(a, b):
    return a + b

class TestCalculadora(unittest.TestCase):

    def test_suma_positivos(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_suma_negativos(self):
        self.assertEqual(sumar(-1, -1), -2)

if __name__ == "__main__":
    unittest.main()
```

Se ejecuta desde la terminal así:

```bash
python test_calculadora.py
```

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

Cada punto `.` es un test que ha pasado. Si alguno falla, te dice exactamente cuál y por qué.

<a name = "4-los-métodos-assert-de-unittest"></a>

## 4. Los métodos assert de unittest

`unittest` ofrece muchos métodos para comprobar distintas cosas. Los más usados:

| Método | Comprueba que... |
| -------------------------- | ----------------------------- |
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` | `x` es verdadero |
| `assertFalse(x)` | `x` es falso |
| `assertIn(a, lista)` | `a` está en la lista |
| `assertIsNone(x)` | `x` es `None` |
| `assertRaises(Error)` | salta esa excepción |

```python
self.assertEqual(2 + 2, 4)
self.assertTrue("a" in "casa")
self.assertIn(3, [1, 2, 3])
```

<a name = "5-pytest-más-sencillo"></a>

## 5. pytest (más sencillo)

**`pytest`** es una librería externa (se instala con `pip install pytest`) muy popular porque es **más simple**: no necesitas clases, solo funciones que empiecen por `test_` y `assert` normales.

```python
# fichero: test_calculadora.py
def sumar(a, b):
    return a + b

def test_suma_positivos():
    assert sumar(2, 3) == 5

def test_suma_negativos():
    assert sumar(-1, -1) == -2
```

Se ejecuta con el comando `pytest`, que busca y corre solos todos los ficheros `test_*.py`:

```bash
pip install pytest
pytest
```

```
test_calculadora.py ..                                          [100%]
2 passed in 0.01s
```

>[!NOTE]
>`unittest` viene incluido y es bueno conocerlo. Pero en proyectos modernos `pytest` es lo más habitual por su sencillez. Aprende los dos: se parecen mucho.

<a name = "6-probar-que-salta-una-excepción"></a>

## 6. Probar que salta una excepción

A veces queremos comprobar que el código **falla cuando debe** (recuerda el `raise` del día 14). Así se prueba que salta la excepción esperada:

```python
import unittest

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

class TestDivision(unittest.TestCase):
    def test_division_entre_cero(self):
        # Comprobamos que dividir(10, 0) lanza ValueError
        with self.assertRaises(ValueError):
            dividir(10, 0)
```

En `pytest` sería:

```python
import pytest

def test_division_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)
```

<a name = "7-buenas-prácticas-al-testear"></a>

## 7. Buenas prácticas al testear

- Pon los tests en ficheros que empiecen por **`test_`** (es la convención que buscan las herramientas).
- Cada test debe probar **una sola cosa** y tener un nombre que diga qué prueba.
- Prueba también los **casos límite**: listas vacías, ceros, números negativos, entradas raras.
- Un test no debería depender de otro: cada uno se ejecuta por su cuenta.

>[!IMPORTANT]
>No hace falta testearlo absolutamente todo desde el primer día. Empieza por las funciones importantes (las que hacen cálculos o tienen reglas) y ve cogiendo el hábito. Tu yo del futuro te lo agradecerá.

<a name = "8-ejercicios"></a>

## 8. Ejercicios

Para estos ejercicios, crea una función y luego pruébala. Puedes usar `unittest` (incluido) o `pytest` (`pip install pytest`).

1. Escribe una función `es_par(n)` y comprueba con varios `assert` que funciona bien con números pares e impares.

2. Crea un fichero `test_matematicas.py` con una clase `unittest` que pruebe una función `multiplicar(a, b)` con dos tests.

3. Añade un test que use `assertTrue` para comprobar que `es_par(10)` es verdadero.

4. Escribe una función `mayor_de_lista(lista)` y un test que compruebe con `assertEqual` que devuelve el mayor de `[3, 9, 1]`.

5. Escribe un test que use `assertIn` para comprobar que la letra "o" está en la palabra "python".

6. Crea una función `dividir(a, b)` que lance `ValueError` si `b` es 0, y un test con `assertRaises` que lo compruebe.

7. Reescribe los tests del ejercicio 2 en formato `pytest` (funciones `test_` y `assert` normales).

8. Escribe una función `invertir_texto(texto)` y pruébala con un caso normal y con el caso límite de un texto vacío.

> [!NOTE]
> Pistas para los ejercicios:
> - Con `unittest`: clase que hereda de `unittest.TestCase`, métodos que empiezan por `test_`, y `unittest.main()` al final.
> - Con `pytest`: solo funciones `test_...()` con `assert`, y se ejecuta con el comando `pytest`.
> - Para probar errores: `with self.assertRaises(ValueError):` (unittest) o `with pytest.raises(ValueError):` (pytest).
> - Recuerda probar casos límite: el texto vacío, el cero, la lista vacía…
> - Los ficheros de test deben empezar por `test_` para que se detecten solos.

<h3 align = "center">
¡Enhorabuena, has terminado toda la teoría del curso! Solo queda lo mejor: mañana, en el día 30, juntamos TODO en el proyecto final.
</h3>

<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/28_Logging/readme.md">Día anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/30_Proyecto_Final/readme.md">Día siguiente</a>
</h4>
