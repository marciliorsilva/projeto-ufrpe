import os.path
import datetime
#arquivo = open("alunos.txt", "r")
#linhas = arquivo.readlines()
#qtdeColunas = 7
#estrutura = []
#for c in range(0,qtdeColunas,1):
#    lista = []
#    for r in range(0, len(linhas)):
#        registro = linhas[r].rsplit("|")
#        lista.append(registro[c].replace(" ",""))


#    estrutura.append(len(sorted(lista, key=len)[-1]))



#print(estrutura)
#x = '{:10} | {:^40} | {:^1} | {:^10} | {:^10} | {:^2} | {:^10}\n'.format("Matricula","Nome","Sexo","Data de Nascimento","Telefone","Quantidade de Disciplina","Status")
#x+= '-----------+------------------------------------------+------+--------------------+------------+--------------------------+----------\n'
#for i in range(0,len(linhas)):
#    registro = linhas[i].rsplit("|")
#    x += '{:10}|{:^42}|{:^6}|{:^20}|{:^10}|{:^26}|{:>10}'.format(*registro)
#print(x)
from Controle import ControleRelatorio
ControleRelatorio.relatorioAniversariantes(11)
