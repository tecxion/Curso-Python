# CURSO de Python desde 0

Bienvenidos este curso aprenderemos a programar en python, no soy experto en ello y a la vez que genero este pequeño curos voy aprendiendo a programar en python, actualmente se java y dart como se puede observar en los repositorios.


>[!NOTE]
>Cualquier duda puedes ponerte conmigo en contacto en mi mail en tecxart@gmail.com
>Al final de este readme teneis recursos que os pueden ayudar a aprender o mejorar en este lenguaje.

**Recursos al pie del readme[^1].**

---

## ¿Qué es Python?

Python es un lenguaje de programación interpretado, de alto nivel y propósito general. Es conocido por su sintaxis clara y legible, lo que lo convierte en una excelente opción tanto para principiantes como para desarrolladores experimentados. Python se utiliza en una amplia variedad de campos, como desarrollo web, análisis de datos, inteligencia artificial, automatización, y mucho más.

---
### Índice del Curso:

1. [Instalación](#instala)
    - [Configuración del IDE (VS Code)](#configuraciónide)
2. [Variables](01_Variables/readme.md)
      * [Variables](01_Variables/readme.md/#variables)
        * [Tipos de variables](01_Variables/readme.md/#tiposdevariables)
        * [Declarar múltiples variables en una línea](01_Variables/readme.md/#multiplesvariableslinea)
      * [Tipos de dato y conversión](01_Variables/readme.md/#tiposdato)
        * [Tipos](01_Variables/readme.md/#tipos)
        * [conversion](01_Variables/readme.md/#conversion)

--- 

<a name="#instala"></a>
## Instalación de Python 

Antes de comenzar, necesitarás instalar Python en tu computadora. A continuación, te proporcionamos instrucciones para instalar Python en diferentes sistemas operativos.
<br>
[1- Instalación en Windows](#instalawindows)<br>
[2- Instalación en MacOS](#2-instalacion-en-macos)<br>
[3- Instalación en Linux](#3-instalacion-en-linux)<br>

---

<a name="instalawindows"></a>

### 1. Instalación en Windows

1. **Descarga el instalador:**
   - Ve al sitio oficial de Python: [https://www.python.org/ ](https://www.python.org/ ).
   - Haz clic en la pestaña "Downloads" y selecciona la versión adecuada para Windows (generalmente la última versión estable).

2. **Ejecuta el instalador:**
   - Abre el archivo descargado.
   - Asegúrate de marcar la casilla que dice **"Add Python to PATH"** antes de hacer clic en "Install Now".

3. **Verifica la instalación:**
   - Abre una terminal (Command Prompt o PowerShell) y ejecuta el siguiente comando:
     ```bash
     python --version
     ```
   - Si la instalación fue exitosa, verás la versión de Python instalada.

---

<a name="2-instalacion-en-macos"></a>

### 2. Instalación en macOS 

1. **Usando Homebrew (recomendado):**
   - Abre la Terminal y ejecuta el siguiente comando para instalar Homebrew (si no lo tienes instalado):
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh )"
     ```
   - Luego, instala Python con el siguiente comando:
     ```bash
     brew install python
     ```

2. **Descarga desde el sitio oficial:**
   - Ve al sitio oficial de Python: [https://www.python.org/ ](https://www.python.org/ ).
   - Descarga el instalador para macOS y sigue las instrucciones.

3. **Verifica la instalación:**
   - En la Terminal, ejecuta:
     ```bash
     python3 --version
     ```
   - Deberías ver la versión de Python instalada.

---
<a name="3-instalacion-en-linux"></a>

### 3. Instalación en Linux

La mayoría de las distribuciones de Linux vienen con Python preinstalado. Sin embargo, puedes verificar la versión o actualizarla si es necesario.

1. **Verifica la versión actual:**
   - Abre una terminal y ejecuta:
     ```bash
     python3 --version
     ```

2. **Instala o actualiza Python:**
   - Para Ubuntu/Debian:
     ```bash
     sudo apt update
     sudo apt install python3
     ```
   - Para Fedora:
     ```bash
     sudo dnf install python3
     ```

3. **Instala pip (gestor de paquetes de Python):**
   - Ejecuta el siguiente comando:
     ```bash
     sudo apt install python3-pip
     ```

4. **Verifica la instalación:**
   - Ejecuta nuevamente:
     ```bash
     python3 --version
     ```

---

<a name="#configuraciónide"></a>

# Instalación en el IDE 

## Cómo Usar Visual Studio Code con Python

Visual Studio Code (VS Code) es un editor de código ligero pero potente que es ideal para programar en Python. A continuación, te guiaremos a través de los pasos necesarios para configurar VS Code y comenzar a trabajar con Python.

---

## 1. Instalación de Visual Studio Code

Si aún no tienes instalado VS Code, sigue estos pasos:

1. **Descarga VS Code:**
   - Ve al sitio oficial de VS Code: [https://code.visualstudio.com/ ](https://code.visualstudio.com/ ).
   - Descarga la versión adecuada para tu sistema operativo.

2. **Instala VS Code:**
   - Ejecuta el archivo descargado y sigue las instrucciones del instalador.

---

## 2. Configuración de Python en VS Code

Una vez que tengas VS Code instalado, sigue estos pasos para configurarlo para trabajar con Python:

### 2.1. Instala la Extensión de Python

1. Abre VS Code.
2. Haz clic en el icono de **Extensiones** en la barra lateral izquierda (o presiona `Ctrl+Shift+X`).
3. Busca "Python" en la barra de búsqueda.
4. Encuentra la extensión oficial de Python (publicada por Microsoft) y haz clic en **Instalar**.

![Extensión de Python](https://code.visualstudio.com/assets/docs/python/tutorial/python-extension.png )

### 2.2. Selecciona el Intérprete de Python

1. Abre la paleta de comandos presionando `Ctrl+Shift+P` (o `Cmd+Shift+P` en macOS).
2. Escribe "Python: Select Interpreter" y selecciona esta opción.
3. Elige el intérprete de Python que instalaste en tu sistema. Si tienes varias versiones de Python instaladas, asegúrate de seleccionar la correcta.

> **Nota:** Si no ves tu intérprete de Python en la lista, verifica que Python esté correctamente instalado en tu sistema.

---

## 3. Crear y Ejecutar un Archivo Python

Ahora que tienes VS Code configurado, puedes crear y ejecutar archivos Python fácilmente.

### 3.1. Crear un Archivo Python

1. Haz clic en **File > New File** (o presiona `Ctrl+N`).
2. Guarda el archivo con la extensión `.py`, por ejemplo, `hola_mundo.py`.
3. Escribe un programa simple en Python, como este:

- Tambien desde la consola de comandos puedes poner python y te saldra una lista solo tienes que elegir Python: New File.
- Ejemplo: 
   ```python
   print("¡Hola, mundo!")
   ```

### 3.2. Ejecutar el Archivo Python

1. Haz clic en el botón de ejecución (o presiona `F5`).
2. El programa se ejecutará y mostrará el mensaje "¡Hola, mundo!" en la consola.





[^1]: Recursos: - Documentación de Python: [Visitar](https://docs.python.org/es/3.13/contents.html) / [Juego aprender python (Codedex)](https://www.codedex.io/) / [GitHub Mouredev](https://github.com/mouredev/Hello-Python) / y para mi el mejor repositorio pero en lengua inglesa [Asabeneh](https://github.com/Asabeneh/30-Days-Of-Python)



