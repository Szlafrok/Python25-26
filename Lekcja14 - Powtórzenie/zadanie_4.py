miesiac = int(input("Podaj miesiąc: "))
#ceny = [50, 50, 100, 100, 200, 200, 250, 200, 200, 100, 100, 50]

if miesiac == 1 or miesiac == 2 or miesiac == 12:
    cena = 50
elif miesiac == 3 or miesiac == 4 or miesiac == 10 or miesiac == 11:
    cena = 100
elif miesiac == 5 or miesiac == 6 or miesiac == 8 or miesiac == 9:
    cena = 200
elif miesiac == 7:
    cena = 250
else:
    print("NIEPOPRAWNY MIESIĄC")
    exit()

bilety = int(input("Podaj liczbę biletów: "))
print(f"Zapłacisz {bilety * cena}")