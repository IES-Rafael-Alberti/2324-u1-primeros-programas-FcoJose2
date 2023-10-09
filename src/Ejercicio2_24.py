#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

def separar(precio):
    euros, centimos = str(precio).split(".")
    return euros, centimos

if __name__ == "__main__":
    precio = float(input("Introduce el precio: "))
    euros, centimos = separar(precio)
    print(euros, "euros y", centimos, "centimos")