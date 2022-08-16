################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingeniería en Computación
################

"""
Probando el ejercicio 11 "Multiplo de"
"""
import pytest

from src.ejercicio11 import es_multiplo

def test_es_multiplo():
    """
    Probando cuando los valores dan como resultado True
    """
    numero = 8
    multiplo = 2
    devolucion = es_multiplo(numero, multiplo)
    assert isinstance(devolucion,bool), 'La devolución debe ser booleana'
    assert devolucion == True, 'La devolución debe ser "True"'

def test_no_es_multiplo():
    """
    Probando cuando los valores dan como resultado False
    """
    numero = 7
    multiplo = 2
    devolucion = es_multiplo(numero, multiplo)
    assert isinstance(devolucion,bool), 'La devolución debe ser booleana'
    assert devolucion == False, 'La devolución debe ser "True"'
