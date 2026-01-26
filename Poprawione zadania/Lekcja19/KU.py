
# QUIZ:
# 80 / 100

def nwmjaktonazwac(): # /🎓 na przykład zadanie2() albo fizzbuzz() ;P
    for i in range(1, 101):           
        if i % 3 == 0 and i % 5 == 0: # Sprawdza czy dzieli się przez 3 i 5 jednocześnie
            print("FizzBuzz")         # Wypisuje FizzBuzz dla liczb podzielnych przez 15
        elif i % 3 == 0:              
            print("Fizz")             # Wypisuje Fizz dla liczb podzielnych przez 3
        elif i % 5 == 0:              
            print("Buzz")             # Wypisuje Buzz dla liczb podzielnych przez 5
        else:                         # Dla liczb niepodzielnych przez 3 ani 5
            print(i)                  
# Bardzo dobrze :)
# 40 / 40

# zad 3
def zadanie3():
    def wzorek(n):
        for i in range(1, n + 1):
            print((str(i) + " ") * i) # konwertuje i na string i powtarza (i) razy z spacją
    wzorek(5)

#zad 4
def zadanie4():
    def minimum(L):
        if not L:
            return None
        min_liczba = L[0]
        for num in L[1:]: # zakłada ze pierwszy element jest najmniejszy i porównuje z resztą
            if num < min_liczba:
                min_liczba = num
        return min_liczba
    print(minimum([5, 4, 6, 1, 6, 2, 3]))

# Komentarze OK, rozwiązanie bardzo ładne :)
# Brakuje mi tu maxa, ale widać że logicznie ogarniasz ;)
# 35 / 50

# zad 5 
def zadanie5():
    def znaki(s, c):
        ilosc = 0
        for char in s:
            if char == c:
                ilosc += 1
        return ilosc
    print(znaki("abrakadabra", "a"))
# Bardzo ładnie :)
# 40 / 40

# zad 6
def zadanie6():
    def gra():
        import random
        punkty_gracza = 0
        punkty_komputera = 0

        while punkty_gracza < 10 and punkty_komputera < 10:
            wybor = input("Wybierz 'o' (orzeł) lub 'r' (reszka): ").lower()
            if wybor not in ['o', 'r']:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")
                continue
            
            rzut = random.choice(['o', 'r'])
            print(f"Wylosowano: {rzut}")

            if wybor == rzut:
                punkty_gracza += 1
                print("Punkt dla Ciebie!")
            
            else:
                punkty_komputera += 1
                print("Punkt dla komputera!")
            
            print(f"Punkty - Ty: {punkty_gracza}, Komputer: {punkty_komputera}\n")
        
        if punkty_gracza == 10:
            print("Gratulacje! Wygrałeś!")
        else:
            print("Niestety, wygrał komputer.")
    gra()
# Zadanie bardzo łądnie, ale brak komentarzy, o które prosiłem w związku z użyciem uzupełniania przez AI
# 30 / 60

# nie wywołuje bo nie skończyłęm /🎓 jeśli tworzysz funkcje wewnątrz funkcji, to trzeba je też tam wywołać. Dopisałem to ;)
nwmjaktonazwac()
zadanie3()
zadanie4()
zadanie5()
zadanie6()

"""
Podsumowanie:

Z1          80  /100
Z2          40  / 40
Z3          40  / 40
Z4          50  / 50
Z5          40  / 40
Z6          30  / 60
Z7          ---
=====================
Razem:     280 ⭐⭐⭐⭐

Znakomicie!

"""