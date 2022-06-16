################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingeniería en Computación
################

"""
Probando el ejercicio 6 "Ordenar 3 valores"
"""
import pytest

from src.ejercicio6 import ordenar_mayor_menor, ordenar_menor_mayor


vector_prueba = [-1, 1000, 500]

def test_mayor_menor():
    """
    Probando de mayor a menor
    """
    global vector_prueba
    devolucion = ordenar_mayor_menor(vector_prueba)
    assert isinstance(devolucion,list), 'El resultado debe ser una lista'
    assert devolucion == [1000, 500, -1], 'Debe devolver [1000, 500, -1]'

def test_menor_mayor():
    """
    Probando de menor a mayor
    """
    global vector_prueba
    devolucion = ordenar_menor_mayor(vector_prueba)
    assert isinstance(devolucion,list), 'El resultado debe ser una lista'
    assert devolucion == [-1, 500, 1000], 'Debe devolver [-1, 500, 1000]'
