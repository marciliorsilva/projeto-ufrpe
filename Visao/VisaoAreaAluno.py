from Controle import ControleLogin,ControleMatricula,ControleDisciplina
from Visao import VisaoLogin
import os,time, datetime
#---------------------------------- Tela principal da area do aluno -------------------------------
#função responsavel por apresentar a tela inicial da area do aluno
def telaInicialAluno():

    menu = ""
    menu += "============================= Bem Vindo "+ControleLogin.getDadosAluno()['nome']+" =================================\n \n"
    menu += "--------------------------- Menu Principal ------------------------------\n"
    menu += "1 - Matricula | 0 - Sair"
    print(menu)
    opcao = input("\nInforme o numero de uma opção:")
    while not(opcao in ['1','0']):#verificando opção informada
        print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
        opcao = input("\033[33m" + "Informe o numero de uma opção:" + "\033[0;0m")
    else:
        #encaminhando para a opção informa
       if opcao == "1":
           os.system('cls' if os.name == 'nt' else 'clear')#limpando console
           telaPrincipalOpcaoMatricula()#apresentando a tela
       elif opcao == "0":
           print("Saindo...")
           time.sleep(3)#intervalo
           os.system('cls' if os.name == 'nt' else 'clear')#limpando console
           VisaoLogin.telaInicialSistema()#voltando para tela inicial do sistema

#------------------------------------------- Matricula ------------------------------------
# função responsavel por apresentar o menu principal
def telaPrincipalOpcaoMatricula():

    print("\033[47;1;30m" + "=" * 42, " Principal >> Matricula", "=" * 42 + '\033[0;0m')
    print("[1] - Matricular na disciplina | [2] - Listar matriculas | [0] - Voltar")
    opcao = input("\nInforme o numero de uma opção:")


    while not(opcao in ['1','2','0']):#validando a opcao informada
        print("\033[31m", "=" * 15, " Opção invalida ", "=" * 15, "\033[0;0m")
        opcao = input("\033[33m" + "Informe o numero de uma opção:" + "\033[0;0m")

    else:
        #encaminhando para opção informada
        if opcao == "1":
            os.system('cls' if os.name == 'nt' else 'clear')#limpano console
            telaMatricularDisciplina()#apresentando a tela
        elif opcao == "2":
            os.system('cls' if os.name == 'nt' else 'clear')#limpando console
            telaListarMatriculas()#apresentando a tela
        elif opcao == "0":
            os.system('cls' if os.name == 'nt' else 'clear')  # limpando console
            VisaoLogin.telaInicialSistema()  # voltando para tela inicial do sistema

#função responsavel por apresentar a tela com a lista das matriculas do aluno logado
def telaListarMatriculas():
    #criando cabeçalho
    print("\033[47;1;30m" + "=" * 30, " Principal >> Matricula >> Lista de matriculas", "=" * 30 + '\033[0;0m\n')
    tabela = '{:10} | {:^40} | {:^1} | {:>10}\n'.format("Codigo", "Nome", "Horario","Sala")
    tabela += '-----------+------------------------------------------+---------+------------+\n'
    #verificando se o aluno logado esta mariculado em alguma disciplina. retorno: false ou uma lista de dicionario da disciplina
    lista = ControleMatricula.listarMatriculasAluno(ControleLogin.getDadosAluno()['matricula'])
    if lista == False:

        print("\033[31m" + "=== Você não esta matriculado em nenhuma disciplina. ===" + "\033[0;0m")
        print("[0] - Voltar")
        opcao = input("\nInforme o numero de uma opção:")
        while opcao != "0":# verificando opção
            print("\033[31m" + "========== Opção invalida =============" + "\033[0;0m")
            opcao = input("\033[33m" + "Informe o numero de uma opção:" + "\033[0;0m")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')#limpando tela
            telaPrincipalOpcaoMatricula()# apresentando tela
    else:
        # formando as linhas da tabela
        for i in range(0,len(lista)):

              tabela += '{:11}|{:^42}|{:^9}|{:>10}\n'.format(lista[i]['codigo'], lista[i]['nome'], lista[i]['horario'],lista[i]['sala'])
        #imprimindo tabela
        print(tabela)

        print("[0] - Voltar")
        opcao = input("\nInforme o numero de uma opção:")
        while opcao != "0":#verificando opção informada
            print("\033[31m" + "========== Opção invalida =============" + "\033[0;0m")
            opcao = input("\033[33m" + "Informe o numero de uma opção:" + "\033[0;0m")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')#limpando console
            telaPrincipalOpcaoMatricula()#apresentando tela


