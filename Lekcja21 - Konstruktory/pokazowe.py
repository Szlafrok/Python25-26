# Proszę wyłapywać błędy w kodzie!

class Samochod():
    marka = ""
    model = ""
    typSilnika = ""
    mocKM = 0

    def wyswietl(self):
        print(self.marka)
        print(self.model)
        print(self.typSilnika)
        print(self.mocKM)

auto = Samochod()
auto.marka = "Toyota"
auto.model = "Corolla"
auto.typSilnika = "Hybrydowy"
auto.mocKM = 200

auto.wyswietl()
