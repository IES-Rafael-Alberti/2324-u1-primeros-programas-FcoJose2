#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética

def resultado():
    resop = ((3+2) / (2*5))**2
    return str(resop)

if __name__ == "__main__":
    print("El resultado de la operación es " + resultado())