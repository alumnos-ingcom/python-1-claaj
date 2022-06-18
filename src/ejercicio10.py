################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingeniería en Computación
################

"""
10. Palíndromo

Escribir una función que indique con True si una palabra o frase ingresada se trata de un palindromo. Palíndromo, es si se lee igual de derecha a izquierda que de izquierda a derecha.

"""

def es_palindromo(cadena):
    """
    Devuelve si la cadena de caracteres dada como un argumento es palindromo.
    """
    cadena_inver = ''
    for letra in cadena.lower():
        cadena_inver = letra + cadena_inver
    return True if cadena.lower() == cadena_inver else False

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    palabra = str(input('Ingrese una palabra: '))
    print(f'{es_palindromo(palabra)}')

if __name__ == "__main__":
    principal()
