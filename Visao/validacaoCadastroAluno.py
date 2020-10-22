def validarNome(nome):
    retorno = True
    for i in range(0,len(nome)):
        if nome[i].isnumeric() == True:
           retorno = False

    return retorno

def validarSexo(sexo):

    if (sexo.upper() == "F" or sexo.upper() == "M") or sexo.isalpha == True:
        return True
    else:
        return print("\033[31m"+"Sexo invalido."+ "\033[0;0m")



def validarTelefone(telefone):

    if (len(telefone) < 10 or len(telefone) < 10) or telefone.isnumeric() == False:
        return print("\033[31m"+"Telefone invalido."+ "\033[0;0m")
    else:
        return True


def validarData(data):
    quantidadeBarra = data.count("/")

    if len(data) < 10 or len(data) > 10:
        return print("\033[31m"+"Tamanho incorreto."+ "\033[0;0m")

    else:
        if quantidadeBarra == 2:

            try:
                ano = int(data[:4])
                mes = int(data[5:7])
                dia = int(data[-2:])

                if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:

                    if dia <= 31:

                        return True
                    else:
                        return print("\033[31m"+"Dia invalido"+ "\033[0;0m")

                # Meses com 30 dias
                elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                    if dia <= 30:

                        return True
                    else:

                        return print("\033[31m"+"Dia Invalido"+ "\033[0;0m")

                elif mes == 2:


                    # Testa se é bissexto
                    if (ano % 4 == 0 and ano % 400 != 0) or (ano % 400 == 0):

                         if (dia <= 29):

                            return True
                         else:
                            return print("\033[31m"+"Ano é Bissexto! Dia invalido"+ "\033[0;0m")

                    elif (dia <= 28):

                        return True
                    else:
                        return print("\033[31m"+"Dia invalido"+ "\033[0;0m")
                else:
                    return print("\033[31m"+"Mes invalido" + "\033[0;0m")

            except:
                print("\033[31m"+"Ano invalido."+ "\033[0;0m")

        else:
               return print("\033[31m"+"Nao tem duas barras."+ "\033[0;0m")


def finalizarCadastroAluno(opcao):
    try:
        a = int(opcao)
        if a >= 3:
            return print("\033[31m"+"========== Opção invalida ============="+"\033[0;0m")
        else:
            return True
    except:
        return print("\033[31m"+"========== Opção invalida ============="+"\033[0;0m")
