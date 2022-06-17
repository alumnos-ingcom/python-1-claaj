################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingeniería en Computación
################

"""
Probando el ejercicio 7 "Transformación de un número"
"""
import pytest

from src.ejercicio7 import decimal_a_sexagesimal, sexagesimal_a_decimal

def test_decimal_a_sexagesimal():
    """
    Probando la conversión de decimal a sexagesimal
    """
    valor = -5415
    resultado = decimal_a_sexagesimal(valor)
    assert isinstance(resultado,tuple), 'El resultado debe ser una tupla'
    assert resultado == (-1, 30, 15), 'El resultado debe ser igual a (1, 30, 15)'

def test_sexagesimal_a_decimal():
    """
    Probando la conversión de sexagesimal a decimal.
    """
    grados = 1
    minutos = 30
    segundos = 15
    resultado = sexagesimal_a_decimal(grados, minutos, segundos)
    assert isinstance(resultado,int), 'El resultado debe ser un entero'
    assert resultado == 5415, 'El resultado debe ser igual a 5415'
