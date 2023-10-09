#Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).
iva = 0.10
def DescubrirIVA(PrecioFinal):
    PrecioSinIVA = PrecioFinal / (1 + iva)
    PrecioIVA = PrecioFinal - PrecioSinIVA
    PrecioIVA = round(PrecioIVA, 2)
    PrecioSinIVA = round(PrecioSinIVA, 2)
    return "El precio sin IVA es de " + str(PrecioSinIVA) + "\nEl precio del IVA es de " + str(PrecioIVA)

if __name__ == "__main__":
    PrecioFinal = float(input("Escriba el precio final del producto: "))
    print(DescubrirIVA(PrecioFinal))