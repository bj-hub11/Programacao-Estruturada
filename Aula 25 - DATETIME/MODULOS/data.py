from datetime import datetime, timedelta

def get_data(mensagem: str):
    print(mensagem)
    data = [int(input('Dia: ')), int(input('Mes: ')), int(input('Ano: '))]
    data = datetime(data[2], data[1], data[0])  
    return data