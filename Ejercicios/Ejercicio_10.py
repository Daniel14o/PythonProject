"""
Ejercicio 10: Contador de Frecuencia de Palabras

Este programa define una función que recibe un texto y devuelve un diccionario con la frecuencia
de cada palabra, ignorando diferencias entre mayúsculas y minúsculas

Conceptos aplicados: Diccionarios (método get), funciones, strings
(métodos split, lower), bucle for.
"""

def contar_palabras(texto: str) -> dict:
    """
    Cuenta la frecuencia de cada palabra en el texto recibido

    :param texto: Cadena de texto.
    :return: Diccionario con palabras como claves y frecuencias como valores
    """
    frecuencia = {}
    palabras = texto.lower().split()

    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

    return frecuencia

def mostrar_frecuencia():
    """
    Solicita al usuario un texto y muestra el conteo de palabras
    """
    texto = input("Escribe un texto: ")
    resultado = contar_palabras(texto)

    print("\nFrecuencia de palabras:")
    for palabra, conteo in resultado.items():
        print(f"'{palabra}': {conteo}")

# Ejecutar el programa
if __name__ == "__main__":
    mostrar_frecuencia()