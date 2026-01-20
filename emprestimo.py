'''
Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:
- O valor da renda mensal precisa ser maior que R$ 2.000,00.
- O valor da parcela não pode ultrapassar 30% da renda.
Crie um programa que receba como entrada a renda mensal de Pedro e o valor da 
parcela desejada. O programa deve informar se o empréstimo foi aprovado ou negado 
com base nas condições acima.
'''
import os
os.system("cls")

print("\nSimulação de empréstimo\n")
renda = float(input("Digite o valor da sua renda mensal: "))
parcela = float(input("Digite o valor da parcela desejada: "))

if renda > 2000:
    if (renda * 0.3) >= parcela:
        print("\nEmpréstimo aprovado")
    else:
        print("Empréstimo negado: parcela acima de 30% da renda")
else:
    print("Empréstimo negado: renda mínima de R$2000,00 não foi atingida")

