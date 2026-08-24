def funkcja(*args):
    wynik = 0
    for element in args:
        wynik += element
    return wynik

print(funkcja(1, 2, 3, 50))