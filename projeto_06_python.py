tarefas = []

def adicionar_tarefa():
    nome = input("Nome da tarefa: ")
    descricao = input("Descrição: ")
    prioridade = input("Prioridade (Alta, Média, Baixa): ")
    categoria = input("Categoria: ")

    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }

    tarefas.append(tarefa)
    print("✅ Tarefa adicionada com sucesso!\n")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
        return

    for i, tarefa in enumerate(tarefas, start=1):
        status = "✔️ Concluída" if tarefa["concluida"] else "⏳ Pendente"
        print(f"{i}. {tarefa['nome']} ({tarefa['prioridade']}) - {tarefa['categoria']} [{status}]")
        print(f"   Descrição: {tarefa['descricao']}")
    print()

def marcar_concluida():
    listar_tarefas()
    if not tarefas:
        return

    indice = int(input("Digite o número da tarefa concluída: ")) - 1
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        print("✅ Tarefa marcada como concluída!\n")
    else:
        print("Número inválido.\n")

def exibir_por_prioridade():
    prioridade = input("Digite a prioridade (Alta, Média, Baixa): ")
    filtradas = [t for t in tarefas if t["prioridade"].lower() == prioridade.lower()]

    if not filtradas:
        print("Nenhuma tarefa com essa prioridade.\n")
        return

    for t in filtradas:
        print(f"- {t['nome']} ({t['categoria']})")
    print()

def exibir_por_categoria():
    categoria = input("Digite a categoria: ")
    filtradas = [t for t in tarefas if t["categoria"].lower() == categoria.lower()]

    if not filtradas:
        print("Nenhuma tarefa nessa categoria.\n")
        return

    for t in filtradas:
        print(f"- {t['nome']} ({t['prioridade']})")
    print()

def menu():
    while True:
        print("==== Gerenciador de Tarefas ====")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Exibir tarefas por prioridade")
        print("5. Exibir tarefas por categoria")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            marcar_concluida()
        elif opcao == "4":
            exibir_por_prioridade()
        elif opcao == "5":
            exibir_por_categoria()
        elif opcao == "6":
            print("👋 Saindo... até logo!")
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    menu()