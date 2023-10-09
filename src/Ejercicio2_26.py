#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

def separar(lista):
    lista = lista.replace(',', '\n')
    return lista

if __name__ == "__main__":
    lista = input("Introduce los productos separados por comas: ")
    print(separar(lista))