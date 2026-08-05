for i in range(10):
    print(i + 2)

# Proszę napisać program, który zapyta użytkownika o 5 ocen cząstkowych
# i wyliczy średnią z przedmiotu

# ocena_1 = int(input("Podaj kolejną ocenę: "))
# ocena_2 = int(input("Podaj kolejną ocenę: "))
# ocena_3 = int(input("Podaj kolejną ocenę: "))
# ocena_4 = int(input("Podaj kolejną ocenę: "))
# ocena_5 = int(input("Podaj kolejną ocenę: "))

# srednia = (ocena_1 + ocena_2 + ocena_3 + ocena_4 + ocena_5) / 5
# print(f"Średnia ocen: {srednia}")

zakupy = ["jajka", "mleko", "żelki", "chleb", "czekolada", "owoce", True, 2, [1, 4]]
print(zakupy)

print("---------")

for elem in zakupy:
    print(elem)

oceny = [5, 3, 6, 1, 2, 4, 4, 5, 6, 3.5]

suma = 0
for oc in oceny:
    suma += oc

srednia = suma / 10
print(srednia)

# Proszę policzyć ILOCZYN ocen.
print("--- ZADANIE SAMODZIELNE ---")

iloczyn = 1
for oc in oceny:
    iloczyn *= oc
print(f"Iloczyn ocen wynosi {iloczyn}")

# --------------------------------------
# INDEKSOWANIE

oceny = [5, 3, 6, 1, 2, 4, 4, 5, 6, 3.5]

print(oceny[0]) # 5
print(oceny[3]) # 1
print(oceny[6]) # 4
# print(oceny[10]) BŁĄD!

print(oceny)
oceny[6] = 5
print(oceny)

print(oceny[-1]) # 3.5
print(oceny[-4]) # 5, bo indeks -4 to to samo miejsce co indeks 6
print(oceny[-10]) # 5
# print(oceny[-11]) BŁĄD!

# --- METODY LIST ---
oceny = [5, 3, 6, 1, 2, 4, 4, 5, 6, 3.5]

print("append")
print(len(oceny))
oceny.append(4.5) # dodaje element do listy
print(oceny)
print(len(oceny))

ilosc_piatek = oceny.count(5) # Liczba podanych elementów w liście
print(f"Ilość piątek: {ilosc_piatek}")

oceny.clear()
print(oceny)

# --- ZADANIE POPRAWIONE ---
oceny = []
odp = ""
print("Podawaj kolejne oceny. Wpisz 'stop' aby przerwać")
while True:
    odp = input("Wprowadź liczbę: ") # Wprowadzamy odpowiedź
    if odp == "stop": # jeśli stop, przerywamy pętlę
        break
    oceny.append(float(odp)) # dopisujemy ocenę przekonwertowaną na liczbę

wynik = sum(oceny) / len(oceny)
print(wynik)

# --- SLICING ---
oceny = [5, 3, 6, 1, 2, 4, 4, 5, 6, 3.5]
print(oceny[4:])
print(oceny[:4])
print(oceny[2:6])