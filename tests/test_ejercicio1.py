################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingeniería en Computación
################

"""
Probando el ejercicio 1 "Convirtiendo temperatura"
"""
import pytest

from src.ejercicio1 import convertir_a_centigrados, convertir_a_fahrrenheit

def test_convertir_a_centigrados():
    """
    Probando la conversión de fahrenheint a centigrados.
    """
    valor = 32
    resultado = convertir_a_centigrados(valor)
    assert isinstance(resultado,float), 'El resultado debe ser un número flotante'
    assert resultado == 0, 'El resultado debe ser igual a 0'

def test_convertir_a_fahrenheint():
    """
    Probando la conversión de centigrados a fahrenheint.
    """
    valor = 0
    resultado = convertir_a_fahrrenheit(valor)
    assert isinstance(resultado,float), 'El resultado debe ser un número flotante'
    assert resultado == 32, 'El resultado debe ser igual a 32'
