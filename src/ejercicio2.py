################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingeniería en Computación
################
# PRE: Se ingresa al programa un número.
#POS: Se indica si el numero es cero, positivo o negativo.
"""
2. Números positivos y negativos
Escribir una función que reciba un número e indique si el mismo es positivo,
negativo o cero utilizando sumas y restas.
"""

def signo(num):
    """
    Función que devuelve si un número es positivo, negativo o cero
    """
    if num + 1 <= 0:
        signo_numero = 'negativo'
    elif num - 1 >= 0:
        signo_numero = 'positivo'
    else:
        signo_numero = 'cero'

    return signo_numero

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input('Ingrese un número: ')) # Se ingresa un número.
    print(f'{numero} es {signo(numero)}')

if __name__ == "__main__":
    principal()
