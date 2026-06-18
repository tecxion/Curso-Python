"""
main.py
Punto de entrada del programa. Importa la lógica desde operaciones.py
y la coordina. Ejecútalo con:  python main.py  (o python3 main.py)
"""
from operaciones import sumar, restar, multiplicar, dividir


def main():
    print("=== Mini calculadora (ejemplo de proyecto multi-archivo) ===")
    a = 10
    b = 5
    print(f"{a} + {b} = {sumar(a, b)}")
    print(f"{a} - {b} = {restar(a, b)}")
    print(f"{a} * {b} = {multiplicar(a, b)}")
    print(f"{a} / {b} = {dividir(a, b)}")


# Este bloque solo se ejecuta si lanzamos main.py directamente,
# no si alguien importa este fichero desde otro.
if __name__ == "__main__":
    main()
