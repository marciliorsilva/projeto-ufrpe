import datetime
from Controle import ControleAluno
def relatorioAlunos():
    arquivo = open("alunos.txt","r")
    linhas = arquivo.readlines()
    linhas.sort()
    relatorio = []
    for i in range(0,len(linhas)):
        if i > 2:
            relatorio.append(linhas[i])


    return relatorio

def relatorioAniversariantes(mes):
    arquivo = open("alunos.txt", "r")
    linhas = arquivo.readlines()

    aniversariantesMes = []
    for i in range(0,len(linhas)):
        if i > 1:
            registro = linhas[i].replace("\n","").split("|")
            for r in range(0,len(registro)):
                if r == 3:
                    data = registro[r].strip().replace("/","-")
                    conversaoData = datetime.datetime.strptime(data, '%Y-%m-%d')
                    if conversaoData.month == int(mes):
                        registroAluno = {'matricula': '', 'nome': '', 'sexo': '', 'data': '', 'telefone': '', 'disciplinas': '','status': ''}
                        registroAluno['matricula'] = registro[0].strip()
                        registroAluno['nome'] = registro[1].strip()
                        registroAluno['sexo'] = registro[2].strip()
                        registroAluno['data'] = registro[3].strip()
                        registroAluno['telefone'] = registro[4].strip()
                        registroAluno['disciplinas'] = registro[5].strip()
                        registroAluno['status'] = registro[6].strip()
                        aniversariantesMes.append(registroAluno)

    relatorio = sorted(aniversariantesMes,key=lambda k: k['data'])
    return relatorio

def relatorioDisciplinaPorAluno(codigo):

    arquivo = open("matriculas.txt","r")
    linhas = arquivo.readlines()
    relatorio = []

    for i in range(0,len(linhas)):
        registro = linhas[i].replace(" ","").split("|")

        if registro[0].strip() == codigo:
            dadosAluno = ControleAluno.pesquisaAluno(registro[1].strip())
            relatorio.append(dadosAluno)

    return relatorio


