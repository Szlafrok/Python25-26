zero = ["0", "zero", "zera", "zerem"]
jeden = ["1", "jeden", "jedynka", "jednego", "jednej", "jedynkę", "jedynką"]
dwa = ["2", "dwa", "dwójka", "dwóch", "dwie", "dwójkę", "dwójką"]
trzy = ["3", "trzy", "trójka", "trzech", "trójkę", "trójką"]
cztery = ["4", "cztery", "czwórka", "czterech", "czwórkę", "czwórką"]
piec = ["5", "pięć", "piątka", "pięciu", "piątkę", "piątką"]
szesc = ["6", "sześć", "szóstka", "sześciu", "szóstkę", "szóstką"]
siedem = ["7", "siedem", "siódemka", "siedmiu", "siódemkę", "siódemką"]
osiem = ["8", "osiem", "ósemka", "ośmiu", "ósemkę", "ósemką"]
dziewiec = ["9", "dziewięć", "dziewiątka", "dziewięciu", "dziewiątkę", "dziewiątką"]
dziesiec = ["10", "dziesięć", "dziesiątka", "dziesięciu", "dziesiątkę", "dziesiątką"]
jedenascie = ["11", "jedenaście", "jedenastka", "jedenastu"]
dwanascie = ["12", "dwanaście", "dwunastka", "dwunastu"]
trzynascie = ["13", "trzynaście", "trzynastka", "trzynastu"]
czternascie = ["14", "czternaście", "czternastka", "czternastu"]
pietnascie = ["15", "piętnaście", "piętnastka", "piętnastu"]
szesnascie = ["16", "szesnaście", "szesnastka", "szesnastu"]
siedemnascie = ["17", "siedemnaście", "siedemnastka", "siedemnastu"]
osiemnascie = ["18", "osiemnaście", "osiemnastka", "osiemnastu"]
dziewietnascie = ["19", "dziewiętnaście", "dziewiętnastka", "dziewiętnastu"]
dwadziescia = ["20", "dwadzieścia", "dwudziestka", "dwudziestu"]

plus = ["+", "plus", "dodaj", "dodać", "dodawanie", "suma"]
minus = ["-", "minus", "odejmij", "odjąć", "odejmowanie", "różnica"]
razy = ["*", "x", "razy", "pomnóż", "pomnożyć", "mnożenie", "iloczyn"]
podziel = ["/", "÷", "podziel", "podzielić", "dzielenie", "iloraz"]

baza = [
    zero, jeden, dwa, trzy, cztery, piec, szesc, siedem, osiem, dziewiec,
    dziesiec, jedenascie, dwanascie, trzynascie, czternascie,
    pietnascie, szesnascie, siedemnascie, osiemnascie,
    dziewietnascie, dwadziescia,
    plus, minus, razy, podziel
]


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

def oblicz(liczba1, liczba2, operator):
    if operator == '+':
        return liczba1 + liczba2
    elif operator == '-':
        return liczba1 - liczba2
    elif operator == '/':
        return liczba1 / liczba2
    elif operator == '*':
        return liczba1 * liczba2 # d       p      5p2 = 5**2 = 25
    else:
        raise Exception(f"Niepoprawna operacja: {operator}")

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
                operacja = znak
                liczba = ''
            else:
                wynik = oblicz(wynik, int(liczba), operacja)
                liczba = ''
                operacja = znak
    if liczba:
        wynik = oblicz(wynik, int(liczba), operacja)
    return wynik



for slowo in tekst.split(" "):
    dzialanie += przetlumacz_slowo(slowo)

print(dzialanie)
print(oblicz_z_tekstu(dzialanie))