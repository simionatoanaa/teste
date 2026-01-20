'''
Uma professora precisa de um programa que ajude a calcular a média final dos alunos e 
informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:
Média >= 7: Aprovado
5 <= Média < 7: Recuperação
Média < 5: Reprovado
Escreva um programa que receba três notas como entrada e calcule a média final. Com base 
na média, exiba a situação do aluno.
'''
import os
os.system("cls")

print("Calculadora de média final")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media_final = (nota1 + nota2 + nota3)/3

print(f"A média é {media_final:.2f}")
if media_final < 5:
    print("Aluno reprovado")
elif media_final >= 7:
    print("Aluno aprovado")
else:
    print("Aluno em recuperação")
