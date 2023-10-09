def Suma(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

if __name__ == "__main__":
    numeros = [float(input("Introduzca un numero: ")) for _ in range(3)]
    print("La suma es", Suma(numeros))
