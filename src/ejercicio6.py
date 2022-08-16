################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingeniería en Computación
################
#PRE: Se ingresa al programa 3 valores
#POS: Se devuelve dos tuplas, una odernada de mayor a menor y la de menor a mayor

"""
6. Ordenar 3 valores

Escribir una función que a partir de tres variables de tipo entero retorne una tupla con dichos valores ordenados de menor a mayor. Y Viceversa
"""

def ordenar_mayor_menor(numeros):
    """
    Ordena los números de mayor a menor
    """
    for i in range(len(numeros)):
        mayor_num = i
        for j in range(i + 1, len(numeros)):
            if numeros[j] > numeros[mayor_num]:
                mayor_num = j
        numeros[i], numeros[mayor_num] = numeros[mayor_num], numeros[i]
    return numeros[0], numeros[1], numeros[2]

def ordenar_menor_mayor(numeros):
    """
    Ordena los números de mayor a menor
    """
    i = 0
    for i in range(len(numeros)):
        menor_num = i
        for j in range(i + 1, len(numeros)):
            if numeros[j] < numeros[menor_num]:
                menor_num = j
        numeros[i], numeros[menor_num] = numeros[menor_num], numeros[i]
    return numeros[0], numeros[1], numeros[2]

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numeros_ingresados = 0
    lista_numeros = [0, 0, 0]
    while numeros_ingresados < 3:
        numero = int(input('Ingrese un número: ')) # Se ingresa un número.
        lista_numeros[numeros_ingresados] = numero
        numeros_ingresados += 1
    print(f'Mayor a menor {ordenar_mayor_menor(lista_numeros)}')
    print(f'Menor a mayor {ordenar_menor_mayor(lista_numeros)}')

if __name__ == "__main__":
    principal()
