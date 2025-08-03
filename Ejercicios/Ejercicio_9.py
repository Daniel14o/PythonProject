"""
Ejercicio 9: Agenda de Contactos con Diccionario

Este programa permite gestionar una agenda de contactos usando un diccionario
El usuario puede agregar nuevos contactos, buscar por nombre y ver todos los contactos registrados

Conceptos aplicados: Diccionarios, funciones, input(), bucle for para
iterar sobre diccionarios
"""

def agregar_contacto(agenda: dict, nombre: str, telefono: str) -> None:
    """
    Agrega un nuevo contacto a la agenda

    :param agenda: Diccionario de contactos.
    :param nombre: Nombre del contacto.
    :param telefono: Numero de teléfono del contacto.
    """
    agenda[nombre] = telefono
    print(f"Contacto '{nombre}' agregado correctamente.")

def buscar_contacto(agenda: dict, nombre: str) -> None:
    """
    Busca y muestra el número de teléfono de un contacto

    :param agenda: Diccionario de contactos.
    :param nombre: Nombre del contacto a buscar.
    """
    if nombre in agenda:
        print(f"{nombre}: {agenda[nombre]}")
    else:
        print(f"El contacto '{nombre}' no se encuentra en la agenda.")

def mostrar_contactos(agenda: dict) -> None:
    """
    Muestra todos los contactos registrados en la agenda

    :param agenda: Diccionario de contactos.
    """
    if agenda:
        print("Lista de contactos:")
        for nombre, telefono in agenda.items():
            print(f"- {nombre}: {telefono}")
    else:
        print("La agenda está vacía.")

def menu_agenda():
    """
    Muestra el menú principal y gestiona las opciones del usuario
    """
    agenda = {}
    while True:
        print("\n--- Agenda de Contactos ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Mostrar todos los contactos")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del contacto: ")
            telefono = input("Teléfono del contacto: ")
            agregar_contacto(agenda, nombre, telefono)
        elif opcion == "2":
            nombre = input("Nombre del contacto a buscar: ")
            buscar_contacto(agenda, nombre)
        elif opcion == "3":
            mostrar_contactos(agenda)
        elif opcion == "4":
            print("Saliendo de la agenda...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu_agenda()