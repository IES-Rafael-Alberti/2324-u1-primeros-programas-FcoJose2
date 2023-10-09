#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética

def resultado():
    resop = ((3+2) / (2*5))**2
    return "El resultado de la operación es " + str(resop)

if __name__ == "__main__":
    print(resultado())