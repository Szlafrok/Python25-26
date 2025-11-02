imie = input("Podaj imie: ")
nazwisko = input("Podaj nazwisko: ")
rok_urodzenia = input("Podaj rok urodzenia: ")

# opcja (a) 
ilosc_lat = 2025 - int(rok_urodzenia)
print(f"(a) {imie} {nazwisko} ma {ilosc_lat} lat.")
# Bardzo dobrze! 2.5 / 2.5

# opcja (b)
print(f"(b) {imie} {nazwisko} ma", 2025 - int(rok_urodzenia), "lat.")
# 0.5 / 0.5


# (3.0 / 3.0) Dobra robota!