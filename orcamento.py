''' Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu 
um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. 
O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda 
está dentro do orçamento.'''

print("\n Calculadora de orçamento mensal")
gastos = float(input("Digite o total de despesas do mês: "))

if gastos > 3000:
    passou = gastos - 3000
    print(f"Atenção, você ultrapassou o limite do orçamento em R${passou:.2f}")
else:
    print("Suas despesas estão dentro do orçamento!")