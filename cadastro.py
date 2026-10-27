#variaveis para cadastro
nome = ""
idade = ""

usuario = ""
senha = ""

login_usuario = ""
login_senha = "" 

# variaveis de controle
controle_cadastro = ""

#apenas a tela de visualizacao
while True:
    #alterando controle_cadastro para poder cadastrar quantas vezes eu quiser
    controle_cadastro = 2
    print("==========")
    print("sistema cadastro")
    print("=================")

    print("1 - cadastar")
    print("2 - fazer login")
    print("3 - sair ")

    opcao = input("escolh\a uma opcao:")
#funcionalidades
 #se o usuario digitar o valor 1, vai ser exebido
 # a acao abaixo:
    if(opcao == "1"):
        while controle_cadastro!= "1":
            print("======tela de cadastro=====")
            print("=================")
            nome = input("digite o seu nome: ")
            idade = input("digite sua idade: ")
            usuario = input("digite seu usuario: ")
            senha = input ("digite sua senha: ")
            
            controle_cadastro = input("\n voce deseja voltar para tela anterior ?\n 1)-voltar para o menu anterior;\n") 
            
            if(controle_cadastro == "1"):
                print("\n cadastro realizado!\n")
        else:
            print("valor invalido, faca o cadastro novamente")
     #se digitar 2, abre a tela de login
    elif(opcao == "2"):
        print("=========")
        print("===tela de login===")
        print("===========")
        login_usuario = input("digite o usuario cadastro: ")
        login_senha = input("digite a senha")
        
     #processamento de usuario e senha
        if login_usuario == usuario and login_senha == senha:
            while True:
            
                print("\nlogin realizado com sucesso!\n")
                print("bem vindo, nome")
                print("\n======area do usuario======\n")
                print("1 - ver ps dados cadastrados")
                print("2- voltar para o menu anterior\n")
                print("3- alterar senha")


                usuario_opcao = input("escolha uma das opcoes  do mrno acima\n")
                if (usuario_opcao == "1"):
                    print("\n==========================")
                    print("===dados cadastrados===")
                    print("============================")
                    #mostrar dados de usuario
                    print("=== cadastro ===")
                    print(" nome do cadastro:",nome)
                    print("idade do usuario:",idade)
                    print("usuario",usuario)
                    print("senha do usuario:",senha)
                elif(usuario_opcao == "2"):
                    print("\n voce esta voltando para o menu anterior")
                    break
                elif(usuario_opcao == "3"):
                    senha = input("\nDigite a nova senha: ")

                else:
                    print("\nopao digitada invalida,use os numeros so menu!")
                #se nao estiver correto entra no caso abaixo
            else:
                    print("\nUsuario ou senha incorretos\n")
                
        #se digitar 3, sai da execucao
        else:
            print("valor")

#se digitar 3, sai da execucao
    elif(opcao == "3"):
        print("voce esta saindo do cadastro, ate mais!")
        break
        # se nao for nem 1,2 ou 3, mostrar erro e repetir o codigo
    else:
        print("valor digitado, invalido,use apenas numeros inteiros do menu ")


 



