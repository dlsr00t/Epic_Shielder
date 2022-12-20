import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import subprocess as sp
import datetime
import openpyxl


user = "Douglas (PROGRAMADOR)"
fim = None
class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        global tipo_evento
        global caminho
        caminho = event.src_path
        tipo = ''
        if event.is_directory == True:
            tipo = 'pasta'
        else:
            tipo = 'arquivo'
        horario = datetime.datetime.now()
        horario = horario.strftime('%H:%M %d/%m/%Y')
        #if event.src_path != '\\\\CAPSV\\Users\\Public\\RAFAEL\\Epic_Shielder-diretamente-do-lenovo-ideapad\\eventos.txt':
        if event.event_type == "modified":
            tipo_evento = "\033[33m modified \033[m"
        elif event.event_type == "created":
            tipo_evento = "\033[32m created \033[m"
        elif event.event_type == "deleted":
            tipo_evento = "\033[31m deleted \033[m"
        
            print(f'Usuario: X | Caminho: {event.src_path} | Tipo: {tipo} | Evento: {tipo_evento} | Horario: {horario}')
            with open("eventos.txt", "a+") as eventos:
                horario = datetime.datetime.now()
                horario = horario.strftime('%H:%M %d/%m/%Y')

                #print(type(hora))
                eventos.write(f'Usuario: Desconhecido | Caminho: {event.src_path} | Tipo: {tipo} | Evento: {tipo_evento} | Horario: {horario}')
                print(horario[:22])
                eventos.write('\n')
            
            append('eventos.xlsx', 'Desconhecido', str(event.src_path), str(tipo), event.event_type, str(horario))
        if not event.src_path=='\\\\CAPSV\\Users\\Public\\RAFAEL\\Epic_Shielder-diretamente-do-lenovo-ideapad\\eventos.txt' and event.event_type != 'deleted' and not event.src_path=='\\\\CAPSV\\Users\\Public\\RAFAEL\\Epic_Shielder-diretamente-do-lenovo-ideapad\\eventos.xlsx' and not event.src_path=='\\\\CAPSV\\Users\\Public\\RAFAEL\\Epic_Shielder-diretamente-do-lenovo-ideapad\\teste.xlsx':
            
            #print(type(event.src_path))
            #event.src_path = "".join(map(chr, event.src_path))

            print(f'Usuario: Desconhecido | Caminho: {event.src_path} | Tipo: {tipo} | Evento: {event.event_type} | Horario: {horario}')
            with open("eventos.txt", "a+") as eventos:
                horario = datetime.datetime.now()
                horario = horario.strftime('%H:%M %d/%m/%Y')

                ##print(type(hora))
                eventos.write(f'Usuario: Desconhecido | Caminho: {event.src_path} | Tipo: {tipo} | Evento: {event.event_type} | Horario: {horario}')
                ##print(horario[:22])
                eventos.write('\n')
                
                eventos.write('\n')
            
            print(type(event.src_path), type(tipo), type(tipo_evento), type(horario))
            
            
            append('eventos.xlsx', 'Desconhecido', str(event.src_path), str(tipo), event.event_type, str(horario))
            global fim
            fim = "acabou!"
        
            time.sleep(1)
            print("\033[34mtérmino da funcao\033[m")

def get_m_time():
    ##path = r'\\capsv\Users\Public\RAFAEL\Epic_Shielder-diretamente-do-lenovo-ideapad\arquivo.pdf'
    ##print(os.path.getmtime(path))
    horario = datetime.datetime.now()
    horario = horario.strftime('%H:%M %d/%m/%Y')

    return horario

def append(nome_do_arquivo_xlsx, usuario, caminho, tipoo, evento, hora):
    try:
        workbook_obj = openpyxl.load_workbook(nome_do_arquivo_xlsx)
        sheet_obj = workbook_obj.active
        col1 = f'Usuário: {usuario}'
        col2 = f'Caminho: {caminho}'
        col3 = f'Tipo: {tipoo}'
        col4 = f'Evento: {evento}'###O parametro tipo e referencia a se é um diretorio ou nao!!!
        col5 = f'Hora: {hora}'
        sheet_obj.append([col1, col2, col3, col4,col5])
        workbook_obj.save(nome_do_arquivo_xlsx)
    except PermissionError:
        print("\033[31;1mFATAL ERROR!!!\033[m")
        print("\033[31;1mNão é possivel executar o programa se a tabela do excel estiver aberta!!!\033[m")
        exit()

os.system('cls')if os.name == 'nt' else os.system('clear')


path = input("Digite o caminho \033[4;33m[pressione enter para uso do caminho padrão]\033[m: ")
if path == "" and os.name == "nt":
    #path = "\\\\CAPSV\\Users\\Public\\RAFAEL"
    path = "\\\\CAPSV\\Users\\Public"
else:    
    path = "/home/foureyes/.programs/python/sqlite"

print(f"Monitorando {path} recursivamente!")
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

print('Rodando...')

observer = Observer()
observer.schedule(MyHandler(), path, recursive=True)
observer.start()

#observer.join()


#try:
while True:
    #print("aguardando")
    #time.sleep(1)
    '''
    observer = Observer()
    observer.schedule(MyHandler(), path, recursive=True)
    observer.start()
    '''
    try:
        #global fim
        if fim == "acabou!":
                
            #observer.stop()
            #os.system("dir")
            '''
            variavel = sp.run(['dir'], shell=True, capture_output=False)
            variavel = variavel.stdout
            variavel = "".join(map(chr, variavel))
            print(variavel)
            observer.stop()
            break
            '''
            #get_m_time(caminho)
            #observer.stop()
            pass
            #break

    except KeyboardInterrupt:
        observer.stop()
        print("interupcao por teclado")
        break
        
        #except:
        #    pass


observer.join()


