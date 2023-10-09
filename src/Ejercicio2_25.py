#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

def formato(fecha):
    dia = fecha[:fecha.find("/")]
    mesaño = fecha[fecha.find("/")+1:]
    mes = mesaño[:mesaño.find("/")]
    año = mesaño[mesaño.find("/")+1:]
    return dia, mes, año

if __name__ == "__main__":
    fecha = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")
    dia, mes, año = formato(fecha)
    print("Día: ", dia)
    print("Mes: ", mes)
    print("Año: ", año)

    

