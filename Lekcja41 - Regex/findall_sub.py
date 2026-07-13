import re

zdanie = "kebab z kebabaem w kebabowie baaaaa baba"

wynik = re.findall(r"kebab.", zdanie)
print(wynik)

wynik = re.findall(r"(ba)+", zdanie)
print(wynik)

wynik = re.sub(r"kebab.", "EK", zdanie)
print(wynik)