################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Números positivos y negativos
Escribir una función que reciba un número e indique si el mismo es positivo,
negativo o cero utilizando sumas y restas.
"""

def signo(num):
    """
    Función que devuelve:
        a) 1 si es positivo.
        b) 0 si es cero.
        c) -1 si es negativo.
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
