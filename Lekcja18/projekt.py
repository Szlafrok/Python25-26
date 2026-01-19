import random
kosci = [0] * 5 # [0, 0, 0, 0, 0]
nazwy_punktow = ["Jedynki", "Dwójki", "Trójki", "Czwórki", "Piątki", "Szóstki"]
punkty = ["Brak"] * 6 # [-1, -1, -1, -1, -1, -1]

def wypisz_punkty():
    print("______________________")
    for i in range(len(punkty)):
        print(f"{i+1}. {nazwy_punktow[i]}: {punkty[i]}")


def przerzuc_kosci(numery_kosci: str) -> None: # 145
    for nr in numery_kosci:
        indeks = int(nr) - 1
        kosci[indeks] = random.randint(1, 6) 
    return

def wypisz_kosci():
    print("______________________")

    for i in range(len(kosci)):
        print(f"{i+1}. {kosci[i]}")
    
    print("______________________")

def czy_przerzucac_kosci():
    odp = input("Czy przerzucać kości? (t/n)")
    odp = odp.lower()
    return odp == "t"

def wybor_pola():
    odp = int(input("Wybierz pole, na które chcesz wpisać punkty: "))
    if punkty[odp-1] == "Brak":
        return odp
    return 0

przerzuc_kosci("12345")
wypisz_punkty()
wypisz_kosci()
for i in range(2):
    przerzut = czy_przerzucac_kosci()
    if przerzut:
        do_przerzutu = input("Podaj numery kości do przerzutu (bez spacji): ")
        przerzuc_kosci(do_przerzutu)
        wypisz_punkty()
        wypisz_kosci()
    else:
        break
wybor = 0
while wybor == 0:
    wybor = wybor_pola()