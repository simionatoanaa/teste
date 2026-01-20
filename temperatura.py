'''
Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores 
não ultrapasse 25°C. Ele quer um programa que receba a temperatura atual como entrada 
e, se necessário, exiba uma mensagem de alerta.
'''

temperatura = float(input("Insira a temperatura da sala em °C: "))

if temperatura > 25:
    print(f"Alerta! A temperatura da sala está em {temperatura}°C. VALOR ACIMA DO LIMITE PERMITIDO")
else:
    print(f"Temperatura sobre controle, atualmente em {temperatura}°C")