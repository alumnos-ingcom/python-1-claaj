################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingeniería en Computación
################

"""
7. Transformación de un número

Escribir un programa que permita transformar un número solicitado expresado en grados, minutos y segundos a segundos a segundos. Y otra que haga el cambio en el sentido contrario, devolviendo una tuple.

Recuerden que un grado son 60 minutos y un minuto son 60 segundos.
"""

def decimal_a_sexagesimal(numero):
    """
    Convierte de segundos a grados, minutos y segundos
    """
    grados = 0
    minutos = 0
    abs_numero = abs(numero)
    while abs_numero >= 3600:
        grados += 1
        abs_numero -= 3600
    while abs_numero >= 60:
        minutos += 1
        abs_numero -= 60

    grados *= numero/abs(numero)
    return grados, minutos, abs_numero


def sexagesimal_a_decimal(grados, minutos, segundos):
    """
    Convierte grados, minutos y segundos a segundos
    """
    numero = (grados * 3600) + (minutos * 60) + segundos
    return numero


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    opcion = int(input('1) Decimal a sexagesimal \n2) Sexagesimal a decimal: '))
    if opcion == 1:
        decimal = int(input('Ingrese un número: '))
        print(f'{decimal} equivale a {decimal_a_sexagesimal(decimal)} en sistema sexagesimal')
    else:
        grad = int(input('Ingrese grados: '))
        min = int(input('Ingrese minutos: '))
        assert min >= 0, 'Minutos debe ser mayor a 0'
        seg = int(input('Ingrese segundos: '))
        assert seg >= 0, 'Segundos debe ser mayor a 0'
        print(f"{grad}° {min}' {seg}'' equivale a {sexagesimal_a_decimal(grad, min, seg)}")

if __name__ == "__main__":
    principal()
