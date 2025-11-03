x = "Orka"

if x == "Koteł" or x == "Orka":
    print("Jest to kot lub jest to orka!")
elif x == "Chomik":
    pass # Zapychacz, żeby Python nie wyrzucał błędu
else:
    print("Nie jest to ani chomik ani kot ani orka!")


# print("---- KALKULATOR ----")
# a = float(input("Podaj pierwszą liczbę: "))
# b = float(input("Podaj drugą liczbę: "))

# print("+ -> Dodawanie") 
# print("- -> Odejmowanie")
# print("* -> Mnożenie")
# print("/ -> Dzielenie")

# operacja = input("Podaj operator: ")

# if operacja == "+":
#     print(f"{a} + {b} = {a + b}")
# elif operacja == "-":
#     print(f"{a} - {b} = {a - b}")
# elif operacja == "*":
#     print(f"{a} * {b} = {a * b}")
# elif operacja == "/":
#     if b == 0:
#         print("Dzielenie przez 0 jest niemożliwe!")
#     else:
#         print(f"{a} / {b} = {a / b}")
# else:
#     print("Operator nie został rozpoznany!")



# -----------------------
# Czy dane słowo zawiera?
print("------- SŁOWO ZAWIERA -------")

tekst = "Kaczka zabiła rondlem borsuka z kebabem"

if "czk" in tekst and "rondla" in tekst:
    print("Zawiera taki podciąg!")
else:
    print("Nie zawiera takiego podciągu!")


# ----- ZADANIE SAMODZIELNE -----
POPRAWNY_LOGIN = "trenerpiotrek@gigant.com"
POPRAWNE_HASLO = "security_is_my_passion"

login = input("Podaj login: ")
haslo = input("Podaj hasło: ")

# Prosze wczytać od użytkownika login i hasło, a następnie
# zweryfikować czy podane dane są poprawne.

if login == POPRAWNY_LOGIN and haslo == POPRAWNE_HASLO:
    print("Zalogowano poprawnie!")
else:
    if login != POPRAWNY_LOGIN:
        print("Taki login nie istnieje!")
    else:
        print("Hasło jest błędne!")

# ---- ŚREDNIA OCEN ----