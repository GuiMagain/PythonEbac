# Variável global de tarefas
tarefas = {}

def adicionar_tarefa(tarefas, nome):
    nome: str = input("Digite o nome da tarefa: ")
    if nome in tarefas:
        return "Tarefa já existe."

    else:
        tarefas[nome] = False
        return "Tarefa adicionada com sucesso."
    
def listar_tarefas(tarefas):
    if not tarefas:
        return "Nenhuma tarefa cadastrada."
    else:
        resultado = []
        for nome, concluida in sorted(tarefas.items(), key=lambda x: x[0]):
            status = "✅ Concluída" if concluida else "❌ Não Concluída"
            resultado.append(f"{status}: {nome}")
        return "\n".join(resultado)

def remover_tarefa(tarefas):
    nome = input("Digite o nome da tarefa a ser removida: ").strip()
    if nome in tarefas:
        del tarefas[nome]
        return f"Tarefa '{nome}' removida com sucesso."
    else:
        return "Erro: Tarefa não encontrada."

def marcar_concluida(tarefas):
    nome = input("Digite o nome da tarefa a ser marcada como concluída: ").strip()
    if nome in tarefas:
        tarefas[nome] = True
        return f"Tarefa '{nome}' marcada como concluída."
    else:
        return "Erro: Tarefa não encontrada."

def exibir_menu():
    return (
        "1. Adicionar tarefa\n"
        "2. Listar tarefas\n"
        "3. Remover tarefa\n"
        "4. Marcar tarefa como concluída\n"
        "5. Sair\n"
    )

def funcao_principal():
    while True:
        print(exibir_menu())
        opcao =input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome: str = input("Digite o nome da tarefa: ")
            print(adicionar_tarefa(tarefas, nome))
        elif opcao == "2":
            print(listar_tarefas(tarefas))
        elif opcao == "3":
            print(remover_tarefa(tarefas))
        elif opcao == "4":
            nome = input("Digite o nome da tarefa a ser marcada como concluída: ").strip()
            print(marcar_concluida(tarefas))
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            print(exibir_menu())

if __name__ == "__main__":
    funcao_principal()