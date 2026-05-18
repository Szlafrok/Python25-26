osoba = {
    "imie": "Piotrek",
    "nazwisko": "Polański",
    "wiek": 22,
    "adres": {
        "ulica": "Dry Dry",
        "numer": 5,
        "miasto": "Trzcina Ziemniakowska"
    }
}

print(osoba["nazwisko"])

print(osoba["imie"] + osoba["nazwisko"])

# print(osoba["imie"] + osoba["wiek"]) BŁĄD

print(osoba["adres"])
print(osoba["adres"]["miasto"])

osoba["adres"]["powiat"] = "Ohio-berliński"

print(osoba["adres"]["powiat"])