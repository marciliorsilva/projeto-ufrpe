from random import choice,randint
import os.path

#lista das letras do alfabeto para gerar a matricula do aluno
alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "X", "W", "Y", "Z"]


#função responsavel por cadastrar o aluno
def cadastrarAluno(matricula, nome,sexo,dataNascimento,telefone,quantidadeDisciplina,status):
    #verificando se o arquivo existe. retorno: true ou false
    if os.path.isfile('alunos.txt'):

        try:
            #carregando arquivo como leitura
            arquivo = open("alunos.txt","r")
            #formando a linha e salvando no arquivo
            arquivo.writelines('{:11}|{:^42}|{:^6}|{:^20}|{:^12}|{:^26}|{:>10}\n'.format(matricula,nome,sexo,dataNascimento,telefone,str(quantidadeDisciplina),status))
            arquivo.close()
            return True

        except:

            return False

    else:

        try:
            #carregando arquivo para gravação
            arquivo = open("alunos.txt","w")
            #formando cabeçalho
            tabela = '{:10} | {:^40} | {:^1} | {:^10} | {:^10} | {:^2} | {:^10}\n'.format("Matricula", "Nome", "Sexo",
                                                                                 "Data de Nascimento", "Telefone",
                                                                                 "Quantidade de Disciplina", "Status")
            tabela += '-----------+------------------------------------------+------+--------------------+------------+--------------------------+----------\n'
            #formando a linha
            tabela += '{:11}|{:^42}|{:^6}|{:^20}|{:^12}|{:^26}|{:>10}\n'.format(matricula,nome,sexo,dataNascimento,telefone,str(quantidadeDisciplina),status)
            #salvando
            arquivo.writelines(tabela)
            arquivo.close()
            return True


        except:
            return False

#função responsavel por verificar a matricula para não gerar matricula duplicada
def verficarMatricula(tempMatricula):
    #verificando se o arquivo existe. retorno: true ou false
    if os.path.isfile('alunos.txt'):
        #carregando arquivo como leitura
        arquivo = open("alunos.txt", "r")
        #sufixo da matricula
        sufixo = "UFRPE"
        #lista das linhas do arquivo
        linhas = arquivo.readlines() 
        #pecorrendo as linhas do arquivo
        for i in range(0, len(linhas), 1):
            #lista de dados do aluno
            coluna= linhas[i].rsplit("|")
            #verificando se a matricula esta cadastrada no arquivo
            if tempMatricula == coluna[0].replace(" ",""):

                novoNumero = randint(1000, 9999)#gerando um numero aleatorio de 4 digitos
                novaLetra = choice(alfabeto)#selecionando uma letra do alfabeto aleatoria
                novaMatricula = sufixo + str(novoNumero) + novaLetra#formando a matricula
                tempMatricula = verficarMatricula(novaMatricula)#verificando a nova matricula novamente
                break
            else:
                continue

    return tempMatricula

#função responsavel por gerar a matricula do aluno
def gerarMatricula():
    sufixo = "UFRPE"#sufixo da matricula
    numero = randint(1000, 9999)  # gerando um numero aleatorio de 4 digitos#
    letra = choice(alfabeto)  # selecionando uma letra do alfabeto aleatoria#
    matricula = sufixo + str(numero) + letra #formando a matricula
    return verficarMatricula(matricula)#verificando a matricula


#função responsavel por atualizar os dados do aluno
def atualizarDadosAluno(dadosAluno):

    try:
        #carregando arquivo como leitura
        alterarArquivo = open("alunos.txt","r")
        #lista da linhas do arquivo
        linhas = alterarArquivo.readlines()
        #pecorrendo as linhas
        for i in range(0,len(linhas)):
        #pulando cabeçalho
            if i > 1:
                #lista de dados do aluno
                coluna = linhas[i].replace(" ","").rsplit("|")
                #verificando se a matricula do aluno existe no arquivo
                if coluna[0]== dadosAluno["matricula"]:
                    #selecionando o item da lista referente a matricula do aluno e alterando o item com os novos dados
                    linhas[i] = '{:11}|{:^42}|{:^6}|{:^20}|{:^12}|{:^26}|{:>10}\n'.format(*dadosAluno.values())
                    break
        #salvando
        salvarAlteracao = open("alunos.txt","w")
        salvarAlteracao.writelines(linhas)
        salvarAlteracao.close()
        return True
    except:
        return False

#função responsavel por excluir aluno, trocando status do registro do aluno para 'excluido'
def removerAluno(dadosAluno):
    try:
        #carregando arquivo como leitura
        alterarArquivo = open("alunos.txt","r")
        #lista da linhas do arquivo
        linhas = alterarArquivo.readlines()
        #pecorrendo as linhas
        for i in range(0,len(linhas)):
            #pulando cabeçalho
            if i > 1:
                #lista de dados do aluno
                coluna = linhas[i].replace(" ","").rsplit("|")
                #verificando se a matricula do aluno existe no arquivo
                if coluna[0]== dadosAluno["matricula"]:
                    #selecionando o item da lista referente a matricula do aluno e alterando o item com os novos dados
                    linhas[i] = '{:11}|{:^42}|{:^6}|{:^20}|{:^12}|{:^26}|{:>10}\n'.format(*dadosAluno.values())
                    break
        #salvando
        salvarAlteracao = open("alunos.txt","w")
        salvarAlteracao.writelines(linhas)
        salvarAlteracao.close()
        return True
    except:
        return False

#função responsavel por pesquisa o aluno no arquivo
def pesquisaAluno(matricula):
    #verificando se o arquivo existe. retorno:true e false
    if os.path.isfile('alunos.txt'):
        #carregando arquivo como leitura
        arquivo = open("alunos.txt","r")
        #lista das linhas do arquivo
        linhas = arquivo.readlines()
        #criando um dicionario
        registroAluno = {'matricula':'','nome':'','sexo':'','data':'','telefone':'','disciplinas':'','status':''}
        #variavel de retorno
        matriculaEncontrada = False

        #pecorrendo as linhas
        for i in range(0,len(linhas)):
            #pulando cabeçalho
            if i > 1:
                #lista dos dados alunos
                coluna = linhas[i].replace("\n","").rsplit("|")
                #verificando se a matricula existe no arquivo
                if coluna[0].strip() == matricula:
                    #atribuindo os dados no dicionario
                    registroAluno['matricula'] = coluna[0].strip()
                    registroAluno['nome'] = coluna[1].strip()
                    registroAluno['sexo'] = coluna[2].strip()
                    registroAluno['data'] = coluna[3].strip()
                    registroAluno['telefone'] = coluna[4].strip()
                    registroAluno['disciplinas'] = coluna[5].strip()
                    registroAluno['status'] = coluna[6].strip()
                    #alterando o valor da variavel
                    matriculaEncontrada = True
                    break


        #retorno
        if matriculaEncontrada == False:

            return False
        else:
            return registroAluno

    else:
        return False





