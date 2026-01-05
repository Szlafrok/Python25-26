def glowne_menu():
    print("Wybierz opcję menu:")
    print("1. Wpłata")
    print("2. Wypłata")
    print("3. Sprawdzenie stanu konta")
    print("4. Zakończenie aplikacji")

    # Proszę uzupełnić tę funkcję w taki sposób, aby wypisywała ona pytanie do użytkownika
    # co chce zrobić oraz opcje 1-4: Wypłata, wpłata, sprawdzenie stanu konta, zakończenie aplikacji.

def wczytaj_dane() -> int:
    return int(input("Wprowadź wybór: "))
    # Proszę uzupełnić tę funkcję w ten sposób, aby zwracała wartość opcji wpisanej przez użytkownika

wybor = 0
saldo = 0

while True:
    glowne_menu()
    wybor = wczytaj_dane()

    if wybor == 1:
        pass
    elif wybor == 2:
        pass
    elif wybor == 3:
        pass
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