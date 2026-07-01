estoque = []

def cadastrar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))

    produto = {
        "nome": nome,
        "Quantidade": quantidade
    }

    estoque.append(produto)
    print("Produto cadastrado com sucesso.")

def listar_produtos():
    if len(estoque) == 0:
        print("Nenhum produto cadastrado.")
    else:
        print("Lista de Produtos")
        for produto in estoque:
            print(f"Produto: {produto["nome"]} Quantidade: {produto["Quantidade"]}")
        print()


def buscar_produto():
    nome = input("Digite o nome do produto: ")

    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            print(f"Produto encontrado: {produto["nome"]}")
            print(f"Quantidade: {produto["Quantidade"]}")
            return

    print("Produto não encontrado.")


def atualizar_estoque():
    nome = input("Digite o nome do produto: ")

    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            nova_quantidade = int(input("Nova quantidade: "))
            produto["Quantidade"] = nova_quantidade
            print("Estoque atualizado com sucesso. ")
            return
    
    print("Produto não encontrado. ")

def remover_produto():
    nome = input("Digite o nome do produto para remover: ")

    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            estoque.remove(produto)
            print("Produto removido. ")
            return
    
    print("Produto não cadastrado. ")

def total_produtos():
    print(f"Total de produtos cadastrados: {len(estoque)}")


while True:
    print("CONTROLE DE ESTOQUE")
    print("1 - Cadstrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Atualizar estoque")
    print("5 - Remover produto")
    print("6 - Total de produtos cadastrados")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        buscar_produto()
    elif opcao == "4":
        atualizar_estoque()
    elif opcao == "5":
        remover_produto()
    elif opcao == "6":
        total_produtos()
    elif opcao == "7":
        print("Programa encerrado")
        break

    else:
        print("Opção inválida.")
