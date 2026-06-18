"""
Ejercicios de Fechas y Tiempo (datetime)
"""
from datetime import date, datetime, timedelta
import time

# 1. Fecha y hora actuales por separado.
print(date.today())
print(datetime.now())


# 2. Día de la semana de tu cumpleaños.
dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
cumple = date(2000, 5, 17)
print(f"Naciste un {dias_semana[cumple.weekday()]}")


# 3. La fecha de hoy en dos formatos.
hoy = date.today()
print(hoy.strftime("%d/%m/%Y"))   # dd/mm/aaaa
print(hoy.strftime("%Y-%m-%d"))   # aaaa-mm-dd


# 4. Pedir una fecha por teclado y decir el año.
texto = input("Introduce una fecha (dd/mm/aaaa): ")
try:
    fecha = datetime.strptime(texto, "%d/%m/%Y")
    print(f"Esa fecha está en el año {fecha.year}")
except ValueError:
    print("Formato de fecha incorrecto.")


# 5. Función dias_hasta(fecha_texto).
def dias_hasta(fecha_texto):
    futura = datetime.strptime(fecha_texto, "%d/%m/%Y").date()
    diferencia = futura - date.today()
    return diferencia.days
print(f"Días hasta fin de año: {dias_hasta('31/12/2030')}")


# 6. Qué día será dentro de 100 días.
dentro_de_100 = date.today() + timedelta(days=100)
print(f"Dentro de 100 días será: {dentro_de_100.strftime('%d/%m/%Y')}")


# 7. Función edad(fecha_nacimiento).
def edad(fecha_nacimiento):
    hoy = date.today()
    años = hoy.year - fecha_nacimiento.year
    # Si todavía no ha sido su cumpleaños este año, resta 1.
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        años -= 1
    return años
print(f"Edad: {edad(date(1990, 1, 1))} años")


# 8. Medir cuánto tarda en sumar del 0 al 10.000.000.
inicio = time.time()
total = sum(range(10_000_001))
fin = time.time()
print(f"La suma da {total} y tardó {fin - inicio:.4f} segundos")
