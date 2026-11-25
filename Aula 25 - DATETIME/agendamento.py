from datetime import datetime, timedelta
import MODULOS.data as data

hoje = datetime.now()
compromiso = data.get_data('Insira a data do compromiso: ')

if hoje < compromiso:
    print(f'Faltam {compromiso - hoje} dias para seu compromiso')
elif hoje > compromiso:
    print(f'Seu comprimiso passou {compromiso - hoje} dias para seu compromiso')
    