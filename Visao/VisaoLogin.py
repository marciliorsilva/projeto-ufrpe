from Controle import ControleLogin
from Controle import ControleAluno
from Visao import VisaoAreaAdministrador, VisaoAreaAluno
import os
import time


#função responsavel por inicializar o sistema e apresentar a tela inicial
def telaInicialSistema():
    print("="*30,"Login","="*30)
    print("-"*24,"Acesso ao sistema","-"*24)
    print("[1] Aluno | [2] Administrador")
    opcao = input("\nInforme o numero de uma opção:")
    while not(opcao in ['1','2']):  # validando a opcao informada
        print("\033[31m" + "========== Opção invalida =============" + "\033[0;0m")
        opcao = input("\033[33m" + "Informe o numero de uma opção:" + "\033[0;0m")

    else:
        #encaminhando para opção informada
        if opcao == '1':
            os.system('cls' if os.name == 'nt' else 'clear')#limpando console
            telaPrimeiraEtapaLoginAluno()#apresentando a tela
        elif opcao == '2':
            os.system('cls' if os.name == 'nt' else 'clear')#limpando console
            telaLoginAdministrador()#apresentando a tela

#função responsavel por apresentar a tela de login do administrador
def telaLoginAdministrador():
    print("="*15,"Login Administrador","="*15)
    usuario = input("Usuario:")
    senha = input("Senha:")
    #verificando o usuario e a senha
    while ControleLogin.verificarLoginAdm(usuario,senha) != True:
        usuario = input("\033[33m" + "Usuario:" + "\033[0;0m")
        senha = input("\033[33m" + "Senha:" + "\033[0;0m")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')#limpando console
        VisaoAreaAdministrador.telaInicialAdministrador()#apresentando tela inicial do administrador


#função responsavel por apresentar a tela de login do aluno
def telaLoginAluno():
    print("=" * 15, "Login Aluno", "=" *15)
    usuario = input("Usuario:")
    #verificando se a matricula informada existe, se não existi retorna false, se existir retorna
    #um dicionario com os dados do aluno
    while ControleAluno.pesquisaAluno(usuario) == False:
        print("\033[31m" + "========== Matricula informada não existe =============" + "\033[0;0m")
        usuario = input("Usuario:")

    else:
        #armazenando o dicionario com os dados do aluno
        registroAluno = ControleAluno.pesquisaAluno(usuario)
        #solicitando a senha
        senha = input("Senha:")
        #verificando se o status do aluno, se estiver ativo: permissão autorizada
        #se estiver excluido: permissão negada
        if registroAluno['status'].upper() == "ATIVO":
            #verificando o usuario e a senha do aluno
            while ControleLogin.verificarLoginAluno(usuario, senha) != True:
                print("\033[31m" + "========== Usuario ou a senha incorreto  =============" + "\033[0;0m")
                usuario = input("\033[33m" + "Usuario:" + "\033[0;0m")
                senha = input("\033[33m" + "Senha:" + "\033[0;0m")
            else:#usuario e senha OK
                #armazenando o dicionario com os dados do aluno na memoria
                ControleLogin.setDadosAluno(registroAluno)
                os.system('cls' if os.name == 'nt' else 'clear')#limpando console
                VisaoAreaAluno.telaInicialAluno()#apresentando tela inicial do administrador
        else:
            print("\033[31m" + "========== Não possivel realizar o cadastro de login. Matricula informada foi EXCLUIDA do sistema =============" + "\033[0;0m")
            time.sleep(4)#intervalo de 4 seg
            os.system('cls' if os.name == 'nt' else 'clear')#limpando console
            telaInicialSistema()# voltando para tela inicial do sistema

#função responsavel por apresentar a tela da primeira etapa do login do aluno
def telaPrimeiraEtapaLoginAluno():
    print("=" * 15, "Login Aluno", "=" * 15)
    print("-" * 10, "Esse é seu primeiro acesso ao sistema?", "-" * 10)
    print("[1] Sim  | [2] Não")
    opcao = input("\nInforme o numero de uma opção:")
    #validando opção informada
    while not(opcao in ['1','2']):
        print("\033[31m" + "========== Opção invalida =============" + "\033[0;0m")
        opcao = input("\033[33m" + "Informe o numero de uma opção:" + "\033[0;0m")
    else:
        #encaminhado para opçao informada
        if opcao == "1":
            os.system('cls' if os.name == 'nt' else 'clear')#limpando console
            segundaEtapaLoginAluno()#apresentando tela de cadastro da senha do primeiro acesso
        elif opcao == "2":
            os.system('cls' if os.name == 'nt' else 'clear')#limpando console
            telaLoginAluno()#apresentando a tela de login do aluno

