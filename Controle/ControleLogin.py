from Visao import VisaoLogin
import os


dadosAluno = {}

def setDadosAluno(dados):
    global dadosAluno
    dadosAluno = dados

def getDadosAluno():
    return dadosAluno


def direcionarPagina(op):

    opcao = int(op)
    if opcao == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        VisaoLogin.primeiraEtapaLoginAluno()
    elif opcao == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        VisaoLogin.loginAdm()


def cadastrarLoginAluno(usuario,senha):
    cadastrado = False
    if os.path.isfile('login.txt'):
        try:
            arquivo = open("login.txt", "a")
            arquivo.writelines('{:11}|{:^42}\n'.format(usuario,senha))
            arquivo.close()
            cadastrado = True

        except ValueError as e:
            print("Erro ao cadastrar o login.", e)

    else:
        try:
            arquivo = open("login.txt", "a")
            tabela = '{:10} | {:^40} \n'.format("Usuario", "Senha")
            tabela += '-----------+------------------------------------------+\n'
            tabela += '{:11}|{:^42}\n'.format(usuario, senha)
            arquivo.writelines(tabela)
            arquivo.close()
            cadastrado = True

        except ValueError as e:
            print("Erro ao cadastrar o login.", e)

    if cadastrado == False:
        return False
    else:
        return True

def verificarLoginAdm(usuario,senha):
    usuarioAdm = "admin"
    senhaAdm = "admin"

    if usuario.upper() == usuarioAdm.upper():

        if senha.upper() == senhaAdm.upper():
            return True
        else:
            return print("\033[31m"+"========== Senha incorreta ============="+"\033[0;0m")

    else:
        return print("\033[31m" + "========== Usuario incorreto =============" + "\033[0;0m")


def verificarLoginAluno(usuario,senha):
    existe = False

    if os.path.isfile('login.txt'):

            arquivo = open("login.txt", "r")
            linhas = arquivo.readlines()


            for i in range(0,len(linhas)):

                registro = linhas[i].replace(" ","").replace("\n","").rsplit("|")

                for r in range(0,len(registro)):

                    if registro[r] == usuario:

                        if registro[1] == senha:
                            existe = True
                            break


            if existe == False:
                return False
            else:
                return True

def verificarMatriculaCadastrada(usuario):
        existe = False

        if os.path.isfile('login.txt'):

            arquivo = open("login.txt", "r")
            linhas = arquivo.readlines()

            for i in range(0, len(linhas)):

                registro = linhas[i].replace(" ", "").replace("\n", "").rsplit("|")

                for r in range(0, len(registro)):

                    if registro[r] == usuario:
                        existe = True
                        break

            if existe == False:
                return False
            else:
                return True

        else:
            return False




