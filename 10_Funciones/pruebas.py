def nombre_completo(nombre, apellido):
    saludo = (f"Hola, {nombre} {apellido}, esto es una función con dos param.")
    return saludo

nombre_alumno = input("¿Cómo te llamas? ")
apellido_alumno = input("¿Y tu apellido? ")
print(nombre_completo(nombre_alumno, apellido_alumno))