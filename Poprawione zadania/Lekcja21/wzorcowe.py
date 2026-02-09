skala_oc = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0] # dopuszczalna skala ocen

class Student():

    def __init__(self, nazwisko: str, informatyka: float, wf: float, matematyka: float) -> None:
        
        # rzuć wyjątek jeśli oceny nie przestrzegają skali
        if not (informatyka in skala_oc and wf in skala_oc and matematyka in skala_oc):
            raise ValueError(f"Niepoprawne oceny! Skala ocen: {skala_oc}")
        
        self.nazwisko = nazwisko
        self.informatyka = informatyka
        self.wf = wf
        self.matematyka = matematyka

        self.srednia = (informatyka + wf + matematyka) / 3

        # True jeśli wszystkie przedmioty są ocenione na >= 3, w przeciwnym razie False
        self.zaliczenie = informatyka >= 3 and wf >= 3 and matematyka >= 3

    def wypisz_oceny(self) -> None:
        print(f"Informatyka: {self.informatyka}")
        print(f"Matematyka: {self.matematyka}")
        print(f"WF: {self.wf}")

    def zdane(self) -> None:
        if self.zaliczenie:
            print("Zdane!")
        else:
            print("Niezdane!")

        # Alternatywna metoda:
        # print("Zdane!" if self.zaliczenie else "Niezdane!")

studenciak = Student("Fąfara", 5.0, 3.5, 2.0)
studenciak.wypisz_oceny()
studenciak.zdane()
print(studenciak.srednia)
