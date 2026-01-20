'''
Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas 
no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele
precisa escrever um programa que identifique e exiba qual deles teve maior venda.

Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando 
qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

Saída esperada:
Digite a quantidade de maças vendidas:
Digite a quantidade de bananas vendidas:
As xxxxxx tiveram mais vendas
'''

print("Sistema de monitoramento de vendas")
maca = int(input("\nDigite a quantidade de maçãs vendidas: "))
banana = int(input("\nDigite a  quantidade de bananas vendidas: "))

if maca > banana:
    print("As maçãs tiveram mais vendas")
elif maca ==  banana:
    print("Foram vendidas a mesma quantidade de maçãs e bananas")
else:
    print("As bananas tiveram mais vendas")

