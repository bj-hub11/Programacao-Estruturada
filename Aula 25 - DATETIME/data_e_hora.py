from datetime import datetime

hoje = datetime.now()
print('data: ',hoje.strftime("%d/%m/%Y"))
print('hora: ',hoje.strftime("%H:%M:%S"))