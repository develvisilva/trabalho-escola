print('Bem vindo(a) a loja do Elvis Silva') #identificador pessoal
# OPÇÃO DO MENU, CADA NÚMERO RECEBE UMA DESCRIÇÃO
menu_da_mercearia {
    1: 'Cadastrar Produto'
    2: ['Consultar Produto', {
        1: 'Consultar Todos os Produtos',
        2: 'Consultar Produtos por Código',
        3: 'Consultar Produto(s) por Fabricante',
        4: 'Retornar',
    }],
    3: 'Remover Produto'
    4: 'Sair'
}

def FUN_menu(menu: dict) -> None: #FUNÇÃO QUE IMPRIME AS OPÇÕES DOS MENUS
        for key, val in menu.itens():
            print(f"{key} - {val if type(val) == str else val[0]}")
        
        print('-' *35)

def mostrar_menu(menu: dict) -> int: #FUNÇÃO QUE IMPRIME E VALIDA A OPÇÃO MENU
    print(f"\n{'Menu Principal':-^30s}")
    fUN_menu(menu)
    
    while True:
        try:
            opcao = int(input('Escolha a opção desejada:'))
            
            #VERIFICA SE A OPÇÃO ESTÁ PRESENTE NO DICIONÁRIO DO MENU
            #SE SIM, LIMPA A TELA E RETORNA A OPÇÃO SELECIONADA
            if opcao in menu.keys():
                break
            else:
                print('\nOpção inválida!\n')
        except ValuError:
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
    produtos[].append(nome)
    produtos[].append(fabricante)
    produtos[].append(valor)

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
            
    

