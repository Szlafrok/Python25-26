import re # re - regex - regular expression - wyrażenie regularne

zdanie = "Ala ma kota a kot ma dosyć Ali"
wynik = re.match(r"Ala", zdanie)
print(f"Wynik wyszukiwania: {wynik}") # formatowany string

wynik = re.match(r"kot", zdanie)
print(f"Wynik wyszukiwania: {wynik}")