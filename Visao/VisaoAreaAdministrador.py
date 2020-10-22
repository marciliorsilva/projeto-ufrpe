from Controle import ControleAluno,ControleDisciplina,ControleMatricula,ControleRelatorio
from Visao import validacaoCadastroAluno as validar
from Visao import validacaoCadastroDisciplina as validarDisciplina

from Visao import VisaoLogin
import os
import time, datetime
#------------------------------------- Menu principal da area do Administrador ------------------------------------------
#função responsavel por apresentar a tela inical do administrador
def telaInicialAdministrador():

    print("="*50, " Bem Vindo ADMINISTRADOR ","="*50,"\n")
    print("-"*50,"Menu Principal","-"*50)
    print("[1] - Aluno | [2] - Disciplina | [3] - Matricula(Aluno/Disciplina) | [4] - Relatorio | [5] - Manutenção | [0] - Sair")
    opcao = input("\nInforme o numero de uma opção:")


    #validando a opcap escolhida
    while not(opcao in ['1','2','3','4','5','0']):
        print("\033[31m","="*15, " Opção invalida ","="*15, "\033[0;0m")
        opcao = input("\033[33m" + "Informe o numero de uma opção:" + "\033[0;0m")

    else:

        #encaminhando para a pagina escolhida
        if opcao == '1':
            os.system('cls' if os.name == 'nt' else 'clear')# limpando o console
            telaPrincipalOpcaoAluno()# apresentando a pagina escolhida
        elif opcao == '2':
            os.system('cls' if os.name == 'nt' else 'clear')# limpando o console
            telaPrincipalOpcaoDisciplina()#apresentando a pagina escolhida
        elif opcao == '3':
            os.system('cls' if os.name == 'nt' else 'clear')# limpando o console
            telaPrincipalOpcaoMatricula()#apresentando a pagina escolhida
        elif opcao == '4':
            os.system('cls' if os.name == 'nt' else 'clear')# limpando o console
            telaPrincipalOpcaoRelatorio()#apresentando a pagina escolhida
        elif opcao == '0':
            os.system('cls' if os.name == 'nt' else 'clear')# limpando o console
            VisaoLogin.telaInicialSistema()#apresentando tela

#---------------------------------------------------- Aluno --------------------------------------------------------------------
# função responsavel por apresentar a tela da opcao do aluno da area do administrador
def telaPrincipalOpcaoAluno():

    print("\033[47;1;30m" + "=" * 42, " Principal >> Aluno", "=" * 42 + '\033[0;0m')
    print("[1] - Cadastrar Aluno | [2] - Consultar Aluno | [3] - Listar alunos cadastrado | [0] - Voltar")
    opcao = input("\nInforme o numero de uma opção:")

    # validando a opcap escolhida
    while not (opcao in ['1', '2', '3','0']):
        print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
        opcao = input("\033[33m" + "Informe o numero de uma opção:" + "\033[0;0m")

    else:

        # encaminhando para a pagina escolhida
        if opcao == '1':
            os.system('cls' if os.name == 'nt' else 'clear')  # limpando o console
            telaCadastrarAluno()# apresentando a tela escolhida
        elif opcao == '2':
            os.system('cls' if os.name == 'nt' else 'clear')  # limpando o console
            telaConsultarAluno() # apresentando a tela escolhida
        elif opcao == '3':
            os.system('cls' if os.name == 'nt' else 'clear')  # limpando o console
            telaListaTodosAlunos() #apresentando a tela escolhida
        elif opcao == '0':
            os.system('cls' if os.name == 'nt' else 'clear')  # limpando o console
            telaInicialAdministrador()


# funcao responsavel por apresentar o formulario de cadastro do aluno
def telaCadastrarAluno():
    print("\033[47;1;30m"+"====================== Principal >> Aluno >> Cadastrar Aluno ========================= [0]Sair"+ "\033[0;0m")
    matricula = ControleAluno.gerarMatricula()# gerando uma matricula aleatoria
    print("Matricula: "+matricula)#informando a matricula
    nome = input("Nome:")

    if nome != "0":# se o valor informado for diferente de 0, vai para validacao
        while validar.validarNome(nome) != True:#validando o nome do aluno. se o retorno da funcao for igual a TRUE, sai do loop

            print("\033[31m" + "O nome so pode conter letras." + "\033[0;0m")
            nome = input("\033[33m"+"Nome:"+"\033[0;0m")
            if nome == "0":# se o valor informado for 0, sai do formulario e volta para o menu principal do Aluno
                os.system('cls' if os.name == 'nt' else 'clear')# apagando o console
                telaPrincipalOpcaoAluno()#apresentando tela
                break
    else:# se o valor informado for 0, sai do formulario e volta para o menu principal do Aluno
        os.system('cls' if os.name == 'nt' else 'clear')
        telaPrincipalOpcaoAluno()#apresentando tela

    sexo = input("Sexo(F - M):")
    if sexo != "0":# se o valor informado for diferente de 0, vai para validacao
        while validar.validarSexo(sexo) != True:#validando o sexo do aluno. se o retorno da funcao for igual a TRUE, sai do loop
            sexo = input("\033[33m" + "Digite o sexo valido(M - masculino ou F - feminino):" + "\033[0;0m")
            if sexo == "0":# se o valor informado for 0, sai do formulario e volta para o menu principal do Aluno
                os.system('cls' if os.name == 'nt' else 'clear')# apagando o console
                telaPrincipalOpcaoAluno()  # apresentando tela
                break
    else:# se o valor informado for 0, sai do formulario e volta para o menu principal do Aluno
        os.system('cls' if os.name == 'nt' else 'clear')#limpando console
        telaPrincipalOpcaoAluno()#apresentando tela


    dataNascimento = input("Data de Nascimento(ano/mes/dia):")
    if dataNascimento != "0":# se o valor informado for diferente de 0, vai para validacao
        while validar.validarData(dataNascimento) != True:#validando a data de nascimento do aluno. se o retorno da funcao for igual a TRUE, sai do loop
            dataNascimento = input("\033[33m" + "Digite uma data válida (Ex. 1985/12/25):" + "\033[0;0m")
            if dataNascimento == "0": #se o valor informado for 0, sai do formulario e volta para o menu principal do Aluno
                os.system('cls' if os.name == 'nt' else 'clear')#limpado o console
                telaPrincipalOpcaoAluno()  # apresentando tela
                break
    else:# se o valor informado for 0, sai do formulario e volta para o menu principal do Aluno
        os.system('cls' if os.name == 'nt' else 'clear')#limpando o console
        telaPrincipalOpcaoAluno()#apresentando tela


    telefone = input("Telefone(ddd+telefone):")
    if telefone != "0":# se o valor informado for diferente de 0, vai para validacao
        while validar.validarTelefone(telefone) != True:#validando o telefone do aluno. se o retorno da funcao for igual a TRUE, sai do loop

            telefone = input("\033[33m" + "Informe um telefone válido!(ddd+telefone):" + "\033[0;0m")
            if telefone == "0":# se o valor informado for 0, sai do formulario e volta para o menu principal do Aluno
                os.system('cls' if os.name == 'nt' else 'clear')# apagando o console
                telaPrincipalOpcaoAluno()  # apresentando tela
                break
    else:# se o valor informado for 0, sai do formulario e volta para o menu principal do Aluno
        os.system('cls' if os.name == 'nt' else 'clear')# apagando o console
        telaPrincipalOpcaoAluno()#apresentando tela

    # como é o primeiro cadastro do aluno, por padrao quantidade de disciplina va ser 0 e o status vai ser ativo
    qtdeDisciplina = 0 #atribuindo a quantidade de disciplina vinculadas do aluno

    status = "Ativo" #atribuindo o status do aluno no sistema
    print("Qtde. Disciplina: 0")#exibindo quantidade de disciplina aluno
    print("Status: Ativo")# exibindo o status do aluno

    # confirma cadastro
    print("\033[33m" + "====== Salvar informações? ========" + "\033[0;0m")
    print("\033[33m" + "[1] Salvar | [2] Cancelar" + "\033[0;0m")
    opcao = input("\033[33m" + "Escolha uma opcao. Digite 1 ou 2:" + "\033[0;0m")

    while not(opcao in ['1','2']):# validando confirmação do cadastro
        print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
        print("\033[33m"+"====== Salvar informações? ========"+"\033[0;0m")
        print("\033[33m"+"[1] Salvar | [2] Cancelar"+"\033[0;0m")
        opcao = input("\033[33m"+"Escolha uma opcao. Digite 1 ou 2:"+"\033[0;0m")

    else:
        if opcao == '1':
            retorno = ControleAluno.cadastrarAluno(matricula, nome.upper(), sexo.upper(), dataNascimento, telefone, qtdeDisciplina, status.upper())
            #verificando o retorno
            if retorno == True:
                print("\033[33m" + "Salvando..." + "\033[0;0m")
                time.sleep(2)#intervalo
                print("\033[32m" + "Aluno Cadastrado com sucesso" + "\033[0;0m")
                time.sleep(2)#intervalo
                os.system('cls' if os.name == 'nt' else 'clear')#limpando console
                telaPrincipalOpcaoAluno()#apresentando tela
            else:
                #erro
                print("\033[31m" + "Erro ao cadastrar o aluno." + "\033[0;0m")
                print("[0] Voltar")
                voltar = input("Informe a opção:")
                while voltar != '0':
                    print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
                    voltar = input("Informe a opção:")
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    telaPrincipalOpcaoAluno()  # apresentando tela


        else:
            os.system('cls' if os.name == 'nt' else 'clear')  #limpando console
            telaPrincipalOpcaoAluno()  #apresentando tela


