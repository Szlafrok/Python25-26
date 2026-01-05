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