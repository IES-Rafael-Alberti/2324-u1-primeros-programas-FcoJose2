# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.

def precioPanF(cantPanNoDia):
    precioPan = 3.49
    descuento = 0.6

    prePanNoDia = precioPan * descuento
    precioTotal = (precioPan - prePanNoDia) * cantPanNoDia
    precioTotal = round(precioTotal, 2)
    return precioPan, descuento, precioTotal

if __name__ == "__main__":
    cantPanNoDia = int(input("Introduzca el numero de barras que no son de hoy: "))
    precioPan, descuento, precioTotal = precioPanF(cantPanNoDia)
    print("Precio de una barra de pan de hoy: ", str(precioPan) + "\nDescuento por ser de ayer: ", str(descuento) + "\nPrecio total del pan de ayer: ", str(precioTotal))

