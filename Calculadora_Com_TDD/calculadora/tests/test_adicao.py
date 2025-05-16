import pytest
from calculadora.operacoes.adicao import Adicao

# Testes para a classe Adicao

def test_adicao_simples():
    # Caso de teste: 2.0 + 3.0 = 5.0
    adicao = Adicao()
    resultado = adicao.executar(2.0, 3.0)
    assert resultado == 5.0, "ao somar 2.0 e 3.0, espero 5.0"

def test_adicao_zero():
    # Caso de teste: 0 + 0 = 0
    adicao = Adicao()
    resultado = adicao.executar(0.0, 0.0)
    assert resultado == 0.0, "ao somar 0.0 e 0.0, espero 0.0"

def test_adicao_negativos():
    # Caso de teste: -1 + 5 = 4
    adicao = Adicao()
    resultado = adicao.executar(-1.0, 5.0)
    assert resultado == 4.0, "ao somar -1.0 e 5.0, espero 4.0"

def test_adicao_float():
    # Caso de tste: 1.5 + 2.5 = 4.0
    adicao = Adicao()
    resultado = adicao.executar(1.5, 2.5)
    assert resultado == 4.0, "ao somar 1.5 e 2.5, espero 4.0"