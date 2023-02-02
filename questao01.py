
#Questão 01 de 04
print('Bem vindo(a) a Loja do Elvis Silva')

#inserir valor de cada produto
valor_unitario = float(input('Entre com o valor do produto:'))

#inserir valor da quantidade
quantidade = int(input('Entre com o valor da quantidade:'))

valor_frete = 0 #variavel que receberá o valor do frete conforme quantidade de produtos

#logica de desconto conforme quantidade

if 0 <= quantidade < 10:
    valor_frete = 0
elif 10 <= quantidade < 100:
    valor_frete = 5
elif 100 <= quantidade < 1000:
    valor_frete = 10
else:
    valor_frete = 15

valor_parcial = float(valor_unitario * quantidade)#calcula valor unitário x quantidade

valor_porcentagem =float(valor_parcial * valor_frete / 100)#calcula porcentagem por quantidade

valor_desconto = float(valor_parcial - valor_porcentagem)#calcula desconto conforme quantidade

print('O valor sem desconto foi: R${:.2f}' .format(valor_parcial)) #irá imprimir o valor sem desconto

print('O valor com desconto foi: R$ {:.2f}' .format(valor_desconto) + ' ''(desconto {}%)'.format(valor_frete))
#mostrará valor com desconto e a porcentagem conforme quantidade
