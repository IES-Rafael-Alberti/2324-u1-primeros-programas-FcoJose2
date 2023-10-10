from src.Ejercicio2_3 import primeraexp
from src.Ejercicio2_3 import segundaexp
from src.Ejercicio2_3 import tercerexp

def test_primeraexp():
    assert primeraexp(17) == "8.5"
def test_segundoexp():
    assert segundaexp(17) == "8"
def test_tercerexp():
    assert tercerexp (12.0) == "4.0"

