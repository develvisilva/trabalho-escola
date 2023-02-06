#QUESTÃO 01 DE 04
print('Bem vindo(a) a Loja do Elvis Silva')

#INSERIR VALOR DE CADA PRODUTO
valor_unitario = float(input('Entre com o valor do produto:'))

#INSERIR VALOR DA QUANTIDADE
quantidade = int(input('Entre com o valor da quantidade:'))

valor_frete = 0 #VARIAVEL QUE RECEBERÁ O VALOR DO FRETE CONFORME QUANTIDADE DE PRODUTOS

#LOGICA DE DESCONTO CONFORME QUANTIDADE

if 0 <= quantidade < 10:
    valor_frete = 0
elif 10 <= quantidade < 100:
    valor_frete = 5
elif 100 <= quantidade < 1000:
    valor_frete = 10
else:
    valor_frete = 15

valor_parcial = float(valor_unitario * quantidade)#CALCULAR VALOR UNITÁRIO X QUANTIDADE

valor_porcentagem =float(valor_parcial * valor_frete / 100)#CALCULA PORCENTAGEM POR QUANTIDADE

valor_desconto = float(valor_parcial - valor_porcentagem)#CALCULA DESCONTO CONFORME QUANTIDADE

print('O valor sem desconto foi: R${:.2f}' .format(valor_parcial))#IRÁ IMPRIMIR O VALOR SEM DESCONTO

print('O valor com desconto foi: R$ {:.2f}' .format(valor_desconto) + ' ''(desconto {}%)'.format(valor_frete))
#MOSTRARÁ VALOR COM DESCONTO E A PORCENTAGEM CONFORME QUANTIDADE

