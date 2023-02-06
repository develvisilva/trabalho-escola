#QUESTÃO 04 DE 04
print('Bem vindo(a) a loja do Elvis Silva') #identificador pessoal
# OPÇÃO DO MENU, CADA NÚMERO RECEBE UMA DESCRIÇÃO
menu_da_mercearia = {
    1: 'Cadastrar Produto',
    2: ['Consultar Produto', {
        1: 'Consultar Todos os Produtos',
        2: 'Consultar Produtos por Código',
        3: 'Consultar Produto(s) por Fabricante',
        4: 'Retornar',
    }],
    3: 'Remover Produto',
    4: 'Sair'
}

def FUN_menu(menu: dict) -> None: #FUNÇÃO QUE IMPRIME AS OPÇÕES DOS MENUS
        for key, val in menu.itens():
            print(f"{key} - {val if type(val) == str else val[0]}")
        
        print('-' *35)

def mostrar_menu(menu: dict) -> int: #FUNÇÃO QUE IMPRIME E VALIDA A OPÇÃO MENU
    print(f"\n{'Menu Principal':-^30s}")
    FUN_menu(menu)
    
    while True:
        try:
            opcao = int(input('Escolha a opção desejada:'))
            
            #VERIFICA SE A OPÇÃO ESTÁ PRESENTE NO DICIONÁRIO DO MENU
            #SE SIM, LIMPA A TELA E RETORNA A OPÇÃO SELECIONADA
            if opcao in menu.keys():
                break
            else:
                print('\nOpção inválida!\n')
        except ValueError:
            print('\nOpção inválida!')
    return opcao

def cadastrarProduto(codigo: int) -> None: #FUNÇÃO QUE CADASTRA PRODUTOS
    print('\nOpção Cadastrar Produtos\n')
    print('Código do Produto {:>3}'.format(codigo))
    
    nome = input('Digite o nome do produto:').strip()
    fabricante = input('Digite o fabricante do produto:').strip()
    
    while True:
        try:
            valor = float(input('Digite o valor (R$) do produto:'))
            
            #VERIFICA SE O VALOR É MAIOR
            if valor <= 0:
                print('\nALERTA!!! Digite um valor maior que zero!\n')
            else:
                break
        except ValueError:
            print('\nALERTA!!! Digite um número válido!\n')
    
    produtos[codigo] = []
    produtos[codigo].append(nome)
    produtos[codigo].append(fabricante)
    produtos[codigo].append(valor)

def removerProduto() -> None: #FUNÇÃO QUE REMOVE PRODUTOS
    while True:
        try:
            codigo = int(input('\nEscreva o código do produto a ser removido:\n'))
            
            #VERIFICA SE EXISTE O PRODUTO COM O CÓDIGO INFORMADO
            # SE SIM, REMOVE O PRODUTO DO DICIONÁRIO
            if codigo not in produto.keys():
                print('\nNenhum produto possui esse código.')
            else:
                produtos.pop(codigo)
            break
        except ValueError:
            print('\nALERTA!!! Digite um código válido!\n')
            
def consultarProduto() -> None: #FUNÇÃO PARA CONSULTA DE PRODUTOS
    #VARIÁVEL USADA PARA CONTROLAR A EXIBIÇÃO DO MENU DE CONSULTA
    exibir_menu = True
    
    cabecalho = f"| {'Código':<10} | {'Nome':<25} | {'Fabricante':<20} | {'Valor (R$)':>10} |" 
    len_cabecalho = len(cabecalho)
    
    while True:
        try:
            #EXIBE O MENU DE CONSULTA
            if exibir_menu:
                print('\nVocê selecionou a opção Consultar Produtos\n')
                print(f"{'Consultar Produtos':-^30s}")
                FUN_menu(menu_da_mercearia[2][1])
            opcao = int(input('Escolha a opção desejada:'))
            
            #OPÇÃO 1 - CONSULTAR TODOS OS PRODUTOS
            if opcao == 1:
                #LISTA TODOS OS PRODUTOS CADASTRADOS, SE HOUVER
                if len(produtos) > 0:
                    print("\nTodos os produtos cadastrados:\n")
                    
                    print('-' * len_cabecalho)
                    print(cabecalho)
                    print('-' * len_cabecalho)
                    
                    for key, val in produtos.items():
                        print(f"| {key:<10} | {val[0]:<25} | {val[1]:<20} | {val[2]:>10.2f} |")
                    print('-' * len_cabecalho)
                else:
                    print('\nNão existem produtos cadastrados!\n')
                print('')
                
            #OPÇÃO 2 - CONSULTAR PRODUTOS POR CÓDIGO
            elif opcao == 2:
                while True:
                    try:
                        codigo = int(input('\nDigite o código do produto a ser consultado.\n'))    
                        
                        #EXIBE O PRODUTO COM SEU RESPECTIVO CÓDIGO, SE HOUVER
                        if codigo in produtos.keys():
                            print("-" * len_cabecalho)
                            print(cabecalho)
                            print("-" * len_cabecalho)
                            print(f"| {codigo:<10} | {produtos[codigo][0]:<25} | {produtos[codigo][1]:<20} | {produtos[codigo][2]:>10.2f} |")
                            print('-' * len_cabecalho)
                        else:
                            print('\nNão existe produto com esse código.\n')
                            break
                    except ValueError:
                        print('\nDigite um código válido\n')
            #OPÇÃO 3 - CONSULTAR PRODUTOS POR FABRICANTE
            elif opcao == 3:
                while True:
                    try:
                        fabricante = input('\nDigite o fabricante do produto a ser consultado:\n')
                        #VARIÁVEL USADA PARA CONTROLAR A EXIBIÇÃO DO CABEÇALHO DA LISTA
                        exibir_produto = False
                        
                        for key, val in produtos.items():
                            #IMPRIME OS DADOS DO PRODUTO DO FABRICANTE INFORMADO
                            if val[1].upper() == fabricante.upper():
                                if not existe_produto:
                                    print("-" * len_cabecalho)
                                    print(cabecalho)
                                    print("-" * len_cabecalho)
                            print(f"| {key:<10} | {val[0]:<25} | {val[1]:<20} | {val[2]:>10.2f} |")
                            existe_produto = True
                        if not existe_produto:
                            print('\nNão existe produto com esse fabricante!\n')
                        else:
                            print('-' * len_cabecalho)
                        break
                    except ValueError:
                        print('Digite um fabricante válido.')
            elif opcao == 4:
                break
            else:
                print('\nAtenção! Você digitou uma opção inválida!\n')
                exibir_menu: True
        except ValueError:
                print('\nAtenção! Você digitou uma opção inválida!\n')
                exibir_menu: False
produtos = {}

while True:
    opcao_selecionada = mostrar_menu
    
    if opcao_selecionada == 1:
        cod_produtos = len(produtos) + 1
        cadastrarProduto(cod_produtos)
        
    elif opcao_selecionada == 2:
        consultarProduto()
        
    elif opcao_selecionada == 3:
        removerProduto
    
    else:
        break                           
                            
                            

