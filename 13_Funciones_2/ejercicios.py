def crear_validador(**reglas):
    """Crea un validador basado en reglas"""
    def validar(datos):
        errores = []
        
        for campo, valor in datos.items():
            if campo in reglas:
                for nombre_regla, regla in reglas[campo].items():
                    if not regla(valor):
                        errores.append(f"{campo}: falló validación {nombre_regla}")
        
        return len(errores) == 0, errores
    
    return validar

# Crear validador para usuario
validar_usuario = crear_validador(
    nombre={
        'no_vacio': lambda x: len(x) > 0,
        'longitud_minima': lambda x: len(x) >= 2
    },
    edad={
        'es_numero': lambda x: isinstance(x, int),
        'mayor_edad': lambda x: x >= 18
    },
    email={
        'contiene_arroba': lambda x: '@' in x,
        'no_vacio': lambda x: len(x) > 0
    }
)

# Usar el validador
usuario1 = {'nombre': 'Juan', 'edad': 25, 'email': 'juan@email.com'}
usuario2 = {'nombre': '', 'edad': 15, 'email': 'invalido'}

es_valido1, errores1 = validar_usuario(usuario1)
es_valido2, errores2 = validar_usuario(usuario2)

print(f"Usuario 1 válido: {es_valido1}")  # True
print(f"Usuario 2 válido: {es_valido2}")  # False
print(f"Errores: {errores2}")