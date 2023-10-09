def manNombre(nombre):
    nombreMin = nombre.lower()
    nombreMay = nombre.upper()
    nombreCap = nombre.title()
    return nombreMin, nombreMay, nombreCap

if __name__ == "__main__":
    nombre = input("Escribe tu nombre completo: ")
    nombreMin, nombreMay, nombreCap = manNombre(nombre)
    print("Nombre en minusculas: ", nombreMin + "\nNombre en mayusculas: ", nombreMay + "\nNombre capitalizado: " + nombreCap)
    