# Przypomnienie
zmienna = 5
if zmienna == 5:
    print("zmienna wynosi 5")
else:
    print("Zmienna nie wynosi 5")

d = 0

while d <= 4:
    print("Kaczka zabiła kaczkę kebabem a jajko pacmana")
    d += 1

# print("Kaczka zabiła kaczkę kebabem a jajko pacmana")
# print("Kaczka zabiła kaczkę kebabem a jajko pacmana")
# print("Kaczka zabiła kaczkę kebabem a jajko pacmana")
# print("Kaczka zabiła kaczkę kebabem a jajko pacmana")
# print("Kaczka zabiła kaczkę kebabem a jajko pacmana")

import time

# sekundy = int(input("Podaj liczbę sekund: "))

# while sekundy > 0:
#     print(f"{sekundy}...")
#     time.sleep(1)
#     sekundy -= 1
# print("KABOOM!")


MINIMUM = 1
MAXIMUM = 100

from random import randint

popr_odp = randint(MINIMUM, MAXIMUM)

odp = int(input("Wprowadź swoją odpowiedź: "))

while not odp == popr_odp:
    if odp > popr_odp:
        print("Liczba za wysoka!")
    else:
        print("Liczba za niska")
    odp = int(input("Wprowadź swoją odpowiedź: "))

# ZADANIE SAMODZIELNE

# Proszę dodać licznik odpowiedzi, który będzie liczył ile razy
# gracz zgadywał i na końcu wypiszę informację o liczbie zgadnięć.