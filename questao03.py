#QUESTÃO 03 DE 04
print('Bem Vindo(a) a Companhia de Logística Elvis Silva S.A.')

pedido = True

#ENTRADA COM DIMENSÃO DA CARGA
def dimensoesObjeto():
    while True:
        try:
            dms1 = int(input('Digite o comprimento do objeto (em cm):'))
            dms2 = int(input('Digite a largura do objeto (em cm):'))
            dms3 = int(input('Digite a altura do objeto (em cm):'))
            x = (dms3 * dms1) * dms2
            print('Volume do objeto é (em cm³): {:.1f}'.format(x))
            if(x <= 999):
                return 10.00
            elif(x >=1000) and (x < 10000):
                return 20.00
            elif(x >=10001) and (x < 30000):
                return 30.00
            elif(x >=30001) and (x < 100000):
                return 50.00
            else:
                print('Não aceitamos objetos com dimensões tão grandes!')
                print('Por favor entre com o peso desejado novamente!')
                continue
        except ValueError:
            print('Você digitou peso do objeto com valor não numérico!')

#ENTRADA COM PESO DA CARGA
def pesoObjeto():
    while True:
        try:
            peso = float(input('Digite o peso da carga em KG:'))
            y = peso
            if(y < 0.1):
                return 1
            elif(y > 0.1) and (y < 1):
                return 1.5
            elif(y > 1) and (y < 10):
                return 2
            elif(y < 30):
                return 3
            else:
                print('Carga excedeu o peso, caso tenha errado o KG ou tenha outra carga! \nDigite o peso novamente:')
                continue
        except ValueError:
            print('Você digitou peso do objeto com valor não numérico \nPor favor entre com o peso desejado novamente!')
            continue
#OPÇÃO DE ROTA COM SEUS RESPECTIVOS VALORES
def rotaObjeto():
    while True:
        try:
            rota = (input('Selecione a rota: \nBR - De Brasília para Rio de Janeiro\nBS - De Brasília para São Paulo\nRB - De Rio de Janeiro para Brasília\nRS - De Rio de Janeiro para São Paulo\nSR - De São Paulo para Rio de Janeiro\nSB - De São Paulo para Brasília\n>>'))
            r = rota
            if(r == 'RS'):
                return 1
            elif(r == 'SR'):
                return 1
            elif(r == 'BS'):
                return 1.2
            elif(r == 'SB'):
                return 1.2
            elif(r == 'BR'):
                return 1.5
            elif(r == 'RB'):
                return 1.5
            else:
                print('Você digitou uma rota que não existe!')
                continue
        except ValueError:
            print('Opa está rota não existe \nPor favor entre com a rota desejada novamente')

dim = dimensoesObjeto()
peso = pesoObjeto()
rot = rotaObjeto()
total = dim*peso*rot
print('O total a pagar ficou R$: {:.2f} (dimensões: {} * peso: {} * rota: {})'.format(total, dim, peso, rot))

print(dim)
print(peso)
print(rot)