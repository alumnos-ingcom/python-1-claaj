################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Probando el ejercicio 2 "Números positivos y negativos"
"""
import pytest

from src.ejercicio2 import signo

def test_signo_cero():
    """
    Probando valor cuando es 0.
    """
    valor = 0
    devolucion = signo(valor)
    assert isinstance(devolucion,str), 'El resultado debe ser una cadena de carácteres'
    assert devolucion == 'cero', 'Debe devolver "cero"'

def test_signo_positivo():
    """
    Probando valor positivo.
    """
    valor = 1
    devolucion = signo(valor)
    assert isinstance(devolucion,str), 'El resultado debe ser una cadena de carácteres'
    assert devolucion == 'positivo', 'Debe devolver "positivo"'


def test_signo_negativo():
    """
    Probando valor negativo.
    """
    valor = -1
    devolucion = signo(valor)
    assert isinstance(devolucion,str), 'El resultado debe ser una cadena de carácteres'
    assert devolucion == 'negativo', 'Debe devolver "negativo"'
