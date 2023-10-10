from src.Ejercicio2_25 import formato

def test_formato():
    assert formato("2/12/2004") == ("2", "12", "2004")