#função responsavel por apresentar a tela da segunda etapa
def segundaEtapaLoginAluno():
    print("=" * 15, "Login Aluno", "=" * 15)
    print("\033[33m" + "[0] - Voltar" + "\033[0;0m")
    matricula = input("Informe sua matricula:")

    while matricula != "0":
        #verificando se a matricula informada existe, se não existi retorna false, se existir retorna
        #um dicionario com os dados do aluno
        while ControleAluno.pesquisaAluno(matricula) == False:
            print("\033[31m" + "========== Matricula informada não existe =============" + "\033[0;0m")
            matricula = input("\033[33m" + "Informe sua matricula:" + "\033[0;0m")
        else:
            # armazenando o dicionario com os dados do aluno
            registroAluno = ControleAluno.pesquisaAluno(matricula.strip())
            #verificando se a matricula ja tem algum login cadastrado
            jaCadastrou = ControleLogin.verificarMatriculaCadastrada(matricula.strip())
            if jaCadastrou == True:

                print("\033[31m" + "========== Matricula ja esta cadastrada no login do sistema =============" + "\033[0;0m")
                voltar = input("\033[33m" + "[0] - Voltar" + "\033[0;0m")
                while voltar != "0":
                    print("\033[31m" + "========== Opção invalida =============" + "\033[0;0m")
                    voltar = input("\033[33m" + "Informe o numero de uma opção:" + "\033[0;0m")
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')#limpando console
                    telaInicialSistema()#voltando para tela inicial do sistem
            else:
                # verificando se o status do aluno, se estiver ativo: permissão autorizada
                # se estiver excluido: permissão negada
                if registroAluno['status'].upper() == "ATIVO":
                    #solicitando as senhas para ser cadastradas
                    senha = input("Informe a senha de acesso:")
                    senha2 = input("Informe a senha novamente:")
                    #verificando as senhas informadas
                    while senha != senha2:
                        print("\033[31m" + "========== Senhas informadas não coincidem =============" + "\033[0;0m")
                        senha = input("\033[33m" + "Senha:" + "\033[0;0m")
                        senha2 = input("\033[33m" + "Informe a senha novamente:" + "\033[0;0m")
                    else:
                        #cadastrando a senha
                        retorno = ControleLogin.cadastrarLoginAluno(matricula, senha)
                        #verificando o retorno
                        if retorno == True:

                            print("\033[33m" + "Salvando..." + "\033[0;0m")
                            time.sleep(2)#intervalo
                            print("\033[32m" + "Seu login foi cadastrado com sucesso" + "\033[0;0m")
                            time.sleep(2)#intervalo
                            print("Voçê vai ser direcionado para pagina Principal. ")
                            time.sleep(4)#intervalo
                            os.system('cls' if os.name == 'nt' else 'clear')#limpando console
                            # armazenando o dicionario com os dados do aluno na memoria
                            ControleLogin.setDadosAluno(registroAluno)
                            VisaoAreaAluno.telaInicialAluno()  # apresentando tela inicial do administrador

                        else:
                            print("\033[31m" + "========== Erro ao cadastrar o login =============" + "\033[0;0m")
                            time.sleep(2)#intervalo
                            telaInicialSistema()#voltando para tela inicial do sistema

                else:
                    print("\033[31m" + "========== Não possivel realizar o cadastro de login. Matricula informada foi EXCLUIDA do sistema =============" + "\033[0;0m")
                    time.sleep(4)
                    os.system('cls' if os.name == 'nt' else 'clear')#limpando console
                    telaInicialSistema()  # voltando para tela inicial
    else:
        os.system('cls' if os.name == 'nt' else 'clear')#limpando console
        telaInicialSistema()  # voltando para tela inicial do sistema


