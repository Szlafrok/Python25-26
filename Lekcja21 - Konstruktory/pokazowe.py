# Proszę wyłapywać błędy w kodzie!

class Samochod():
    marka = ""
    model = ""
    typSilnika = ""
    mocKM = 0

    def __init__(self, marka: str, model: str, typSilnika: str, mocKM: float):
        print("Obiekt został utworzony!")
        self.marka = marka
        self.model = model
        self.typSilnika = typSilnika
        self.mocKM = mocKM

    def wyswietl(self):
        print(self.marka)
        print(self.model)
        print(self.typSilnika)
        print(self.mocKM)

auto = Samochod("Toyota", "Yaris", "Gęsie pióra", 200)

auto.wyswietl()
