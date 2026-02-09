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
auto1 = Samochod("Honda", "Civic", "Wodór", 10)
auto2 = Samochod("Honda", "Civic", "Wodór", 10)
auto3 = Samochod("Toyota", "Civic", "Wodór", 10)
auto4 = Samochod("Honda", "Civic", "Wodór", 10)

print(auto1.marka)
print(auto3.marka)

print(Samochod.licznik)