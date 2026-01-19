import random
kosci = [0] * 5 # [0, 0, 0, 0, 0]
nazwy_punktow = ["Jedynki", "Dwójki", "Trójki", "Czwórki", "Piątki", "Szóstki"]
punkty = [-1] * 6 # [-1, -1, -1, -1, -1, -1]

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


przerzuc_kosci("12345")
wypisz_punkty()
wypisz_kosci()