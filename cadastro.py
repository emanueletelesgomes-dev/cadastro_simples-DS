#variaveis para cadastro
nome = ""
idade = ""
usuario = ""
senha = ""

login_usuario = ""
login_senha = "" 

#apenas a tela de visualizacao
while True:

    print("==========")
    print("sistema cadastro")
    print("=================")

    print("1 - cadastar")
    print("2 - fazer login")
    print("3 - sair ")

    opcao = input("escolha uma opcao:")
#funcionalidades
 #se o usuario digitar o valor 1, vai ser exebido
 # a ação abaixo:
    if(opcao == "1"):
        print("======tela de cadastro=====")
        print("=================")
        nome = input("digite o seu nome: ")
        idade = input("digite sua idade: ")
        usuario = input("digite seu usuario: ")
        senha = input ("digite sua senha: ")
        print("\n cadastro realizado!\n")
     #se digitar 2, abre a tela de login
    elif(opcao == "2"):
        print("=========")
        print("===tela de login===")
        print("===========")
        login_usuario = input("digite o usuario cadastro: ")
        login_senha = input("digite a senha")
        
     #processamento de usuario e senha
       if login_usuario == usuario and login_senha == senha:
         print("\n longin realizado com sucesso!\n")
         print("bem vindo,",nome)
#se nao estiver correto entra no caso abaixo
       else:
         print("usuario ou senha incorretos")

#se digitar 3, sai da execucao
    elif(opcao == "3"):
        print("voce esta saindo do cadastro, até mais!")
        break
        # se nao for nem 1,2 ou 3, mostrar erro e repetir o codigo
    else:
        print("valor digitado, invalido,use apenas numeros inteiros do menu ")


 



