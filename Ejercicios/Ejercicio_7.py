"""
Ejercicio 7: Lista de Compras Interactiva

Este programa permite al usuario gestionar una lista de compras mediante un menú interactivo.
Se pueden agregar ítems, eliminar ítems, ver la lista completa y salir del programa.

Conceptos aplicados: Listas (métodos append, remove), bucle while,
if/elif/else, input().
"""

def mostrar_menu():
    """
    Muestra el menú de opciones disponibles al usuario.
    """
    print("\n--- Menú de Lista de Compras ---")
    print("1. Agregar ítem a la lista")
    print("2. Eliminar ítem de la lista")
    print("3. Ver la lista completa")
    print("4. Salir")

def lista_compras_interactiva():
    """
    Función principal que ejecuta el menú y permite al usuario interactuar con la lista.
    """
    lista = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            item = input("Ingrese el nombre del ítem: ").strip()
            if item:
                lista.append(item)
                print(f"'{item}' fue agregado a la lista.")
            else:
                print("No se ingresó ningún ítem.")

        elif opcion == "2":
            item = input("Ingrese el nombre del ítem a eliminar: ").strip()
            if item in lista:
                lista.remove(item)
                print(f"'{item}' fue eliminado de la lista.")
            else:
                print(f"'{item}' no está en la lista.")

        elif opcion == "3":
            if lista:
                print("\nLista de Compras:")
                for i, item in enumerate(lista, 1):
                    print(f"{i}. {item}")
            else:
                print("La lista está vacía.")

        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    lista_compras_interactiva()