def telaAlterarDadosAluno(registroAluno):
    #formando cabecalho
    tabela = '{:10} | {:^40} | {:^1} | {:^10} | {:^10} | {:^2} | {:^10}\n'.format("Matricula", "Nome", "Sexo",
                                                                                  "Data de Nascimento", "Telefone",
                                                                                  "Quantidade de Disciplina",
                                                                                  "Status")
    tabela += '-----------+------------------------------------------+------+--------------------+------------+--------------------------+----------\n'
    #formando os registro
    tabela += '{:11}|{:^42}|{:^6}|{:^20}|{:^12}|{:^26}|{:>10}\n'.format(*registroAluno.values())

    print("\033[47;1;30m", "=" * 32, "Principal >> Aluno >> Consultar Aluno >> Alterar dados", "=" * 32, "\033[1;31m [5] Finalizar\n",
          "\033[0;0m")

    #imprimindo tabela
    print(tabela+"\n")
    atributo = input("Informe o numero do dado a ser alterado: [1] Nome  | [2] Sexo | [3] Data de Nascimento | [4] Telefone :")
    print("Outras opções: [0] Cancelar | [5] Finalizar")
    #verificando opção informada
    while not(atributo in ['1','2','3','4','5','0']):
        print("\033[31m" + "Opção invalida." + "\033[0;0m")
        atributo = input("\033[33m" + "Informe o numero do dado a ser alterado: [1] Nome  | [2] Sexo | [3] Data de Nascimento | [4] Telefone  :" + "\033[0;0m")
        print("Outras opções: [0] Cancelar | [5] Finalizar")
    else:

            #atributo nome escolhido
            if atributo == "1":

                nome = input("Nome:")
                if nome != "0":
                    #validando nome
                    while validar.validarNome(nome) != True:

                        print("\033[31m" + "O nome so pode conter letras." + "\033[0;0m")
                        nome = input("\033[33m" + "Nome:" + "\033[0;0m")
                        if nome == "0":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            telaPrincipalOpcaoAluno()  # apresentando tela
                            break
                    else:
                        #atualizando dicionario com os dados do aluno
                        registroAluno["nome"] = nome.upper()
                        #atualizando no arquivo
                        retorno = ControleAluno.atualizarDadosAluno(registroAluno)
                        if retorno == True:

                            print("\033[32m" + "Nome alterado com sucesso." + "\033[0;0m")
                            time.sleep(2)#intervalo
                            os.system('cls' if os.name == 'nt' else 'clear')#limpando console
                            #repassando o dicionario atualizado para a mesma tela
                            telaAlterarDadosAluno(registroAluno)
                        else:

                            print("\033[31m" + "Erro alterar os dados do alunos." + "\033[0;0m")
                            print("[0] Voltar")
                            voltar = input("Informe a opção:")
                            while voltar != '0':
                                print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
                                voltar = input("Informe a opção:")
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                telaPrincipalOpcaoAluno()  # apresentando tela

                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    telaPrincipalOpcaoAluno()  # apresentando tela

            #atributo sexo escolhido
            elif atributo == "2":

                sexo = input("Sexo(F - M):")
                if sexo != "0":
                    while validar.validarSexo(sexo) != True:
                        sexo = input(
                            "\033[33m" + "Digite o sexo valido(M - masculino ou F - feminino):" + "\033[0;0m")
                        if sexo == "0":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            telaPrincipalOpcaoAluno()  # apresentando tela
                            break
                    else:
                        #atualizando dicionario com os dados do aluno
                        registroAluno["sexo"] = sexo.upper()
                        #atualizando no arquivo
                        retorno = ControleAluno.atualizarDadosAluno(registroAluno)
                        if retorno == True:
                            print("\033[32m" + "Sexo alterado com sucesso." + "\033[0;0m")
                            time.sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            telaAlterarDadosAluno(registroAluno)
                        else:
                            print("\033[31m" + "Erro alterar os dados do alunos." + "\033[0;0m")
                            print("[0] Voltar")
                            voltar = input("Informe a opção:")
                            while voltar != '0':
                                print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
                                voltar = input("Informe a opção:")
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                telaPrincipalOpcaoAluno()  # apresentando tela

                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    telaPrincipalOpcaoAluno()  # apresentando tela

            #atributo data de nascimento escolhido
            elif atributo == "3":

                dataNascimento = input("Data de Nascimento(ano/mes/dia):")

                if dataNascimento != "0":
                    while validar.validarData(dataNascimento) != True:
                        dataNascimento = input(
                            "\033[33m" + "Digite uma data válida (Ex. 1985/12/25):" + "\033[0;0m")
                        if dataNascimento == "0":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            telaPrincipalOpcaoAluno()  # apresentando tela
                            break
                    else:
                        #atualizando dicionario com os dados do aluno
                        registroAluno["data"] = dataNascimento
                        #atualizando no arquivo
                        retorno = ControleAluno.atualizarDadosAluno(registroAluno)
                        if retorno == True:
                            print("\033[32m" + "Data de Nascimento alterada com sucesso." + "\033[0;0m")
                            time.sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            telaAlterarDadosAluno(registroAluno)
                        else:
                            print("\033[31m" + "Erro alterar os dados do alunos." + "\033[0;0m")
                            print("[0] Voltar")
                            voltar = input("Informe a opção:")
                            while voltar != '0':
                                print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
                                voltar = input("Informe a opção:")
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                telaPrincipalOpcaoAluno()  # apresentando tela

                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    telaPrincipalOpcaoAluno()  # apresentando tela

            #atributo telefone escolhido
            elif atributo == "4":

                telefone = input("Telefone(ddd+telefone):")
                if telefone != "0":
                    while validar.validarTelefone(telefone) != True:
                        telefone = input("\033[33m" + "Informe um telefone válido!(ddd+telefone):" + "\033[0;0m")
                        if telefone == "0":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            telaPrincipalOpcaoAluno()  # apresentando tela
                            break
                    else:
                        #atualizando dicionario com os dados do aluno
                        registroAluno["telefone"] = telefone
                        #atualizando no arquivo
                        retorno = ControleAluno.atualizarDadosAluno(registroAluno)
                        if retorno == True:
                            print("\033[32m" + "Telefone alterado com sucesso." + "\033[0;0m")
                            time.sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            telaAlterarDadosAluno(registroAluno)
                        else:
                            print("\033[31m" + "Erro alterar os dados do alunos." + "\033[0;0m")
                            print("[0] Voltar")
                            voltar = input("Informe a opção:")
                            while voltar != '0':
                                print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
                                voltar = input("Informe a opção:")
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                telaPrincipalOpcaoAluno()  # apresentando tela

                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    telaPrincipalOpcaoAluno()  # apresentando tela


            elif atributo == "0" or atributo == "5":
                os.system('cls' if os.name == 'nt' else 'clear')
                telaPrincipalOpcaoAluno()  # apresentando tela



