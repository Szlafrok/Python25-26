class Osoba():
    imie = ""
    nazwisko = ""
    wiek = 0

    def dane(self):
        return f"Jestem {self.imie} {self.nazwisko} i mam {self.wiek} lat."
    
        # Proszę wykomentować obecną zawartość metody dane(self) i zamienić jej
        # działanie, tak aby:
        
        # - od razu printowała imię i nazwisko osoby
        # - od razu printowała informację, czy jest ona pełnoletnia

        # - proszę następnie zmienić wywołanie metody dane() w pliku, gdzie
        #   tworzymy te obiekty, biorąc pod uwagę, że funkcja sama w sobie
        #   już wypisuje tekst, a nie zwraca stringa.