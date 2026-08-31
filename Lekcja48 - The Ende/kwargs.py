def info_miasto(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

info_miasto(miasto = "Rzeszów", kraj = "Polska", fajny = True)

# (++) Proszę napisać inną przykładową funkcję z wykorzystaniem **kwargs
#      i napisać jej przykładowe wywołanie

def statystyki(**srednia):
    klucze = list(srednia.keys())
    print(klucze)

    wartosc = sum(srednia.values()) / len(srednia.values())
    print(wartosc)

statystyki(hp = 5, moc = 10)