import random
from decimal import Decimal


def defini_score():
    return random.randint(1, 999)

def gerar_credito(renda, score):

    renda = formataDecimal(renda)
    if score in range(1, 300):
        return('Crédito Reprovado')
    elif score in range(300, 600):
        return formataValor(Decimal('1000'))
    elif score in range(600, 800):
        novo_credito = renda / 2
        return formataValor(novo_credito)if novo_credito > Decimal('1000') else formataValor(Decimal('1000'))
    elif score in range(800, 951):
        return formataValor((renda * 200) / 100)
    elif range(951, 999):
        return formataValor(Decimal('1000000'))


def formataValor(valor):
    return ('{:.2f}'.format(valor))

def formataDecimal(valor):
    return Decimal(valor.replace(',', '.'))

def formataCpf(cpf, base):
    cpf = ('%011d' % int(cpf))
    if (base):
        return cpf
    else:
        return cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]