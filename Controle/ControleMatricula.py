from Controle import ControleDisciplina, ControleAluno
import os
import os.path
import time

#função responsavel por cadastrar a matricula do aluno na disciplina
def cadastrarMatricula(dataMatricula, status, dadosAluno, dadosDisciplina):
    if os.path.isfile('matriculas.txt'):

        try:
            #salvado matricula nova
            arquivo = open("matriculas.txt","a")
            arquivo.writelines('{:17} | {:^18} | {:^16} | {:>10}\n'.format(dadosDisciplina['codigo'],dadosAluno['matricula'],dataMatricula, status))
            arquivo.close()

            #atualizando a quantidade vagas e vaga ocupadas da disciplina
            atualizandoQuatidadeVagas = int(dadosDisciplina['quantidadeVagas']) - 1
            atualizandoVagasOcupadas = int(dadosDisciplina['vagasOcupadas']) + 1
            dadosDisciplina['quantidadeVagas'] = atualizandoQuatidadeVagas
            dadosDisciplina['vagasOcupadas'] = atualizandoVagasOcupadas
            retorno1 = ControleDisciplina.atualizarDadosDisciplina(dadosDisciplina)

            #atualizando as diciplinas do registro do aluno
            atualizandoDisciplinas = int(dadosAluno['disciplinas']) + 1
            dadosAluno['disciplinas'] = atualizandoDisciplinas
            retorno2 = ControleAluno.atualizarDadosAluno(dadosAluno)



            return retorno1,retorno2

        except:
            return False, False
    else:
        try:
            arquivo = open("matriculas.txt","w")
            tabela = '{:10} | {:^10} | {:^16} | {:^10}\n'.format("Codigo Disciplina", "Matricula do Aluno", "Data","Status")
            tabela += '------------------+--------------------+------------------+------------+\n'
            tabela += '{:17} | {:^18} | {:^16} | {:>10}\n'.format(dadosDisciplina['codigo'], dadosAluno['matricula'], dataMatricula, status)
            arquivo.writelines(tabela)
            arquivo.close()

            # atualizando a quantidade vagas e vaga ocupadas da disciplina
            atualizandoQuatidadeVagas = int(dadosDisciplina['quantidadeVagas']) - 1
            atualizandoVagasOcupadas = int(dadosDisciplina['vagasOcupadas']) + 1
            dadosDisciplina['quantidadeVagas'] = atualizandoQuatidadeVagas
            dadosDisciplina['vagasOcupadas'] = atualizandoVagasOcupadas
            retorno1 = ControleDisciplina.atualizarDadosDisciplina(dadosDisciplina)

            # atualizando as diciplinas do registro do aluno
            atualizandoDisciplinas = int(dadosAluno['disciplinas']) + 1
            dadosAluno['disciplinas'] = atualizandoDisciplinas
            retorno2 = ControleAluno.atualizarDadosAluno(dadosAluno)

            return retorno1, retorno2

        except:
            return False, False



def alunoJaEstaMatriculado(matricula,codigoDisciplina):

    if os.path.isfile('matriculas.txt'):
        estaMatriculado = False
        arquivo = open("matriculas.txt", "r")
        linhas = arquivo.readlines()

        for i in range(0,len(linhas)):
            if i > 1:
                colunas = linhas[i].replace("\n","").split("|")
                if colunas[1].strip() == matricula:
                    if colunas[0].strip() == codigoDisciplina:
                        estaMatriculado = True
                        break

        if estaMatriculado == False:
            return False
        else:
            return True

    else:
        return False


def exclusaoMatriculaAluno(matriculaAluno,codigoDisciplina,dadosMatricula):
    dadosAluno = ControleAluno.pesquisaAluno(matriculaAluno)
    dadosDisciplina = ControleDisciplina.pesquisaDisciplina(codigoDisciplina)
    dadosMatricula['status'] = 'EXCLUIDO'
    dadosAluno['disciplinas'] = int(dadosAluno['disciplinas']) - 1
    dadosDisciplina['quantidadeVagas'] = int(dadosDisciplina['quantidadeVagas']) + 1
    dadosDisciplina['vagasOcupadas'] = int(dadosDisciplina['vagasOcupadas']) - 1
    retorno = ControleAluno.atualizarDadosAluno(dadosAluno)
    retorno2 = ControleDisciplina.atualizarDadosDisciplina(dadosDisciplina)
    retorno3 = atualizarDadosMatricula(dadosMatricula)
    if retorno == True and retorno2 == True and retorno3 == True:
        return True
    else:
        return False

