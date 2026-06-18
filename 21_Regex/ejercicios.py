"""
Ejercicios de Expresiones Regulares (re)
"""
import re

# 1. Extraer todos los números.
texto = "Compré 3 manzanas, 12 peras y 7 plátanos"
print(re.findall(r"\d+", texto))   # ['3', '12', '7']


# 2. ¿"Python3" contiene algún dígito?
print(bool(re.search(r"\d", "Python3")))   # True


# 3. Función es_codigo_postal(texto).
def es_codigo_postal(texto):
    return bool(re.fullmatch(r"\d{5}", texto))
print(es_codigo_postal("28080"))   # True
print(es_codigo_postal("2808"))    # False
print(es_codigo_postal("ABCDE"))   # False


# 4. Función es_email(texto).
def es_email(texto):
    return bool(re.fullmatch(r"\w+@\w+\.\w{2,}", texto))
print(es_email("ana@correo.com"))   # True
print(es_email("ana@correo"))       # False
print(es_email("hola"))             # False


# 5. Extraer los dos goles con grupos.
resultado = re.search(r"(\d)-(\d)", "El partido acabó 3-2 en el minuto 89")
print(f"Local: {resultado.group(1)}, Visitante: {resultado.group(2)}")  # 3 y 2


# 6. Sustituir espacios por guiones bajos.
frase = "esto es una prueba"
print(re.sub(r"\s", "_", frase))   # esto_es_una_prueba


# 7. Palabras que empiezan por mayúscula.
texto2 = "Ana y Luis fueron a Madrid en Marzo"
print(re.findall(r"[A-Z]\w*", texto2))   # ['Ana', 'Luis', 'Madrid', 'Marzo']


# 8. Función validar_telefono(numero) (9 dígitos, empieza por 6-9).
def validar_telefono(numero):
    return bool(re.fullmatch(r"[6-9]\d{8}", numero))
print(validar_telefono("600123456"))   # True
print(validar_telefono("123456789"))   # False
print(validar_telefono("60012345"))    # False (solo 8 dígitos)
