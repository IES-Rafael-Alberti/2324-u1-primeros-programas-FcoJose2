# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: "la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario, y c y r son el cociente y el resto de la división entera respectivamente.

def division(dividendo, divisor):
    if divisor == 0:
        return "No se puede dividir entre 0"
    else:
        cociente = dividendo // divisor
        resto = dividendo % divisor
        resultado = "La división da un cociente de " + str(cociente) + " y un resto de " + str(resto)
        return resultado 

if __name__ == "__main__":
    dividendo = int(input("Introduzca el primer numero entero: "))
    divisor = int(input("Introduzca el segundo numero entero: "))
    print(division(dividendo, divisor))