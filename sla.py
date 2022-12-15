#nome = '\\CAPSV\\Users\\Public\\01 - ASPER\\ACA\\12 - 0359-22 - RENAULT-MASTER ACA V20P\\PROCESSO ESCANEADO\\ENVIO ITL VIV'
###objetivo desse programa é controle de login, para ver qual usuario acessou qual arquivo
###e quando o usuario acessa algum arquivo o epic_shielder tem que assegurar que fique registrado
###quem acessou o arquivo e quando foi acessado

import os

class userCreator:
    def __init__(self):
        with open('UserList.txt', 'a') as usuarios:
            while True:
                nome = input("Digite o ID do usuario que você quer criar: ")
                if len(nome) < 6:
                    print("O tamanho do ID TEM que ter no minimo 6 caracteres!")
                else:
                    break
            
            while True:
                senha = input("Digite a senha para o Usuario que você: ")
                if len(senha) < 8:
                    print("O tamanho da senha TEM que ter no minimo 8 caracteres!")
                else:
                    break
            
            usuarios.write(nome)
            usuarios.write('\n')
            usuarios.write(senha)
            usuarios.write('\n')
            ###se o ID de usuario ja existir vc nao pode deixar outro usuario com o mesmo ID ser criado!

            #print(usuarios.readlines())

class userDelete:
    def __init__(self):
        with open('UserList.txt', 'w') as usuarios:
            usuarios.write('')

class viewAllUsers:
    def __init__(self):
        with open('UserList.txt', 'r') as usuarios:
            tst = usuarios.read() 
            print(type(tst))
            print(tst)
   
            if tst == "" or tst == None:
                print("Não existem usuarios!")
            else:   
                print(tst)

#class Identificacao:
#    def __init__(self):
#        usuario = input("Digite o seu ID: ")
#        senha = int(input("Digite sua senha: "))
#
#        if (usuario in usuarios.values()) and (senha in senhas.values(usuarios.keys())):
#            print("Logado")
#
#        else:
#            print("Login ou Senha INCORRETO!")

class Pasta:
    def __init__(self):
        caminho = input("Usuario digite o caminho: ")
        print(caminho)


class Exec:
    def __init__(self):
        while True:
            print("[1] Criar Usuario\n[2] Deleta TODOS os Usuarios\n[3] Ver todos os Usuarios\n[4] Abrir uma pasta")
            pergunta = input("Digite o numero da ação que vc deseja realizar: ")
            if pergunta == "1":
                acao = userCreator()
                break
            elif pergunta == "2":
                acao = userDelete()
                break
            elif pergunta == "3":
                acao = viewAllUsers()
                break
            elif pergunta == "4":
                acao = Pasta()
            else:
                print("Você não escolheu um numero de ação valido!\n\n\n")



executar = Exec()


#pessoa1 = userCreator()

#Pasta()