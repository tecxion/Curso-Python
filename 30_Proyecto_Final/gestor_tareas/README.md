# Gestor de Tareas TecXion 📝

Aplicación de consola para gestionar una lista de tareas. Es el **proyecto final**
del [Curso de Python desde 0](https://github.com/tecxion/Curso-Python) y reúne todo
lo aprendido: clases (POO), manejo de ficheros (JSON), control de errores,
comprensiones y organización de un proyecto en varios archivos.

## ¿Qué hace?

- Añadir tareas con una prioridad (alta / media / baja).
- Ver todas las tareas o solo las pendientes.
- Marcar tareas como completadas.
- Eliminar tareas.
- Guardar todo automáticamente en `tareas.json`, de modo que **al cerrar y volver
  a abrir el programa tus tareas siguen ahí**.

## Estructura del proyecto

```
gestor_tareas/
├── main.py              # Punto de entrada: el menú de la consola
├── gestor.py            # Clase GestorTareas: la lógica principal
├── tarea.py             # Clase Tarea: representa una tarea
├── almacenamiento.py    # Lee y escribe el fichero tareas.json
├── requirements.txt     # Dependencias (este proyecto no necesita externas)
├── .gitignore           # Qué ignora git
└── README.md            # Este archivo
```

## Cómo ejecutarlo

1. Abre una terminal dentro de la carpeta `gestor_tareas`.
2. (Opcional pero recomendado) crea y activa un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate        # En Windows: venv\Scripts\activate
   ```
3. Arranca la aplicación:
   ```bash
   python3 main.py                 # En Windows: python main.py
   ```

¡Y listo! Sigue las opciones del menú escribiendo el número correspondiente.
