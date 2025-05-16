import pytest
from calculadora.operacoes.exponenciacao import Exponenciacao

# Testando a classe Exponenciacao

def test_exponenciacao_simples():
    # Caso de teste: 2.0 elevado a 3.0 deve resultar em 8.0
    exponenciacao = Exponenciacao()
    resultado = exponenciacao.executar(2.0, 3.0)
    assert resultado == 8.0

def test_exponenciacao_zero():
    # Caso de teste: qualquer número elevado a 0 deve resultar em 1.0
    exponenciacao = Exponenciacao()
    resultado = exponenciacao.executar(5.0, 0.0)
    assert resultado == 1.0

def test_exponenciacao_negativa():
    # aso de teste: 2.0 elevado a -3.0 deve resultar em 0.125
    exponenciacao = Exponenciacao()
    resultado = exponenciacao.executar(2.0, -3.0)
    assert resultado == 0.125

def test_exponenciacao_decimal():
    # Caso de teste: 4.0 elevado a 0.5 deve resultar em 2.0 (raiz quadrada)
    exponenciacao = Exponenciacao()
    resultado = exponenciacao.executar(4.0, 0.5)
    assert resultado == 2.0

def test_exponenciacao_base_zero():
    # Caso de teste: 0.0 elevado a 5.0 deve resultar em 0.0
    exponenciacao = Exponenciacao()
    resultado = exponenciacao.executar(0.0, 5.0)
    assert resultado == 0.0