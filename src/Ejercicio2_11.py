#Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:

def sumaF(numero):
    if numero < 0:
        return "El numero tiene que ser positivo"
    suma = 0
    for i in range(1, numero + 1):
        suma += i
    return suma

if __name__ == "__main__":
    numero = int(input("Introduzce un numero: "))
    print("La suma de los enteros es: " + str(sumaF(numero)))
    

   