################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingeniería en Computación
################

"""
Probando el ejercicio 8 "Números primos"
"""
import pytest

from src.ejercicio8 import es_primo

def test_no_es_primo_negativo():
    """
    Probando la devolución de la función cuando se da como argumento
    un número negativo
    """
    numero = -13
    devolucion = es_primo(numero)
    assert isinstance(devolucion,bool), 'La devolución debe ser de tipo booleana'
    assert devolucion == False, 'La devolución debe ser False'
    
def test_es_primo_positivo():
    """
    Probando la devolución de la función cuando se da como argumento
    un número positivo que es primo
    """
    numero = 13
    devolucion = es_primo(numero)
    assert isinstance(devolucion,bool), 'La devolución debe ser de tipo booleana'
    assert devolucion == True, 'La devolución debe ser "True"'
    
def test_no_es_primo_positivo():
    """
    Probando la devolución de la función cuando se da como argumento
    un número positivo que no es primo
    """
    numero = 10
    devolucion = es_primo(numero)
    assert isinstance(devolucion,bool), 'La devolución debe ser de tipo booleana'
    assert devolucion == False, 'La devolución debe ser "False"'
    
def test_es_primo_cero():
    """
    Probando la devolución de la función cuando se da como argumento 0
    """
    numero = 0
    devolucion = es_primo(numero)
    assert isinstance(devolucion,bool), 'La devolución debe ser de tipo booleana'
    assert devolucion == False, 'La devolución debe ser "False"'
