"""
Contador de Vocales y Consonantes

Este programa solicita una frase al usuario y cuenta cuantas vocales y
cuantas consonantes contiene, ignorando espacios, números y símbolos.

Autor: Daniel Leonardo Cáceres Montañez
Fecha: 01/08/2025
"""

def contar_vocales_consonantes(frase):
    """
    Cuenta vocales y consonantes en la frase proporcionada.
    Parámetros:
        frase (str): La frase ingresada por el usuario.
    Retorna:
        (int, int): Número de vocales y consonantes respectivamente.
    """
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    letras = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    contador_vocales = 0
    contador_consonantes = 0

    for caracter in frase.lower():
        if caracter in letras:
            if caracter in vocales:
                contador_vocales += 1
            else:
                contador_consonantes += 1

    return contador_vocales, contador_consonantes


def main():
    """
    Función principal del programa. Solicita frase y muestra resultados.
    """
    frase = input("Ingrese una frase: ")
    vocales, consonantes = contar_vocales_consonantes(frase)

    print(f"\nResultado:")
    print(f"Vocales: {vocales}")
    print(f"Consonantes: {consonantes}")


if __name__ == "__main__":
    main()