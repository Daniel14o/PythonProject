"""
Verificador de Mayoría de Edad

Este programa solicita la edad del usuario e indica si es mayor de edad.
Si tiene entre 18 y 25 años, también muestra que es un "joven adulto".

Autor: Daniel Leonardo Cáceres Montañez
Fecha: 01/08/2025
"""

def verificar_mayoria_edad():
    """
    Solicita la edad al usuario y muestra mensajes según su rango de edad.
    """
    try:
        edad = int(input("Ingrese su edad: "))

        if edad < 0:
            print("La edad no puede ser menor que 0.")
        elif edad < 18:
            print("Eres menor de edad.")
        elif 18 <= edad <= 25:
            print("Eres mayor de edad y perteneces al grupo de jóvenes adultos.")
        else:
            print("Eres mayor de edad.")
    except ValueError:
        print("Por favor, ingrese un número entero válido para la edad.")

if __name__ == "__main__":
    verificar_mayoria_edad()
