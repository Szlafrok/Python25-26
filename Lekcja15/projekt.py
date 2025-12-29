### Zadanie 1

def binarne_na_dzies(n: str) -> int: # z systemu binarnego
    res = 0 # result
    potega = 0
    for bit in reversed(n): # n[::-1]
        res += int(bit) * 2 ** potega
        potega += 1
    return res

print(binarne_na_dzies("100110110"))