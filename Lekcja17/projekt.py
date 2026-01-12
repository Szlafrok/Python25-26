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

for slowo in tekst.split(" "):
    dzialanie += przetlumacz_slowo(slowo)

print(dzialanie)