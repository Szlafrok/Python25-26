#L6-1
a = 3
b = 4
c = 5

# Ciekawostka: Mógłbyś zrobić:
if not c >= b >= a:
    raise Exception("Podane dane nie są w kolejności rosnącej!")

if a + b > c:
    print("Można") 
else:
    print("Nie można") # OK


#zadanie dodatkowe
if a >= b and a >= c:
    if b + c > a:
        print("Można")
    else:
        print("Nie można")
elif b >= a and b >= c:
    if c + a > b:
        print("Można")
    else:
        print("Nie można")
elif c >= a and c >= b:
    if b + a > c:
        print("Można")
    else:
        print("Nie można") # +2p :D

# 5 / 5

#L7-1
"""
aby odgadnąć liczbę w jak najmniejszej ilości prób znajdujemy środek zakresu i dzielimy zakres na 2 i od nowa
np. mamy zakres 1-100 to wpisujemy 50, 1 - 50 wpisujemy 25
Algorytm to wyszukiwanie binarne(Binary search)
"""
# Tak jest! 1 / 1



#L8-1
wysokosc = int(input("Podaj wysokość: "))
if wysokosc % 2 == 0:
    for pion in range(1, wysokosc + 1):
        for poziom in range(1, wysokosc + pion):
            if wysokosc - pion >= poziom:
                print(end = " ")
            elif pion % 2 == 1:
                if poziom % 2 == 0:
                    print(end = "*")
                else:
                    print(end = " ")
            else:
                if poziom % 2 == 1:
                    print(end = "*")
                else:
                    print(end = " ")
        print()
else:
    for pion in range(1, wysokosc + 1):
        for poziom in range(1, wysokosc + pion):
            if wysokosc - pion >= poziom:
                print(end = " ")
            elif pion % 2 == 1:
                if poziom % 2 == 0:
                    print(end = " ")
                else:
                    print(end = "*")
            else:
                if poziom % 2 == 1:
                    print(end = " ")
                else:
                    print(end = "*")
        print()

# Rozwiązanie poprawne, ale bardzo skomplikowane!
# Bardzo duża część logiki się powtarza. Da się to rozumieć, ale ciężko się w tym rozeznać.
# Przede wszystkim zauważ, że możesz wypisywać znaki parami - po gwiazdce zawsze wystąpi
# spacja. To powinno bardzo uprościć rozwiązanie. Wersję skróconą zapisałem w pliku
# alt8-1.py, który Ci odsyłam :)

# 4 / 4

#L8-1
czy_pusty = input("Podaj czy ma być puste(Tak lub Nie): ").lower()
wysokosc = int(input("Podaj wysokość: "))
szerokosc = int(input("Podaj szerokość: "))
if czy_pusty == "tak":
    czy_pusty = True
elif czy_pusty == "nie":
    czy_pusty = False
else:
    print("BŁĄD-1") # Polecam zainteresować się słowem kluczowym "raise" ;)
    exit()
if czy_pusty == True: 
    print(end = "■"*szerokosc) # Działa, ale jest trochę brzydkie i psuje czytelność!
    print()
    for sciana in range(wysokosc-2):
        print(end = "■")
        print(end = " " * (szerokosc - 2))
        print(end = "■")
        print()
    print(end = "■"*szerokosc)
elif czy_pusty == False:
    for sciana in range(wysokosc):
        print(end = "■" * szerokosc)
        print()
else:
    print("BŁĄD-2")
    exit()

# Zadanie poprawne, natomiast generalne uwagi:
# 1.  Wprowadzasz czy_pusty i tam już obsługujesz podanie niepoprawnej wartości.
#       Z tego powodu nie musisz już sprawdzać BŁĘDU-2 - nigdy do niego nie dotrzesz.
# 2.  Zmienna czy_pusty jest typu logicznego bool, co oznacza, że możesz ją od razu
#       podstawić do instrukcji if.
# 3.  Jeśli badasz prawdziwość zmiennej bool, nie musisz wprowadzać jej warunku elif!
#       Jeśli nie jest True, to na 100% będzie False.
# 4. Puste printy, zamiast tego zastąpione wpisywaniem treści do endów, jest brzydkie,
#       bo (a) zmniejsza czytelność printa, (b) zmusza Cię do rozbicia polecenia na 2.
#       W sytuacji tworzenia pustego środka prostokąta możesz użyć konkatenacji (dodawania/łączenia) stringów.
# 5. Spierałbym się, czy nie czytelniej byłoby zrobić tego zadania na zasadzie wypisz górną
#       krawędź - zrób pusty lub pełny środek zależnie od warunku - wypisz dolną krawędź.
#       Ale to już drobna rzecz ;P
# 6. Zastosowałeś recykling zmiennej "czy_puste", tutaj to działa, ale na przyszłość tego unikaj,
#       przydatna rzecz w Scratchu, ale w Pythonie może Ci wprowadzić dużo chaosu.

# Rozwiązanie samo w sobie poprawne, ale można je o wiele bardziej uczytelnić i zwinąć ;)
# Przykład w pliku alt8-2.py

# 3.75 / 4

print() # Żeby oddzielić to od kolejnego zadania ;)

# #L9-1
lista_a = [-5, -3, 1, 5, 100]
lista_b = []
for cyfra in range(len(lista_a)-1,-1,-1):
    lista_b.append(lista_a[cyfra]) # no i bomba ;P
print(lista_a)
print(lista_b)

# 3 / 3

#L10-1
def poleprostokata(a,b):
    print(f"Pole wynosi {a*b}")

poleprostokata(5,5) # Super

# 1 / 1

#L10-2

def join(lacznik, teksty):
    for slowo in teksty[:len(teksty)-1]: # Dobre spostrzeżenie
        print(end = slowo)
        print(end = lacznik)
    print(teksty[len(teksty)-1])

# 1. Ta sama uwaga z endami jak ostatnio, nie wyrób sobie takiego zwyczaju!!!
# 2. teksty[len(teksty) - 1] jest bezpieczne i w C++ lub Javie byś tak robił.
#    W Pythonie możesz prościej ;P
# Dla zachowania porządku swoje sugestie zapiszę do alt10-2.py

# 3 / 3