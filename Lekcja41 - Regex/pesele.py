import re

pesel = "01234567890"

wynik = bool(re.search(r"^0[0-9]{9}0$", pesel))

# Proszę napisać wywołanie funkcji search, która sprawdzi poprawność adresu
# e-mail.

# Adres e-mail może zawierać wyłącznie małe litery, cyfry. W środku adresu musi
# być małpa, na końcu musi być treść .com

# \.
mail = "michalpyndzel@gmail.com"
wynik = bool(
    re.search(r"--- \.com$", mail)
)