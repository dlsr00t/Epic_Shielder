'''tst = {1: "12345678",
 2: "87654321"}

tst2 = {1: 2412356,
    2: 2345613
}

print(tst2.keys(2412356))'''
import ast


def note():
    print("Função note()")
    with open('UserList.txt', 'r+') as login:
        try:
            dicionario = ast.literal_eval(login.read())
            tamanho = len(list(dicionario.keys()))
            proximoLog = tamanho+1
            if dicionario == '' or dicionario == None:
                login.write('{1: "123456","12345678"}')
            else:
                login.write(proximoLog)
        except:
            print("Não foi possivel realizar a conversão")
        
        
        

        
def tst():
    print("Função tst()")
    with open('UserList.txt','r+') as login:
        dicionario = login.read()
        print(type(dicionario))
        print(dicionario)

#tst()
                

note()


def get():
    print("Função get()")
    with open('UserList.txt', 'r') as login:
        dicionario = login.read()
        print(dicionario)

#get()