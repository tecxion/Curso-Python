<h4 align="center">
<a href="https://github.com/tecxion/Curso-Python/tree/main/11_Listas_2/readme.md">Capítulo anterior</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main">Inicio</a> | <a href="https://github.com/tecxion/Curso-Python/tree/main/13_Funciones_2/readme.md">Siguiente Capítulo</a>
</h4>

<h1 align="center">
<img src="https://github.com/tecxion/Curso-Python/blob/main/Media/modulos.png">
</h1>


<h1 align="center">Módulos</h1><br>

<h3>Índice</h3>

- [1. Módulos](#1-módulos)
  - [1.1 ¿Qué es un módulo?](#11-qué-es-un-módulo)
  - [1.2 Creando un módulo](#12-creando-un-módulo)
  - [1.3 Importar un módulo](#13-importar-un-módulo)
  - [1.4 Importar funciones desde un módulo](#14-importar-funciones-desde-un-módulo)
  - [1.5 Importar funciones desde un módulo y cambiar el nombre](#15-importar-funciones-desde-un-módulo-y-cambiar-el-nombre)
- [2. Importar módulos integrados](#2-importar-módulos-integrados)
  - [2.1 Módulos del sistema operativo](#21-módulos-del-sistema-operativo)
  - [2.2 Módulos del sistema](#22-módulos-del-sistema)
  - [2.3 Módulos de estadísticas](#23-módulos-de-estadísticas)
  - [2.4 Módulo de matemáticas](#24-módulo-de-matemáticas)
  - [2.5 Módulo de cadenas](#25-módulo-de-cadenas)
  - [2.6 Módulo aleatorio](#26-módulo-aleatorio)
- [3. Ejercicios](#3-ejercicios)



<a name = "1-módulos"></a>

## 1. Módulos

Los módulos son uno de los pilares fundamentales de Python, permitiendo organizar y reutilizar código de manera eficiente.


<a name = "11-qué-es-un-módulo"></a>

### 1.1 ¿Qué es un módulo?

Un módulo es un archivo .py que contiene:
- Funciones.
- Clases.
- Variables.
- Código jecutable.

<a name= "12-creando-un-módulo"></a>

### 1.2 Creando un módulo

Para crear un módulo, escribimos nuestro código en un script de Python y lo guardamos como un archivo .py.
- Vamos a comenzar creando un archivo en la carpeta del capítulo un archivo que se llame mi_modulo.py y escribamos código en el.
```python
# mi_modulo.py código
def nombre_completo(nombre, apellido):
    return nombre + " " + apellido
```
ahora crea otro archivo que se llame principal.py e importamos el archivo mi_modulo.py

<a name = "13-importar-un-módulo" ></a>

### 1.3 Importar un módulo

- Para importar un módulo usamos la palabra reservada import y solo el nombre del archivo sin la extensión.

```python
# Sintaxis
import nombre_modulo 
# archivo principal.py
import mi_modulo
print(mi_modulo.nombre_completo("Paco", "Pascal"))
```

>[!NOTE]
>Prueba con los códigos anteriores y ejecuta el principal.py, te animo a que pruebes con otras funciones a ver que vas consiguiendo.


<a name = "14-importar-funciones-desde-un-módulo"></a>

### 1.4 Importar funciones desde un módulo

En un módulo podemos tener diferentes funciones y se pueden importar de forma diferente, para eso usaremos la siguiente sintaxis:
```python
# Sintaxis
from nombre_modulo import nombre_funciones
```

añade la función sumar a mi_modulo.py y probamos.
```python
# función nueva en mi_modulo.py
def sumar(a, b):
    return a + b
# el archivo principal.py se verá asi.
from mi_modulo import sumar, nombre_completo
print(nombre_completo("Paco", "Gimenez"))
print(sumar(3, 6))
```

<a name = "15-importar-funciones-desde-un-módulo-y-cambiar-el-nombre" ></a>

### 1.5 Importar funciones desde un módulo y cambiar el nombre

- Durante la importación de las funciones podemos cambiar el nombre del módulo, esto es util para organizarnos nosotros.
```python
# en el principal.py
from mi_modulo import nombre_completo as nombres, sumar as suma_numeros
print(nombres("Paco", "Pozas"))
print(suma_numeros(3, 1))

```

--- 

<a name="2-importar-módulos-integrados"></a>

## 2. Importar módulos integrados

Al igual que en java había que importar diferentes módulos que ya venían con el lenguaje en python tenemos lo mismo, los módulos integrados que se usan con más frecuencia son: _math_, _datetime_, _os_, _sys_, _random_, _statistical_, _collections_, _json_ y _re_.

- A continuación explico los más utilizados

<a name = "21-módulos-del-sistema-operativo" ></a>

### 2.1 Módulos del sistema operativo

El módulo os en Python proporciona funciones para interactuar con el sistema operativo, permitiendo manejar archivos, directorios, variables de entorno y procesos.
```python
# Importamos el módulo
import os
# Crear una carpeta
os.mkdir("carpeta_1")
# Cambiar al directorio actual
os.chdir("path")
# Obtener el directorio actual de trabajo
os.getcwd()
# Eliminar el directorio
os.rmdir()
```

- A continuación te dejo un fichero para que sepas más sobre el módulo os [Ver módulo](./os.md)

<a name = "22-módulos-del-sistema" ></a>

### 2.2 Módulos del sistema

<a name = "23-módulos-de-estadísticas" ></a>

### 2.3 Módulos de estadísticas

<a name = "24-módulo-de-matemáticas" ></a>

### 2.4 Módulo de matemáticas

<a name = "25-módulo-de-cadenas" ></a>

### 2.5 Módulo de cadenas

<a name = "26-módulo-aleatorio" ></a>

### 2.6 Módulo aleatorio

<a name = "3-ejercicios" ></a>

## 3. Ejercicios