from random import randint

ile_rzutow = int(input())

for i in range(ile_rzutow):
    wynik = randint(1, 6)
    if wynik == 6:
        print(wynik, "TRAFIENIE KRYTYCZNE!")
    else:
        print(wynik)