# Módulo sys

## 📌 Funciones y Atributos Principales

| Comando/Atributo        | Descripción                                         | Ejemplo                                                    |
| ----------------------- | --------------------------------------------------- | ---------------------------------------------------------- |
| sys.argv                | Lista de argumentos de línea de comandos            | python script.py arg1 arg2 → ['script.py', 'arg1', 'arg2'] |
| sys.path                | Lista de rutas donde Python busca módulos           | sys.path.append('/nueva/ruta')                             |
| sys.exit()              | Termina la ejecución del programa                   | sys.exit(1) (código de error)                              |
| sys.version             | Versión de Python instalada                         | print(sys.version)                                         |
| sys.platform            | Sistema operativo (win32, linux, darwin para macOS) | if sys.platform == 'win32': ...                            |
| sys.stdin/stdout/stderr | Flujos de entrada/salida estándar                   | sys.stdout.write("Hola")                                   |
| sys.getsizeof()         | Tamaño en bytes de un objeto                        | sys.getsizeof(lista)                                       |
| sys.modules             | Diccionario de módulos importados                   | 'math' in sys.modules                                      |

## 🖥️ Diferencias entre Sistemas Operativos

| Característica    | Windows               | Linux/macOS       |
| ----------------- | --------------------- | ----------------- |
| Rutas             | Usa \ (o \\ escapado) | Usa /             |
| Ejecutables       | .exe                  | Sin extensión     |
| sys.platform      | win32                 | linux o darwin    |
| Línea de comandos | cmd o PowerShell      | Terminal bash/zsh |


## ⚠️ Consideraciones Cruzadas

Rutas: Usa os.path.join() para compatibilidad multiplataforma:
```python
import os
ruta = os.path.join('carpeta', 'archivo.txt')
```
Ejecución: Los scripts Python (.py) funcionan igual en todos los sistemas si el intérprete está instalado.

## 🔧 Comandos Útiles en Terminal

| Comando            | Windows            | Linux/macOS         |
| ------------------ | ------------------ | ------------------- |
| Ejecutar script    | python script.py   | python3 script.py   |
| Ver versión Python | python --version   | python3 --version   |
| Instalar módulo    | pip install modulo | pip3 install modulo |


## 📂 Ejemplos Prácticos
1. Manejo de argumentos (sys.argv)
```python
import sys

if len(sys.argv) > 1:
    print(f"Argumentos recibidos: {sys.argv[1:]}")
else:
    print("No se pasaron argumentos")
```
- Uso en la terminal pon
  - python script.py hola 123

2. Verificar SO
```python
import sys

if sys.platform.startswith('win'):
    print("Ejecutando en Windows")
elif sys.platform == 'linux':
    print("Ejecutando en Linux")
elif sys.platform == 'darwin':
    print("Ejecutando en macOS")

```

[Volver al Readme de módulos](../readme.md/#221-documento-relacionado-con-módulo-sys)