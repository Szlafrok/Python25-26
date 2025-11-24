def artym(ciag):
    if len(ciag) == 1: return True
    r = ciag[1] - ciag[0]
    for i in range(1, len(ciag)):
        if ciag[i] - ciag[i-1] != r:
            return False
    return True

x = []
while True: 
    odp = input("Wprowadź element ciągu: ")
    print("Napisz stop jesli chcesz skonczyc wpisywanie")
    if odp.lower() == "stop": 
        break
    else:
        x.append(int(odp))


if artym(x) == True:
    print("Tak")
else:
    print("Nie")

# 2 / 2



x = int(input("Podaj N"))
 
def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 2 / 2

if czy_pierwsza(x) == True:
    print("Pierwsza!")
else:
    print("Nie :()")


# Funkcja 'check' pozwala sprawdzić poprawność rozwiązania danego zadania.
# Przyjmuje argument 'zad', który mówi, które zadanie chcemy przetestować:
# zad == 1 -> sprawdzamy, czy ciąg jest arytmetyczny
# zad == 2 -> sprawdzamy, czy liczba jest pierwsza

def check(zad):
    if zad == 1:  # Jeśli chcemy sprawdzić zadanie z ciągiem arytmetycznym
        x = []  # Tworzymy pustą listę, do której będą wpisywane liczby
        print("Wpisz 'stop', aby przerwać wpisywanie liczb.")
        while True:
            odp = input("Wprowadź element ciągu: ")  # Pobieramy od użytkownika liczbę
            if odp == "stop":  # Jeśli wpisze 'stop', przerywamy pętlę
                break
            x.append(int(odp))  # Zamieniamy wpis na liczbę całkowitą i dodajemy do listy
        # Wyświetlamy wynik, korzystając z funkcji arytm(x)
        print("Ciąg jest arytmetyczny" if artym(x) else "Ciąg nie jest arytmetyczny")
    else:  # Jeśli chcemy sprawdzić, czy liczba jest pierwsza
        x = int(input("Podaj liczbę: "))  # Pobieramy liczbę od użytkownika
        # Wyświetlamy wynik, korzystając z funkcji is_prime(x)
        print("Liczba jest pierwsza" if czy_pierwsza(x) else "Liczba nie jest pierwsza")

# Wywołanie sprawdzarki:
print("Wpisz 1 jesli chcesz artymetycznosc lub 2 zeby oblicz liczby pierwsze")
h = int(input())
check(h)  # Wprowadź numer zadania (1 lub 2), aby przetestować swoje rozwiązanie.

# 1 / 1