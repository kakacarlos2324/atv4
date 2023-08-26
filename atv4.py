lista_compras = []

def adicionar_item():
    item = input("Digite o item que deseja adicionar: ")
    lista_compras.append(item)
    print(f"{item} foi adicionado à lista de compras.")

def apagar_item():
    if not lista_compras:
        print("A lista de compras está vazia.")
        return
    
    print("Itens na lista de compras:")
    for index, item in enumerate(lista_compras):
        print(f"{index + 1}: {item}")
    
    indice = int(input("Digite o número do item que deseja apagar: ")) - 1
    if 0 <= indice < len(lista_compras):
        item_removido = lista_compras.pop(indice)
        print(f"{item_removido} foi removido da lista de compras.")
    else:
        print("Índice inválido.")

def editar_item():
    if not lista_compras:
        print("A lista de compras está vazia.")
        return
    
    print("Itens na lista de compras:")
    for index, item in enumerate(lista_compras):
        print(f"{index + 1}: {item}")
    
    indice = int(input("Digite o número do item que deseja editar: ")) - 1
    if 0 <= indice < len(lista_compras):
        novo_item = input("Digite o novo item: ")
        lista_compras[indice] = novo_item
        print("Item editado.")
    else:
        print("Índice inválido.")

def listar_itens():
    if not lista_compras:
        print("A lista de compras está vazia.")
        return
    
    print("Itens na lista de compras:")
    for index, item in enumerate(lista_compras):
        print(f"{index + 1}: {item}")

while True:
    print("\nOpções:")
    print("1. Adicionar item")
    print("2. Apagar item")
    print("3. Editar item")
    print("4. Listar itens")
    print("5. Sair")
    
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == "1":
        adicionar_item()
    elif opcao == "2":
        apagar_item()
    elif opcao == "3":
        editar_item()
    elif opcao == "4":
        listar_itens()
    elif opcao == "5":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Digite novamente.")