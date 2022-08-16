################
# Matías Cajal - @claaj
# UNRN Andina - Introducción a la Ingeniería en Computación
################

"""
Probando el ejercicio 10 "Palindromo"
"""
import pytest

from src.ejercicio10 import es_palindromo

def test_es_palindromo():
    """
    Probando una palabra que es palindromo
    """
    palabra = 'neuquen'
    devolucion = es_palindromo(palabra)
    assert isinstance(devolucion,bool), 'La devolución debe ser booleana'
    assert devolucion == True, 'La devolución debe ser "True"'

def test_no_es_palindromo():
    """
    Probando una palabra que no es palindromo
    """
    palabra = 'naranja'
    devolucion = es_palindromo(palabra)
    assert isinstance(devolucion,bool), 'La devolución debe ser booleana'
    assert devolucion == False, 'La devolución debe ser "False"'
