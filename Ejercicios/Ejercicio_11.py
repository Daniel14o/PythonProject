"""
Ejercicio 11: Elementos Comunes y Únicos entre Listas

Este programa define una función que recibe dos listas y devuelve una tupla con tres conjuntos:
1. Elementos en común
2. Elementos únicos de la primera lista
3. Elementos únicos de la segunda lista

Conceptos aplicados: Funciones, listas, conjuntos (sets), operadores de
conjuntos (&, -).
"""

def comparar_listas(lista1: list, lista2: list) -> tuple[set, set, set]:
    """
    Compara dos listas y devuelve tres conjuntos:
    - Elementos comunes.
    - Elementos únicos de la primera lista.
    - Elementos únicos de la segunda lista.

    :param lista1: Primera lista de elementos.
    :param lista2: Segunda lista de elementos.
    :return: Tupla con tres conjuntos.
    """
    set1 = set(lista1)
    set2 = set(lista2)

    comunes = set1 & set2
    solo_en_lista1 = set1 - set2
    solo_en_lista2 = set2 - set1

    return comunes, solo_en_lista1, solo_en_lista2

def ejecutar_comparacion():
    """
    Solicita dos listas al usuario y muestra los resultados.
    """
    entrada1 = input("Ingresa los elementos de la primera lista (separados por comas): ")
    entrada2 = input("Ingresa los elementos de la segunda lista (separados por comas): ")

    lista1 = entrada1.split(",")
    lista2 = entrada2.split(",")

    comunes, solo1, solo2 = comparar_listas(lista1, lista2)

    print("\nResultados:")
    print(f"Elementos comunes: {comunes}")
    print(f"Solo en la primera lista: {solo1}")
    print(f"Solo en la segunda lista: {solo2}")

# Ejecutar si se llama directamente
if __name__ == "__main__":
    ejecutar_comparacion()