#Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma.

def Suma(numeroUno, numeroDos, numeroTres):
    ResultadoSuma = numeroUno + numeroDos + numeroTres
    return str(ResultadoSuma)

if __name__=="__main__":
    numeroUno = float(input("Introduzca el primer numero: "))
    numeroDos = float(input("Introduzca el segundo numero: "))
    numeroTres = float(input("Introduzca el tercer numero: "))
    ResultadoSuma = Suma(numeroUno, numeroDos, numeroTres)
    print("El resultado de la suma es " + Suma(numeroUno, numeroDos, numeroTres))