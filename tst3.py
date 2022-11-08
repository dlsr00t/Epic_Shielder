###codigo para transformar bytes em string

import subprocess as sp
import os

diretorio = os.scandir(str(input(r'cole o diretrio: ')))
for item in diretorio:
    if item.is_file:
        print(item.name)


'''
variavel = sp.run(['dir'], shell=True, capture_output=True)
variavel = variavel.stdout
variavel = "".join(map(chr, variavel))
print(f'\033[32m{variavel}\033[m')
'''


'''
import os
import datetime

def get_m_time():
    path = r'\\capsv\\Users\\Public\\RAFAEL\\Epic_Shielder-diretamente-do-lenovo-ideapad\\arquivo.pdf'
    #print(os.path.getmtime(path))
    tempo = os.path.getmtime(path)
    tempo_for_humans = datetime.datetime.fromtimestamp(tempo)
    print(tempo_for_humans)


if __name__ == '__main__':
    get_m_time()

'''

