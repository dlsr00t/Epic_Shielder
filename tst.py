'''tst = {1: "12345678",
 2: "87654321"}

tst2 = {1: 2412356,
    2: 2345613
}

print(tst2.keys(2412356))'''

id = "565464"
senha = "12345678"
id2 = "795132"
senha2 = "87654321"
with open("UserList.txt", "w") as arquivo:
    arquivo.write("ID_1: "+id+"\n")
    arquivo.write("Senha_1: "+senha+"\n")
    arquivo.write("ID_2: "+id2+"\n")
    arquivo.write("Senha_2: "+senha2+"\n")