def telaConsultarAluno():

    print("\033[47;1;30m", "="*45, "Principal >> Aluno >> Consultar Aluno","="*40 , "\033[1;31m [0] Voltar" ,"\033[0;0m\n")
    matricula = input("Informe o numero da matricula do aluno:")
    if matricula != "0":

        dadosAlunos = ControleAluno.pesquisaAluno(matricula)
        while dadosAlunos == False:

            print("\033[31m" + "Aluno não encontrado." + "\033[0;0m")
            matricula = input("\033[33m" + "Informe o numero da matricula do aluno:" + "\033[0;0m")

            if matricula == "0":
                os.system('cls' if os.name == 'nt' else 'clear')
                telaPrincipalOpcaoAluno()  # apresentando a pagina escolhida
                break

            dadosAlunos = ControleAluno.pesquisaAluno(matricula)

        else:
            while True:

                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[47;1;30m", "=" * 45, "Principal >> Aluno >> Consultar Aluno", "=" * 40,
                      "\033[1;31m [0] Voltar", "\033[0;0m\n")

                tabela = '{:10} | {:^40} | {:^1} | {:^10} | {:^10} | {:^2} | {:^10}\n'.format("Matricula", "Nome", "Sexo",
                                                                                          "Data de Nascimento", "Telefone",
                                                                                          "Quantidade de Disciplina",
                                                                                          "Status")
                tabela += '-----------+------------------------------------------+------+--------------------+------------+--------------------------+----------\n'
                tabela += '{:11}|{:^42}|{:^6}|{:^20}|{:^12}|{:^26}|{:>10}\n'.format(*dadosAlunos.values())
                print(tabela)
                print("="*87, "\033[1;36m [1] Alterar dados | [2] Remover | [0] Voltar")
                opcao = input("\nInforme o numero de uma opção:")
                while not(opcao in ['1','2','0']):

                    print("\033[31m" + "Opção invalida." + "\033[0;0m")
                    opcao = input("\033[33m" + "Informe o numero de uma opção:" + "\033[0;0m")
                    
                else:

                    if opcao != "0":

                        if opcao == "1":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            telaAlterarDadosAluno(dadosAlunos)
                            break

                        elif opcao == "2":

                            if dadosAlunos['status'] == "ATIVO":

                                if dadosAlunos['disciplinas'] == "0":

                                    print("\033[33m", "=" * 10, " Tem certeza que deseja excluir esse Aluno?", "=" * 10,
                                      "\033[0;0m")
                                    print("\033[33m" + "[1] Sim | [2] Não" + "\033[0;0m")
                                    excluirOpcao = input("\033[33m" + "Escolha uma opcao. Digite 1 ou 2:" + "\033[0;0m")
                                    while not(excluirOpcao in ['1','2']):
                                        print("\033[31m" + "Opção invalida." + "\033[0;0m")
                                        excluirOpcao = input("\033[33m" + "Escolha uma opcao. Digite 1 ou 2:" + "\033[0;0m")
                                    else:
                                        if excluirOpcao == "1":
                                            dadosAlunos['status'] = "EXCLUIDO"
                                            retorno = ControleAluno.removerAluno(dadosAlunos)

                                            if retorno == True:
                                                print("\033[32m" + "Aluno Removido com sucesso." + "\033[0;0m")
                                                time.sleep(2)
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                continue
                                            else:
                                                print("\033[31m" + "Erro ao remover o aluno." + "\033[0;0m")
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                continue


                                        elif excluirOpcao == "2":

                                            os.system('cls' if os.name == 'nt' else 'clear')

                                            continue
                                else:
                                   
                                    print( "\033[33m Não é possivel excluir. Pois aluno esta vinculado com algumas disciplinas \033[0;0m")
                                    continue
                            else:
                                print("\033[33m Esse aluno ja foi excluido \033[0;0m")
                                continue


                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        telaPrincipalOpcaoAluno()  # apresentando a pagina escolhida
                        break

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        telaPrincipalOpcaoAluno()  # apresentando a pagina escolhida




def telaListaTodosAlunos():
    arquivo = open("alunos.txt","r")
    linhas = arquivo.readlines()
    print("\033[47;1;30m"+"="*42," Principal >> Aluno >> Listar alunos cadastrado" ,"="*42+'\033[0;0m')
    for i in range(0,len(linhas),1):
        print(linhas[i],end="")

    print("="*134)
    print("[0] Voltar")
    opcao = input("Escolha uma opcao:")
    while opcao != "0":
        print("\033[31m" + "========== Opção invalida =============" + "\033[0;0m")
        opcao = input("\033[33m" + "Escolha uma opção:" + "\033[0;0m")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        telaPrincipalOpcaoAluno()  # apresentando a pagina escolhida

# ------------------------------------------ Disciplina ------------------------------------

