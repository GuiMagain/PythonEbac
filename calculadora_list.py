def obter_numero(mensagem):

    while True:
        try:
            return float(input(mensagem).replace(',', '.'))
        except ValueError:
            print("Valor inválido! Por favor, insira apenas números.")

def main():

    operacoes = {
        1: lambda a, b: a + b,
        2: lambda a, b: a - b,
        3: lambda a, b: a * b,
        4: lambda a, b: a / b
    }

    nomes_operacoes = ["Soma", "Subtração", "Multiplicação", "Divisão"]
    
    menu = [f"{i} - {nome}" for i, nome in enumerate(nomes_operacoes, start=1)]

    print("--- Calculadora Simples ---")

    while True:
        
        num1 = obter_numero("Insira o primeiro número: ")
        num2 = obter_numero("Insira o segundo número: ")

        print("\nEscolha uma operação:")
        for item in menu:
            print(item)

        try:
            escolha = int(input("Você escolheu: "))
    
            if escolha not in operacoes:
                print("Operação inválida! Por favor, escolha um número de 1 a 4.")
                continue
                
        except ValueError:
            print("Entrada inválida! Por favor, digite o número da operação desejada.")
            continue

        if escolha == 4:
            while num2 == 0:
                print("Divisão por zero não é permitida.")
                num2 = obter_numero("Por favor, insira outro número para o divisor: ")

        resultado = operacoes[escolha](num1, num2)
        
        if resultado.is_integer():
            resultado = int(resultado)
            
        print(f"O resultado é: {resultado}")
        
        continuar = input("\nDeseja realizar outra operação? (S/N): ").strip().upper()
        if continuar != 'S':
            print("Encerrando a calculadora. Até logo!")
            break
        print("-" * 30)

if __name__ == "__main__":
    main()