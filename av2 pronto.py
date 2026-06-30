from datetime import datetime
import random

estoque = []


def cadastrar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))

    produto = {
        "codigo": random.randint(1, 9999),
        "nome": nome,
        "Quantidade": quantidade,
        "data_cadastro": datetime.now().strftime("%d/%m/%Y")
    }

    estoque.append(produto)
    print("Produto cadastrado com sucesso.")

def listar_produtos():
    if len(estoque) == 0:
        print("Nenhum produto cadastrado.")
    else:
        print("Lista de Produtos")
        for produto in estoque:
            print(
                f"Código: {produto["codigo"]} "
                f"Produto: {produto["nome"]} "
                f"Quantidade{produto["Quantidade"]} "
                f"Data: {produto["data_cadastro"]} "
            )
        print()


def buscar_produto():
    nome = input("Digite o nome do produto: ")

    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            print(f"Produto encontrado: {produto["nome"]}")
            print(f"Código: {produto["codigo"]}")
            print(f"Quantidade: {produto["Quantidade"]}")
            print(f"Data de cadastro: {produto["data_cadastro"]}")
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

def gerar_relatorio():
    tabela = [["Código", "Poduto", "Quantidade"]]

    for produto in estoque:
        tabela.append([
            produto["codigo"],
            produto["nome"],
            produto["Quantidade"],
            ])

    
    print("Relatório: ")
    for linha in tabela:
        print(linha)
    print()

while True:
    print("CONTROLE DE ESTOQUE")
    print("1 - Cadstrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Atualizar estoque")
    print("5 - Remover produto")
    print("6 - Gerar relatório")
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
        gerar_relatorio()
    elif opcao == "7":
        print("Programa encerrado")
        break

    else:
        print("Opção inválida.")