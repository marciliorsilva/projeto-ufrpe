from random import choice,randint
import os.path

#lista das letras do alfabeto para gerar o codigo da disciplina
alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "X", "W", "Y", "Z"]

#função responsavel por cadastrar a disciplina
def cadastrarDisciplina(codigo, nome,horario,sala,quantidadeVagas,vagasOcupadas,status):
    #verificando se o arquivo existe. retorno: true ou false
    if os.path.isfile('disciplinas.txt'):

        try:
            #carregando arquivo como leitura
            arquivo = open("disciplinas.txt","a")
            #formando a linha e salvando no arquivo
            arquivo.writelines('{:11}|{:^42}|{:^9}|{:^12}|{:^21}|{:^16}|{:>10}\n'.format(codigo,nome,horario,sala,quantidadeVagas,vagasOcupadas,status))
            arquivo.close()
            return True

        except:

            return False
    else:
        try:
            #carregando arquivo para gravação
            arquivo = open("disciplinas.txt","w")
            #formando cabeçalho
            tabela = '{:10} | {:^40} | {:^1} | {:^10} | {:^10} | {:^2} | {:^10}\n'.format("Codigo", "Nome", "Horario",
                                                                                 "Sala", "Quantidade de Vagas",
                                                                                 "Vagas ocupadas", "Status")
            tabela += '-----------+------------------------------------------+---------+------------+---------------------+----------------+----------\n'
            #formando a linha
            tabela += '{:11}|{:^42}|{:^9}|{:^12}|{:^21}|{:^16}|{:>10}\n'.format(codigo,nome,horario,sala,quantidadeVagas,vagasOcupadas,status)
            #salvando
            arquivo.writelines(tabela)
            arquivo.close()
            return True

        except:

            return False

#função responsavel por verificar a matricula para não gerar matricula duplicada
def verficarCodigo(tempCodigo):

    #verificando se o arquivo existe. retorno: true ou false
    if os.path.isfile('disciplinas.txt'):
        #carregando arquivo como leitura
        arquivo = open("disciplinas.txt", "r")
        #sufixo do codigo
        sufixo = "DISC"
        #lista das linhas do arquivo
        linhas = arquivo.readlines() 
        #pecorrendo as linhas do arquivo
        for i in range(0, len(linhas), 1):
           #lista de dados da disciplina
           coluna= linhas[i].rsplit("|")
           #verificando se o codigo esta cadastrada no arquivo
           if tempCodigo == coluna[0].replace(" ",""):

                novoNumero = randint(1000, 9999)#gerando um numero aleatorio de 4 digitos
                novaLetra = choice(alfabeto)#selecionando uma letra do alfabeto aleatoria
                novoCodigo = sufixo + str(novoNumero) + novaLetra#formando o codigo
                tempCodigo = verficarCodigo(novoCodigo)#verificando o codigo novamente
                break

           else:
               continue


    return tempCodigo

#função responsavel por gerar o codigo da disciplina
def gerarCodigo():
    sufixo = "DISC"#sufixo do codigo
    numero = randint(1000, 9999)  # gerando numero aleatorio de 4 digitos#
    letra = choice(alfabeto)  # selecionando uma letra do alfabeto aleatoria#
    codigo = sufixo + str(numero) + letra# formando o codigo
    return verficarCodigo(codigo)#verificando o codigo

#função responsavel por atualizar os dados da disciplina
def atualizarDadosDisciplina(dadosDisciplina):
    try:
        #carregando arquivo como leitura
        alterarArquivo = open("disciplinas.txt", "r")
        #lista da linhas do arquivo
        linhas = alterarArquivo.readlines()
        #pecorrendo as linhas
        for i in range(0, len(linhas)):
        #pulando cabeçalho
            if i > 1:
                #lista de dados da disciplina
                coluna = linhas[i].replace(" ", "").rsplit("|")
                #verificando se o codigo da disciplina existe no arquivo
                if coluna[0] == dadosDisciplina["codigo"]:
                #selecionando o item da lista referente ao codigo da disciplina e alterando o item com os novos dados
                   linhas[i] = '{:11}|{:^42}|{:^9}|{:^12}|{:^21}|{:^16}|{:>10}\n'.format(*dadosDisciplina.values())
                   break
        #salvando
        salvarAlteracao = open("disciplinas.txt", "w")
        salvarAlteracao.writelines(linhas)
        salvarAlteracao.close()
        return True
    except:
        return False

