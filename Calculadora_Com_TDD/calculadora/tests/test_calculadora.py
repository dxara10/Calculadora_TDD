# Importando o pytest para fazer os testes automatizados
import pytest
# Importando a classe Calculadora que será testada
from calculadora.calculadora import Calculadora

# Testando a função de soma da calculadora
def test_somar():
    calc = Calculadora()  # Cria uma instância da calculadora
    assert calc.somar(2.0, 3.0) == 5.0  # Teste básico de soma
    assert calc.somar(0.0, 0.0) == 0.0  # Soma de zeros
    assert calc.somar(-1.0, 5.0) == 4.0  # Soma com número negativo
    assert calc.somar(1.5, 2.5) == 4.0  # Soma com números decimais

# Testando a função de subtração
def test_subtrair():
    calc = Calculadora()
    assert calc.subtrair(5.0, 2.0) == 3.0  # Subtração simples
    assert calc.subtrair(0.0, 0.0) == 0.0  # Subtração de zeros
    assert calc.subtrair(-3.0, -2.0) == -1.0  # Subtração com negativos
    assert calc.subtrair(2.5, 1.5) == 1.0  # Subtração com decimais

# Testando a função de multiplicação
def test_multiplicar():
    calc = Calculadora()
    assert calc.multiplicar(4.0, 2.5) == 10.0  # Multiplicação comum
    assert calc.multiplicar(0.0, 5.0) == 0.0  # Multiplicação com zero
    assert calc.multiplicar(-2.0, 3.0) == -6.0  # Multiplicação com negativo
    assert calc.multiplicar(0.1, 0.2) == 0.02  # Multiplicação com números pequenos

# Testando a função de divisão
def test_dividir():
    calc = Calculadora()
    assert calc.dividir(10.0, 2.0) == 5.0  # Divisão comum
    # Testando divisão por zero, que deve lançar um erro
    with pytest.raises(ZeroDivisionError):
        calc.dividir(10.0, 0.0)
    assert calc.dividir(-10.0, -2.0) == 5.0  # Divisão com dois negativos
    assert calc.dividir(5.0, 0.1) == 50.0  # Divisão com divisor pequeno

# Testando a função de raiz quadrada
def test_raiz_quadrada():
    calc = Calculadora()
    assert calc.raiz_quadrada(9.0) == 3.0  # Raiz de número exato
    # Testando raiz de número negativo, que deve lançar erro
    with pytest.raises(ValueError):
        calc.raiz_quadrada(-4.0)
    assert calc.raiz_quadrada(0.0) == 0.0  # Raiz de zero
    assert calc.raiz_quadrada(2.25) == 1.5  # Raiz de número decimal

# Testando a função de exponenciação (potência)
def test_exponenciar():
    calc = Calculadora()
    assert calc.exponenciar(2.0, 3.0) == 8.0  # Potência comum
    assert calc.exponenciar(2.0, 0.0) == 1.0  # Qualquer número elevado a zero
    assert calc.exponenciar(2.0, -2.0) == 0.25  # Potência com expoente negativo
    assert calc.exponenciar(0.5, 2.0) == 0.25  # Potência com base decimal
