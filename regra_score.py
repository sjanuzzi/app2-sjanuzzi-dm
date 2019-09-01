import random

def defini_score():
    return random.randint(1, 999)

def gerar_credito(renda, score):

    if score in range(1, 300):
        return('Crédito Reprovado')
    elif score in range(300, 600):
        return 1000
    elif score in range(600, 800):
        novo_credito = renda / 2
        return novo_credito if novo_credito > 1000 else 1000.00
    elif score in range(800, 951):
        return ((renda * 200) / 100) #TODO revisar regras
    elif (951, 999):
        return 1000000
