POPRAWNY_LOGIN = "trenerpiotr@gigant.com" 

POPRAWNE_HASLO ="haslomaslo"
haslo=input("podaj hasło")
login=input("podaj login")
# ORYGINALNY KOD:
# if haslo == "haslomaslo" and login == "trener giganci programowania.com"
 
#  else:   
#     print(hasło i login są poprawne)

# POPRAWKA:
"""
1. W instrukcji "if" porównujemy z zawartością stałych POPRAWNY_LOGIN i POPRAWNE_HASLO,
zamiast "trenerpiotr@gigantcom" i "haslomaslo". Jeśli robilibyśmy więcej miejsc w kodzie,
gdzie musielibyśmy sprawdzić poprawność danych logowania, wystarczyłoby je zmienić w POPRAWNY_LOGIN
i POPRAWNE_HASLO, zamiast we wszystkich miejscach w kodzie.

2. Sprawdzany login powinien być "trenerpiotr@gigant.com" zamiast "trener giganci programowania.com"

3. Piszemy, że "Hasło i login są poprawne", jeśli login się zgadza i hasło się zgadza, więc musimy dać
je do bloku "if", a nie do "else".

4. "else" miało spację przed sobą, a musi być równo z "if"!

5. Ani blok z "if" ani blok z "else" nie może być pusty.
Wersja poprawiona:
"""
if login == POPRAWNY_LOGIN and haslo == POPRAWNE_HASLO: # Jeśli mam poprawny login oraz mam poprawne hasło
    print("Dane logowania poprawne!")                   # To powiadomię gracza, że dane są poprawne
else:                                                   # W przeciwnym razie
    print("Błędny login lub hasło")                     # Powiem mu, że coś się nie zgadza!




zachowanie=int(input("podaj ocenę z zachowania") )
matematyka=int(input("podaj ocenę"))
    
historia=int(input("podaj ocenę"))
wf=int(input("podaj ocenę"))