#Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.

def escribir_saludo(nombre):
    return nombre

if __name__=="__main__":
    nombre = input("Escribe tu nombre: ")
    print("Hola, " + escribir_saludo(nombre))