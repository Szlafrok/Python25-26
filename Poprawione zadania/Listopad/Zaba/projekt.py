# Jeszcze nie poprawiłem tego zadania jakby co

#Projekt P1
from random import randint # import polecenia

from time import time # import polecenia
czas_startu = time()#zapisuje czas startu


losowa_1 = randint(1, 10) # Losuje losową liczbę dla rundy 1
losowa_2 = randint(1, 10) # Losuje losową liczbę dla rundy 1
print("Runda 1:")
print(f"{losowa_1}-{losowa_2}")#pytanie runda 1
odpowiedz = int(input("Wprowadź odpowieź do rundy 1:  "))#Wprowadzenie odpowiedzi
if losowa_1 - losowa_2 == odpowiedz:#Sprawdzenie czy odpowiedź jest poprawna
    print("To poprawna odpowiedź")
else:
    print("Popełniłeś/aś jakiś błąd(przegrałeś)")
    exit()
print()#odstęp


losowa_1 = randint(1, 10) # Losuje losową liczbę dla rundy 2
losowa_2 = randint(1, 10) # Losuje losową liczbę dla rundy 2
print("Runda 2:")
print(f"{losowa_1}+{losowa_2}")#pytanie runda 2
odpowiedz = int(input("Wprowadź odpowieź do rundy 2:  "))#Wprowadzenie odpowiedzi
if losowa_1 + losowa_2 == odpowiedz:#Sprawdzenie czy odpowiedź jest poprawna
    print("To poprawna odpowiedź!")
else:
    print("Popełniłeś/aś jakiś błąd(przegrałeś/aś)")
    exit()
print()#odstęp


losowa_1 = randint(1, 10) # Losuje losową liczbę dla rundy 3
losowa_2 = randint(1, 10) # Losuje losową liczbę dla rundy 3
print("Runda 3:")
print(f"{losowa_1}*{losowa_2}")#pytanie runda 3
odpowiedz = int(input("Wprowadź odpowieź do rundy 3:  "))#Wprowadzenie odpowiedzi
if losowa_1 * losowa_2 == odpowiedz:#Sprawdzenie czy odpowiedź jest poprawna
    print("To poprawna odpowiedź!")
else:
    print("Popełniłeś/aś jakiś błąd(przegrałeś/aś)")
    exit()
print()#odstęp

losowa_1 = randint(1, 10) # Losuje losową liczbę dla rundy 4
losowa_2 = randint(1, 10) # Losuje losową liczbę dla rundy 4
print("Runda finałowa:")
print(f"podaj resztę z dzielenia {losowa_1} przez {losowa_2}")#pytanie runda 3
odpowiedz = int(input("Wprowadź odpowieź do rundy finałowej:  "))#Wprowadzenie odpowiedzi
if losowa_1 % losowa_2 == odpowiedz:#Sprawdzenie czy odpowiedź jest poprawna
    print("To poprawna odpowiedź! Wygrałeś!!!")
else:
    print("Popełniłeś/aś jakiś błąd(przegrałeś/aś)")
    exit()


czas_końca = time()#zapisuje czas końca
print(f"Twój czas wynosi:{(czas_końca-czas_startu)} sekund")#mierzy czas przeprowadzenia operacji i podaje je 
