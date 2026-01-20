'''
Lucas está desenvolvendo um jogo e precisa de uma funcionalidade que verifique 
se um número é par ou ímpar. Essa verificação será usada para definir ações diferentes 
dentro do jogo. Escreva um programa que receba um número inteiro e exiba uma mensagem 
informando se ele é par ou ímpar.'''

import os 
os.system("cls")

print("Verificando paridade de um número inteiro")
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"\nO número {numero} é par")
else:
    print(f"\nO número {numero} é ímpar")