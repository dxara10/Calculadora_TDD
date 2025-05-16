import pytest
from calculadora.operacoes.multiplicacao import Multiplicacao

# Testando a classe Multiplicacao
class TestMultiplicacao:

    # Caso de teste: 4.0 * 2.5 = 10.0
    def test_multiplicacao_simples(self):
        multiplicacao = Multiplicacao()
        resultado = multiplicacao.executar(4.0, 2.5)
        assert resultado == 10.0

    # Caso de teste: 0 * qualquer número = 0
    def test_multiplicacao_zero(self):
        multiplicacao = Multiplicacao()
        resultado = multiplicacao.executar(0, 5.0)
        assert resultado == 0.0

    # Caso de teste: número negativo
    def test_multiplicacao_negativo(self):
        multiplicacao = Multiplicacao()
        resultado = multiplicacao.executar(-3.0, 2.0)
        assert resultado == -6.0

    # Caso de teste: floats pequenos
    def test_multiplicacao_floats_pequenos(self):
        multiplicacao = Multiplicacao()
        resultado = multiplicacao.executar(0.1, 0.2)
        assert resultado == 0.02