def telaPrincipalOpcaoDisciplina():
    print("============================= Principal >> Disciplina =================================\n \n")
    print("[1] - Cadastrar disciplina | [2] - Consultar disciplina | [3] - Listar disciplina cadastradas | [0] - Voltar")

    opcao = input("\nInforme o numero de uma opção:")
   
    # validando a opcap escolhida
    while not (opcao in ['1', '2', '3', '0']):
        print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
        opcao = input("\033[33m" + "Informe o numero de uma opção:" + "\033[0;0m")
            
    else:
        # encaminhando para a pagina escolhida
        if opcao == '1':
            os.system('cls' if os.name == 'nt' else 'clear')  # limpando o console
            telaCadastrarDisciplina()  # apresentando a pagina escolhida
        elif opcao == '2':
            os.system('cls' if os.name == 'nt' else 'clear')  # limpando o console
            telaConsultarDisciplina() # apresentando a pagina escolhida
        elif opcao == '3':
            os.system('cls' if os.name == 'nt' else 'clear')  # limpando o console
            telaListaTodasDisciplinas()  # apresentando a pagina escolhida
        elif opcao == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            telaInicialAdministrador()
                



# funcao responsavel por apresentar o formulario de cadastro da Disciplina
def telaCadastrarDisciplina():
    print("\033[47;1;30m"+"====================== Principal >> Disciplina >> Cadastrar Disciplna ========================= [0]Sair"+ "\033[0;0m")

    codigo = ControleDisciplina.gerarCodigo()# gerando codigo aleatorio
    print("Codigo: "+codigo)#informando o codigo
    nome = input("Nome da disciplina:")
    if nome == "0":# se o valor informado for 0, sai do formulario e volta para o menu principal do Aluno
        os.system('cls' if os.name == 'nt' else 'clear')
        telaPrincipalOpcaoDisciplina()

    horario = input("Horario:")
    if horario != "0":# se o valor informado for diferente de 0, vai para validacao

        while validarDisciplina.validarHorario(horario) != True:#validando o harario. se o retorno da funcao for igual a TRUE, sai do loop
            horario = input("\033[33m" + "Horario:" + "\033[0;0m")
            if horario == "0":# se o valor informado for 0, sai do formulario e volta para o menu principal da Disciplina
                os.system('cls' if os.name == 'nt' else 'clear')# apagando o console
                telaPrincipalOpcaoDisciplina()
                break
    else:# se o valor informado for 0, sai do formulario e volta para o menu principal da Disiciplna
        os.system('cls' if os.name == 'nt' else 'clear')
        telaPrincipalOpcaoDisciplina()


    sala = input("Sala:")
    if sala == "0":# se o valor informado for 0, sai do formulario e volta para o menu principal da Disciplina
        os.system('cls' if os.name == 'nt' else 'clear')
        telaPrincipalOpcaoDisciplina()


    quantidadeVagas = input("Quantidade total de vagas:")
    if quantidadeVagas != "0":# se o valor informado for diferente de 0, vai para validacao
        while quantidadeVagas.isnumeric() != True:#validando a quantidade de vagas. se o retorno da funcao for igual a TRUE, sai do loop

            quantidadeVagas = input("\033[33m" + "Quantidade total de vagas:" + "\033[0;0m")
            if quantidadeVagas == "0":# se o valor informado for 0, sai do formulario e volta para o menu principal do Aluno
                os.system('cls' if os.name == 'nt' else 'clear')# apagando o console
                telaPrincipalOpcaoDisciplina()
                break
    else:# se o valor informado for 0, sai do formulario e volta para o menu principal do Aluno
        os.system('cls' if os.name == 'nt' else 'clear')# apagando o console
        telaPrincipalOpcaoDisciplina()

    #como é o primeiro cadastro do aluno, por padrao quantida de disciplina va ser 0 e o status vai ser ativo#

    vagasOcupadas = 0   #atribuindo a quantidade de disciplina vinculadas do aluno

    status = "Ativo" #atribuindo o status do aluno no sistema
    print("Vagas ocupadas: 0")#exibindo quantidade de disciplina aluno
    print("Status: Ativo")# exibindo o status do aluno

    # confirma cadastro
    print("\033[33m" + "====== Salvar informações? ========" + "\033[0;0m")
    print("\033[33m" + "[1] Salvar | [2] Cancelar" + "\033[0;0m")
    opcao = input("\033[33m" + "Escolha uma opcao. Digite 1 ou 2:" + "\033[0;0m")

    while not(opcao in ['1','2']):# validando confirmação do cadastro, caso o retorno da funcao for TRUE, sai do loop

        print("\033[33m"+"====== Salvar informações? ========"+"\033[0;0m")
        print("\033[33m"+"[1] Salvar | [2] Cancelar"+"\033[0;0m")
        opcao = input("\033[33m"+"Escolha uma opcao. Digite 1 ou 2:"+"\033[0;0m")

    else:
        if opcao == '1':
            retorno = ControleDisciplina.cadastrarDisciplina(codigo,nome.upper(),horario,sala.upper(),quantidadeVagas,vagasOcupadas,status.upper())
            if retorno == True:
                print("\033[33m" + "Salvando..." + "\033[0;0m")
                time.sleep(2)
                print("\033[32m" + "Disciplina Cadastrada com sucesso" + "\033[0;0m")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')  # apagando o console
                telaPrincipalOpcaoDisciplina()
            else:
                # erro
                print("\033[31m" + "Erro ao cadastrar a disciplina." + "\033[0;0m")
                print("[0] Voltar")
                voltar = input("Informe a opção:")
                while voltar != '0':
                    print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
                    voltar = input("Informe a opção:")
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    telaPrincipalOpcaoDisciplina()
                
                
        else:
            os.system('cls' if os.name == 'nt' else 'clear')  # apagando o console
            telaPrincipalOpcaoDisciplina()




