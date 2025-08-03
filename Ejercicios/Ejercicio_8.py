"""
Ejercicio 8: Validador de Palíndromos

Este programa define una función que verifica si una palabra o frase es un palíndromo
Ignora mayúsculas, minúsculas y espacios.

Conceptos aplicados: Funciones, strings (métodos replace, lower), slicing
([::-1]), booleanos
"""

def es_palindromo(texto):
    """
    Determina si el texto ingresado es un palíndromo

    Parámetros:
        texto (str): Palabra o frase a evaluar

    Retorna:
        bool: True si es un palíndromo, False si no lo es
    """
    # Normalizar el texto: sin espacios y en minúsculas
    texto_limpio = texto.replace(" ", "").lower()
    return texto_limpio == texto_limpio[::-1]


if __name__ == "__main__":
    entrada = input("Ingresa una palabra o frase: ")
    if es_palindromo(entrada):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")