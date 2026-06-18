"""
main.py
Punto de entrada del Gestor de Tareas TecXion.
Muestra el menú, lee lo que escribe el usuario y llama al GestorTareas.

Ejecutar con:   python main.py     (o python3 main.py)
"""
from gestor import GestorTareas


def mostrar_menu():
    print("\n========== GESTOR DE TAREAS TECXION ==========")
    print("1. Ver todas las tareas")
    print("2. Ver solo pendientes")
    print("3. Añadir tarea")
    print("4. Marcar tarea como completada")
    print("5. Eliminar tarea")
    print("6. Salir")
    print("==============================================")


def mostrar_tareas(tareas):
    if not tareas:
        print("\n  (No hay tareas para mostrar)")
        return
    print()
    for numero, tarea in enumerate(tareas, start=1):
        print(f"  {numero}. {tarea}")


def pedir_numero(mensaje):
    """Pide un número entero y controla que lo sea (día 14: errores)."""
    try:
        return int(input(mensaje))
    except ValueError:
        print("Debes escribir un número.")
        return None


def main():
    gestor = GestorTareas()
    print("¡Bienvenido a tu gestor de tareas!")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ").strip()

        if opcion == "1":
            mostrar_tareas(gestor.tareas)

        elif opcion == "2":
            mostrar_tareas(gestor.pendientes())

        elif opcion == "3":
            titulo = input("Título de la tarea: ").strip()
            if not titulo:
                print("El título no puede estar vacío.")
                continue
            prioridad = input("Prioridad (alta/media/baja): ").strip().lower()
            gestor.agregar(titulo, prioridad)
            print(f"Tarea '{titulo}' añadida.")

        elif opcion == "4":
            mostrar_tareas(gestor.tareas)
            numero = pedir_numero("Número de la tarea a completar: ")
            if numero is not None and gestor.completar(numero - 1):
                print("Tarea marcada como completada.")
            else:
                print("Ese número de tarea no existe.")

        elif opcion == "5":
            mostrar_tareas(gestor.tareas)
            numero = pedir_numero("Número de la tarea a eliminar: ")
            if numero is not None:
                eliminada = gestor.eliminar(numero - 1)
                if eliminada:
                    print(f"Tarea '{eliminada.titulo}' eliminada.")
                else:
                    print("Ese número de tarea no existe.")

        elif opcion == "6":
            print("¡Hasta pronto! Tus tareas quedan guardadas.")
            break

        else:
            print("Opción no válida. Elige un número del 1 al 6.")


if __name__ == "__main__":
    main()