def telaAlterarDadosDisciplina(registroDisciplina):
    tabela = '{:10} | {:^40} | {:^1} | {:^10} | {:^10} | {:^2} | {:^10}\n'.format("Codigo", "Nome", "Horario",
                                                                                  "Sala", "Quantidade de Vagas",
                                                                                  "Vagas ocupadas", "Status")
    tabela += '-----------+------------------------------------------+---------+------------+---------------------+----------------+----------\n'

    tabela += '{:11}|{:^42}|{:^9}|{:^12}|{:^21}|{:^16}|{:>10}\n'.format(*registroDisciplina.values())

    print("\033[47;1;30m", "=" * 25, "Principal >> Disciplina >> Consultar Disciplina >> Alterar dados", "=" * 25, "\033[1;31m [0] Finalizar\n",
          "\033[0;0m")

    print(tabela+"\n")
    atributo = input("Informe o numero do dado a ser alterado: [1] Nome  | [2] Horario | [3] Sala | [4] Quantidade de vagas:")
    print("Outras opções: [0] Cancelar | [5] Finalizar")
    while not(atributo in ['1','2','3','4','5','0']):
        print("\033[31m" + "Opção invalida." + "\033[0;0m")
        atributo = input("\033[33m" + "Informe o numero do dado a ser alterado: [1] Nome  | [2] Horario | [3] Sala | [4] Quantidade de vagas:" + "\033[0;0m")
 
    else:

            if atributo == "1":

                nome = input("Nome:")
                if nome != "0":


                    registroDisciplina["nome"] = nome.upper()
                    retorno = ControleDisciplina.atualizarDadosDisciplina(registroDisciplina)
                    if retorno == True:

                      print("\033[32m" + "Nome da disciplina alterado com sucesso." + "\033[0;0m")
                      time.sleep(2)
                      os.system('cls' if os.name == 'nt' else 'clear')
                      telaAlterarDadosDisciplina(registroDisciplina)
                    else:
                      print("\033[31m" + "Erro alterar os dados da Disciplina." + "\033[0;0m")
                      print("[0] Voltar")
                      voltar = input("Informe a opção:")
                      while voltar != '0':
                          print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
                          voltar = input("Informe a opção:")
                      else:
                          os.system('cls' if os.name == 'nt' else 'clear')
                          telaPrincipalOpcaoDisciplina()# apresentando tela




                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    telaPrincipalOpcaoDisciplina()


            elif atributo == "2":

                horario = input("Horario(hh:mm):")
                if horario != "0":
                    while validarDisciplina.validarHorario(horario) != True:
                        horario = input(
                            "\033[33m" + "Horario(hh:mm):" + "\033[0;0m")
                        if horario == "0":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            telaPrincipalOpcaoDisciplina()
                            break
                    else:
                        registroDisciplina["horario"] = horario

                        retorno = ControleDisciplina.atualizarDadosDisciplina(registroDisciplina)
                        if retorno == True:
                            print("\033[32m" + "Horario alterado com sucesso." + "\033[0;0m")
                            time.sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            telaAlterarDadosDisciplina(registroDisciplina)
                        else:
                            print("\033[31m" + "Erro alterar os dados da disciplina." + "\033[0;0m")
                            print("[0] Voltar")
                            voltar = input("Informe a opção:")
                            while voltar != '0':
                                print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
                                voltar = input("Informe a opção:")
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                telaPrincipalOpcaoDisciplina()  # apresentando tela

                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    telaPrincipalOpcaoDisciplina()

            elif atributo == "3":

                sala = input("Sala:")

                if sala != "0":

                        registroDisciplina["sala"] = sala.upper()
                        retorno = ControleDisciplina.atualizarDadosDisciplina(registroDisciplina)
                        if retorno == True:
                            print("\033[32m" + "Sala alterada com sucesso." + "\033[0;0m")
                            time.sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            telaAlterarDadosDisciplina(registroDisciplina)
                        else:
                            print("\033[31m" + "Erro alterar os dados da disciplina" + "\033[0;0m")
                            print("[0] Voltar")
                            voltar = input("Informe a opção:")
                            while voltar != '0':
                                print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
                                voltar = input("Informe a opção:")
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                telaPrincipalOpcaoDisciplina()  # apresentando tela

                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    telaPrincipalOpcaoDisciplina()

            elif atributo == "4":

                quantidadeVagas = input("Quantidade de vagas:")
                if quantidadeVagas != "0":
                    while quantidadeVagas.isnumeric() != True:
                        quantidadeVagas = input("\033[33m" + "Quantidade de vagas:" + "\033[0;0m")
                        if quantidadeVagas == "0":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            telaPrincipalOpcaoDisciplina()
                            break
                    else:
                        registroDisciplina["quantidadeVagas"] = quantidadeVagas
                        retorno = ControleDisciplina.atualizarDadosDisciplina(registroDisciplina)
                        if retorno == True:
                            print("\033[32m" + "Quantidade de vagas alterada com sucesso." + "\033[0;0m")
                            time.sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            telaAlterarDadosDisciplina(registroDisciplina)
                        else:
                            print("\033[31m" + "Erro alterar os dados da disciplina." + "\033[0;0m")
                            print("[0] Voltar")
                            voltar = input("Informe a opção:")
                            while voltar != '0':
                                print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
                                voltar = input("Informe a opção:")
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                telaPrincipalOpcaoDisciplina()  # apresentando tela

                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    telaPrincipalOpcaoDisciplina()

            elif atributo == "0" or atributo == "5":
                os.system('cls' if os.name == 'nt' else 'clear')
                telaPrincipalOpcaoDisciplina()

def telaConsultarDisciplina():

    print("\033[47;1;30m", "="*45, "Principal >> Disciplina >> Consultar disciplina","="*40 , "\033[1;31m [0] Voltar" ,"\033[0;0m\n")
    codigo = input("Informe o codigo da disciplina:")
    if codigo != "0":

        while ControleDisciplina.pesquisaDisciplina(codigo) == False:

            print("\033[31m" + "Disciplina não encontrada." + "\033[0;0m")
            codigo = input("\033[33m" + "Informe o codigo da disciplina:" + "\033[0;0m")
            if codigo == "0":
                os.system('cls' if os.name == 'nt' else 'clear')
                telaPrincipalOpcaoDisciplina()
                break

        else:
            
            dadosDisciplina = ControleDisciplina.pesquisaDisciplina(codigo)
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[47;1;30m", "=" * 45, "Principal >> Disciplina >> Consultar disciplina", "=" * 40,
                      "\033[1;31m [0] Voltar", "\033[0;0m\n")
                tabela = '{:10} | {:^40} | {:^1} | {:^10} | {:^10} | {:^2} | {:^10}\n'.format("Codigo", "Nome", "Horario",
                                                                                 "Sala", "Quantidade de Vagas",
                                                                                 "Vagas ocupadas", "Status")
                tabela += '-----------+------------------------------------------+---------+------------+---------------------+----------------+----------\n'
                tabela += '{:11}|{:^42}|{:^9}|{:^12}|{:^21}|{:^16}|{:>10}\n'.format(*dadosDisciplina.values())
                print(tabela)
                print("="*87, "\033[1;36m [1] Alterar dados | [2] Remover | [0] Voltar")
                opcao = input("\nInforme o numero de uma opção:")
                while not(opcao in ['1','2','0']):

                    print("\033[31m" + "Opção invalida." + "\033[0;0m")
                    opcao = input("\033[33m" + "Informe o numero de uma opção:" + "\033[0;0m")
                    
                else:

                    if opcao != "0":

                        if opcao == "1":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            telaAlterarDadosDisciplina(dadosDisciplina)
                        elif opcao == "2":

                            if dadosDisciplina['status'] == "ATIVO":

                                if dadosDisciplina['vagasOcupadas'] == "0":

                                    print("\033[33m", "=" * 10, " Tem certeza que deseja excluir esse Aluno?", "=" * 10,
                                      "\033[0;0m")
                                    print("\033[33m" + "[1] Sim | [2] Não" + "\033[0;0m")
                                    excluirOpcao = input("\033[33m" + "Escolha uma opcao. Digite 1 ou 2:" + "\033[0;0m")
                                    while not(excluirOpcao in ['1','2']):
                                        print("\033[31m" + "Opção invalida." + "\033[0;0m")
                                        excluirOpcao = input("\033[33m" + "Escolha uma opcao. Digite 1 ou 2:" + "\033[0;0m")
                                    else:
                                        if excluirOpcao == "1":
                                            dadosDisciplina['status'] = "Excluído".upper()
                                            retorno = ControleDisciplina.removerDisciplina(dadosDisciplina)

                                            if retorno == True:
                                                print("\033[32m" + "Disciplina Removida com sucesso." + "\033[0;0m")

                                                time.sleep(2)
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                continue
                                            else:
                                                print("\033[31m" + "Erro ao remover o aluno." + "\033[0;0m")
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                continue


                                        elif excluirOpcao == "2":
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            continue
                                
                                else:
                                    print( "\033[33m Não é possivel excluir. Pois a disciplina contem alunos cadastrados \033[0;0m")
                                    continue
                            else:
                                print("\033[33m Esse aluno ja foi excluido \033[0;0m")
                                continue

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        telaPrincipalOpcaoDisciplina()
                        break

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        telaPrincipalOpcaoDisciplina()



