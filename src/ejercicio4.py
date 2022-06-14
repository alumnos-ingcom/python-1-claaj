################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingeniería en Computación
################

"""
4. Suma lenta

Escribir una función que haga la suma entre dos números enteros sin hacer la operación de manera directa. Esto quiere decir que para hacer la suma entre 4 y 3, las operaciones resultantes deberán ser 4+1+1+1.

La función debe ser capaz de sumar cualquier numero entero positivo y negativo.
"""

def suma_lenta(num, otro_num):
    """
    Función que devuelve la suma de num y otro_num sumando de a 1.
    """
    i = 0
    while i < abs(otro_num):
        num += int(otro_num/abs(otro_num))
        i += 1
    return num

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input('Ingrese un número: ')) # Se ingresa un número.
    otro_numero = int(input('Ingrese otro número: ')) # Se ingresa otro número
    print(f'La suma de {numero} y {otro_numero} es: {suma_lenta(numero,otro_numero)}')

if __name__ == "__main__":
    principal()
