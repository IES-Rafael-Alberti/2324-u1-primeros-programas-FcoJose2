from src.Ejercicio2_18 import manNombre

def test_manNombre():
    nombre = "fco jose"
    nombreMin, nombreMay, nombreCap = manNombre(nombre)
    assert nombreMin == "fco jose"
    assert nombreMay == "FCO JOSE"
    assert nombreCap == "Fco Jose"