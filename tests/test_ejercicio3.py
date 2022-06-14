################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Probando el ejercicio 3 "Comparación de números"
"""
import pytest

from src.ejercicio3 import compara

def test_compara_numero_mayor():
    """
    Probando cuando numero es mayor a otro_numero
    """
    valor1 = 10
    valor2 = 8
    devolucion = compara(valor1, valor2)
    assert isinstance(devolucion,int), 'El resultado debe ser int'
    assert devolucion == 1, 'Debe devolver 1'

def test_compara_numero_menor():
    """
    Probando cuando numero es menor a otro_numero
    """
    valor1 = 8
    valor2 = 18
    devolucion = compara(valor1, valor2)
    assert isinstance(devolucion,int), 'El resultado debe ser int'
    assert devolucion == -1, 'Debe devolver -1'

def test_compara_iguales():
    """
    Probando cuando numero y otro_numero son iguales
    """
    valor1 = 10
    valor2 = 10
    devolucion = compara(valor1, valor2)
    assert isinstance(devolucion,int), 'El resultado debe ser int'
    assert devolucion == 0, 'Debe devolver 0'
