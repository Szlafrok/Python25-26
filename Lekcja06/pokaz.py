x = "Orka"

if x == "Koteł" or x == "Orka":
    print("Jest to kot lub jest to orka!")
elif x == "Chomik":
    pass # Zapychacz, żeby Python nie wyrzucał błędu
else:
    print("Nie jest to ani chomik ani kot ani orka!")


print("---- KALKULATOR ----")
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

print("+ -> Dodawanie") 
print("- -> Odejmowanie")
print("* -> Mnożenie")
print("/ -> Dzielenie")

operacja = input("Podaj operator: ")

if operacja == "+":
    print(f"{a} + {b} = {a + b}")
if operacja == "-":
    print(f"{a} - {b} = {a - b}")
if operacja == "*":
    print(f"{a} * {b} = {a * b}")
if operacja == "/":
    