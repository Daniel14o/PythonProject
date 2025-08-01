"""
Calculadora de Índice de Masa Corporal (IMC)

Este programa solicita al usuario su peso en kilogramos y su altura en metros,
luego calcula el IMC usando la fórmula:

    IMC=altura2peso

Finalmente, muestra el IMC redondeado a dos decimales con un mensaje claro.

Conceptos aplicados: input(), print(), float(), variables, operadores
aritméticos, f-strings.

Autor: Daniel Leonardo Cáceres Montañez
Fecha: 01/08/2025
"""

def calcular_imc():
    """
    Solicita peso y altura al usuario, calcula el IMC y muestra el resultado.

    """
    try:
        peso = float(input("Ingrese su peso en kilogramos (kg): "))
        altura = float(input("Ingrese su altura en metros (m): "))
        if altura <= 0:
            print("La altura debe ser mayor que cero.")
            return

        imc = peso / (altura ** 2)
        print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    calcular_imc()