def telaListaTodasDisciplinas():
    arquivo = open("disciplinas.txt","r")
    linhas = arquivo.readlines()
    print("\033[47;1;30m"+"="*35," Principal >> Disciplinas >> Listar disciplinas cadastradas" ,"="*35+'\033[0;0m\n')
    for i in range(0,len(linhas),1):
        print(linhas[i],end="")

    print("="*134)
    print("[0] Voltar")
    opcao = input("Escolha uma opcao:")
    while opcao != "0":
        print("\033[31m" + "========== Opção invalida =============" + "\033[0;0m")
        opcao = input("\033[33m" + "Escolha uma opção:" + "\033[0;0m")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        telaPrincipalOpcaoDisciplina()
#------------------------------------------------ Matricula ----------------------------------------


def telaPrincipalOpcaoMatricula():
    print("\033[47;1;30m" + "=" * 30, " Principal >> Matricula(Aluno/Disciplna)", "=" * 30 + '\033[0;0m\n')
    print("[1] - Trancamento de matricula | [2] - Exclusão de matricula | [0] - Voltar")

    opcao = input("\nInforme o numero de uma opção:")

    # se opcao for 0 volta para menu principal
    if opcao == "0":
        os.system('cls' if os.name == 'nt' else 'clear')
        telaInicialAdministrador()
        
    else:
        
        while not (opcao in ['1', '2', '0']):  # validando a opcao informada

            print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
            opcao = input("\033[33m" + "Informe o numero de uma opção:" + "\033[0;0m")
           

        else:  # se o retorno da funcao for TRUE, sai do loop e encaminhara para a opcao do menu escolhido

            if opcao == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                telaTrancarMatricula()
            elif opcao == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                telaExcluirMatricula()
            elif opcao == "0":
                os.system('cls' if os.name == 'nt' else 'clear')
                telaInicialAdministrador()


def telaTrancarMatricula():
    print("\033[47;1;30m" + "=" * 30, " Principal >> Matricula(Aluno/Disciplina) >> Tracamento", "=" * 30 + '\033[0;0m\n')
    print("[0] - Voltar\n")
    matriculaAluno = input("Informe a matricula do aluno:")

    if matriculaAluno == "0":
        os.system('cls' if os.name == 'nt' else 'clear')
        telaPrincipalOpcaoMatricula()
    else:
        while ControleAluno.pesquisaAluno(matriculaAluno) == False:
            print("\033[31m", "=" * 15, " Matricula não encontrada ", "=" * 15, "\033[0;0m")
            matriculaAluno = input("\033[33m" + "Informe a matricula do aluno:" + "\033[0;0m")

            if matriculaAluno == "0":
                telaPrincipalOpcaoMatricula()
                break
        else:


            listaMatriculasAluno = ControleMatricula.listarMatriculasAlunoAdm(matriculaAluno)
            dadosAluno = ControleAluno.pesquisaAluno(matriculaAluno)
            print("\n\033[32mInformações do Aluno","="*115, "\033[0;0m")
            print("\nNome do Aluno: "+ dadosAluno['nome'], "\t"*4,"Sexo: "+dadosAluno['sexo'],"\t"*4,"Data nascimento: "+dadosAluno['data'])
            print("\nTelefone: " + dadosAluno['telefone'], "\t" *5, "Status: " + dadosAluno['status'])

            print("\n\033[32mDisciplinas que o aluno esta matriculado","="*95, "\033[0;0m")
            print('{:^10} | {:^40} | {:^1} | {:^10} | {:^10} | {:^10}'.format("Codigo da disciplina", "Nome da disciplina", "Horario","Sala", "Data que o aluno se matriculou","Status"))
            print('---------------------+------------------------------------------+---------+------------+---------------------------------+------------')
            dataMatricula = ""

            for i in range(0,len(listaMatriculasAluno)):
                dataMatricula = listaMatriculasAluno[i]['data']
                disciplina = ControleDisciplina.pesquisaDisciplina(listaMatriculasAluno[i]['codigo'])
                print('{:^20} | {:^40} | {:^7} | {:^10} | {:^30} | {:^10}'.format(disciplina['codigo'], disciplina['nome'], disciplina['horario'], disciplina['sala'],listaMatriculasAluno[i]['data'], listaMatriculasAluno[i]['status']))

            # confirma trancamento
            print("\033[33m" + "======= Tem certeza que deseja trancar a matricula deste Aluno? ========" + "\033[0;0m")
            print("\033[33m" + "[1] Sim | [2] Cancelar" + "\033[0;0m")
            opcao = input("\033[33m" + "Escolha uma opcao. Digite 1 ou 2:" + "\033[0;0m")
            # Data inicial
            d1 = datetime.datetime.strptime(dataMatricula, '%Y-%m-%d')
            # Calculo da quantidade de dias
            quantidadeDias = abs((datetime.datetime.today() - d1).days)

            while not(opcao in ['1','2']):
                print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
                print("\033[33m" + "======= Tem certeza que deseja trancar a matricula deste Aluno? ========" + "\033[0;0m")
                print("\033[33m" + "[1] Sim | [2] Cancelar" + "\033[0;0m")
                opcao = input("\033[33m" + "Escolha uma opcao. Digite 1 ou 2:" + "\033[0;0m")


            else:
                
                if opcao == '1':
                    if quantidadeDias > 30:

                        print("\033[31m", "=" * 15, "Não é possivel trancar a matricula.. pois excedeu o prazo maximo de 30 dias.", "=" * 15, "\033[0;0m")
                        print("[0] Voltar")
                        voltar = input("\033[33m" + "Informe o numero de uma opção:" + "\033[0;0m")
                        while not(voltar == '0'):
                                print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
                                voltar = input("\033[33m" + "Informe o numero de uma opção:" + "\033[0;0m")
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            telaPrincipalOpcaoMatricula()

                    else:
                        retorno = ControleMatricula.cadastrarTracamentoMatricula(listaMatriculasAluno,matriculaAluno)
                        if retorno == True:
                            print("\033[33m" + "Realizando trancamento..." + "\033[0;0m")
                            time.sleep(2)
                            print("\033[32m" + "Trancamento efetuado com sucesso" + "\033[0;0m")
                            time.sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')  # apagando o console
                            telaPrincipalOpcaoMatricula()
                        else:
                            print("\033[31m", "=" * 15, " Erro ao trancar a matricula ", "=" * 15, "\033[0;0m")
                            os.system('cls' if os.name == 'nt' else 'clear')  # apagando o console
                            telaPrincipalOpcaoMatricula()
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    telaPrincipalOpcaoMatricula()


