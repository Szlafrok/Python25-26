# Proszę napisać program, który wypisze ile miałeś lat w kolejnych latach kalendarzowych
# od Twojego roku urdzoenia. Program powinien wykorzystać zmienną wiek oraz pętlę for
# z wywołaniem range.

rok_urodzenia = int(input("Podaj rok urodzenia: "))

for rok in range(rok_urodzenia + 1, 2026):
    print(f"W roku {rok} miałem {rok - rok_urodzenia}")
