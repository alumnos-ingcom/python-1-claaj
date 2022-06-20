################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingeniería en Computación
################
#PRE: Dos numeros enteros
#POS: Devuelve el cociente y resto de la división entre el primer numero ingresado y el segundo


"""
5. Divisiones

Escribir una función que mediante restas sucesivas,
obtenga el valor del cociente y resto de dos números enteros.
"""

def division_lenta(dividendo, divisor):
    """
    Función que resuelve una división utilizando resta.
    """
    try:
        i = 0
        cociente = 0
        num = abs(dividendo)
        signo = (dividendo/abs(dividendo)) * (divisor/abs(divisor))
        while num >= abs(divisor):
            cociente += 1
            num -= (abs(divisor))
        cociente = int(cociente * signo)
        num = int(num * signo)
        return cociente, num

    except ZeroDivisionError as exc:
        print('No se puede dividir por cero')

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input('Ingrese un número: ')) # Se ingresa un número.
    otro_numero = int(input('Ingrese otro número: ')) # Se ingresa otro número
    print(f'La división de {numero} entre {otro_numero} es:\nCociente: {division_lenta(numero,otro_numero)[0]}\nResto: {division_lenta(numero,otro_numero)[1]}')

if __name__ == "__main__":
    principal()