def telaExcluirMatricula():
    print("\033[47;1;30m" + "=" * 30, " Principal >> Matricula(Aluno/Disciplina) >> Exclusão de disciplina", "=" * 30 + '\033[0;0m\n')
    print("[0] - Voltar\n")
    matriculaAluno = input("Informe a matricula do aluno:")

    if matriculaAluno == "0":
        os.system('cls' if os.name == 'nt' else 'clear')
        telaPrincipalOpcaoMatricula()
    else:
        while ControleAluno.pesquisaAluno(matriculaAluno) == False:
            print("\033[31m", "=" * 15, " Matricula não encontrada ", "=" * 15, "\033[0;0m")
            matriculaAluno = input("\033[33m" + "Informe a matricula do aluno:" + "\033[0;0m")

            if matriculaAluno == "0":
                os.system('cls' if os.name == 'nt' else 'clear')
                telaPrincipalOpcaoMatricula()
                break
        else:
            listaMatriculasAluno = ControleMatricula.listarMatriculasAlunoAdm(matriculaAluno)
            dadosAluno = ControleAluno.pesquisaAluno(matriculaAluno)
            print("\n\033[32mInformações do Aluno", "=" * 115, "\033[0;0m")
            print("\nNome do Aluno: " + dadosAluno['nome'], "\t" * 4, "Sexo: " + dadosAluno['sexo'], "\t" * 4,
                  "Data nascimento: " + dadosAluno['data'])
            print("\nTelefone: " + dadosAluno['telefone'], "\t" * 5, "Status: " + dadosAluno['status'])
            print("\n\033[32mDisciplinas que o aluno esta matriculado","="*95, "\033[0;0m")
            print('{:^3} | {:^10} | {:^40} | {:^1} | {:^10} | {:^10} | {:^10}'.format("  ","Codigo da disciplina", "Nome da disciplina", "Horario","Sala", "Data que o aluno se matriculou","Status"))
            print('----+----------------------+------------------------------------------+---------+------------+--------------------------------+---------')

            for i in range(0,len(listaMatriculasAluno)):
                if listaMatriculasAluno[i]['status'].upper() != 'TRANCADO':
                    disciplina = ControleDisciplina.pesquisaDisciplina(listaMatriculasAluno[i]['codigo'])
                    print('{:^13} | {:^20} | {:^40} | {:^7} | {:^10} | {:^30} |{:^10}'.format("\033[33m["+str(i+1)+"]\033[0;0m",disciplina['codigo'], disciplina['nome'], disciplina['horario'], disciplina['sala'],listaMatriculasAluno[i]['data'],listaMatriculasAluno[i]['status']))

            opcao = input("\nInforme o \033[33m numero da linha\033[0;0m da disciplina que deseja trancar:")
            while opcao >= '5':
                print("\033[31m", "=" * 15, " Linha não encontrada ", "=" * 15, "\033[0;0m")
                opcao = input("\nInforme o \033[33m numero da linha\033[0;0m da disciplina que deseja trancar:")

            else:

               if opcao == "0":
                   os.system('cls' if os.name == 'nt' else 'clear')
                   telaPrincipalOpcaoMatricula()
               status = listaMatriculasAluno[int(opcao)-1]['status'].upper()
               while status == 'EXCLUIDO':
                   print("\033[31m", "=" * 15, " Essa disciplina ja foi excluida ", "=" * 15, "\033[0;0m")
                   opcao = input("\nInforme o \033[33m numero da linha\033[0;0m da disciplina que deseja trancar:")
                   status = listaMatriculasAluno[int(opcao) - 1]['status'].upper()
                   if opcao == "0":
                       os.system('cls' if os.name == 'nt' else 'clear')
                       telaPrincipalOpcaoMatricula()
               else:

                    dataMatricula = listaMatriculasAluno[int(opcao)-1]['data'].replace("/","-")
                    codidoDisciplina = listaMatriculasAluno[int(opcao)-1]['codigo']
                    # Data inicial
                    d1 = datetime.datetime.strptime(dataMatricula, '%Y-%m-%d')

                    # Calculo da quantidade de dias
                    quantidadeDias = abs((datetime.datetime.today() - d1).days)
                    if quantidadeDias > 15:
                        print("\033[31m", "=" * 15,"Não é possivel fazer a exclusao da matricula na disciplina.. pois excedeu o prazo maximo de 15 dias.", "=" * 15,"\033[0;0m")
                        print("[0] Voltar")
                        voltar = input("\033[33m" + "Informe o numero de uma opção:" + "\033[0;0m")
                        while not (voltar == '0'):
                            print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
                            voltar = input("\033[33m" + "Informe o numero de uma opção:" + "\033[0;0m")
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            telaPrincipalOpcaoMatricula()
                    else:
                        # confirma exclusao
                        print(
                       "\033[33m" + "======= Tem certeza que deseja realizar a exclusão da matricula nessa Disciplina? ========" + "\033[0;0m")
                        print("\033[33m" + "[1] Sim | [2] Cancelar" + "\033[0;0m")
                        opcao = input("\033[33m" + "Escolha uma opcao. Digite 1 ou 2:" + "\033[0;0m")

                        while not (opcao in ['1', '2']):
                            print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
                            print(
                           "\033[33m" + "======= Tem certeza que deseja realizar a exclusão da matricula nessa Disciplina? ========" + "\033[0;0m")
                            print("\033[33m" + "[1] Sim | [2] Cancelar" + "\033[0;0m")
                            opcao = input("\033[33m" + "Escolha uma opcao. Digite 1 ou 2:" + "\033[0;0m")


                        else:
                            if opcao == '1':
                                retorno = ControleMatricula.exclusaoMatriculaAluno(matriculaAluno,codidoDisciplina,listaMatriculasAluno[int(opcao)-1])
                                if retorno == True:
                                    print("\033[33m" + "Realizando Exclusão da matricula..." + "\033[0;0m")
                                    time.sleep(2)
                                    print("\033[32m" + "Exclusão efetuada com sucesso" + "\033[0;0m")
                                    time.sleep(2)
                                    os.system('cls' if os.name == 'nt' else 'clear')  # apagando o console
                                    telaPrincipalOpcaoMatricula()
                                else:
                                    print("\033[31m", "=" * 15, " Erro ao excluir a matricula ", "=" * 15, "\033[0;0m")
                                    os.system('cls' if os.name == 'nt' else 'clear')  # apagando o console
                                    telaPrincipalOpcaoMatricula()
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                telaPrincipalOpcaoMatricula()