#função responsavel por apresentar a tela de matricula na disciplina
def telaMatricularDisciplina():
    #guardando matricula do aluno logado
    matricula = ControleLogin.getDadosAluno()['matricula']

    print("\033[47;1;30m" + "=" * 30, " Principal >> Matricula >> Matricular na disciplina", "=" * 30, '\033[0;0m\n')

    #verificando se aluno atingiu a cota maxima
    if int(ControleLogin.getDadosAluno()['disciplinas']) >= 5:
        print("\033[31m"+"===== Você atingiu sua cota maxima de disciplinas por período  ====="+"\033[0;0m")
        print("[0] - Voltar")
        opcao = input("\nInforme o numero de uma opção:")
        #verificando opção informada
        while opcao != "0":
            print("\033[31m" + "========== Opção invalida =============" + "\033[0;0m")
            opcao = input("\033[33m" + "Informe o numero de uma opção:" + "\033[0;0m")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')#limpando console
            telaPrincipalOpcaoMatricula()#apresentando tela
    else:
        #formando cabeçalho
        tabela = '{:10} | {:^40} | {:^1} | {:^10} | {:^10} | {:^2}\n'.format("Codigo", "Nome", "Horario", "Sala", "Quantidade de Vagas","Vagas ocupadas")
        tabela += '-----------+------------------------------------------+---------+------------+---------------------+----------------+'
        #imprimindo tabela
        print(tabela)

        #lsta de discplinas. retorna lista de disciplinas ativas e com vagas disponiveis
        disciplinas = ControleDisciplina.listaDisciplinasAlunoMatricula()

        #pecorrendo lista
        for i in range(0,len(disciplinas)):
            #verificando se o aluno ja esta matriculado na disciplina. retorno: true ou false
            if ControleMatricula.alunoJaEstaMatriculado(matricula,disciplinas[i]['codigo'].strip()) == False:
                registro = '{:11}|{:^42}|{:^9}|{:^12}|{:^21}|{:^16}'.format(*disciplinas[i].values())
                print(registro)#imprimindo
        print("-"*44,"^ Disciplinas disponiveis ^","-"*44)

        #formulario de matricula
        print("Matricula:"+matricula)#imprimindo matricula do aluno
        dataMatricula = datetime.date.today()#pegando a data atual
        print("Data da matricula:"+str(dataMatricula))#imprimindo data


        codigoDisciplina = input("Informe o codigo da disciplina:")
        #condicao de cancelamento do formaulario
        if codigoDisciplina == "0":
            os.system('cls' if os.name == 'nt' else 'clear')#limpando console
            telaPrincipalOpcaoMatricula()#apresentando tela
        else:

            #verificando se o usuario não digitou o codigo da disciplina errado
            while len([d for d in disciplinas if d['codigo'] == codigoDisciplina.upper()]) == 0:
                print("\033[31m" + "========== Disciplina informada não contem na lista =============" + "\033[0;0m")
                codigoDisciplina = input("\033[33m" + "Informe o codigo da disciplina:" + "\033[0;0m")
                # condicao de cancelamento do formaulario
                if codigoDisciplina == "0":
                    os.system('cls' if os.name == 'nt' else 'clear')  # limpando console
                    telaPrincipalOpcaoMatricula()  # apresentando tela
            else:
                #pegando os dados da disciplina escolhida
                disciplinaEscolhida = ControleDisciplina.pesquisaDisciplina(codigoDisciplina)

                #por padrao o status vai ser ativo
                status = "ATIVO"  # atribuindo o status dA MATRICULA no sistema
                print("Status: Ativo")  # exibindo o status da matricula

                # confirma matricula
                print("\033[33m" + "====== Confirma matricula? ========" + "\033[0;0m")
                print("\033[33m" + "[1] Confirma | [2] Cancelar" + "\033[0;0m")
                opcao = input("\033[33m" + "Escolha uma opcao. Digite 1 ou 2:" + "\033[0;0m")
                while not(opcao in ['1','2']):#verficando opção informada
                    print("\033[31m" + "=========== Opção invalida ============" + "\033[0;0m")
                    print("\033[33m" + "========= Confirma matricula? =========" + "\033[0;0m")
                    print("\033[33m" + "[1] Confirma | [2] Cancelar" + "\033[0;0m")
                    opcao = input("\033[33m"+"Escolha uma opcao. Digite 1 ou 2:"+"\033[0;0m")
                else:
                    #encaminhando para opção informada
                    if opcao == '1':
                        #verificando se a matricula foi gravada no arquivo. retorno.: uma lista com dois itens- [true OU false , true OU false]
                        #primeiro item da lista: se a quantidade de vagas e a vagas ocupadas da disciplina foram atualzadas
                        #segundo item da lista: se foi adicionado mais uma disciplina no registro do aluno
                        retorno = ControleMatricula.cadastrarMatricula(str(dataMatricula),status,ControleLogin.getDadosAluno(),disciplinaEscolhida)
                        #verficando retorno
                        if retorno[0] == True and retorno[1] == True:
                            print("\033[33m" + "Salvando..." + "\033[0;0m")
                            time.sleep(2)
                            print("\033[32m" + "Matricula Cadastrada com sucesso" + "\033[0;0m")
                            time.sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')  # apagando o console
                            telaPrincipalOpcaoMatricula()
                    elif opcao == '2':
                        os.system('cls' if os.name == 'nt' else 'clear')  # limpando console
                        telaPrincipalOpcaoMatricula()#apresentado tela
