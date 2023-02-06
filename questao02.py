#QUESTÃO 02 DE 04
print('Bem Vindo(a) a Lachonete de Elvis Silva')
print('----------------Cardápio---------------')

print("|Código |       Descrição       |Valor|")
print("|  100  |    Cachorro Quente    | 9,00|")
print("|  101  | Cachorro Quente Duplo |11,00|")
print("|  102  |         X-Egg         |12,00|")
print("|  103  |       X-Salada        |12,00|")
print("|  104  |        X-Bacon        |14,00|")
print("|  105  |        X-Tudo         |17,00|")
print("|  200  |   Refrigerante Lata   | 5,00|")
print("|  201  |      Chá Gelado       | 4,00|")

pedido = True
resposta = ''
codigo = 0
total = 0

#LÓGICA DO PEDIDO

while pedido == True:
        codigo = input('Informe um código de acordo com a tabela:')
        if codigo == '100':
            print('100 - Cachorro-Quente - R$9,00')
            total = total + 9
            resposta = input('Deseja pedir mais alguma coisa? \n1 - Sim \n0 - Não\n')
            if resposta == '1':
                continue
            if resposta == '0':
                print('Seu pedido foi finalizado!')
                break
        elif codigo == '101':
            print('101 - Cachorro-Quente Duplo - R$11,00')
            total = total + 11
            resposta = input('Deseja pedir mais alguma coisa? \n1 - Sim \n0 - Não\n')
            if resposta == '1':
                continue
            if resposta == '0':
                print('Seu pedido foi finalizado!')
                break
        elif codigo == '102':
            print('102 - X-Egg - R$12,00')
            total = total + 12
            resposta = input('Deseja pedir mais alguma coisa? \n1 - Sim \n0 - Não\n')
            if resposta == '1':
                continue
            if resposta == '0':
                print('Seu pedido foi finalizado!')
                break
        elif codigo == '103':
            print('103 - X-Salada - R$13,00')
            total = total + 13
            resposta = input('Deseja pedir mais alguma coisa? \n1 - Sim \n0 - Não\n')
            if resposta == '1':
                continue
            if resposta == '0':
                print('Seu pedido foi finalizado!')
                break
        elif codigo == '104':
            print('104 - X-Bacon - R$14,00')
            total = total + 14
            resposta = input('Deseja pedir mais alguma coisa? \n1 - Sim \n0 - Não\n')
            if resposta == '1':
                continue
            if resposta == '0':
                print('Seu pedido foi finalizado!')
                break
        elif codigo == '105':
            print('105 - X-Tudo - R$17,00')
            total = total + 17
            resposta = input('Deseja pedir mais alguma coisa? \n1 - Sim \n0 - Não\n')
            if resposta == '1':
                continue
            if resposta == '0':
                print('Seu pedido foi finalizado!')
                break
        elif codigo == '200':
            print('200 - Refrigerante Lata - R$5,00')
            total = total + 5
            resposta = input('Deseja pedir mais alguma coisa? \n1 - Sim \n0 - Não\n')
            if resposta == '1':
                continue
            if resposta == '0':
                print('Seu pedido foi finalizado!')
                break
        elif codigo == '201':
            print('201 - Chá Gelado - R$4,00')
            total = total + 4
            resposta = input('Deseja pedir mais alguma coisa? \n1 - Sim \n0 - Não\n')
            if resposta == '1':
                continue
            if resposta == '0':
                print('Seu pedido foi finalizado!')
                break
        else:
            print('Opção Inválida')
            resposta = input('Deseja continuar seu pedido? Sim ou Não?')
            continue

print('Valor Total: R${}'.format(total))