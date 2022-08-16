################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Probando el ejercicio 4 "Suma lenta"
"""
import pytest

from src.ejercicio4 import suma_lenta

def test_suma_lenta_positivos():
    """
    Probando cuando ambos son positivos
    """
    valor1 = 10
    valor2 = 8
    devolucion = suma_lenta(valor1, valor2)
    assert isinstance(devolucion,int), 'El resultado debe ser int'
    assert devolucion == 18, 'Debe devolver 18'

def test_suma_lenta_negativos():
    """
    Probando cuando ambos son negativos
    """
    valor1 = -10
    valor2 = -15
    devolucion = suma_lenta(valor1, valor2)
    assert isinstance(devolucion,int), 'El resultado debe ser int'
    assert devolucion == -25, 'Debe devolver -25'

def test_suma_lenta_numpos_otroneg():
    """
    Probando cuando numero es positivo y otro_numero es negativo
    """
    valor1 = 10
    valor2 = -5
    devolucion = suma_lenta(valor1, valor2)
    assert isinstance(devolucion,int), 'El resultado debe ser int'
    assert devolucion == 5, 'Debe devolver 5'

def test_suma_lenta_numneg_otropos():
    """
    Probando cuando numero es positivo y otro_numero es negativo
    """
    valor1 = -5
    valor2 = 20
    devolucion = suma_lenta(valor1, valor2)
    assert isinstance(devolucion,int), 'El resultado debe ser int'
    assert devolucion == 15, 'Debe devolver 15'
