#imie = input("Wprowadź imię: ")
#nazwisko = input("Wprowadź nazwisko: ")

#print(imie, nazwisko)
#wiek = int(input("Wprowadź wiek: "))

a = 12
b = 5

print(a + b) # 12 + 5 =17
print(a - b) # 12 - 5 = 7
print(a * b) # 12 * 5 = 60
print(a / b) # 12 / 5 = 2.4 -> ZAWSZE DAJE FLOAT

c = 2 * a + b # 2 * 12 + 5 = 24 + 5 = 29
print(c)

print(-a) # -12

print(a // b) # 2 ->

# Operacje int-int, int-float, float-float
print(2 + 2)
print(2 + 2.5)
print(2.5 + 2.5)

# Potęgowanie
print(a ** b) # a - podstawa, b - wykładnik. 248832

# Dzielenie z resztą (modulo)
print(a % b) # 12 % 5 = 2

# ZADANIE SAMODZIELNE
# Wzór na pole powierzchni prostopadłościanu: 2ab + 2ac + 2bc
# 2ab = 2 * a * b
# Proszę napisać skrypt, który wczyta od gracza wartości liczbowe
# a, b, c i wyznaczy (wypisze do konsoli) pole powierzchni całkowitej
# prostopadłościanu o bokach a, b, c.

# a = float(input())
# b = float(input())
# c = float(input())

# pole = 2 * a * b + 2 * a * c + 2 * b * c
# print(pole)

# OPERATORY PRZYPISANIA
print("--------")
a = 3
b = 4
a = a + 2 # zwiększ a o 2
print(a)

a += 2 # zwiększ a o 2
print(a)

a -= 4 # odejmij 4
print(a) # 3

a *= b 
print(a)

a /= b
print(f"Wynik przed samodzielnym: {a}") # a = 3.0, b = 4

# ZADANIE SAMODZIELNE

# Proszę wykonać działania:
# - podnieś a do potęgi 2
# - podziel a z resztą przez b
# - przemnóż a przez trzykrotność b (przemnóż przez b * 3)
# - podziel a całkowicie przez 3

a **= 2 # a = a**2
a %= b # a = a%b
a *= b * 3 # a = a * b * 3
a //= 3 # a = a // 3
print(a)

# a = 3

tekst_a = "Witaj"
tekst_b = "Piotrze"

print(tekst_a + tekst_b) # Połączenie stringów
print(tekst_a * 3)  # mnożenie stringa przez n -> powtórzenie stringa n razy

# F-STRING
tekst_wypisania = f"Wynik wykonywania naszych działań to {a}"
print(tekst_wypisania)