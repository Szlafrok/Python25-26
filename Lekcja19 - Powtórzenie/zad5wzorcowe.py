def find(s, c):             # funkcja liczy, ile razy znak c pojawia się w napisie s
    licznik = 0             # zaczynamy od zera – jeszcze nic nie znaleźliśmy
    for znak in s:          # przechodzimy po każdym znaku w napisie
        if znak == c:       # jeśli aktualny znak jest tym, którego szukamy
            licznik += 1    # zwiększamy licznik o 1
    return licznik          # zwracamy łączną liczbę wystąpień

print(find("aaaabbbbaaaacccc", "a"))  # wypisuje, ile razy 'a' występuje w podanym napisie
