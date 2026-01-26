x = 'pieseł'

if x == 'koteł' or x == 'orka':
    print('jest to kot lub orka')
elif x == 'chomik':
    pass
else:
    print('nie jest to ani chomik, ani kont, ani orka')

print("---- KALKULATOR ----")

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

print("+ -> Dodawanie")
print("- -> Odejmowanie")
print("* -> Mnożenie")
print("/ -> Dzielenie")

operacja = input('podaj operator')

if operacja == '+':
    print(f'{a} + {b} = {a + b}')
elif operacja == '-': # literówka - było "f" zamiast "if". Poza tym operacja jest zmienną, nie piszemy jej w '' - wówczas zostanie to potraktowane jako słowo "operacja", a nie zmienna.
    print(f'{a} - {b} = {a - b}')
elif operacja == '*':  # literówka - było "f" zamiast "if"
    print(f'{a} * {b} = {a * b}')
elif operacja == '/':
    if b == 0: # Literówka: \ zamiast :. Poza tym musimy dać wcięcie, ten "if" musi być wewnątrz "elifa".
        # Chcesz zapytać, czy b jest równe 0 tylko wtedy, gdy znak operacji to "/", ponieważ nie możemy dzielić przez 0.
        print("Błąd: Nie można dzielić przez zero!")
    else:
        print(f'{a} / {b} = {a / b}')
else:
    print("Nieznany operator")




tekst = 'Kaczka zabiła rondlem borsuka z kebabem' # literówka (kacka -> kaczka)


if 'czka' in tekst:
    print('Zawiera taki podciąg') # literówka (pociąg -> podciąg)
else:
    print('Nie zawiera takiego podciągu.')






POPRAWNY_LOGIN = "gigant@mail.com.pl" # Określamy tu tzw. stałe, czyli wartości, których nie będziemy zmieniać w ciągu działania programu.
POPRAWNE_HASLO = "haslomaslo123" # Ustawiamy je po to, żeby wygodnie porównywać z nimi podane przez użytkownika wartości.

login = input('podaj login: ')
haslo = input('podaj hasło: ') # wczytanie danych OK

if login == POPRAWNY_LOGIN and haslo == POPRAWNE_HASLO:
    print('Zalogowano pomyślnie.')
elif login != POPRAWNY_LOGIN:# było "else:" - istotny błąd!!! - wyjaśnienie poniżej
    print('taki login nie istnieje')
else:
    print('nieprawidłowe hasło')

"""
- Brak zadania ze średnią ocen

Wyjaśnienie błędu:
Napisałeś instrukcję składającą się z:
if warunek:
    ...
else:
    ...
else:
    ...

Nie możesz 2 razy użyć else w tej samej instrukcji! Instrukcje warunkowe działają na zasadzie:

Jeśli (1) to zrób (A)
W przeciwnym razie, jeśli (2) to zrób (B)
W przeciwnym razie, jeśli (3) to zrób (C)
...
W przeciwnym razie zrób (D)

Sprawdzamy warunki 1, 2, 3, ..., aż któryś się spełni. Kiedy to nastąpi, wykona się instrukcja
przypisana do tego warunku, czyli: dla 1 będzie to A, dla 2 - B, dla 3 - C, itd.

Jeśli poprzeni warunek się nie wypełnił, to pytamy o kolejny, i o kolejny, i tak dalej, dopóki mamy
podane instrukcje "W przeciwnym razie, jesli..." (elif).

Na końcu możemy RAZ wykorzystać instrukcję "else" - "W przeciwnym razie". Jeśli ŻADEN z moich warunków
wcześniej się nie wypełnił, to wykonuje się to, co podałem przy instrukcji "else". Jednak nie mogę
rozważyć "wszystkich pozostałych możliwości" dwa razy! To tak, jakbym powiedział Ci:

- Jeśli kot jest zdrowy, to go pogłaszcz, w przeciwnym razie idź do weterynarza, w przeciwnym razie... ???

Nie wiadomo, do czego odnosi się to drugie "w przeciwnym razie". W związku z tym mogę z niego skorzystać tylko raz.

Dla lepszego zobrazowania, pokażę to na przykładzie poniżej:
"""

if login == POPRAWNY_LOGIN and haslo == POPRAWNE_HASLO: # Jeśli mam poprawny login i poprawne hasło
    print('Zalogowano pomyślnie.')                      # to powiem użytkownikowi, że zalogował się poprawnie.
elif login != POPRAWNY_LOGIN:                           # Ale jeśli nie, to sprawdzę, czy podał poprawny login, i jeśli nie,
    print('taki login nie istnieje')                    # to powiem mu, że podał błędny login
else:                                                   # A jeśli NIE PODAŁ niepoprawnego loginu, to w takim razie
    print('nieprawidłowe hasło')                        # musiał podać niepoprawne hasło.

"""

Na koniec dodam ważną rzecz - wiele Twoich błędów wynikało z nieuwagi. Zwracaj uwagę, kiedy Twój program
się nie uruchamia, albo kiedy Twój kod podkreśla się na czerwono - to sygnały, że coś jest nie tak. Jeśli
zgłosiłbyś mi te błędy w trakcie zajęć, bez problemu byśmy je naprawili i wyjaśnili.

Zgłoszenie problemu wymaga odwagi, ale bardzo pomaga w zajęciach, i mnie, i Tobie. Dzięki temu ja wiem, że
coś może nie być jasne i wyjaśniam to jeszcze raz, a Ty nie gubisz się w kodzie. To dlatego kładę ogromny
nacisk na sygnalizowanie kłopotów, jest Was na zajęciach dużo i nie zawsze wyłapię osoby mające problemy.

Jesteście na tym kursie, żeby nauczyć się programować, a nauka programowania wymaga ćwiczeń. Ćwiczeń, ćwiczeń,
ćwiczeń. Jeśli to możliwe, proszę rozwiązywać zadawane przeze mnie zadania domowe. Proszę zacząć od zadań
z września i przerobić także zadania z października. W razie napotkania problemów lub potrzeby wyjaśnień, proszę
dać mi znać w czasie przerwy lub pod koniec lekcji, napisać maila lub pisać na Discordzie Gigantów (link do
dołączenia znajduje się w Panelu Ucznia). Zależy mi, żebyście wszyscy to ogarnęli, ale musimy współpracować 😉

Słowem podsumowania:
- Proszę uruchamiać kod wtedy, kiedy my to robimy! Przypomnę odpowiednio jak to robić na początku następnych zajęć.
  Pozwoli to wykrywać błędy wcześnie
- Proszę zwracać uwagę na literówki, błędów nieuwagi bardzo łatwo uniknąć! Jeśli coś podkreśla Ci się na czerwono, to znaczy
  że coś jest nie tak.
- Proszę ZGŁASZAĆ BŁĘDY W KODZIE! To mega ważne, jeśli się zgubisz na lekcji i nie dopytasz, nie poszukasz pomocy, 
  to tylko Ty na tym stracisz, a ja jako trener fizycznie nie jestem w stanie prowadzić zajęć i równocześnie uważnie obserwować ekrany Was wszystkich.
- Proszę ćwiczyć swoje umiejętności! Niećwiczone umiejętności zanikają, a szkoda byłoby utracić już włożoną pracę.

Pozdrawiam i widzimy się w poniedziałek ;)

"""