# Funkcje wbudowane
print( abs(-10) ) # 10

print(min (5, 4, 2, 7, 6)) # 2
print(max (5, 4, 2, 7, 6)) # 7

print(round(3.566)) # 4

print(len("Nowu Huttu")) # 10

print("--- OPERACJE LOGCZINE ---")

# operatory relacyjne (operatory PORÓWNANIA)

print("--- > ---")
print(250 > 42.01) # True
print(250 > 250) # False
print(250 > 300) # False

print("--- < ---")
print(250 < 42.01) # False
print(250 < 250) # False
print(250 < 300) # True

print("--- == ---")
print(250 == 42.01) # False
print(250 == 250) # True
print(250 == 300) # False
print(250 == "250") # False
print(250 == 250.0) # True

print("--- != ---")
print(250 != 42.01) # True
print(250 != 250) # False
print(250 != 300) # True
print(250 != "250") # True
print(250 != 250.0) # False

print("--- >= ---")
print(250 >= 42.01) # True
print(250 >= 250) # True
print(250 >= 300) # False
#print(250 >= "250") # BŁĄD
print(250 >= 250.0) # True

print("--- <= ---")
print(250 <= 42.01) # False
print(250 <= 250) # True
print(250 <= 300) # True
#print(250 >= "250") # BŁĄD
print(250 <= 250.0) # True

# --- ĆWICZENIE ---
print(12 > 15) # Fałsz // >, ==, >=
print(5 < 15000) # Prawda 
print(120 != 120) # Fałsz
print(60 == 15) # Fałsz
print(25.3421 == 25.3421) # Prawda

# Wypisz w konsoli zasadę działania programu
# print("Czy możesz skorzystać z roller-coastera?")
# print("True - możesz skorzystać z roller-coastera")
# print("False - nie możesz skorzystać z roller-coastera")
print("--- Rollercoaster --- ")
# Zapytaj użytkownika o jego wzrost - pamiętaj o konwersji odpowiedzi do typu int
# Domyślnie odpowiedź użytkownika jest tekstem
wzrost_cm = int(input("Podaj swój wzrost w cm: "))

# Sprawdź wynik działania logicznego i zapisz go do zmiennej "werdykt"
werdykt = wzrost_cm >= 150

# Wyświetl zawartość zmiennej werdykt
print(werdykt)