print('Bem Vindo(a) a Companhia de Logística Elvis Silva S.A.')

pedido = True

# area   = base * altura / 2.0
def dimensoesObjeto():
    while True:
        try:
            dms1 = int(input('Digite o comprimento do objeto (em cm):'))
            dms2 = int(input('Digite a largura do objeto (em cm):'))
            dms3 = int(input('Digite a altura do objeto (em cm):')) 
            x = (dms3 * dms1) * dms2
            print('Volume do objeto é (em cm³): {}'.format(x))
            if(x <=1000):
                return 10.00
            elif(x >=1001) and (x < 10000):
                return 20.00
            elif(x >=30001) and (x < 100000):
                return 50.00
            else:
                print('Não aceitamos objetos com dimensões tão grandes!')
                continue
        except ValueError:
            print('Você digitou peso do objeto com valor não numérico!')
            print('Por favor entre com o peso desejado novamente!')
                