# ¿Es posible escribir el programa del ejercicio 1.7 sin usar variables? Inténtalo.

def Suma(suma):
    suma = int(input("Introduzca el primer numero: ")) + int(input("Introduzca el segundo numero: ")) + int(input("Introduzca el tercer numero: "))
    return "La suma de los numeros es " + str(suma)

if __name__ == "__main__":
    print(Suma(Suma))