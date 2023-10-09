#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

def reemplazar(frase, vocal):
    frase = frase.replace(vocal, vocal.upper())
    return frase

if __name__ == "__main__":
    frase = input("Introduce una frase: ")
    vocal = input("Introduce una letra en minusculas: ")
    print(reemplazar(frase, vocal))
