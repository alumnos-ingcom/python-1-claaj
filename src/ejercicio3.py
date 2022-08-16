################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingeniería en Computación
################
#PRE: Se ingresan dos números.
#POS: Se devuelve:
#   -1 si el primeros es menor que el segundo
#   0 si son iguales
#   1 si el primero es mayor que el segundo

"""
3. Comparación de números

Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

    Retornar -1 si el primero es menor que el segundo
    Retornar 0 si son iguales
    Retornar 1 si el primero es mayor que el segundo

"""

def compara(num, otro_num):
    """
    Función que devuelve:
        * 1 si num es menor que otro_num.
        * 0 si son iguales.
        * -1 si num es mayor que otro num.
    """
    if num - otro_num < 0:
        comp = -1
    elif num - otro_num > 0:
        comp = 1
    else:
        comp = 0
    return comp

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input('Ingrese un número: ')) # Se ingresa un número.
    otro_numero = int(input('Ingrese otro número: ')) # Se ingresa otro número
    print(f'{compara(numero,otro_numero)}') # Se imprime el resultado de la función en base a los numeros ingresados

if __name__ == "__main__":
    principal()
