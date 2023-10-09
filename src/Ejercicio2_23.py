#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

def extension(correo):
    correo = correo[:correo.find('@')] + '@ceu.es'
    return correo

if __name__ == "__main__":
    correo = input("Introduce tu correo: ")
    print(extension(correo))