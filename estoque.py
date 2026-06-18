##Definir as varíaveis
## id, nome, quantidade, localização 
produtos = [
    [1, "Pão de forma", 5, "Prateleira 01"],
    [2, "Bolacha", 4, "Prateleira 02"],
    [3, "Macarrão", 3, "Prateleira 03"]
]

proximoId = 4

## Definir funções:

def registrarProdutos():
    global proximoId
    ##Essa funções pergunta o nome do produto e adicona na lista de produtos
    novoProduto = input("Digite o nome do produto: ") ##Pergunta qual produto
    ###produto.append(novoProduto) ##Inserimos o produto
    quantidade = input("Digite  a quantidade: ")
    localizacao = input("Digite a localização: ")
    
    produtos.append([proximoId, novoProduto, quantidade, localizacao])
    proximoId = proximoId + 1
    print("Produto inserido com sucesso!✔️")

    travarMenu()

def listarProdutos():
    ##Lista os produtos registrados
    print("\n----- PRODUTOS LISTADOS -----")
    for item in produtos: ##Para cada item, ele mostra no formato abaixo e soma no total
        print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]}")
    print("--------------------------------")

    travarMenu()

def buscarProduto():
    ##Busca produtos por ID
    valorProcurado = int(input("Digite o ID do item: "))
    posicaoProcurada = -1
    
    for i in range(len(produtos)):
        if (produtos[i][0] == valorProcurado):
            posicaoProcurada = i
    if (posicaoProcurada == -1):
        print("Produto não encontrado.")
    else:
        print(f"O produto é {produtos[posicaoProcurada]}")
        
    travarMenu()

def atualizarEstoque():
    idProduto = int(input("Digite o ID do produto: "))
    posicaoProcurada = -1
    for i in range(len(produtos)):
        if(produtos[i][0] == idProduto):
            posicaoProcurada = i

    print(f"Produto atualizado {produtos[posicaoProcurada]}")
    novaQuantidade= int(input(f"Qual a nova quantidade do produto?: "))
    produtos[posicaoProcurada][2] = novaQuantidade ## Muda a quantidade do produto desejado
    print("Quantidade atualizada!✔️")
    print(f"{produtos[posicaoProcurada]}")
    
    travarMenu()

def excluirProduto():
    itemProcurado = int(input("Digite o ID do item para excluir: "))
    linhaProcurada = -1


    for i in range(len(produtos)): ##Varre linha a linha da matriz
        if (produtos [i][0] == itemProcurado): ##Verifica se a posição do nome é igual ao nome procurado
            linhaProcurada = i
    print(f"O item procurado está na linha {linhaProcurada}")

    print("\nItem selecionado excluido.✔️ ")
    produtos.pop(linhaProcurada)
    
    
##Criar uma função para pausar o código entre as interações do usuario
def travarMenu():

    input("\nPressione <ENTER> para continuar...")

##Criar um menu

while True: ##Esse loop roda para sempre!
    print("\nPor favor selecione uma opção: ")
    print("\n1- Novo produto | 2- Listar produtos | 3- Buscar por ID | 4- Atualizar estoque | 5- Excluir produto | 6- Sair")
    opcao = input("Escolha: ")
    if (opcao == "1"):
        registrarProdutos()
    elif (opcao == "2"):
        listarProdutos()
    elif (opcao == "3"):
        buscarProduto()
    elif (opcao == "4"):
        atualizarEstoque()
    elif(opcao == "5"):
        excluirProduto()
    elif (opcao == "6"):
        print("Sistema encerrado. Volte sempre!")
        break
    else:
        print("Opcão inválida! Escolha outra.")
  




    


