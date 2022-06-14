################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingeniería en Computación
################

"""
1. Conversión de temperaturas

Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.
Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit como un número decimal,
utilice esta formula para calcular los grados centígrados y retorne el resultado obtenido. Y viceversa.
"""

def convertir_a_fahrrenheit(centigrados):
    """
    función que en base a un valor en °C devuelve la conversión de a °F.
    """
    return ((centigrados * 9/5) + 32)

def convertir_a_centigrados(fahrenheit):
    """
    función que en base a un valor en °F devuelve la conversión de a °C.
    """
    return ((fahrenheit - 32) / (9/5))

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    # Se pide por la opción
    opcion = int(input('Convertir a:\n 1) Centigrados\n 2) Fahrenheit\n Ingrese la opción elegida: '))

    if opcion == 1: # Si es 1 se pide el valor en centigrados e imprime la conversión
        valor = float(input(' Ingrese valor en centigrados: '))
        print(f' {valor:.2f}°C equivale a {convertir_a_fahrrenheit(valor):.2f}°F')

    elif opcion == 2: #Si es 2 se pide el valor en fahrenheit e imprime  la conversión
        valor = float(input('Ingrese valor en fahrenheit: '))
        print(f' {valor:.2f}°F equivale a {convertir_a_centigrados(valor):.2f}°C')

    else: # En caso de no 1 o 2 se imprime el error
        print('Opción inválida, corra de nuevo el programa e intente nuevamente.')

if __name__ == "__main__":
    principal()