def atualizarDadosMatricula(dadosMatricula):
    try:
        alterarArquivo = open("matriculas.txt", "r")
        linhas = alterarArquivo.readlines()
        for i in range(0, len(linhas)):
            if i > 1:
                registro = linhas[i].replace(" ", "").replace("\n","").rsplit("|")
                print(registro[0], dadosMatricula["codigo"], registro[1], dadosMatricula['matricula'])

                if registro[0] == dadosMatricula["codigo"] and registro[1] == dadosMatricula['matricula']:
                     linhas[i] = '{:17} | {:^18} | {:^16} | {:>10}\n'.format(*dadosMatricula.values())
                     break

        salvarAlteracao = open("matriculas.txt", "w")
        salvarAlteracao.writelines(linhas)
        salvarAlteracao.close()
        return True
    except ValueError as e:
        print(e)
        return False


def cadastrarTracamentoMatricula(dadosMatriculaDisciplinas,matriculaAluno):
    cadastro = False
    aluno = {}
    for i in range(0,len(dadosMatriculaDisciplinas)):
        disciplina = ControleDisciplina.pesquisaDisciplina(dadosMatriculaDisciplinas[i]['codigo'])
        aluno = ControleAluno.pesquisaAluno(matriculaAluno)
        aluno['disciplinas'] = 0
        aluno['status'] = "TRANCADO"
        dadosMatriculaDisciplinas[i]['status'] = 'TRANCADO'
        disciplina['quantidadeVagas'] = int(disciplina['quantidadeVagas']) + 1
        disciplina['vagasOcupadas'] = int(disciplina['vagasOcupadas']) - 1

        retorno = ControleDisciplina.atualizarDadosDisciplina(disciplina)
        retorno2 = atualizarDadosMatricula(dadosMatriculaDisciplinas[i])


        if retorno == True and retorno2 == True:
            cadastro = True
        else:
            cadastro = False


    retorno3 = ControleAluno.atualizarDadosAluno(aluno)
    if cadastro == True and retorno3 == True:
        return True
    else:
        return False





def listarMatriculasAluno(matricula):
    matriculasDisciplinasAluno = []
    if os.path.isfile('matriculas.txt'):

        arquivo = open("matriculas.txt","r")
        linhas = arquivo.readlines()
        for i in range(0,len(linhas)):
            if i > 1:
                registro = linhas[i].replace("\n","").rsplit("|")
                if registro[1].strip() == matricula:
                    matriculasDisciplinasAluno.append(ControleDisciplina.pesquisaDisciplina(registro[0].strip()))

        return matriculasDisciplinasAluno

    else:
        return False



def listarMatriculasAlunoAdm(matricula):

    matriculasDisciplinasAluno = []
    if os.path.isfile('matriculas.txt'):

        arquivo = open("matriculas.txt","r")
        linhas = arquivo.readlines()

        for i in range(0,len(linhas)):
            registroMatricula = {'codigo': '', 'matricula': '', 'data': '','status': ''}
            if i > 1:
                registro = linhas[i].replace("\n","").rsplit("|")

                if registro[1].strip() == matricula:
                    registroMatricula['codigo'] = registro[0].strip()
                    registroMatricula['matricula'] = registro[1].strip()
                    registroMatricula['data'] = registro[2].strip()
                    registroMatricula['status'] = registro[3].strip()
                    matriculasDisciplinasAluno.append(registroMatricula)

        return matriculasDisciplinasAluno

    else:
        return print("\033[31m"+"=== Nenhum registro encontrado ==="+"\033[0;0m")