class Divisao:
    """Classe para realizar a operação de divisão."""

    def executar(self, a: float, b: float) -> float:
        """USO DO COPILOT PARA ESTA DOCSTRING: Executa a divisão de a por b.

        Parâmetros:
        a (float): O numerador.
        b (float): O denominador.

        Retorna:
        float: O resultado da divisão.

        Levanta:
        ZeroDivisionError: Se b for igual a zero.
        """
        if b == 0.0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return a / b