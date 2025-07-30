<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/05_Tuplas/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/07_Diccionarios/readme.md">Siguiente Capítulo</a>
</h4>


<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/diccionarios.png">
</h1>

<h1 align="center">Diccionarios</h1><br>

<h4>Índice</h4>



<h4>Índice</h4>

- [1. ¿Qué es un diccionario?](#1-qué-es-un-diccionario)
- [2. Longitud del diccionario](#2-longitud-del-diccionario)
- [2. Acceso a los elementos del diccionario](#2-acceso-a-los-elementos-del-diccionario)
- [4. Agregar elementos a un diccionario](#4-agregar-elementos-a-un-diccionario)
- [5. Modificar elementos de un diccionario](#5-modificar-elementos-de-un-diccionario)
- [6. Comprobar las claves de un diccionario](#6-comprobar-las-claves-de-un-diccionario)
- [7. Cómo eliminar pares clave-valor de un diccionario](#7-cómo-eliminar-pares-clave-valor-de-un-diccionario)
- [8. Cambiar el diccionario a una lista](#8-cambiar-el-diccionario-a-una-lista)
- [9. Limpiar un diccionario](#9-limpiar-un-diccionario)
- [10. Eliminar un diccionario](#10-eliminar-un-diccionario)
- [11. Copiar un diccionario](#11-copiar-un-diccionario)
- [12. Obtener claves de diccionario como una lista](#12-obtener-claves-de-diccionario-como-una-lista)
- [13. Obtener valores del diccionario como una lista](#13-obtener-valores-del-diccionario-como-una-lista)
- [13. Ejercicios](#13-ejercicios)

<a name = "1-qué-es-un-diccionario"></a>

## 1. ¿Qué es un diccionario?

Los diccionarios en Python son estructuras de datos que almacenan pares de clave-valor. Son mutables, desordenados y muy eficientes para buscar valores por clave.

- Características principales:
    - Se definen con llaves {}
    - Cada elemento tiene una clave y un valor separados por dos puntos :
    - Las claves deben ser inmutables (strings, números, tuplas)
    - Los valores pueden ser de cualquier tipo
    - No permiten claves duplicadas

Ejemplo:
```python
# Sintaxis
diccionario_vacio = {}
diccionario = {"clave_1":"valor_1", "clave_2":"valor_2", "clave_3":"valor_3"}
# Ejemplo
alumno_1 = {
    "nombre": "Pepe",
    "apellido": "Gomez",
    "edad":23,
    "pais": "España",
    "asignaturas":["Mates","Lengua","Ingles","Sociales"],
    "direccion": {"calle":"falsa 123",
                  "codigo_postal": 25342
                  }
}
```

<a name = "2-longitud-del-diccionario"></a>

## 2. Longitud del diccionario

Para comprobar la lóngitud del diccionario usamos _len()_ como ya hemos visto anteriormente, Ejemplo:
```python
# Sintaxis
diccionario = {"clave_1":"valor_1", "clave_2":"valor_2", "clave_3":"valor_3"}
print(len(diccionario)) #4
# Ejemplo
alumno_1 = {
    "nombre": "Pepe",
    "apellido": "Gomez",
    "edad":23,
    "pais": "España",
    "asignaturas":["Mates","Lengua","Ingles","Sociales"],
    "direccion": {"calle":"falsa 123",
                  "codigo_postal": 25342
                  }
}
print(len(alumno_1))   # 6
```

<a name = "3-acceso-a-los-elementos-del-diccionario"></a>

## 2. Acceso a los elementos del diccionario

Podemos acceder a los elementos del diccionario haciendo referencia a su clave. Ejemplo:
```python
# Sintaxis
diccionario = {"clave_1":"valor_1", "clave_2":"valor_2", "clave_3":"valor_3"}
print(diccionario["clave_1"])
print(diccionario["clave_2"])
# Ejemplo
alumno_1 = {
    "nombre": "Pepe",
    "apellido": "Gomez",
    "edad":23,
    "pais": "España",
    "asignaturas":["Mates","Lengua","Ingles","Sociales"],
    "direccion": {"calle":"falsa 123",
                  "codigo_postal": 25342
                  }
}
print(alumno_1["nombre"]) # Pepe
print(alumno_1["apellido"]) # Gomez
```

>[!WARNING]
>Tenemos que tener en cuenta que si la clave no existe en el diccionario arrojará un error por eso accedemos con el método get y si la clave no existe devolverá `None`

```python
alumno_1 = {
    "nombre": "Pepe",
    "apellido": "Gomez",
    "edad":23,
    "pais": "España",
    "asignaturas":["Mates","Lengua","Ingles","Sociales"],
    "direccion": {"calle":"falsa 123",
                  "codigo_postal": 25342
                  }
}
print(alumno_1.get("nombre")) # Pepe
print(alumno_1.get("apellido")) # Gomez
print(alumno_1.get("estado_civil")) # None
```

>[!CAUTION]
>Hay que fijarse que si accedemos al diccionario directamente se usa `[]`y si lo hacemos con el método get usamos `()`


<a name = "4-agregar-elementos-a-un-diccionario"></a>

## 4. Agregar elementos a un diccionario

- Para agregar nuevos pares de clave-valor es muy sencillo, tan solo hace falta hacer referencia al diccionario, escribir la clave y el valor, veamos un ejemplo.
```python
#Sintaxis
diccionario = {"clave_1":"valor_1", "clave_2":"valor_2", "clave_3":"valor_3"}
diccionarop["calve_4"] = "valor_4"
# Ejemplo
alumno_1 = {
    "nombre": "Pepe",
    "apellido": "Gomez",
    "edad":23,
    "pais": "España",
    "asignaturas":["Mates","Lengua","Ingles","Sociales"],
    "direccion": {"calle":"falsa 123",
                  "codigo_postal": 25342
                  }
}
alumno_1["Documento_identidad"] = "09578864S"
print(alumno_1)
```

- Si queremos agregar un nuevo valor a la lista que tenemos como asignaturas usaremos el método append, ejemplo.
```python
# Sintaxis
diccionario = {"clave_1":"valor_1", 
    "clave_2":"valor_2", 
    "clave_3":["valor_3", "valor_4", "valor_5"]}
diccionarop["clave_3"].append("valor_6")
# Ejemplo
alumno_1 = {
    "nombre": "Pepe",
    "apellido": "Gomez",
    "edad":23,
    "pais": "España",
    "asignaturas":["Mates","Lengua","Ingles","Sociales"],
    "direccion": {"calle":"falsa 123",
                  "codigo_postal": 25342
                  }
}
alumno_1["asignaturas"].append("Fisica")
print(alumno_1) # {'nombre': 'Pepe', 'apellido': 'Gomez', 'edad': 23, 'pais': 'Espa�a', 'asignaturas': ['Mates', 'Lengua', 'Ingles', 'Sociales'], 'direccion': {'calle': 'falsa 123', 'codigo_postal': 25342}, 'Documento_identidad': '09578864S'}
```

<a name = "5-modificar-elementos-de-un-diccionario"></a>

## 5. Modificar elementos de un diccionario

Si queremos modificar elementos de un diccionario es tan sencillo como agregar pero especificando el nombre de la clave.
```python
# Sintaxis
diccionario = {"clave_1":"valor_1", "clave_2":"valor_2", "clave_3":"valor_3"}
diccionarop["calve_2"] = "valor-dos"
# Ejemplo
alumno_1 = {
    "nombre": "Pepe",
    "apellido": "Gomez",
    "edad":23,
    "pais": "España",
    "asignaturas":["Mates","Lengua","Ingles","Sociales"],
    "direccion": {"calle":"falsa 123",
                  "codigo_postal": 25342
                  }
}
alumno_1["nombre"] = ("Jesus")
print(alumno_1) # {'nombre': 'Jesus', 'apellido': 'Gomez', 'edad': 23, 'pais': 'Espa�a', 'asignaturas': ['Mates', 'Lengua', 'Ingles', 'Sociales'], 'direccion': {'calle': 'falsa 123', 'codigo_postal': 25342}}
```

<a name = "6-comprobar-las-claves-de-un-diccionario"></a>

## 6. Comprobar las claves de un diccionario

Si queremos comprobar las claves de un diccionario usamos el operador _in_ que ya vimos en ocasiones anteriores.
```python
# Sintaxis
diccionario = {"clave_1":"valor_1", "clave_2":"valor_2", "clave_3":"valor_3"}
print("clave_2" in diccionario) # True
print("clave_4" in diccionario) # False
# Ejemplo
alumno_1 = {
    "nombre": "Pepe",
    "apellido": "Gomez",
    "edad":23,
    "pais": "España",
    "asignaturas":["Mates","Lengua","Ingles","Sociales"],
    "direccion": {"calle":"falsa 123",
                  "codigo_postal": 25342
                  }
}
print("nombre" in alumno_1) # True
print("estado_civil" in alumno_1) # False
```

<a name = "7-cómo-eliminar-pares-clave-valor-de-un-diccionario"></a>

## 7. Cómo eliminar pares clave-valor de un diccionario

Para eliminar pares podemos usar varias formas que explico a continuación.
- _popitem()_: elimina el último elemento.
- _pop(clave)_: elimina el elemento con el nombre de clave especificado
- _del_ elimina un elemento con el nombre de clave que se especifique.
```python
# Sintaxis
diccionario = {"clave_1":"valor_1", "clave_2":"valor_2", "clave_3":"valor_3"}
diccionario.pop("clave_1") # Elimina el elemento con clave "clave_1"
diccionario.popintem() # eliminará el último elemento en este caso "clave_3":"valor_3"
del diccionario["clave_2"] # Elimina el elemento con clave "clave_2"
# Ejemplo
alumno_1 = {
    "nombre": "Pepe",
    "apellido": "Gomez",
    "edad":23,
    "pais": "España",
    "asignaturas":["Mates","Lengua","Ingles","Sociales"],
    "direccion": {"calle":"falsa 123",
                  "codigo_postal": 25342
                  }
}
alumno_1.pop("edad")
alumno_1.popitem()
del alumno_1["pais"]
print(alumno_1) # {'nombre': 'Pepe', 'apellido': 'Gomez', 'asignaturas': ['Mates', 'Lengua', 'Ingles', 'Sociales']}
```

<a name = "8-cambiar-el-diccionario-a-una-lista"></a>

## 8. Cambiar el diccionario a una lista

Podemos realizar un cambio de diccionario a una lista de tuplas para realizar trabajo con ellos de manera más flexible para ello usamos el método _items()_.
```python
# Sintaxis
diccionario = {"clave_1":"valor_1", "clave_2":"valor_2", "clave_3":"valor_3"}
print(diccionario.items()) # dict_items([('clave_1', 'valor_1'), ('clave_2', 'valor_2'), ('clave_3', 'valor_3')])
# Ejemplo
alumno_1 = {
    "nombre": "Pepe",
    "apellido": "Gomez",
    "edad":23,
    "pais": "España",
    "asignaturas":["Mates","Lengua","Ingles","Sociales"],
    "direccion": {"calle":"falsa 123",
                  "codigo_postal": 25342
                  }
}
print(alumno_1.items()) # dict_items([('nombre', 'Pepe'), ('apellido', 'Gomez'), ('edad', 23), ('pais', 'Espa�a'), ('asignaturas', ['Mates', 'Lengua', 'Ingles', 'Sociales']), ('direccion', {'calle': 'falsa 123', 'codigo_postal': 25342})])
```

<a name = "9-limpiar-un-diccionario"></a>

## 9. Limpiar un diccionario

Si no queremos los elementos de un diccionario podemos usar el método _clear()_ para limpiar el diccionario por completo.
```python
# Sintaxis
diccionario = {"clave_1":"valor_1", "clave_2":"valor_2", "clave_3":"valor_3"}
print(diccionario.clear()) # None
# Ejemplo
alumno_1 = {
    "nombre": "Pepe",
    "apellido": "Gomez",
    "edad":23,
    "pais": "España",
    "asignaturas":["Mates","Lengua","Ingles","Sociales"],
    "direccion": {"calle":"falsa 123",
                  "codigo_postal": 25342
                  }
}
print(alumno_1.clear()) # None
print(alumno_1) # {}
print(type(alumno_1)) # <class 'dict'>
```

>[!NOTE]
>Como podemos ver el diccionario no se elimina tan solo limpia todos los pares clave-valor que contiene, si queremos eliminarlo mira el siguiente paso.

<a name = "10-eliminar-un-diccionario"></a>

## 10. Eliminar un diccionario

Para eliminar un diccionario es tan facil como las listas, las tuplas y los Conjuntos.
```python
# Sintaxis
diccionario = {"clave_1":"valor_1", "clave_2":"valor_2", "clave_3":"valor_3"}
del diccionario
print(diccionario) # NameError: name 'diccionario' is not defined
```

<a name = "11-copiar-un-diccionario"></a>

## 11. Copiar un diccionario

Si lo que queremos es evitar modificar el diccionario original podemos usar el método _copy()_, ejemplo.
```python
# Sintaxis
diccionario = {"clave_1":"valor_1", "clave_2":"valor_2", "clave_3":"valor_3"}
copia_diccionario = diccionario.copy()
print(copia_diccionario) # {'clave_1': 'valor_1', 'clave_2': 'valor_2', 'clave_3': 'valor_3'}
```

<a name = "12-obtener-claves-de-diccionario-como-una-lista"></a>

## 12. Obtener claves de diccionario como una lista

Para obtener todas las claves del diccionario como una lista usamos el método _key()_
```python
# Sintaxis
diccionario = {"clave_1":"valor_1", "clave_2":"valor_2", "clave_3":"valor_3"}
claves = diccionario.keys()
print(claves) # dict_keys(['clave_1', 'clave_2', 'clave_3'])
# Ejemplo
alumno_1 = {
    "nombre": "Pepe",
    "apellido": "Gomez",
    "edad":23,
    "pais": "España",
    "asignaturas":["Mates","Lengua","Ingles","Sociales"],
    "direccion": {"calle":"falsa 123",
                  "codigo_postal": 25342
                  }
}
claves_alumno_1 = alumno_1.keys()
print(claves_alumno_1) # dict_keys(['nombre', 'apellido', 'edad', 'pais', 'asignaturas', 'direccion'])
```

<a name = "13-obtener-valores-del-diccionario-como-una-lista"></a>

## 13. Obtener valores del diccionario como una lista

Si queremos obtener los valores del diccionario es tan fácil como el método anterior pero ahora usamos el método _values()_.
```python
# Sintaxis
diccionario = {"clave_1":"valor_1", "clave_2":"valor_2", "clave_3":"valor_3"}
valores = diccionario.values()
print(valores) # dict_values(['valor_1', 'valor_2', 'valor_3'])
# Ejemplo
alumno_1 = {
    "nombre": "Pepe",
    "apellido": "Gomez",
    "edad":23,
    "pais": "España",
    "asignaturas":["Mates","Lengua","Ingles","Sociales"],
    "direccion": {"calle":"falsa 123",
                  "codigo_postal": 25342
                  }
}
valores_alumno_1 = alumno_1.values()
print(valores_alumno_1) # dict_values(['Pepe', 'Gomez', 23, 'Espa�a', ['Mates', 'Lengua', 'Ingles', 'Sociales'], {'calle': 'falsa 123', 'codigo_postal': 25342}])
```

😁 ¡Excelente! Ya sabes todo lo que tienes que saber sobre diccionarios para manejarte con ellos, vamos ahora a por unos ejercicios.

<a name="13-ejercicios"></a>

## 13. Ejercicios

- Crea un diccionario vacio llamado casa.
- Agrega al diccionario casa, pais, ciudad, código postal, nombre de la casa. 
- Crea un diccionario coche y añade la marca, modelo, cilindrada, potencia, color, número de puertas, matrícula, extras, ciudad donde aparcas y código postal.
- Obten la longitud del diccionario coche.
- Imprime el tipo de dato que es extras y los valores que tiene.
- Agrega algún extra que quieres que tenga.
- Pasa el diccionario a una lista.
- Imprime por pantalla solo las claves del diccionario coche.
- Almacena en una variable los valores del diccionario coche.
- Elimina la clave matrícula del diccionario.
- Limpia el diccionario casa.
- Elimina por completo uno de los dos diccionarios.

[Solución ejercicios](./ejercicios.py)


<h3 align="center"> Estás a un paso menos de saber programar en python</h3>


<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/05_Tuplas/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/07_Diccionarios/readme.md">Siguiente Capítulo</a>
</h4>