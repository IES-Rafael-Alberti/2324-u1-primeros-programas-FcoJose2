from src.Ejercicio2_19 import contarYMay

def test_contarYMay():
    nombre = "fran"
    prueba = contarYMay(nombre)
    assert prueba == "Su nombre es FRAN que tiene 4 letras."