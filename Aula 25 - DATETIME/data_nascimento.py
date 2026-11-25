from datetime import datetime

print('INSIRA SUA DATA DE NASCIMENTO')
data = [int(input('Dia: ')), int(input('Mes: ')), int(input('Ano: '))]
nascimento = datetime(data[2], data[1], data[0])

print(f'SUA DATA DE NASCIMENTO:\n{nascimento.strftime("%d/%m/%Y")}')