try:
    print(1/1)
except:
    print("Błąd")
else:
    # Try wykona się bez wyjątków
    print("Wykonane poprawnie!")
finally:
    # Wykona się ZAWSZE
    print("Koniec!")