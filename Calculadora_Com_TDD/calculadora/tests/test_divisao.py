import pytest
from calculadora.operacoes.divisao import Divisao

# Teste para a operação de divisão
class TestDivisao:

    # Teste simples de divisão
    def test_divisao_simples(self):
        # Expectativa: ao dividir 10.0 por 2.0, espero 5.0
        divisao = Divisao()
        resultado = divisao.executar(10.0, 2.0)
        assert resultado == 5.0

    # Teste para divisão por zero
    def test_divisao_por_zero(self):
        # Expectativa: ao dividir 10.0 por 0.0, deve levantar ZeroDivisionError
        divisao = Divisao()
        with pytest.raises(ZeroDivisionError):
            divisao.executar(10.0, 0.0)

    # Teste para divisão com zero como numerador
    def test_divisao_zero_numerador(self):
        # Expectativa: ao dividir 0.0 por 5.0, espero 0.0
        divisao = Divisao()
        resultado = divisao.executar(0.0, 5.0)
        assert resultado == 0.0

    # Teste para divisão de números negativos
    def test_divisao_negativos(self):
        # Expectativa: ao dividir -10.0 por -2.0, espero 5.0
        divisao = Divisao()
        resultado = divisao.executar(-10.0, -2.0)
        assert resultado == 5.0

    # Teste para divisão de float
    def test_divisao_float(self):
        # Expectativa: ao dividir 5.0 por 2.0, espero 2.5
        divisao = Divisao()
        resultado = divisao.executar(5.0, 2.0)
        assert resultado == 2.5