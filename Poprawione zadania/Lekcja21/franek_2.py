from math import sqrt

class Prostokat():

    def __init__ (self, a: float,b: float):
        self.a = a
        self.b = b 
    def obwod (self):
        return 2 * self.a + 2 * self.b
    def pole (self):
        return self.a * self.b 

# Poniższy kod miałeś wcięty o 1 wcięcie w głąb, czyli zamiast

# kod
# kod 
# kod

# miałeś

#   kod
#   kod
#   kod

# To sprawiało, że kod był wewnątrz klasy. Wyciągnąłem go z powrotem, teraz działa ;)

figura1 = Prostokat(3, 5)
print(figura1.obwod())
print(figura1.pole())