#------------------------------------------ Relatorios ------------------------------------
# função responsavel por apresentar o menu ralatorio
def telaPrincipalOpcaoRelatorio():

    print("\033[47;1;30m" + "=" * 42, " Principal >> Relatório", "=" * 42 + '\033[0;0m')
    print("[1] - Relatório de alunos | [2] - Relatório de Aniversariantes do mês | [3] - Relatório da disciplina | [0] - Voltar")
    opcao = input("\nInforme o numero de uma opção:")

    # validando a opcap escolhida
    while not (opcao in ['1', '2', '3', '0']):
        print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
        opcao = input("\033[33m" + "Informe o numero de uma opção:" + "\033[0;0m")

    else:

            # encaminhando para a pagina escolhida
            if opcao == '1':
                os.system('cls' if os.name == 'nt' else 'clear')  # limpando o console
                telaRelatorioAlunos()# apresentando a pagina escolhida
            elif opcao == '2':
                os.system('cls' if os.name == 'nt' else 'clear')  # limpando o console
                telaRelatorioAniversariante() # apresentando a pagina escolhida
            elif opcao == '3':
                os.system('cls' if os.name == 'nt' else 'clear')  # limpando o console
                telaRelatorioAlunosPorDisciplina() #apresentando a pagina escolhida
            elif opcao == "0":
                os.system('cls' if os.name == 'nt' else 'clear')
                telaInicialAdministrador()



def telaRelatorioAlunos():
    print("\033[47;1;30m" + "=" * 25, " Principal >> Relatório >> Relatório de alunos - ordenado po matricula", "=" * 25   + '\033[0;0m')
    lista = ControleRelatorio.relatorioAlunos()
    tabela = '{:10} | {:^40} | {:^1} | {:^10} | {:^10} | {:^2} | {:^10}\n'.format("Matricula", "Nome", "Sexo",
                                                                                  "Data de Nascimento", "Telefone",
                                                                                  "Quantidade de Disciplina",
                                                                                  "Status")
    tabela += '-----------+------------------------------------------+------+--------------------+------------+--------------------------+----------'
    print(tabela)
    for i in range(0,len(lista)):
        print(lista[i],end="")
    print("=" * 134)
    print("[0] Voltar")
    opcao = input("Escolha uma opcao:")
    while opcao != "0":
        print("\033[31m" + "========== Opção invalida =============" + "\033[0;0m")
        opcao = input("\033[33m" + "Escolha uma opção:" + "\033[0;0m")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        telaPrincipalOpcaoRelatorio()

def telaRelatorioAniversariante():
    print("\033[47;1;30m" + "=" * 25, " Principal >> Relatório >> Relatório de Aniversariantes do mes", "=" * 25+ '\033[0;0m')
    print("\n[1] Janeiro | [2] Fevereiro | [3] Março | [4] Abril | [5] Maio | [6] Junho \n[7] Julho | [8] Agosto | [9] Setembro | [10] Outubro | [11] Novembro | [12] Dezembro ")
    print("\n\n[0] Voltar")
    mes = input("Informe o numero do mês:")
    if mes == '0':
        os.system('cls' if os.name == 'nt' else 'clear')
        telaPrincipalOpcaoRelatorio()
    else:
        while not(mes in ['1','2','3','4','5','6','7','8','9','10','11','12']):
            print("\033[31m" + "========== Opção invalida =============" + "\033[0;0m")
            mes = input("\033[33m" + "Informe o numero do mês:" + "\033[0;0m")
            if mes == '0':
                os.system('cls' if os.name == 'nt' else 'clear')
                telaPrincipalOpcaoRelatorio()
                break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            telaRelatorioAniversarianteMes(mes)


def telaRelatorioAniversarianteMes(mes):
    meses = ['Janeiro ', 'Fevereiro ','Março ','Abril ','Maio ','Junho ','Julho ','Agosto ','Setembro ','Outubro ','Novembro ','Dezembro ']
    print("\033[47;1;30m" + "=" * 25, " Principal >> Relatório >> Relatório de Aniversariantes do mes de "+meses[int(mes) - 1] + "=" * 25   + '\033[0;0m\n')
    lista = ControleRelatorio.relatorioAniversariantes(mes)
    tabela = '{:10} | {:^40} | {:^1} | {:^10} | {:^10} | {:^2} | {:^10}\n'.format("Matricula", "Nome", "Sexo",
                                                                                  "Data de Nascimento", "Telefone",
                                                                                  "Quantidade de Disciplina",
                                                                                  "Status")
    tabela += '-----------+------------------------------------------+------+--------------------+------------+--------------------------+----------'
    print(tabela)
    for i in range(0,len(lista)):
        print('{:11}|{:^42}|{:^6}|{:^20}|{:^12}|{:^26}|{:>10}\n'.format(*lista[i].values()),end="")

    print("=" * 134)
    print("[0] Voltar")
    opcao = input("Escolha uma opcao:")
    while opcao != "0":
        print("\033[31m" + "========== Opção invalida =============" + "\033[0;0m")
        opcao = input("\033[33m" + "Escolha uma opção:" + "\033[0;0m")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        telaPrincipalOpcaoRelatorio()


def telaRelatorioAlunosPorDisciplina():
    print("\033[47;1;30m" + "=" * 25, " Principal >> Relatório >> Relatório de Alunos por Disciplina", "=" * 25+ '\033[0;0m')

    print("\n\n[0] Voltar")
    codigo = input("Informe o codigo da disciplina:")
    if codigo == '0':
        os.system('cls' if os.name == 'nt' else 'clear')
        telaPrincipalOpcaoRelatorio()
    else:
        dadosDisciplina = ControleDisciplina.pesquisaDisciplina(codigo)
        while dadosDisciplina == False:

            print("\033[31m" + "Disciplina não encontrada." + "\033[0;0m")
            codigo = input("\033[33m" + "Informe o codigo da disciplina:" + "\033[0;0m")

            if codigo == "0":
                os.system('cls' if os.name == 'nt' else 'clear')
                telaPrincipalOpcaoRelatorio()
                break

            dadosDisciplina = ControleDisciplina.pesquisaDisciplina(codigo)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            telaListaRelatorioAlunosPorDisciplina(dadosDisciplina)


def telaListaRelatorioAlunosPorDisciplina(dadosDisciplina):

    print("\033[47;1;30m" + "=" * 25, " Principal >> Relatório >> Relatório de Alunos da disciplina " +dadosDisciplina['nome']+ " =" * 25   + '\033[0;0m')
    lista = ControleRelatorio.relatorioDisciplinaPorAluno(dadosDisciplina['codigo'])
    tabela = '{:10} | {:^40} | {:^1} | {:^10} | {:^10} | {:^2} | {:^10}\n'.format("Matricula", "Nome", "Sexo",
                                                                                  "Data de Nascimento", "Telefone",
                                                                                  "Quantidade de Disciplina",
                                                                                  "Status")
    tabela += '-----------+------------------------------------------+------+--------------------+------------+--------------------------+----------'
    print(tabela)
    for i in range(0,len(lista)):
        print('{:11}|{:^42}|{:^6}|{:^20}|{:^12}|{:^26}|{:>10}\n'.format(*lista[i].values()))

    print("=" * 134)
    print("[0] Voltar")
    opcao = input("Escolha uma opcao:")
    while opcao != "0":
        print("\033[31m" + "========== Opção invalida =============" + "\033[0;0m")
        opcao = input("\033[33m" + "Escolha uma opção:" + "\033[0;0m")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        telaPrincipalOpcaoRelatorio()
