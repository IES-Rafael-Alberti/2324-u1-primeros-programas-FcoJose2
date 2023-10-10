# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

def eliminar(telefono):
    telefono = telefono[4:-3]
    return str(telefono)

if __name__ == "__main__":
    telefono = input("Inserte el numero de telefono: ")
    print("El numero de telefono es " + eliminar(telefono))