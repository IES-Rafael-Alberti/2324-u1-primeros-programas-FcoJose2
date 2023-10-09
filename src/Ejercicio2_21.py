#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
def invertidaF(frase):
    frase = frase[::-1]
    return "La frase invertida es: " +  frase

if __name__ == "__main__":
    frase = input("Introduzca una frase: ")
    print(invertidaF(frase))
