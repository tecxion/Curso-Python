# Manual de Comandos de Terminal para Python

Comandos esenciales de terminal para Windows, macOS y Linux organizados por plataforma.

---

## 🔵 Windows (CMD/PowerShell)

### Navegación y Archivos
| Comando            | Descripción                   |
| ------------------ | ----------------------------- |
| `dir`              | Listar archivos y directorios |
| `cd <ruta>`        | Cambiar directorio            |
| `mkdir <nombre>`   | Crear directorio              |
| `del <archivo>`    | Eliminar archivo              |
| `copy <or> <dest>` | Copiar archivos               |
| `move <or> <dest>` | Mover/renombrar archivos      |

### Python
| Comando              | Descripción                |
| -------------------- | -------------------------- |
| `python --version`   | Ver versión de Python      |
| `python <script.py>` | Ejecutar script Python     |
| `pip install <paq>`  | Instalar paquete           |
| `pip list`           | Listar paquetes instalados |

### Utilidades
| Comando        | Descripción        |
| -------------- | ------------------ |
| `cls`          | Limpiar pantalla   |
| `where python` | Ver ruta de Python |

---

## 🍎 macOS (Terminal)

### Navegación y Archivos
| Comando          | Descripción               |
| ---------------- | ------------------------- |
| `ls`             | Listar archivos           |
| `cd <ruta>`      | Cambiar directorio        |
| `pwd`            | Mostrar directorio actual |
| `mkdir <nombre>` | Crear directorio          |
| `rm <archivo>`   | Eliminar archivo          |
| `cp <or> <dest>` | Copiar archivos           |
| `mv <or> <dest>` | Mover/renombrar archivos  |

### Python
| Comando               | Descripción                |
| --------------------- | -------------------------- |
| `python3 --version`   | Ver versión de Python      |
| `python3 <script.py>` | Ejecutar script Python     |
| `pip3 install <paq>`  | Instalar paquete           |
| `pip3 list`           | Listar paquetes instalados |

### Utilidades
| Comando         | Descripción        |
| --------------- | ------------------ |
| `clear`         | Limpiar pantalla   |
| `which python3` | Ver ruta de Python |

---

## 🐧 Linux (Terminal)

### Navegación y Archivos
| Comando          | Descripción               |
| ---------------- | ------------------------- |
| `ls`             | Listar archivos           |
| `cd <ruta>`      | Cambiar directorio        |
| `pwd`            | Mostrar directorio actual |
| `mkdir <nombre>` | Crear directorio          |
| `rm <archivo>`   | Eliminar archivo          |
| `cp <or> <dest>` | Copiar archivos           |
| `mv <or> <dest>` | Mover/renombrar archivos  |

### Python
| Comando               | Descripción                |
| --------------------- | -------------------------- |
| `python3 --version`   | Ver versión de Python      |
| `python3 <script.py>` | Ejecutar script Python     |
| `pip3 install <paq>`  | Instalar paquete           |
| `pip3 list`           | Listar paquetes instalados |

### Utilidades
| Comando                  | Descripción                       |
| ------------------------ | --------------------------------- |
| `clear`                  | Limpiar pantalla                  |
| `which python3`          | Ver ruta de Python                |
| `sudo apt install <pkg>` | Instalar paquetes (Debian/Ubuntu) |

---

## 🔄 Comandos Universales para Python
| Comando                                 | Descripción                |
| --------------------------------------- | -------------------------- |
| `python -m venv <env>`                  | Crear entorno virtual      |
| `source env/bin/activate` (macOS/Linux) | Activar entorno virtual    |
| `.\env\Scripts\activate` (Windows)      | Activar entorno virtual    |
| `deactivate`                            | Desactivar entorno virtual |

> 💡 Tip: En Windows 10/11 también puedes usar WSL (Windows Subsystem for Linux) para comandos tipo Unix.