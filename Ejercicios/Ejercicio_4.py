"""
Tablas de Multiplicar

Pide al usuario un número entero y muestra la tabla de multiplicar de ese número
del 1 al 10. El formato de salida debe ser claro, por ejemplo: 5 x 1 = 5.

Conceptos aplicados: input(), int(), bucle for con range(), f-strings.

Autor: Daniel Leonardo Cáceres Montañez
Fecha: 01/08/2025
"""

def mostrar_tabla(numero):
    """
    Muestra la tabla de multiplicar del número dado del 1 al 10.
    Parámetros:
        numero (int): Número del cual se mostrará la tabla.
    """
    print(f"\nTabla de multiplicar del {numero}:\n")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


def main():
    """
    Función principal que pide el número y llama a la función de tabla.
    """
    try:
        numero = int(input("Ingrese un número entero para ver su tabla de multiplicar: "))
        mostrar_tabla(numero)
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
