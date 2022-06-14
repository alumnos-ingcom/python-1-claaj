################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Conversión de temperaturas

Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.
Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit como un número decimal,
utilice esta formula para calcular los grados centígrados y retorne el resultado obtenido. Y viceversa.
"""
# Reemplazar por las funciones del ejercicio

def convertir_a_fahrrenheit(centigrados):
    return (centigrados * 9/5) + 32

def convertir_a_centigrados(fahrenheit):
    return (fahrenheit - 32) / (9/5)

def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    opcion = int(input('Convertir a:\n 1) Centigrados\n 2) Fahrenheit\n Ingrese la opción elegida: '))

    if opcion == 1:
        valor = float(input('Ingrese valor en centigrados: '))
        print(f'{valor} °C equivale a {convertir_a_fahrrenheit(valor)} °F')

    elif opcion == 2:
        valor = float(input('Ingrese valor en fahrenheit: '))
        print(f'{valor} °F equivale a {convertir_a_centigrados(valor)} °C')

    else:
        print('Opción inválida, corra de nuevo el programa e intente nuevamente.')


    pass


if __name__ == "__main__":  # pragma: no cover
    principal()
