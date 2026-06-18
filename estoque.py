##Definir as varíaveis
## id, nome, quantidade, localização 
produto = [
    [1, "Pão de forma", 5, "Prateleira 01"],
    [2, "Bolacha", 4, "Prateleira 02"],
    [3, "Macarrão", 3, "Prateleira 03"]

]



proximoId = 1
## Definir funções:

def registrarProdutos():
    global proximoId
    ##Essa funções pergunta o nome do produto e adicona na lista de produtos
    novoProduto = input("Digite o nome do produto: ") ##Pergunta qual produto
    ###produto.append(novoProduto) ##Inserimos o produto
    quantidade = input("Digite  a quantidade: ")
    localizacao = input("Digite a localização: ")
    
    produto.append([novoProduto, quantidade, localizacao])
    proximoId = proximoId + 1
    print("Produto inserido com sucesso!")


def listarProdutos():
    ##Lista os produtos registrados
    print("\n----- PRODUTOS LISTADOS -----")
    #print(f"Produtos disponíveis: {produto}")
    for item in produto: ##Para cada item, ele mostra no formato abaixo e soma no total
        print(f"ID: {item[0]} | {item[1]} | {item[2]} ")
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
    #elif (opcao == "3"):




    


