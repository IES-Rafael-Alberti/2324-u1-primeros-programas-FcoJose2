from src.Ejercicio2_11 import sumaF

def test_sumaF():
    assert sumaF(5) == 15
    assert sumaF(-1) == "El numero tiene que ser positivo"
