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
            print('{} - {val if type(val) == str else val[0]}'.format(key))
        
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
def

