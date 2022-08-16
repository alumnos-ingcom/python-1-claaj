################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingeniería en Computación
################
#PRE: Se ingresan dos numeros
#POS: Devuelve True si el primero es multiplo del segundo, sino devuelve false

"""
11. Multiplos de

Escribir una función que indique con True si un número entero es multiplo de otro, utilizando sumas y restas.
"""

def es_multiplo(num, mul):
    """
    Devuelve si un número es multiplo de otro
    """
    aux = 0
    while aux < num:
        aux += mul
    return True if aux == num else False

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input('Ingrese un número: '))
    multiplo = int(input('Ingrese el múltiplo: '))
    print(f'{es_multiplo(numero, multiplo)}')

if __name__ == "__main__":
    principal()
