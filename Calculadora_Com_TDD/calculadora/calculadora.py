class Adicao:
    def executar(self, a: float, b: float) -> float:
        # Realiza a adição entre dois números
        return a + b


class Subtracao:
    def executar(self, a: float, b: float) -> float:
        # Realiza a subtração entre dois números
        return a - b


class Multiplicacao:
    def executar(self, a: float, b: float) -> float:
        # Realiza a multiplicação entre dois números
        return a * b


class Divisao:
    def executar(self, a: float, b: float) -> float:
        # Verifica se o divisor é zero
        if b == 0.0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        # Realiza a divisão entre dois números
        return a / b


class RaizQuadrada:
    def executar(self, a: float) -> float:
        # Verifica se o número é negativo
        if a < 0:
            raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
        # Calcula a raiz quadrada
        return a ** 0.5


class Exponenciacao:
    def executar(self, base: float, exp: float) -> float:
        # Calcula a exponenciação
        return base ** exp


class Calculadora:
    def __init__(self):
        # Instancia as classes de operação
        self.adicao = Adicao()
        self.subtracao = Subtracao()
        self.multiplicacao = Multiplicacao()
        self.divisao = Divisao()
        self.raiz = RaizQuadrada()
        self.exponenciacao = Exponenciacao()

    def somar(self, a: float, b: float) -> float:
        # Chama o método de adição
        return self.adicao.executar(a, b)

    def subtrair(self, a: float, b: float) -> float:
        # Chama o método de subtração
        return self.subtracao.executar(a, b)

    def multiplicar(self, a: float, b: float) -> float:
        # Chama o método de multiplicação
        return self.multiplicacao.executar(a, b)

    def dividir(self, a: float, b: float) -> float:
        # Chama o método de divisão
        return self.divisao.executar(a, b)

    def raiz_quadrada(self, a: float) -> float:
        # Chama o método de raiz quadrada
        return self.raiz.executar(a)

    def exponenciar(self, base: float, exp: float) -> float:
        # Chama o método de exponenciação
        return self.exponenciacao.executar(base, exp)