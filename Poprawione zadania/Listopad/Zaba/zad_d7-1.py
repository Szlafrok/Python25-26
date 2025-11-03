naturalna = int(input("Wprowadź liczbę naturalną:   "))
if naturalna == 0 or naturalna == 1:
        print("Twoja liczba nie jest pierwsza ani złożona")
        exit()

dzielnik = 2
while dzielnik < naturalna:
    if naturalna % dzielnik == 0:#sprawdza czy liczba jest liczbą złożoną
        print("Twoja liczba jest złożona")
        exit()#kiedy znalazł liczbę naturalną kończy pętlę
    dzielnik += 1

print("Twoja liczba jest liczbą pierwszą")