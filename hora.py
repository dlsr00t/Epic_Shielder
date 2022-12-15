import datetime

horario = datetime.datetime.now()
horario = horario.strftime('%H:%M:%S %d/%m/%Y')

print(type(horario))
