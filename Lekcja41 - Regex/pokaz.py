import re # re - regex - regular expression - wyrażenie regularne

zdanie = "Michałek ma kota a kot ma dosyć Ali"
wynik = re.match(r"Mich", zdanie)
print(f"Wynik wyszukiwania: {wynik}") # formatowany string

wynik = re.match(r"kot", zdanie)
print(f"Wynik wyszukiwania: {wynik}")

wynik = re.match(r"mich", zdanie, re.IGNORECASE)
print(f"Wynik wyszukiwania: {wynik}")

print(f"Znaleziono element {wynik.group()}")
print(f"{wynik.start()}") # wynik.span()[0]
print(f"{wynik.end()}") # wynik.span()[1]
print(f"{wynik.span()}")


print("-----------------")

napis = "KEBAB z wołowwołoinom 12345 wołowinowom wołowinomnomnom konstantynopolitańczykowianeczką i sosem tysiąca wysp"
wynik = re.search(r"wołowinom", napis)
print(wynik)

wynik = re.search(r"[0-9a-e]", napis)
print(wynik)

wynik = re.search(r"[2-7C-G]", napis)
print(wynik)

wynik = re.search(r"[0-9]+", napis) # + oznacza 1 lub więcej takich znaków
print(wynik)

wynik = re.search(r"[A-Za-z]+", napis)
print(wynik)

wynik = re.search(r"[A-Za-z]*", napis) # * oznacza 0 lub więcej takich znaków
print(wynik)

wynik = re.search(r"[A-Za-z]{4}", napis) # {x} oznacza DOKŁADNIE x znaków
print(wynik)

# proszę napisać search, który w podanym ciągu znajdzie ciąg dokładnie 3 cyfr 0-9
wynik = re.search(r"\d{3}", napis) # {x} oznacza DOKŁADNIE x znaków
print(wynik)

wynik = re.search(r"woło.woło", napis)
print(wynik)

wynik = re.search(r"woło.*woło", napis)
print(wynik)