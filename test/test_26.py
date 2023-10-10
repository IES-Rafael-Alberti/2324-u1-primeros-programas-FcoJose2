from src.Ejercicio2_26 import separar

def test_separar():
    assert separar("galletas,naranjas,platanos,natillas") == "galletas\nnaranjas\nplatanos\nnatillas"
