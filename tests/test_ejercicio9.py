################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingeniería en Computación
################

"""
Probando el ejercicio 8 "Números primos"
"""
import pytest

from src.ejercicio9 import factores_primos

def test_factores_primos():
    """
    Probando la devolución de la función cuando se da como argumento
    un número negativo
    """
    numero = 10
    devolucion = factores_primos(numero)
    assert isinstance(devolucion,tuple), 'La devolución debe ser una tupla'
    assert devolucion == (2, 5), 'La devolución debe ser (2, 5)'
