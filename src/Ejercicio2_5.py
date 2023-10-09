# Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.

def calcularpreciofinal(precio, iva):
    precioiva = precio * iva
    preciofinal = precio + precioiva
    return "El precio final es " + str(preciofinal)

if __name__ == "__main__":
    precio = float(input("Escriba el precio sin IVA: "))
    iva = float(input("Escriba el IVA que va a ser aplicado: "))
    print(calcularpreciofinal(precio, iva))
