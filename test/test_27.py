from src.Ejercicio2_27 import formato

def test_formato():
    assert formato("Prueba",12.34,2) == "Prueba:   2 unidades x     12.34€ =       24.68€"