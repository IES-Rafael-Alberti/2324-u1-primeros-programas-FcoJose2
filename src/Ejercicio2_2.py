#Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.
def calculo_importe (horas, coste):
    importe = horas * coste
    return importe

if __name__=="__main__":
    horas = int(input("Introduce el número de horas: "))
    coste = int(input("Introduce el coste por hora: "))

    print("Importe total: " + str(calculo_importe(horas, coste)))
