zero = ["0", "zero", "zera", "zerem"]
jeden = ["1", "jeden", "jedynkę", "jedynka", "jednego", "jedynką"]
plus = ["+", "dodaj", "dodawanie", "dodać", "plus"] # tego komentarza już w liście nie ma

baza = [zero, jeden, plus]

# print(baza[2])
# plus.append("dodawaj")
# print(baza[2])

dzialanie = ""
tekst = input("Podaj treść działania: ")

print(tekst)
print(tekst.split(" "))

def przetlumacz_slowo(slowo):
    for wyrazenie in baza:
        if slowo in wyrazenie:
            return wyrazenie[0]
    return ""

def oblicz_z_tekstu(tekst: str):
    wynik = None
    liczba = ''
    operacja = ''
    for znak in tekst:
        if znak.isdigit():
            liczba += znak # konkatenacja
        else:
            if wynik == None:
                wynik = int(liczba)
                operacja += znak
            else:
                pass



for slowo in tekst.split(" "):
    dzialanie += przetlumacz_slowo(slowo)

print(dzialanie)