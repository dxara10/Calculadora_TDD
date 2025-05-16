import pytest
from calculadora.operacoes.raiz_quadrada import RaizQuadrada

# Testando a classe RaizQuadrada

def test_raiz_quadrada_simples():
    # Caso de teste: √9.0 = 3.0
    raiz = RaizQuadrada()
    resultado = raiz.executar(9.0)
    assert resultado == 3.0, "ao calcular a raiz quadrada de 9.0, espero 3.0"

def test_raiz_quadrada_negativo():
    # Caso de teste: √(-4.0) → ValueError
    raiz = RaizQuadrada()
    with pytest.raises(ValueError, match="não é possível calcular a raiz quadrada de um número negativo"):
        raiz.executar(-4.0)

def test_raiz_quadrada_zero():
    # Caso de teste: √0 = 0.0
    raiz = RaizQuadrada()
    resultado = raiz.executar(0.0)
    assert resultado == 0.0, "ao calcular a raiz quadrada de 0.0, espero 0.0"

def test_raiz_quadrada_float():
    # Caso de teste: √2.25 = 1.5
    raiz = RaizQuadrada()
    resultado = raiz.executar(2.25)
    assert resultado == 1.5, "ao calcular a raiz quadrada de 2.25, espero 1.5"