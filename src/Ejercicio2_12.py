# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.

def IMC(peso, altura):
    resultado = round(float(peso)/(float(altura)**2),2)
    return "Su IMC es: " + str(resultado)
 
if __name__ == "__main__":
    peso = input("Introduzca su peso: ")
    altura = input("Introduzca su altura: ")
    print(IMC(peso, altura))
