# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario en mayúsculas y n es el número de letras que tienen el nombre.

def contarYMay(nombre):
    nombre = nombre.upper()
    letras = len(nombre)
    return "Su nombre es " + str(nombre) + " que tiene " + str(letras) + " letras."

if __name__ == "__main__":
    nombre = input("Introduzca su nombre: ")
    print(contarYMay(nombre))


