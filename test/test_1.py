from src.Ejercicio2_1 import escribir_saludo

def test_escribir_saludo():
    nombre = "Juan"
    assert escribir_saludo(nombre) == "Juan"