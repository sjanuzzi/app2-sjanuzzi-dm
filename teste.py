from decimal import Decimal
import locale
import re

locale.setlocale(locale.LC_ALL, 'pt_BR')
renda = '12345,60'

valor = Decimal(renda.replace(',', '.'))

a = 'aa'
b = 'bb'
print(a + b)

p = Decimal(valor)/2
x = locale.currency(Decimal(((valor * 200) / 100)), grouping=True)
print(x)
"""
print(x)
if x >= locale.currency(Decimal('10000000000000000000000000000000'), grouping=True):
    print(x /2)
else:
    print(int(x) / 3 )
print(locale.currency(Decimal(renda.replace(',', '.')), grouping=True))
print(locale.currency(Decimal('1000000'), grouping=True))


test = "22478673442"
test = ('%011d' % int(test))
print(test)
cpf = test[:3] + "." + test[3:6] + "." + test[6:9] + "-" + test[9:]
print(cpf)"""