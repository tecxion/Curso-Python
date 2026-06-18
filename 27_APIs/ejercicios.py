"""
Ejercicios de Consumir APIs Web (requests)

REQUISITOS:
  - Conexión a internet.
  - Instalar la librería:  pip install requests
Si no tienes 'requests' instalada, el programa te avisará amablemente.
"""
try:
    import requests
except ImportError:
    print("Necesitas instalar requests:  pip install requests")
    raise SystemExit

BASE = "https://jsonplaceholder.typicode.com"


def main():
    # 1. Petición GET e imprimir el código de estado.
    respuesta = requests.get(f"{BASE}/todos/1", timeout=5)
    print(f"Código de estado: {respuesta.status_code}")

    # 2. Convertir a JSON e imprimir el título.
    print(f"Título: {respuesta.json()['title']}")

    # 3. Datos del usuario 2.
    usuario = requests.get(f"{BASE}/users/2", timeout=5).json()
    print(f"Nombre: {usuario['name']}")
    print(f"Email: {usuario['email']}")
    print(f"Ciudad: {usuario['address']['city']}")

    # 4. Número total de posts.
    posts = requests.get(f"{BASE}/posts", timeout=5).json()
    print(f"Hay {len(posts)} posts en total")

    # 5. Posts del usuario 1 con params.
    posts_user1 = requests.get(f"{BASE}/posts", params={"userId": 1}, timeout=5).json()
    print(f"El usuario 1 tiene {len(posts_user1)} posts")

    # 6. Función obtener_post(id) con control de 404.
    def obtener_post(id):
        respuesta = requests.get(f"{BASE}/posts/{id}", timeout=5)
        if respuesta.status_code == 404:
            return "Ese post no existe"
        return respuesta.json()["title"]
    print(f"Post 5: {obtener_post(5)}")
    print(f"Post 9999: {obtener_post(9999)}")

    # 7. Contar todos completados del usuario 1.
    todos = requests.get(f"{BASE}/todos", params={"userId": 1}, timeout=5).json()
    completados = [t for t in todos if t["completed"]]
    print(f"El usuario 1 ha completado {len(completados)} de {len(todos)} tareas")


# 8. Envolver todo en un try/except completo de red.
if __name__ == "__main__":
    try:
        main()
    except requests.exceptions.ConnectionError:
        print("No hay conexión a internet.")
    except requests.exceptions.Timeout:
        print("El servidor tardó demasiado en responder.")
    except requests.exceptions.HTTPError as error:
        print(f"Error en la respuesta: {error}")
