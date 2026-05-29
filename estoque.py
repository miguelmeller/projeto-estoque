##Definir as varíaveis
## id, nome quantidade, localização
produto = [
    [1, "Martelo", 5, "Prateleira 01"],
    [2, "Alicate", 4, "Prateleira 02"],
    [3, "Martelo", 3, "Prateleira 03"]

]

## Definir funções:

def registrarProdutos():
    ##Essa funções pergunta o nome do produto e adicona na lista de produtos
    novoProduto = input("Digite o nome do produto: ") ##Pergunta qual produto
    produto.append(novoProduto) ##Inserimos o produto
    print("Produto inserido com sucesso!")


def listarProdutos():
    ##Lista os produtos registrados
    print("\n----- PRODUTOS LISTADOS -----")
    print(f"Produtos disponíveis: {produto}")
    print("--------------------------------")

##Criar um menu

while True: ##Esse loop roda para sempre!
    print("\nPor favor selecione uma opção: ")
    print("\n1- Novo produto | 2- Listar produtos | 3- Buscar por ID | 4- Atualizar estoque | 5- Sair")
    opcao = input("Escolha: ")
    if (opcao == "1"):
        registrarProdutos()
    elif (opcao == "2"):
        listarProdutos()



    


