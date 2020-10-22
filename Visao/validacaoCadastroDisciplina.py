def validarHorario(horario):
    if len(horario) > 5:
        return print("\033[31m"+"Tamanho do horario invalido"+ "\033[0;0m")
    else:


            ok = False
            horas = horario[:2]
            minutos = horario[-2:]

            if horas.isnumeric() == True and int(horas) < 24:
                if ":" in horario:
                    if minutos.isnumeric() == True and int(minutos) < 59:
                        ok = True
                    else:
                        return print("\033[31m" + "Minutos invalido" + "\033[0;0m")
                else:
                    return print("\033[31m" + "Horario invalido. Falta o ':'" + "\033[0;0m")

            else:
                return print("\033[31m" + "Hora invalida" + "\033[0;0m")


            if ok == True:

                return True

