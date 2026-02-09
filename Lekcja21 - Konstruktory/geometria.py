from math import sqrt

class TrojkatRownoboczny():

    def __init__(self, a: float):
        self.a = a

    def obwod(self):
        return 3 * self.a
    
    def pole(self):
        return self.a**2 * sqrt(3) / 4
    
trojkat = TrojkatRownoboczny(5)
print(trojkat.obwod())
print(trojkat.pole())

# Proszę utworzyć klasę prostokąt i utworzyć w niej
# - konstruktor, w którym podajemy jego wymiary
# - metodę obwod(), która zwraca jego obwód
# - metodę pole(), która zwraca jego pole
# Proszę następnie przetestować tę klasę (+++)

# Alternatywnie (+++++)
# Proszę przygotować taką klasę dla figury KOŁO.
# Proszę wykorzystać stałą matematyczną pi
# Wzór na obwód koła: 2 * pi * r
# Wzór na pole koła: pi * r**2

class Prostokat():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def obwod(self):
        return self.a * 2 + self.b * 2 # 2 * (self.a + self.b)
    
    def pole(self):
        return self.a * self.b
    
from math import pi
class Kolo():
    def __init__(self, promien):
        self.promien = promien

    def obwod(self):
        return 2 * pi * self.promien
    
    def pole(self):
        return pi * self.promien**2
    
figura1 = Prostokat(3, 5)
print(figura1.obwod())
print(figura1.pole())

figura2 = Kolo(5)
print(figura2.obwod())
print(figura2.pole())