while True:
    try:
        liczba1 = int(input("Podaj liczbę 1: "))
        liczba2 = int(input("Podaj liczbę 2: "))
        print(liczba1 + liczba2)
        break
    except Exception as e:
        print("Wpisano nieprawidłową liczbę!") 