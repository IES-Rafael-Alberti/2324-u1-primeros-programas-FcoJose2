from src.Ejercicio2_2 import calculo_importe

def test_calculo_importe():
    assert calculo_importe(8, 10) == 80
    assert calculo_importe(5, 7) == 35