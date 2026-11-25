from datetime import datetime, timedelta

categoria = input('Categoria do cliente:\n(NORMAL: 1\nASSINANTE: 2)\n> ')
data = input('Data da compra: (DIA/MES/ANO) ').split('/')
datacompra = datetime(int(data[2]), int(data[1]), int(data[0]))

if categoria == '1':
    prazo = datacompra + timedelta(days=10)
else:
    prazo = datacompra + timedelta(days=5)

print(f"Prazo de entrega: {prazo.strftime('%d/%m/%Y')}")

