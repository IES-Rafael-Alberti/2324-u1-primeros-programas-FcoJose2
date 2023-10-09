#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

def nombreRep(nombre, numero):
    resultado = nombre * numero
    return resultado


if __name__ == "__main__":
    nombre = input("Introduzca su nombre: ")
    numero = int(input("Introduzca las veces que se va a repetir: "))
    print(nombreRep(nombre, numero))