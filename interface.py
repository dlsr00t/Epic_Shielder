from tkinter import *
from tkinter import ttk

logado = False


    
root = Tk()
root.title("Epic Shielder")
root.geometry('900x600')
log = Label(root, text="Insira seu login:")
log.pack()
caixa = Text(root, height=1, width=20)
caixa.pack()
log2 = Label(root, text="Insira sua senha:")
log2.pack()
senha = Text(root, height=1, width=20)
senha.pack()
def printInput(): 
    inp = caixa.get(1.0, "end-1c") 
    inp2 = senha.get(1.0, "end-1c")
    if inp == "clecio" and inp2 == "12345":
        lbl.config(text = "Olá "+inp)
        logado = True
        print("logado")
        root.destroy()
printButton = Button(root, text = "logar", command = printInput)
printButton.pack() 
lbl = Label(root, text = "") 
lbl.pack() 
#ttk.Label(frm, text="Insira seu login:").grid(column=0, row=0)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)


root.mainloop()


