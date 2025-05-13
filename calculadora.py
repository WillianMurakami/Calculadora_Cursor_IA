import math
import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_boas_vindas():
    limpar_tela()
    print("\n" + "="*60)
    print("                   CALCULADORA PYTHON v1.0")
    print("="*60)
    print("\nBem-vindo à Calculadora Python!")
    print("\nEste é um projeto desenvolvido para demonstrar as capacidades")
    print("de programação em Python, oferecendo uma interface simples e")
    print("intuitiva para realizar cálculos matemáticos básicos e avançados.")
    print("\nDesenvolvido por: [Seu Nome]")
    print("Versão: 1.0")
    print("Data: 2024")
    print("\nPressione ENTER para continuar...")
    input()

def mostrar_ajuda():
    limpar_tela()
    print("\n" + "="*60)
    print("                      MENU DE AJUDA")
    print("="*60)
    print("\nComo usar a calculadora:")
    print("\n1. Soma (+)")
    print("   - Soma dois números")
    print("   - Exemplo: 2 + 2 = 4")
    print("\n2. Subtração (-)")
    print("   - Subtrai o segundo número do primeiro")
    print("   - Exemplo: 5 - 3 = 2")
    print("\n3. Multiplicação (*)")
    print("   - Multiplica dois números")
    print("   - Exemplo: 4 × 3 = 12")
    print("\n4. Divisão (/)")
    print("   - Divide o primeiro número pelo segundo")
    print("   - Exemplo: 10 ÷ 2 = 5")
    print("\n5. Potenciação (^)")
    print("   - Eleva o primeiro número ao segundo")
    print("   - Exemplo: 2 ^ 3 = 8")
    print("\n6. Raiz Quadrada (√)")
    print("   - Calcula a raiz quadrada de um número")
    print("   - Exemplo: √16 = 4")
    print("\n7. Sair")
    print("   - Encerra o programa")
    print("\nObservações:")
    print("- Para números decimais, use ponto (.)")
    print("- Em caso de erro, siga as instruções na tela")
    print("\nPressione ENTER para voltar ao menu principal...")
    input()

def apresentacao():
    print("\n" + "="*60)
    print("                   CALCULADORA PYTHON v1.0")
    print("="*60)
    print("\nEscolha uma operação:")
    print("  1. Soma (+)          - Soma dois números")
    print("  2. Subtração (-)     - Subtrai dois números")
    print("  3. Multiplicação (*) - Multiplica dois números")
    print("  4. Divisão (/)       - Divide dois números")
    print("  5. Potenciação (^)   - Eleva um número a outro")
    print("  6. Raiz Quadrada (√) - Calcula a raiz quadrada")
    print("  7. Sair             - Encerra o programa")
    print("\n  8. Ajuda            - Mostra instruções detalhadas")
    print("="*60)

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    if a < 0:
        return "Erro: Não é possível calcular raiz quadrada de número negativo!"
    return math.sqrt(a)

def continuar_calculando():
    while True:
        opcao = input("\nDeseja fazer outro cálculo? (S/N): ").upper()
        if opcao in ['S', 'N']:
            return opcao == 'S'
        print("Por favor, digite apenas S ou N.")

def calculadora():
    mostrar_boas_vindas()
    
    while True:
        limpar_tela()
        apresentacao()
        
        try:
            opcao = int(input("\nSua escolha (1-8): "))
            
            if opcao == 8:
                mostrar_ajuda()
                continue
            
            if opcao == 7:
                print("\nObrigado por usar a calculadora!")
                print("Encerrando programa...")
                time.sleep(2)
                break
                
            if opcao == 6:
                num = float(input("\nDigite o número para calcular a raiz quadrada: "))
                resultado = raiz_quadrada(num)
                print(f"\nA raiz quadrada de {num} é: {resultado}")
            else:
                if opcao == 1:
                    print("\n=== SOMA ===")
                elif opcao == 2:
                    print("\n=== SUBTRAÇÃO ===")
                elif opcao == 3:
                    print("\n=== MULTIPLICAÇÃO ===")
                elif opcao == 4:
                    print("\n=== DIVISÃO ===")
                elif opcao == 5:
                    print("\n=== POTENCIAÇÃO ===")
                else:
                    print("Opção inválida!")
                    time.sleep(2)
                    continue
                
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if opcao == 1:
                    resultado = soma(num1, num2)
                    print(f"\n{num1} + {num2} = {resultado}")
                elif opcao == 2:
                    resultado = subtracao(num1, num2)
                    print(f"\n{num1} - {num2} = {resultado}")
                elif opcao == 3:
                    resultado = multiplicacao(num1, num2)
                    print(f"\n{num1} × {num2} = {resultado}")
                elif opcao == 4:
                    resultado = divisao(num1, num2)
                    print(f"\n{num1} ÷ {num2} = {resultado}")
                elif opcao == 5:
                    resultado = potencia(num1, num2)
                    print(f"\n{num1} ^ {num2} = {resultado}")
            
            if not continuar_calculando():
                print("\nObrigado por usar a calculadora!")
                print("Encerrando programa...")
                time.sleep(2)
                break
                
        except ValueError:
            print("\nErro: Por favor, digite apenas números!")
            time.sleep(2)
        except Exception as e:
            print(f"\nErro inesperado: {e}")
            time.sleep(2)

if __name__ == "__main__":
    calculadora() 