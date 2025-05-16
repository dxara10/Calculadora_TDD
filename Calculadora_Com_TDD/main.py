# Importando a classe Calculadora do módulo calculadora
from calculadora.calculadora import Calculadora

def main():
    # Inicializando a calculadora
    calc = Calculadora()
    
    while True:
        # Exibindo o menu de operações
        print("\nEscolha uma operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Raiz Quadrada")
        print("6. Exponenciação")
        print("7. Sair")
        
        # Lendo a escolha do usuário
        escolha = input("Digite o número da operação: ")
        
        if escolha == '7':
            print("Saindo...")
            break
        
        # Lendo os números de entrada
        if escolha in ['1', '2', '3', '4', '6']:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        
        elif escolha == '5':
            a = float(input("Digite o número: "))
        
        # Executando a operação escolhida
        try:
            if escolha == '1':
                resultado = calc.somar(a, b)
                print(f"Resultado: {resultado}")
            elif escolha == '2':
                resultado = calc.subtrair(a, b)
                print(f"Resultado: {resultado}")
            elif escolha == '3':
                resultado = calc.multiplicar(a, b)
                print(f"Resultado: {resultado}")
            elif escolha == '4':
                resultado = calc.dividir(a, b)
                print(f"Resultado: {resultado}")
            elif escolha == '5':
                resultado = calc.raiz_quadrada(a)
                print(f"Resultado: {resultado}")
            elif escolha == '6':
                resultado = calc.exponenciar(a, b)
                print(f"Resultado: {resultado}")
            else:
                print("Escolha inválida. Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()