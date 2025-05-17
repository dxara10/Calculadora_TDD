# 🧮 Projeto: Calculadora com TDD em Python

## ✅ Objetivo

Este projeto tem como objetivo desenvolver uma **Calculadora Modular em Python**, utilizando os princípios de **Programação Orientada a Objetos (POO)** e **Desenvolvimento Orientado a Testes (TDD)** com `pytest`.

### Características:
- Arquitetura baseada em **composição de classes**
- Estrutura **modular e extensível**
- Totalmente **testada com pytest**
- Operações com valores do tipo **float**
- Documentação com uso expressivo de IA ChatGPT
- Implementação com Python, com condução da IA Github Copilot
- Abordagem de Desenvolvimento: Test Driven Development
- Técnicas de Teste: Particionamento de Equivalência, Análise do Valor Limite, Tabela de Decisão, Teste de Exceção

## 🔧 Funcionalidades

A Calculadora suporta as seguintes operações:

- Adição
- Subtração
- Multiplicação
- Divisão (com validação de divisão por zero)
- Raiz Quadrada (com validação de valores negativos)
- Exponenciação

---

## 📘 Diagrama de Classes (UML textual)

```
+---------------------------+
|        Calculadora        |
+---------------------------+
| - adicao: Adicao                         |
| - subtracao: Subtracao                   |
| - multiplicacao: Multiplicacao           |
| - divisao: Divisao                       |
| - raiz: RaizQuadrada                     |
| - exponenciacao: Exponenciacao           |
+---------------------------+
| + somar(a: float, b: float): float              |
| + subtrair(a: float, b: float): float           |
| + multiplicar(a: float, b: float): float        |
| + dividir(a: float, b: float): float            |
| + raiz_quadrada(a: float): float                |
| + exponenciar(base: float, exp: float): float   |
+---------------------------+

+-------------------+       +----------------------+
|      Adicao       |       |   Subtracao          |
+-------------------+       +----------------------+
| + executar(a: float, b: float): float            |
+-------------------+       +----------------------+

+---------------------------+
|      Multiplicacao        |
+---------------------------+
| + executar(a: float, b: float): float            |
+---------------------------+

+-------------------+       +--------------------------+
|      Divisao      |       |      RaizQuadrada        |
+-------------------+       +--------------------------+
| + executar(a: float, b: float): float              |
| (valida divisão por zero)                          |
+-------------------+       +--------------------------+

+--------------------------+
|      Exponenciacao       |
+--------------------------+
| + executar(base: float, exp: float): float         |
+--------------------------+
```

---

## 🧱 Estrutura de Arquivos

```
Calculadora_Com_TDD/
│
├── main.py
├── calculadora/
│   ├── __init__.py
│   ├── calculadora.py
│   ├── operacoes/
│   │   ├── __init__.py
│   │   ├── adicao.py
│   │   ├── subtracao.py
│   │   ├── multiplicacao.py
│   │   ├── divisao.py
│   │   ├── raiz_quadrada.py
│   │   └── exponenciacao.py
│   └── tests/
│       ├── __init__.py
│       ├── test_calculadora.py
│       ├── test_adicao.py
│       ├── test_subtracao.py
│       ├── test_multiplicacao.py
│       ├── test_divisao.py
│       ├── test_raiz_quadrada.py
│       └── test_exponenciacao.py
```

---

## ✅ Operações e TDD

### 🧪 Passo a Passo Geral

Para cada operação:

1. Criar o nome da operação e seu caso de teste.
2. Descrever a expectativa (entrada → saída esperada).
3. Criar o teste (que deve falhar inicialmente).
4. Implementar o método mínimo que faz o teste passar.
5. Rodar os testes e validar.
6. Refatorar se necessário.
7. Adicionar testes extras (valores limites, exceções etc).

---

## 🔢 Casos e Implementações

### ✅ 1. Adição

- Cenário: `2.0 + 3.0 = 5.0`
- Teste: `test_adicao_simples`
- Implementação: `return a + b`
- Testes adicionais:
  - `0 + 0`
  - `-1 + 5`
  - floats com casas decimais

---

### ➖ 2. Subtração

