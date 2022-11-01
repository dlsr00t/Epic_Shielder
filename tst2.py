import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import subprocess as sp

class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        
        print('Evento', event.event_type,' caminho:'+ event.src_path+ 'diretorio?', event.is_directory)
        with open("eventos.txt", "a") as eventos:
            eventos.write(f'Evento {event.event_type} caminho: {event.src_path} diretorio? {event.is_directory}')
            eventos.write('\n')

        print("fim da funcao")
        global fim
        fim = "acabou!"
        global caminho
        caminho = event.src_path
        time.sleep(1)

os.system('cls')if os.name == 'nt' else os.system('clear')

path = input("Digite o caminho \033[4;33m[pressione enter para uso do caminho padrão]\033[m: ")
if path == "" and os.name == "nt":
    path = "\\\\CAPSV\\Users\\Public\\RAFAEL\\Epic_Shielder-diretamente-do-lenovo-ideapad"
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


try:
    while True:
        #print("aguardando")
        #time.sleep(1)
        
        try:

            if fim == "acabou!":
                    
                    observer.stop()
                    #os.system("dir")
                    variavel = sp.run(['dir'], shell=False, capture_output=True)
                    variavel = variavel.stdout
                    variavel = "".join(map(chr, variavel))
                    print(variavel)
                    break
        except:
            pass

except KeyboardInterrupt:
    observer.stop()

observer.join()


