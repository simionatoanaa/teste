'''
Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. 
O valor do pedágio depende da distância percorrida:
Até 100 km: R$ 10,00
Entre 100 km e 200 km: R$ 20,00
Acima de 200 km: R$ 30,00
Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.
'''
import os
os.system("cls")

print("Calculadora de pedágio")
distancia = float(input("Digite a distância percorrida em km: "))

if distancia < 100:
    valor_final = 10 * distancia
    print(f"Valor do pedágio: R${valor_final:.2f}")
elif 100 <= distancia <= 200:
    valor_final = 20 * distancia
    print(f"Valor do pedágio: R${valor_final:.2f}")
else:
    valor_final = 30 * distancia
    print(f"Valor do pedágio: R${valor_final:.2f}")