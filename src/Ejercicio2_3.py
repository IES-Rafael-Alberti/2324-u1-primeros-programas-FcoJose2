# Suponiendo que se han ejecutado las siguientes sentencias de asignación:
ancho = 17
alto = 12.0
# Para cada una de las expresiones siguientes, intenta adivinar el valor de la expresión y su tipo sin ejecutarlas en el intérprete:
# 1. ancho / 2
# 2. ancho // 2
# 3. alto / 3
# 4. 1 + 2 * 5


# 1. El valor es 8.5 y es float.
# 2. El valor es 8 y es int.
# 3. El valor es 4.0 y es float.
# 4. El valor es 11 y es int.

def primeraexp(ancho):
    resultado1 = ancho / 2
    return str(resultado1)

def segundaexp(ancho):
    resultado2 = ancho // 2
    return str(resultado2)

def tercerexp(alto):
    resultado3 = alto / 3
    return str(resultado3)

if __name__ == "__main__":
    print("El primer resultado es " + primeraexp(ancho))
    print("El segundo resultado es "+ segundaexp(ancho))
    print("El tercer resultado es "+ tercerexp(alto))