- Cenário: `5.0 - 2.0 = 3.0`
- Teste: `test_subtracao_simples`
- Implementação: `return a - b`
- Casos extras:
  - `0 - 0`
  - `-3 - (-2)`
  - floats com casas decimais

---

### ✖️ 3. Multiplicação

- Cenário: `4.0 * 2.5 = 10.0`
- Teste: `test_multiplicacao_simples`
- Implementação: `return a * b`
- Casos extras:
  - `0 * qualquer número`
  - negativos
  - floats pequenos

---

### ➗ 4. Divisão

- Cenários:
  - `10.0 / 2.0 = 5.0`
  - `10.0 / 0 → ZeroDivisionError`
- Testes:
  - `test_divisao_simples`
  - `test_divisao_por_zero`
- Implementação:
  ```python
  if b == 0.0:
      raise ZeroDivisionError("Divisão por zero não permitida")
  return a / b
  ```

---

### 🟰 5. Raiz Quadrada

- Cenários:
  - `√9.0 = 3.0`
  - `√-4.0 → ValueError`
- Testes:
  - `test_raiz_quadrada_simples`
  - `test_raiz_quadrada_negativo`
- Implementação:
  ```python
  if a < 0.0:
      raise ValueError("Raiz de número negativo não permitida")
  return math.sqrt(a)
  ```

---

### 🔼 6. Exponenciação

- Cenário: `2.0 ^ 3.0 = 8.0`
- Teste: `test_exponenciacao_simples`
- Implementação: `return base ** expoente`
- Casos adicionais:
  - expoente negativo
  - expoente zero
  - base decimal

---

## 🧮 7. Integração com a Classe Calculadora

- A classe `Calculadora` instancia internamente as 6 operações.
- Métodos públicos:
  - `somar(a, b)`
  - `subtrair(a, b)`
  - `multiplicar(a, b)`
  - `dividir(a, b)`
  - `raiz_quadrada(a)`
  - `exponenciar(base, expoente)`

- Todos os testes de integração da `Calculadora` devem chamar essas funções e validar os resultados.

---

## 📐 Resumo

Este projeto contém:

- ✅ **7 classes**:
  - `Calculadora` (principal)
  - `Adicao`
  - `Subtracao`
  - `Multiplicacao`
  - `Divisao`
  - `RaizQuadrada`
  - `Exponenciacao`
  
- ✅ **Cobertura completa de testes com `pytest`**
- ✅ **Boas práticas de TDD**
- ✅ **Estrutura modular e extensível**

---

## 🚀 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/Calculadora_Com_TDD.git
   cd Calculadora_Com_TDD
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Instale o pytest:
   ```bash
   pip install pytest
   ```

4. Execute os testes:
   ```bash
   pytest
   ```

---

## 🧪 Requisitos

- Python 3.8+
- pytest

---

## 📄 Documentação

https://douglasxara2011.atlassian.net/wiki/external/MzBjN2EwOWUxNjI2NDYwMjliNTE4YjJiNzdlNTY5NGQ


📚 Referências Utilizadas no Projeto
Este projeto foi desenvolvido com base em diversas fontes de conhecimento técnico e acadêmico, bem como com o apoio de ferramentas modernas de desenvolvimento e inteligência artificial:

🎓 Formação em Qualidade de Software (QA) pela Scholarship Compass UOL, com foco em testes automatizados, boas práticas de verificação e validação, e uso de frameworks como pytest.

🧠 Engenharia de Software pela Unicesumar, aplicada no projeto através de:

Elaboração de diagramas de classe UML.

Uso de Programação Orientada a Objetos (POO) como base estrutural.

Organização e sincronização de métodos, utilizando a classe main() para controle de fluxo.

🚀 Conhecimentos consolidados em Programação de Sistemas, também pela Unicesumar, especialmente na modelagem e modularização do código.

👨‍🏫 Aplicação de TDD (Test Driven Development) com apoio da mentoria da Compass UOL, garantindo confiabilidade nas funcionalidades antes da implementação.

🤖 Documentação extensiva com IA, utilizando o ChatGPT (OpenAI) para:

Apoio na redação e organização técnica do conteúdo.

Geração assistida de trechos de código, análises e explicações.

💡 Apoio prático com GitHub Copilot, para sugestões de código, estruturação automatizada de testes e otimização do desenvolvimento.
