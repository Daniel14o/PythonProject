"""
Adivina el Número

Este juego genera un número secreto (por ahora definido manualmente) y el usuario
debe adivinarlo. El programa guía al jugador diciendo si el número ingresado es
mayor o menor. El juego termina cuando el usuario adivine el numero secreto.

Conceptos aplicados: Bucle while, if/elif/else, input(), int(), operadores
relacionales.

Autor: Daniel Leonardo Cáceres Montañez
Fecha: 01/08/2025
"""

def adivina_el_numero():



    numero_secreto = 42
    intentos = 0

    print("Adivina el número secreto entre 1 y 100")

    while True:
        try:
            intento = int(input("Introduce tu intento: "))
            intentos += 1

            if intento < 1 or intento > 100:
                print("El número debe estar entre 1 y 100.")
            elif intento < numero_secreto:
                print("Demasiado bajo. Intenta un número más alto.")
            elif intento > numero_secreto:
                print("Demasiado alto. Intenta un número más bajo.")
            else:
                print(f"Felicidades, Adivinaste el número {numero_secreto} en {intentos} intento(s).")
                break
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
    adivina_el_numero()