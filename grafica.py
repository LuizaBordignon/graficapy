orcamentos = {}
clientes = {}

def menu():
    while True:
        print('Bem vindo a gráfica ArtFox!\n')
        vcadastro = input("Possui cadastro?\n[S|N]: ").upper()
        if vcadastro == 'S':
            cpf = int(input('Informe seu CPF (sem numeração): '))
            if cpf in clientes:
                print('Aba orçamento')
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
    
menu()
