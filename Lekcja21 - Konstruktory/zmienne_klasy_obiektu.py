class Samochod():
    licznik = 0
    marka = "pusto"
    model = ""
    typSilnika = ""
    mocKM = 0

    def __init__(self, marka: str, model: str, typSilnika: str, mocKM: float):
        print("Obiekt został utworzony!")
        Samochod.licznik += 1
        self.marka = marka
        self.model = model
        self.typSilnika = typSilnika
        self.mocKM = mocKM

    def wyswietl(self):
        print(self.marka)
        print(self.model)
        print(self.typSilnika)
        print(self.mocKM)

print(Samochod.marka)
auto = Samochod("Honda", "Civic", "Wodór", 10)
auto = Samochod("Honda", "Civic", "Wodór", 10)
auto = Samochod("Honda", "Civic", "Wodór", 10)
auto = Samochod("Honda", "Civic", "Wodór", 10)
print(Samochod.licznik)