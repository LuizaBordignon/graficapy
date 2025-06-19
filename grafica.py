from datetime import date
from tabulate import tabulate

from enum import Enum
orders = {}
clientes = {}
product = {}

orderNum = 0

class PaymentWay(Enum):
    PIX = 1
    CREDIT = 2
    DEBIT = 3
    MONEY = 4

class Materials(Enum):
    FOSCO = 1
    BRILHOSO = 2
    RESINADO = 3
    LAMINADO = 4

class Status(Enum):
    PENDENTE = 1
    EM_ANDAMENTO = 2
    FEITO = 3
    CANCELADO = 4

def menu():
    global orderNum
    while True:
        if (len(orders) == 0 and len(clientes) == 0):
            print(15*'--')
            print("ARTFOX")
            print(15*'--')
            cadastros()
        else:
            print(40*"__")
            print(15*'--')
            print("MENU")
            print(15*'--')
            action = int(input("O que deseja fazer?\n[1] - Cadastrar novo pedido\n[2] - Visualizar\n[3] - Editar status de pedido\n[4] - Sair \n-> "))
            if (action == 1):
                vcadastro = input("Possui cadastro?\n[S|N]: ").upper()
                if vcadastro == 'S':
                    cpf = input('Informe seu CPF (sem pontuação): ')
                    if cpf in clientes:
                        orderNum += 1
                        handleOrder(cpf)
                    else:
                        validar = input('CPF inexistente, deseja se cadastrar?\n[S|N]: ').upper()
                        if validar == 'S':
                            cadastros()
                        else:
                            print('Até mais!\n')
                elif vcadastro == 'N':
                    cadastros()
                else:
                    print('Ops! Informação incorreta, por gentileza, informe novamente:')
            elif (action == 2):
                action = int(input("O que deseja visualizar?\n[1] - Todos\n[2] - Por Status\n[3] - Detalhes do pedido\n-> "))
                print(40*"--")
                match action:
                    case 1:
                        visualizar()
                    case 2:               
                        status = int(input("[1] - Pendente\n[2] - Em andamento\n[3] - Feito\n[4] - Cancelado\n-> "))
                        visualizarPorStatus(status)
                    case 3:
                        orderNum = int(input("Digite o número do pedido: "))
                        if orderNum in orders:
                            visualizarDetalhes(orderNum)
                        else:
                            print("Pedido não encontrado!")
            elif (action == 3):
                visualizar()
                orderNumToEdit = int(input("Digite o número de pedido que deseja editar: "))
                if orderNumToEdit in orders:
                    editar(orderNumToEdit)
                else:
                    print("Pedido não encontrado!")
            elif (action == 4):
                return
            else:
                print("Opção inválida!")

def handleProductsOrder():
    ordering = 's'
    products = []
    while ordering == 's':
       
        print("--------- Material ------------")
        productType = int(input("[1] - Fosco\n[2] - Brilhoso\n[3] - Resinado\n[4] - Laminado\n-> "))

        print("--------- Tamanho (cm) ------------")
        width = float(input("Largura: "))
        height = float(input("Altura: "))

        print("--------- Descrição ------------")
        description = input("Descrição do pedido: ")

        print("--------- Quantidade ------------")
        quantity = int(input("Quantidade: "))

        match productType:
            case 1:
                productType = Materials.FOSCO
                squareCmValue = 0.5
            case 2:
                productType = Materials.BRILHOSO
                squareCmValue = 0.3
            case 3:
                productType = Materials.RESINADO
                squareCmValue = 0.8
            case 4:
                productType = Materials.LAMINADO
                squareCmValue = 0.7
        
        product = {
            'Material': productType,
            'Largura': width,
            'Altura': height,
            'Quantidade': quantity,
            'Descrição': description,
            'Cm²': width * height,
            'Preço do Produto': (squareCmValue * (width * height)) * quantity
        }
        
        products.append(product)

        ordering = input('Deseja adicionar mais adesivos?\n[S|N]:  ').lower()

    return products

def handleOrder(cpf):
    global orderNum
    discount = 0
    print(40*"__")
    print(15*'--')
    print("ORÇAMENTO")
    print(15*'--')

    products = handleProductsOrder()
     
    print("--------- Forma de pagamento ------------")
    payment = int(input("[1] - Pix\n[2] - Crédito\n[3] - Débito\n[4] - Dinheiro\n-> "))

    match payment:
        case 1:
            payment = PaymentWay.PIX
        case 2:
            payment = PaymentWay.CREDIT
        case 3:
            payment = PaymentWay.DEBIT
        case 4:
            payment = PaymentWay.MONEY
            discount = 0.2

    if (clientes[cpf]['nascimento'][:5] == date.today().strftime("%d/%m")):
        print("Parabéns! Você acabou ganhar um desconto de aniversário.")
        discount = 0.4
    
    total = 0
    for product in products:
        total += product['Preço do Produto']

    orderDetails = {
        'Número do pedido': orderNum,
        'Pagamento': payment,
        'Desconto': discount,
        'Cliente': clientes[cpf],
        'Status': Status.PENDENTE,
        'Produto': products,
        'Valor Total': total * (1 - discount)
    }

    orders[orderNum] = orderDetails
    print(f"Pedido {orderNum} cadastrado com sucesso!")

