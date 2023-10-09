# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.

def CaF(celsius):
    farenheit = (celsius * 9/5)+32
    return "La temperatura en Farenheit es " +str(farenheit)

if __name__ == "__main__":
    celsius = float(input("Escriba la temperatura en Celsius: "))
    resultado = CaF(celsius)
    print(resultado)