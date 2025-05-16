import pytest
from calculadora.operacoes.subtracao import Subtracao

# Teste para a operação de subtração
class TestSubtracao:

    # Caso de teste: 5.0 - 2.0 = 3.0
    def test_subtracao_simples(self):
        subtracao = Subtracao()
        resultado = subtracao.executar(5.0, 2.0)
        assert resultado == 3.0, "ao subtrair 5.0 e 2.0, espero 3.0"

    # Caso de teste: 0 - 0 = 0.0
    def test_subtracao_zero(self):
        subtracao = Subtracao()
        resultado = subtracao.executar(0.0, 0.0)
        assert resultado == 0.0, "ao subtrair 0.0 e 0.0, espero 0.0"

    # Caso de teste: -3 - (-2) = -1.0
    def test_subtracao_negativos(self):
        subtracao = Subtracao()
        resultado = subtracao.executar(-3.0, -2.0)
        assert resultado == -1.0, "ao subtrair -3.0 e -2.0, espero -1.0"

    # Caso de teste: 5.5 - 2.5 = 3.0
    def test_subtracao_float(self):
        subtracao = Subtracao()
        resultado = subtracao.executar(5.5, 2.5)
        assert resultado == 3.0, "ao subtrair 5.5 e 2.5, espero 3.0"