#função responsavel por excluir a disciplina, trocando status do registro da disciplina para 'excluido'
def removerDisciplina(dadosDisciplina):
     try:
        #carregando arquivo como leitura
        alterarArquivo = open("disciplinas.txt", "r")
        #lista da linhas do arquivo
        linhas = alterarArquivo.readlines()
        #pecorrendo as linhas
        for i in range(0, len(linhas)):
            #pulando cabeçalho
            if i > 1:
                #lista de dados da disciplina
                coluna = linhas[i].replace(" ", "").rsplit("|")
                #verificando se o codigo da disciplina existe no arquivo
                if coluna[0] == dadosDisciplina["codigo"]:
                   #selecionando o item da lista referente ao codigo da disciplina e alterando o item com os novos dados
                   linhas[i] = '{:11}|{:^42}|{:^9}|{:^12}|{:^21}|{:^16}|{:>10}\n'.format(*dadosDisciplina.values())
                   break
        #salvando
        salvarAlteracao = open("disciplinas.txt", "w")
        salvarAlteracao.writelines(linhas)
        salvarAlteracao.close()

        return True
     except:
        return False

#função responsavel por pesquisa a disciplina no arquivo
def pesquisaDisciplina(codigo):
    #verificando se o arquivo existe. retorno:true e false
    if os.path.isfile('disciplinas.txt'):
        #carregando arquivo como leitura
        arquivo = open("disciplinas.txt", "r")
        #lista das linhas do arquivo
        linhas = arquivo.readlines()
        #criando um dicionario
        registroDisciplina = {'codigo': '', 'nome': '', 'horario': '', 'sala': '', 'quantidadeVagas': '', 'vagasOcupadas': '',
                         'status': ''}
        #variavel de retorno
        disciplinaEncontrada = False
        #pecorrendo as linhas
        for i in range(0, len(linhas)):
            #pulando cabeçalho
            if i > 1:
                #lista dos dados da disciplina
                coluna = linhas[i].replace("\n", "").rsplit("|")
                #verificando se o codigo existe no arquivo
                if coluna[0].strip() == codigo:
                  #atribuindo os dados no dicionario
                  registroDisciplina['codigo'] = coluna[0].strip()
                  registroDisciplina['nome'] = coluna[1].strip()
                  registroDisciplina['horario'] = coluna[2].strip()
                  registroDisciplina['sala'] = coluna[3].strip()
                  registroDisciplina['quantidadeVagas'] = coluna[4].strip()
                  registroDisciplina['vagasOcupadas'] = coluna[5].strip()
                  registroDisciplina['status'] = coluna[6].strip()
                  #alterando o valor da variavel
                  disciplinaEncontrada = True
                  break
        #retorno
        if disciplinaEncontrada == False:

            return False

        else:
            return registroDisciplina

    else:
        return False



def listaDisciplinasAlunoMatricula():
    arquivo = open("disciplinas.txt", "r")
    linhas = arquivo.readlines()
    disciplinas = []
    for i in range(0, len(linhas)):
        registroDisciplina = {'codigo': '', 'nome': '', 'horario': '', 'sala': '', 'quantidadeVagas': '','vagasOcupadas': ''}
        if i > 1:
            colunas = linhas[i].replace("\n", "").rsplit("|")
            for c in range(0, len(colunas)):
                if colunas[6].strip().upper() == "ATIVO" and colunas[4].strip() != "0":
                    registroDisciplina['codigo'] = colunas[0].strip()
                    registroDisciplina['nome'] = colunas[1].strip()
                    registroDisciplina['horario'] = colunas[2].strip()
                    registroDisciplina['sala'] = colunas[3].strip()
                    registroDisciplina['quantidadeVagas'] = colunas[4].strip()
                    registroDisciplina['vagasOcupadas'] = colunas[5].strip()


            disciplinas.append(registroDisciplina)

    return disciplinas