def cadastros():
    global orderNum
    print(15*'--')
    print("CADASTRO")
    print(15*'--')
    cpf = input('Informe seu CPF (sem pontuação): ')
    nome = input('Informe seu nome completo: ')
    datanasc = input('Informe sua data de nascimento (ex: DD/MM/AAAA): ')
    email = input('Informe seu e-mail para contato: ')
    telefone = input('Informe seu telefone: ')
    dados = {
        'nome': nome,
        'nascimento': datanasc,
        'email': email,
        'telefone': telefone
    }
    clientes[cpf] = dados
    orderNum += 1
    handleOrder(cpf)

def formatter(ordersData, visualizationMode):
    if visualizationMode == 1:
        tables = []
        for order in ordersData.values():
            table_data = [
                ["Número do pedido", order['Número do pedido']],
                ["Status", order['Status'].name], 
                ["Valor Total", f"R$ {order['Valor Total']:.2f}"]
            ]
            
            for i, produto in enumerate(order['Produto'], 1):
                table_data.extend([
                    [f"Produto {i} - Material", produto['Material'].name],
                    [f"Produto {i} - Largura", f"{produto['Largura']} cm"],
                    [f"Produto {i} - Altura", f"{produto['Altura']} cm"],
                    [f"Produto {i} - Descrição", produto['Descrição']],
                    [f"Produto {i} - Quantidade", produto['Quantidade']],
                    [f"Produto {i} - Preço", f"R$ {produto['Preço do Produto']:.2f}"]
                ])
            
            tables.append(tabulate(table_data, headers=["Campo", "Valor"], tablefmt="grid"))
        
        return "\n\n".join(tables)
    
    elif visualizationMode == 2:
        table_data = []
        for order in ordersData.values():
            table_data.append([
                order['Número do pedido'],
                order['Status'].name,
                f"R$ {order['Valor Total']:.2f}"
            ])
        
        return tabulate(table_data, headers=["Número", "Status", "Valor Total"], tablefmt="grid")
    
    elif visualizationMode == 3:
        order = ordersData
        table_data = [
            ["Número do pedido", order['Número do pedido']],
            ["Pagamento", order['Pagamento'].name],
            ["Desconto", f"{order['Desconto']*100:.0f}%"],
            ["Status", order['Status'].name], 
            ["Valor Total", f"R$ {order['Valor Total']:.2f}"],
            ["Nome do cliente", order['Cliente']['nome']],
            ["Email do cliente", order['Cliente']['email']],
            ["Telefone do cliente", order['Cliente']['telefone']],
            ["Nascimento do cliente", order['Cliente']['nascimento']]
        ]

        for i, produto in enumerate(order['Produto'], 1):
            table_data.extend([
                [f"Produto {i} - Material", produto['Material'].name],
                [f"Produto {i} - Largura", f"{produto['Largura']} cm"],
                [f"Produto {i} - Altura", f"{produto['Altura']} cm"],
                [f"Produto {i} - Descrição", produto['Descrição']],
                [f"Produto {i} - Quantidade", produto['Quantidade']],
                [f"Produto {i} - Preço", f"R$ {produto['Preço do Produto']:.2f}"]
            ])
        
        return tabulate(table_data, headers=["Campo", "Valor"], tablefmt="grid")

def visualizar():
    if orders:
        print(formatter(orders, 1))
    else:
        print("Nenhum pedido cadastrado ainda.")

def visualizarDetalhes(orderNum):
    print(formatter(orders[orderNum], 3))
    
def visualizarPorStatus(status):
    print(40*"__")
    match status:
        case 1:
            statusName = "Pendente"
            status_enum = Status.PENDENTE
        case 2:
            statusName = "Em andamento"
            status_enum = Status.EM_ANDAMENTO
        case 3:
            statusName = "Feito"
            status_enum = Status.FEITO
        case 4:
            statusName = "Cancelado"
            status_enum = Status.CANCELADO

    print(f"Pedidos com status: {statusName}")
    filtered_orders = {k: v for k, v in orders.items() if v['Status'] == status_enum}
    
    if filtered_orders:
        print(formatter(filtered_orders, 2))
    else:
        print(f"Nenhum pedido com status {statusName}")

def editar(orderNum):
    orderToEdit = orders[orderNum]
    print('Selecione o novo Status: ')
    status = int(input("[1] - Pendente\n[2] - Em andamento\n[3] - Feito\n[4] - Cancelado\n-> "))
    match status:
        case 1:
            orderToEdit['Status'] = Status.PENDENTE
        case 2:
            orderToEdit['Status'] = Status.EM_ANDAMENTO
        case 3:
            orderToEdit['Status'] = Status.FEITO
        case 4:
            orderToEdit['Status'] = Status.CANCELADO
    
    print(f"Status do pedido {orderNum} atualizado para {orderToEdit['Status'].name}")

menu()