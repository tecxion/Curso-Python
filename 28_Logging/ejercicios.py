"""
Ejercicios de Logging y Depuración

NOTA: el ejercicio 4 en adelante guarda los mensajes en el fichero
'mi_app.log'. Ábrelo después para ver el registro.
"""
import logging

# 2, 3 y 4. Configuramos el logging: nivel DEBUG, formato con fecha y a fichero.
logging.basicConfig(
    filename="mi_app.log",
    filemode="w",   # 'w' empieza el log de cero cada ejecución
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# 1. Un mensaje de cada nivel.
logging.debug("Mensaje de depuración")
logging.info("Mensaje informativo")
logging.warning("Mensaje de aviso")
logging.error("Mensaje de error")
logging.critical("Mensaje crítico")


# 5. Función dividir(a, b) que registra el error de dividir entre cero.
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logging.exception("Se intentó dividir entre cero")
        return None
dividir(10, 0)


# 6. Simular un inicio de sesión.
def iniciar_sesion(usuario, password):
    if usuario == "admin" and password == "1234":
        logging.info(f"Login correcto del usuario '{usuario}'")
        return True
    else:
        logging.warning(f"Intento de login fallido para '{usuario}'")
        return False
iniciar_sesion("admin", "1234")
iniciar_sesion("hacker", "0000")


# 7. Registrar con warning cada número negativo de una lista.
def revisar_numeros(numeros):
    for numero in numeros:
        if numero < 0:
            logging.warning(f"Número negativo encontrado: {numero}")
revisar_numeros([4, -2, 7, -8, 1])


# 8. Pedir un número y registrar un error si no lo es.
try:
    valor = int(input("Introduce un número: "))
    logging.info(f"El usuario introdujo el número {valor}")
except ValueError:
    logging.error("El usuario no introdujo un número válido")


print("Programa terminado. Revisa el fichero 'mi_app.log' para ver los registros.")
