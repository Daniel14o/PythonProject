"""
Análisis de Calificaciones

Este programa define una función que recibe una lista de calificaciones numéricas
y retorna una tupla con el promedio, la calificación más alta y la más baja.
Luego, se prueba la función con una lista de ejemplo.

Autor: Daniel Leonardo Cáceres Montañez
Fecha: 01/08/2025
"""

def analizar_calificaciones(calificaciones):
    """
    Analiza una lista de calificaciones.

    Parámetros:
        calificaciones (list): Lista de números (int o float)

    Retorna:
        tuple: (promedio, nota_máxima, nota_mínima)
    """
    if not calificaciones:
        return (0, 0, 0)  # En caso de lista vacía

    promedio = sum(calificaciones) / len(calificaciones)
    nota_maxima = max(calificaciones)
    nota_minima = min(calificaciones)

    return (promedio, nota_maxima, nota_minima)


def main():
    """
    Función principal que prueba la función de análisis con una lista de ejemplo.
    """
    ejemplo = [3.5, 4.0, 2.8, 5.0, 3.9, 4.2]
    resultado = analizar_calificaciones(ejemplo)

    print("Analisis de Calificaciones")
    print(f"Lista de calificaciones: {ejemplo}")
    print(f"Promedio: {resultado[0]:.2f}")
    print(f"Nota más alta: {resultado[1]}")
    print(f"Nota más baja: {resultado[2]}")

if __name__ == "__main__":
    main()