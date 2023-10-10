from src.Ejercicio2_6 import DescubrirIVA

def test_DescubrirIVA():
    assert DescubrirIVA(32) == "El precio sin IVA es de 29.09\nEl precio del IVA es de 2.91"