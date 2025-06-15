orcamentos = {}
clientes = {}

def menu():
    while True:
        orcamento()
        print('Bem vindo a gráfica ArtFox!\n')
        vcadastro = input("Possui cadastro?\n[S|N]: ").upper()
        if vcadastro == 'S':
            cpf = int(input('Informe seu CPF (sem numeração): '))
            if cpf in clientes:
                orcamento()
                break
            else:
                validar = input('CPF inexistente, deseja se cadastrar?\n[S|N]: ').upper
                if validar == 'S':
                    menu()
                else:
                    print('Até mais!\n')
        elif vcadastro == 'N':
            cadastros()
            break
        else:
            print('Ops! Informação incorreta, por gentileza, informe novamente:')

def orcamento():
    print(40*"__")
    print('')
    print('Bem vindo a aba orçamentos! Escolha as especificações do adesivo: ')
    print('')
    print("--------- Material ------------")
    productType = int(input("[1] - Fosco\n[2] - Brilhoso\n[3] - Resinado\n[4] - Laminado\n-> "))

    print("--------- Tamanho (cm) ------------")
    width = float(input("Largura: "))
    height = float(input("Altura: "))

    print("--------- Descrição ------------")
    description = input("Descrição do pedido: ")

    print("--------- Quantidade ------------")
    quantity = input("Quantidade: ")

    print("--------- Forma de pagamento ------------")
    payment = int(input("[1] - Pix\n[2] - Crédito\n[3] - Débito\n[4] - Dinheiro\n-> "))


    match productType:
        case 1:
            squareCmValue = 0.5
        case 2:
            squareCmValue = 0.3
        case 3:
            squareCmValue = 0.8
        case 4:
            squareCmValue = 0.7

    price = (squareCmValue * (width * height) * quantity)

    # match payment:
    #     case 1:
    #         di = 0.5 #calcular disconto ihuu
    #     case 2:
    #         squareCmValue = 0.3
    #     case 3:
    #         squareCmValue = 0.8
    #     case 4:
    #         squareCmValue = 0.7

    return


def cadastros():
    print('\nBem vindo a tela de cadastros! Por gentileza, preencha os dados:\n')
    cpf = input('Informe seu CPF (sem numeração): ')
    nome = input('Informe seu nome completo: ')
    datanasc = input('Informe sua data de nascimento (ex: DD/MM/AAAA): ')
    email = input('Informe seu e-mail para contato: ')
    telefone = int(input('Informe seu telefone: '))
    dados = {}
    dados['nome'] = nome
    dados['nascimento'] = datanasc
    dados['email'] = email
    dados['telefone'] = telefone
    clientes.update({cpf:dados})
    print(clientes)
    
menu()
