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

        #if event.src_path != '\\\\CAPSV\\Users\\Public\\RAFAEL\\Epic_Shielder-diretamente-do-lenovo-ideapad\\eventos.txt':
        if event.event_type == "modified":
            tipo_evento = "\033[33m modified \033[m"
        elif event.event_type == "created":
            tipo_evento = "\033[32m created \033[m"
        elif event.event_type == "deleted":
            tipo_evento = "\033[31m deleted \033[m"
            
            print(f'Evento {tipo_evento} caminho: {event.src_path} diretorio? {event.is_directory}')
            with open("eventos.txt", "a+") as eventos:
                horario = datetime.datetime.now()
                horario = horario.strftime('%H:%M:%S %d/%m/%Y')

                #print(type(hora))
                eventos.write(f'Evento {event.event_type} caminho: {event.src_path} diretorio? {event.is_directory} user: {user} Hora: {horario}')
                print(horario[:22])
                eventos.write('\n')

        if not event.src_path=='\\\\CAPSV\\Users\\Public\\RAFAEL\\Epic_Shielder-diretamente-do-lenovo-ideapad\\eventos.txt' and event.event_type != 'deleted':
            
            #print(type(event.src_path))
            #event.src_path = "".join(map(chr, event.src_path))

            print(f'Evento {tipo_evento} caminho: {event.src_path} diretorio? {event.is_directory}')
            with open("eventos.txt", "a+") as eventos:
                horario = datetime.datetime.now()
                horario = horario.strftime('%H:%M:%S %d/%m/%Y')

                #print(type(hora))
                eventos.write(f'Evento {event.event_type} caminho: {event.src_path} diretorio? {event.is_directory} user: {user} Hora: {horario}')
                print(horario[:22])
                eventos.write('\n')

        
            global fim
            fim = "acabou!"
        
            time.sleep(1)
            print("\033[34mtérmino da funcao\033[m")

def get_m_time():
    #path = r'\\capsv\Users\Public\RAFAEL\Epic_Shielder-diretamente-do-lenovo-ideapad\arquivo.pdf'
    #print(os.path.getmtime(path))
    horario = datetime.datetime.now()
    horario = horario.strftime('%H:%M:%S %d/%m/%Y')

    return horario



os.system('cls')if os.name == 'nt' else os.system('clear')


path = input("Digite o caminho \033[4;33m[pressione enter para uso do caminho padrão]\033[m: ")
if path == "" and os.name == "nt":
    #path = "\\\\CAPSV\\Users\\Public\\RAFAEL\\Epic_Shielder-diretamente-do-lenovo-ideapad"
    path = "\\\\CAPSV\\Users\\Public"
else:    
    path = "/home/foureyes/.programs/python/sqlite"


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


