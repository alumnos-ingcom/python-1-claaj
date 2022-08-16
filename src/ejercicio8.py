################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingeniería en Computación
################
#PRE: Se ingresa un número
#POS: Se devuelve si el número es primo o no
"""
8. Números primos

Escribir una función que indique con True si un numero indicado es Primo.

"""

def es_primo(num):
    """
    Determina si el argumento dado es primo o no.
    """
    primo = False
    i = 1
    divisores = 0
    if num > 0:
        while i <= num:
            if num % i == 0:
                divisores += 1
            i += 1
        return True if divisores <= 2 else False
    else:
        return False

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input('Ingrese un número: '))
    if es_primo(numero) == True:
        print(f'{numero} es primo.')
    else:
        print(f'{numero} no es primo.')

if __name__ == "__main__":
    principal()
