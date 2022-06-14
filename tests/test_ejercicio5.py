################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Probando el ejercicio 5 "Divisiones"
"""
import pytest

from src.ejercicio5 import division_lenta

def test_division_lenta_positivos():
    """
    Probando cuando ambos son positivos
    """
    dividendo = 10
    divisor = 3
    resultado = division_lenta(dividendo, divisor)
    assert isinstance(resultado[0],int), 'El resultado debe ser int'
    assert isinstance(resultado[1],int), 'El resultado debe ser int'
    assert resultado[0] == 3, 'Debe devolver 3'
    assert resultado[1] == 1, 'Debe devolver 1'

def test_division_lenta_negativos():
    """
    Probando cuando ambos son negativos
    """
    dividendo = -10
    divisor = -3
    resultado = division_lenta(dividendo, divisor)
    assert isinstance(resultado[0],int), 'El resultado debe ser int'
    assert isinstance(resultado[1],int), 'El resultado debe ser int'
    assert resultado[0] == 3, 'Debe devolver 3'
    assert resultado[1] == 1, 'Debe devolver 1'

def test_division_lenta_dividendopos_divisorneg():
    """
    Probando cuando el dividendo es positivo y el divisor negativo
    """
    dividendo = 10
    divisor = -3
    resultado = division_lenta(dividendo, divisor)
    assert isinstance(resultado[0],int), 'El resultado debe ser int'
    assert isinstance(resultado[1],int), 'El resultado debe ser int'
    assert resultado[0] == -3, 'Debe devolver -3'
    assert resultado[1] == -1, 'Debe devolver -1'

def test_division_lenta_dividendoneg_divisorpos():
    """
    Probando cuando el dividendo es negativo y el divisor positivo
    """
    dividendo = 10
    divisor = -3
    resultado = division_lenta(dividendo, divisor)
    assert isinstance(resultado[0],int), 'El resultado debe ser int'
    assert isinstance(resultado[1],int), 'El resultado debe ser int'
    assert resultado[0] == -3, 'Debe devolver -3'
    assert resultado[1] == -1, 'Debe devolver -1'

#def test_division_lenta_div_por_cero():
#    """
#    Probando cuando se divide por 0
#    """
#    dividendo = 10
#    divisor = 0
#   resultado = division_lenta(dividendo, divisor)
#    assert isinstance(resultado,str), 'El resultado debe ser cadena de carácteres'
