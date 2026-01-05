def glowne_menu():
    print("Wybierz opcję menu:")
    print("1. Wpłata")
    print("2. Wypłata")
    print("3. Sprawdzenie stanu konta")
    print("4. Zakończenie aplikacji")

    # Proszę uzupełnić tę funkcję w taki sposób, aby wypisywała ona pytanie do użytkownika
    # co chce zrobić oraz opcje 1-4: Wypłata, wpłata, sprawdzenie stanu konta, zakończenie aplikacji.

def wczytaj_dane(zapytanie) -> int:
    return int(input(zapytanie))
    # Proszę uzupełnić tę funkcję w ten sposób, aby zwracała wartość opcji wpisanej przez użytkownika

def wypisz_stan_konta(saldo):
    print(f"Aktualny stan konta: {saldo} zł")
    # Proszę wypisać aktualny stan konta w formacie: "Aktualny stan konta: XX zł"
    # Proszę zastosować format f-string: f"{}"

def wyplata_pieniedzy(saldo, wartosc): # Funkcja przyjmuje argumenty i zwraca NOWE SALDO
    if wartosc > saldo:
        print("Nie możesz tyle wypłacić - za mało pieniędzy!")
        return saldo
    print(f"Wypłacono {wartosc} zł!")
    nowe_saldo = saldo - wartosc
    wypisz_stan_konta(nowe_saldo)
    return nowe_saldo

def wplata_pieniedzy(saldo, wartosc):
    print(f"Wpłacono {wartosc} zł!")
    nowe_saldo = saldo + wartosc
    wypisz_stan_konta(nowe_saldo)
    return nowe_saldo

# Proszę:
# 1. Uzupełnić kod do aktualnej formy (+)
# 2. Napisać funkcję wplata_pieniedzy(saldo, wartosc), która zwraca nowe saldo i wypisuje odpowiednie
#    informacje podobnie jak funkcja wplata_pieniedzy (++)
# 3. Proszę odpowiednio zastosować tę funkcję w głównej pętli projektu (czyli pętli while) (+)


wybor = 0
saldo = 0

while True:
    glowne_menu()
    wybor = wczytaj_dane("Podaj wybór: ")

    if wybor == 1:
        wartosc = wczytaj_dane("Podaj wartość: ")
        saldo = wplata_pieniedzy(saldo, wartosc)
    elif wybor == 2:
        wartosc = wczytaj_dane("Podaj wartość: ")
        saldo = wyplata_pieniedzy(saldo, wartosc)
    elif wybor == 3:
        wypisz_stan_konta(saldo)
    elif wybor == 4:
        print("Aplikacja została zamknięta!")
        break
    else:
        print("Niepoprawny wybór!")
    print()




# (Można skorzystać z czatu GPT, ale trzeba to dorzbe wytłumaczyć) 
# Jaka struktura danych mogłaby przechowywać kursy 
# walut w naszym projekcie (++)

waluty = {"zl": 1, 
          "dolar": 4,
          "euro": 5}

print(waluty["dolar"])