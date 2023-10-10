from src.Ejercicio2_3 import primeraexp
from src.Ejercicio2_3 import segundaexp
from src.Ejercicio2_3 import tercerexp

def test_primeraexp():
    assert primeraexp(17) == "El primer resultado es 8.5"
def test_segundoexp():
    assert segundaexp(17) == "El segundo resultado es 8"
def test_tercerexp():
    assert tercerexp (12.0) == "El tercer resultado es 4.0"

