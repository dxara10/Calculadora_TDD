class RaizQuadrada:
    """CUSO DO COPILOT PARA ESTA DOCSTRING: lasse para calcular a raiz quadrada de um número."""

    def executar(self, a: float) -> float:
        """Calcula a raiz quadrada de 'a'.

        Lança ValueError se 'a' for negativo.
        """
        if a < 0:
            raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
        return a ** 0.5  # Retorna a raiz quadrada de 'a'