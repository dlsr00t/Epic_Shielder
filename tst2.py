import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import subprocess as sp
import datetime


fim = None
class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        global tipo_evento
        
        if event.src_path != '\\\\CAPSV\\Users\\Public\\RAFAEL\\Epic_Shielder-diretamente-do-lenovo-ideapad\\eventos.txt':
            if event.event_type == "modified":
                tipo_evento = "\033[33m modified \033[m"
            elif event.event_type == "created":
                tipo_evento = "\033[32m created \033[m"
            elif event.event_type == "deleted":
                tipo_evento = "\033[31m deleted \033[m"

            print(f'Evento {tipo_evento} caminho: {event.src_path} diretorio? {event.is_directory}')
            with open("eventos.txt", "a") as eventos:
                eventos.write(f'Evento {event.event_type} caminho: {event.src_path} diretorio? {event.is_directory}')
                eventos.write('\n')

            
            global fim
            fim = "acabou!"
            global caminho
            caminho = event.src_path
            time.sleep(1)
            print("\033[34mtérmino da funcao\033[m")

def get_m_time(path):
    #path = r'\\capsv\Users\Public\RAFAEL\Epic_Shielder-diretamente-do-lenovo-ideapad\arquivo.pdf'
    #print(os.path.getmtime(path))
    tempo = os.path.getmtime(path)
    tempo_for_humans = datetime.datetime.fromtimestamp(tempo)
    print(tempo_for_humans)


os.system('cls')if os.name == 'nt' else os.system('clear')


path = input("Digite o caminho \033[4;33m[pressione enter para uso do caminho padrão]\033[m: ")
if path == "" and os.name == "nt":
    path = "\\\\CAPSV\\Users\\Public\\RAFAEL\\Epic_Shielder-diretamente-do-lenovo-ideapad"
    path = "\\\\CAPSV\\Users"
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
            get_m_time(caminho)
            observer.stop()
            break

    except KeyboardInterrupt:
        observer.stop()
        print("interupcao")
        break
        
        #except:
        #    pass



observer.join()


