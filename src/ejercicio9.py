################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingeniería en Computación
################
#PRE: Se ingresa un número.
#POS: Se devuelve una tupla con los factores primos.

"""
9. Factores Primos

Escribir una función que retorne una tuple con factores primos de un numero entero positivo.

"""

def factores_primos(num):
    """
    Devuelve los factores primos de un número
    """
    factores = ()
    for i in range(2, num + 1):
        while num % i == 0:
            factores += (i,)
            num = num / i
    return factores

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input('Ingrese un número: '))
    print(f'Los factores primos de {numero} son: {factores_primos(numero)}')

if __name__ == "__main__":
    principal()
