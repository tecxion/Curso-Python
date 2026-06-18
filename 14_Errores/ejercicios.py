"""
Ejercicios de Manejo de Errores y Excepciones
"""

# 1. Pide un número y muestra su raíz cuadrada. Controla que sea un número válido.
try:
    numero = float(input("Introduce un número para su raíz cuadrada: "))
    print(f"La raíz cuadrada es {numero ** 0.5}")
except ValueError:
    print("Eso no es un número válido.")


# 2. Función division_segura(a, b) que controle la división entre cero.
def division_segura(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir entre cero"
print(division_segura(10, 2))   # 5.0
print(division_segura(10, 0))   # No se puede dividir entre cero


# 3. Pide una posición de la lista y muéstrala. Controla número y posición válida.
colores = ["rojo", "verde", "azul", "amarillo"]
try:
    posicion = int(input("¿Qué posición de colores quieres ver? "))
    print(colores[posicion])
except ValueError:
    print("Debes introducir un número entero.")
except IndexError:
    print("Esa posición no existe en la lista.")


# 4. Función acceder(diccionario, clave) que controle claves inexistentes.
def acceder(diccionario, clave):
    try:
        return diccionario[clave]
    except KeyError:
        return "Clave no encontrada"
persona = {"nombre": "Ana", "edad": 30}
print(acceder(persona, "nombre"))   # Ana
print(acceder(persona, "telefono")) # Clave no encontrada


# 5. Programa con try / except / else / finally que pida la edad.
try:
    edad = int(input("Introduce tu edad: "))
except ValueError:
    print("La edad debe ser un número.")
else:
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")
finally:
    print("Gracias por usar el programa.")


# 6. Función validar_password que lance ValueError según las reglas.
def validar_password(password):
    if len(password) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres.")
    if not any(caracter.isdigit() for caracter in password):
        raise ValueError("La contraseña debe contener al menos un número.")
    return "Contraseña válida"

try:
    print(validar_password("python123"))   # Contraseña válida
    print(validar_password("corta"))        # Lanza error
except ValueError as error:
    print(f"Error: {error}")


# 7. Excepción personalizada TemperaturaInvalidaError.
class TemperaturaInvalidaError(Exception):
    """Se lanza cuando la temperatura está fuera de los límites posibles."""
    pass

def registrar_temperatura(grados):
    if grados < -90 or grados > 60:
        raise TemperaturaInvalidaError(f"{grados}º no es una temperatura posible.")
    return f"Temperatura registrada: {grados}º"

try:
    print(registrar_temperatura(25))    # Temperatura registrada: 25º
    print(registrar_temperatura(120))   # Lanza error
except TemperaturaInvalidaError as error:
    print(f"Error: {error}")


# 8. Calculadora por consola con manejo de errores.
def calculadora():
    try:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        operacion = input("Operación (+, -, *, /): ")

        if operacion == "+":
            print(f"Resultado: {a + b}")
        elif operacion == "-":
            print(f"Resultado: {a - b}")
        elif operacion == "*":
            print(f"Resultado: {a * b}")
        elif operacion == "/":
            print(f"Resultado: {a / b}")
        else:
            print("Operación no válida.")
    except ValueError:
        print("Debes introducir números válidos.")
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")

calculadora()
