# Calculadora Com TDD

## Descrição do Projeto
Este projeto implementa uma calculadora simples em Python, utilizando o conceito de Test-Driven Development (TDD). A calculadora é composta por uma classe principal, `Calculadora`, que delega operações a seis classes de operações: `Adicao`, `Subtracao`, `Multiplicacao`, `Divisao`, `RaizQuadrada` e `Exponenciacao`.

## Estrutura do Projeto
```
Calculadora_Com_TDD
├── main.py
├── calculadora
│   ├── __init__.py
│   ├── calculadora.py
│   ├── operacoes
│   │   ├── __init__.py
│   │   ├── adicao.py
│   │   ├── subtracao.py
│   │   ├── multiplicacao.py
│   │   ├── divisao.py
│   │   ├── raiz_quadrada.py
│   │   └── exponenciacao.py
│   └── tests
│       ├── __init__.py
│       ├── test_calculadora.py
│       ├── test_adicao.py
│       ├── test_subtracao.py
│       ├── test_multiplicacao.py
│       ├── test_divisao.py
│       ├── test_raiz_quadrada.py
│       └── test_exponenciacao.py
└── README.md
```

## Classes
- **Calculadora**: Classe principal que compõe as operações.
- **Adicao**: Realiza a soma de dois números.
- **Subtracao**: Realiza a subtração de dois números.
- **Multiplicacao**: Realiza a multiplicação de dois números.
- **Divisao**: Realiza a divisão de dois números, com validação para divisão por zero.
- **RaizQuadrada**: Calcula a raiz quadrada de um número, com validação para números negativos.
- **Exponenciacao**: Calcula a potência de um número.

## Instruções de Uso
1. Clone o repositório.
2. Navegue até o diretório do projeto.
3. Execute o arquivo `main.py` para interagir com a calculadora.

## Exemplos de Uso
```python
from calculadora.calculadora import Calculadora

calc = Calculadora()

# Adição
resultado = calc.somar(2.0, 3.0)
print(resultado)  # Saída: 5.0

# Subtração
resultado = calc.subtrair(5.0, 2.0)
print(resultado)  # Saída: 3.0

# Multiplicação
resultado = calc.multiplicar(4.0, 2.5)
print(resultado)  # Saída: 10.0

# Divisão
resultado = calc.dividir(10.0, 2.0)
print(resultado)  # Saída: 5.0

# Raiz Quadrada
resultado = calc.raiz_quadrada(9.0)
print(resultado)  # Saída: 3.0

# Exponenciação
resultado = calc.exponenciar(2.0, 3.0)
print(resultado)  # Saída: 8.0
```

## Testes
Os testes foram implementados para cada operação e para a classe `Calculadora`, garantindo que todas as funcionalidades estejam corretas. Utilize o `pytest` para executar os testes.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
