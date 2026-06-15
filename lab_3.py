def exibir_menu():
    print("\n" + "="*35)
    print("   SISTEMA DE GESTÃO DE ESTOQUE")
    print("="*35)
    print("1. Adicionar produto")
    print("2. Listar produtos")
    print("3. Remover produto")
    print("4. Atualizar quantidade de produto")
    print("5. Sair")
    print("="*35)
    return input("Escolha uma opção (1-5): ").strip()

def adicionar_produto(estoque):
    print("\n--- ADICIONAR PRODUTO ---")
    nome = input("Digite o nome do produto: ").strip()
    
    if not nome:
        print("Erro: O nome do produto não pode ser vazio.")
        return

    try:
        quantidade = int(input(f"Digite a quantidade de '{nome}': "))
        preco = float(input(f"Digite o preço de '{nome}': R$ "))
        
        if quantidade < 0 or preco < 0:
            print("Erro: Quantidade e preço não podem ser valores negativos.")
            return
            
        estoque[nome] = {"quantidade": quantidade, "preço": preco}
        print(f"Sucesso: Produto '{nome}' adicionado/atualizado com êxito!")
    except ValueError:
        print("Erro: Entrada inválida. Quantidade deve ser número inteiro e Preço deve ser número decimal.")

def listar_produtos(estoque):
    print("\n--- PRODUTOS EM ESTOQUE ---")
    if not estoque:
        print("O estoque está completamente vazio.")
        return
    
    # Ordenação alfabética utilizando uma função lambda
    produtos_ordenados = sorted(estoque.items(), key=lambda item: item[0].lower())
    
    for nome, dados in produtos_ordenados:
        print(f"Nome do produto: {nome} | Quantidade disponível: {dados['quantidade']} - Preço: R$ {dados['preço']:.2f}")

def remover_produto(estoque):
    print("\n--- REMOVER PRODUTO ---")
    nome = input("Digite o nome do produto que deseja remover: ").strip()
    
    if nome in estoque:
        del estoque[nome]
        print(f"Sucesso: O produto '{nome}' foi removido do estoque.")
    else:
        print(f"Erro: O produto '{nome}' não foi encontrado no estoque.")

def atualizar_quantidade(estoque):
    print("\n--- ATUALIZAR QUANTIDADE ---")
    nome = input("Digite o nome do produto para atualizar o estoque: ").strip()
    
    if nome in estoque:
        try:
            nova_qtd = int(input(f"Digite a nova quantidade para '{nome}': "))
            if nova_qtd < 0:
                print("Erro: A quantidade não pode ser negativa.")
                return
            estoque[nome]["quantidade"] = nova_qtd
            print(f"Sucesso: Quantidade de '{nome}' atualizada para {nova_qtd}!")
        except ValueError:
            print("Erro: Entrada inválida. A quantidade deve ser um número inteiro.")
    else:
        print(f"Erro: O produto '{nome}' não foi encontrado no estoque.")

def main():
    estoque = {}  # Dicionário principal que armazenará todo o estoque
    
    while True:
        opcao = exibir_menu()
        
        if opcao == "1":
            adicionar_produto(estoque)
        elif opcao == "2":
            listar_produtos(estoque)
        elif opcao == "3":
            remover_produto(estoque)
        elif opcao == "4":
            atualizar_quantidade(estoque)
        elif opcao == "5":
            print("\nEncerrando o programa. Sistema finalizado com sucesso!")
            break
        else:
            print("\nErro: Opção inválida! Escolha um número entre 1 e 5.")

if __name__ == "__main__":
    main()