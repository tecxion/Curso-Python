# Gestor de Tareas Web 🌐

Versión **web full-stack** del gestor de tareas. Es el **segundo proyecto final**
(día 40) del [Curso de Python en 40 días](https://github.com/tecxion/Curso-Python).
Lleva la idea del proyecto de consola (día 39) a la web: misma funcionalidad, pero
con interfaz web, base de datos y lista para desplegar en internet.

## ¿Qué hace?

- Añadir tareas desde un formulario web.
- Marcar tareas como completadas / pendientes.
- Eliminar tareas.
- Guardar todo en una base de datos SQLite (Flask-SQLAlchemy).
- Exponer además una **API JSON** en `/api/tareas`.

## Estructura

```
gestor_web/
├── app.py              # la aplicación y sus rutas
├── models.py           # la base de datos y el modelo Tarea (ORM)
├── templates/          # las plantillas HTML (Jinja2)
│   ├── base.html
│   └── index.html
├── static/
│   └── estilo.css      # los estilos
├── requirements.txt    # dependencias
└── .gitignore
```

## Cómo ejecutarlo en local

```bash
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Abre `http://127.0.0.1:5000` en tu navegador.

## Cómo desplegarlo (Render)

1. Sube el proyecto a GitHub.
2. En Render: **New + → Web Service**, conecta el repo.
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `gunicorn app:app`
5. Plan **Free** → Create. Render te dará una URL pública.

Tienes la guía completa en el [día 38 (Despliegue)](../../38_Despliegue/readme.md).
