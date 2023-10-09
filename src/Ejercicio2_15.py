def interesF(inicial):
    interes = 0.04
    año1 = inicial *(1+interes)
    año2 = año1 *(1+interes)
    año3 = año2 *(1+interes)
    return round(año1, 2), round(año2, 2), round(año3, 2)


    

  

if __name__ == "__main__":
    inicial = float(input("Introduce la cantidad inicial: "))
    año1, año2, año3 = interesF(inicial)
    print("El saldo del primer año es: " + str(año1))
    print("El saldo del segundo año es: " + str(año2))
    print("El saldo del tercer año es: " + str(año3))


   